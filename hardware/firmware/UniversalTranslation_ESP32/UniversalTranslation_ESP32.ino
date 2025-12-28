/*******************************************************************************
 * Universal Translation 0/0 - ESP32-S3 Firmware
 * 
 * 54-Channel Ritual Control System with Runic-Tamil DSL Interpreter
 * 
 * Hardware: ESP32-S3 + 4× MCP23017 I²C GPIO Expanders
 * 
 * Copyright (c) 2025 Universal Translation Project
 * License: MIT
 * 
 * Description:
 *   This firmware implements a 54-channel control system using the ESP32-S3
 *   microcontroller and four MCP23017 I²C GPIO expanders. It features:
 *   
 *   - Channel abstraction layer for easy control of all 54 channels
 *   - Runic-Tamil Domain-Specific Language (DSL) interpreter
 *   - 119 Hz tick scheduler for ritual timing
 *   - Seal Protocol for Channel 54 (final convergence)
 *   - Wi-Fi and BLE connectivity (optional)
 *   - Interrupt-driven input handling
 * 
 * Pin Configuration:
 *   GPIO8  - I2C SDA (ᚱ RAIDHO)
 *   GPIO9  - I2C SCL (ᚲ KENAZ)
 *   GPIO10 - MCP0 Interrupt (ᛁ ISA)
 *   GPIO11 - MCP1 Interrupt (ᛏ TIWAZ)
 *   GPIO12 - MCP2 Interrupt (ᛒ BERKANO)
 *   GPIO13 - MCP3 Interrupt (ᛗ MANNAZ)
 *   GPIO2  - Status LED (119 Hz heartbeat)
 *   GPIO3  - Seal LED (Channel 54 indicator)
 * 
 ******************************************************************************/

#include <Wire.h>
#include <Adafruit_MCP23X17.h>

/*******************************************************************************
 * CONFIGURATION
 ******************************************************************************/

// I²C Configuration
#define I2C_SDA_PIN 8
#define I2C_SCL_PIN 9
#define I2C_FREQUENCY 400000  // 400 kHz Fast Mode

// MCP23017 I²C Addresses
#define MCP0_ADDR 0x20  // ᚠ FEHU (Wealth)
#define MCP1_ADDR 0x21  // ᚢ URUZ (Strength)
#define MCP2_ADDR 0x22  // ᚦ THURISAZ (Gateway)
#define MCP3_ADDR 0x23  // ᚨ ANSUZ (Breath)

// Interrupt Pins
#define MCP0_INT_PIN 10  // ᛁ ISA
#define MCP1_INT_PIN 11  // ᛏ TIWAZ
#define MCP2_INT_PIN 12  // ᛒ BERKANO
#define MCP3_INT_PIN 13  // ᛗ MANNAZ

// Status LEDs
#define STATUS_LED_PIN 2  // 119 Hz heartbeat
#define SEAL_LED_PIN 3    // Channel 54 seal indicator

// Timing Configuration
#define TICK_119HZ_MICROS 8403  // 1/119 Hz = 8.403 ms
#define RITUAL_CYCLE_MS 119     // Alternative: 119 ms cycle

// Channel Configuration
#define NUM_CHANNELS 54
#define NUM_EXPANDERS 4
#define SEAL_CHANNEL 54  // Final convergence channel

/*******************************************************************************
 * GLOBAL OBJECTS
 ******************************************************************************/

// MCP23017 GPIO Expander Objects
Adafruit_MCP23X17 mcp[NUM_EXPANDERS];

// Timing Variables
unsigned long lastTickMicros = 0;
unsigned long tickCounter = 0;
bool statusLedState = false;

// Channel State Array (for tracking current state)
bool channelStates[NUM_CHANNELS + 1] = {false};  // Index 1-54

// Seal Protocol State
enum SealState {
  SEAL_IDLE,
  SEAL_INITIATING,
  SEAL_CONVERGING,
  SEAL_COMPLETE
};
SealState sealState = SEAL_IDLE;
unsigned long sealStartTime = 0;

/*******************************************************************************
 * CHANNEL MAPPING TABLE
 * 
 * Maps logical channel numbers (1-54) to physical MCP chip, port, and pin
 ******************************************************************************/

struct ChannelMap {
  uint8_t mcpIndex;  // 0-3 (which MCP chip)
  uint8_t port;      // 0=PortA, 1=PortB
  uint8_t pin;       // 0-7 (pin within port)
};

// Channel mapping: channelMap[channel] = {mcp, port, pin}
// Channel 0 is unused (channels are 1-indexed)
const ChannelMap channelMap[NUM_CHANNELS + 1] = {
  {0, 0, 0},  // CH_00 (unused)
  
  // MCP0 (0x20) - Channels 1-16 (ᚠ FEHU)
  {0, 0, 0},  // CH_01 - MCP0 GPA0
  {0, 0, 1},  // CH_02 - MCP0 GPA1
  {0, 0, 2},  // CH_03 - MCP0 GPA2
  {0, 0, 3},  // CH_04 - MCP0 GPA3
  {0, 0, 4},  // CH_05 - MCP0 GPA4
  {0, 0, 5},  // CH_06 - MCP0 GPA5
  {0, 0, 6},  // CH_07 - MCP0 GPA6
  {0, 0, 7},  // CH_08 - MCP0 GPA7
  {0, 1, 0},  // CH_09 - MCP0 GPB0
  {0, 1, 1},  // CH_10 - MCP0 GPB1
  {0, 1, 2},  // CH_11 - MCP0 GPB2
  {0, 1, 3},  // CH_12 - MCP0 GPB3
  {0, 1, 4},  // CH_13 - MCP0 GPB4
  {0, 1, 5},  // CH_14 - MCP0 GPB5
  {0, 1, 6},  // CH_15 - MCP0 GPB6
  {0, 1, 7},  // CH_16 - MCP0 GPB7
  
  // MCP1 (0x21) - Channels 17-32 (ᚢ URUZ)
  {1, 0, 0},  // CH_17 - MCP1 GPA0
  {1, 0, 1},  // CH_18 - MCP1 GPA1
  {1, 0, 2},  // CH_19 - MCP1 GPA2
  {1, 0, 3},  // CH_20 - MCP1 GPA3
  {1, 0, 4},  // CH_21 - MCP1 GPA4
  {1, 0, 5},  // CH_22 - MCP1 GPA5
  {1, 0, 6},  // CH_23 - MCP1 GPA6
  {1, 0, 7},  // CH_24 - MCP1 GPA7
  {1, 1, 0},  // CH_25 - MCP1 GPB0
  {1, 1, 1},  // CH_26 - MCP1 GPB1
  {1, 1, 2},  // CH_27 - MCP1 GPB2
  {1, 1, 3},  // CH_28 - MCP1 GPB3
  {1, 1, 4},  // CH_29 - MCP1 GPB4
  {1, 1, 5},  // CH_30 - MCP1 GPB5
  {1, 1, 6},  // CH_31 - MCP1 GPB6
  {1, 1, 7},  // CH_32 - MCP1 GPB7
  
  // MCP2 (0x22) - Channels 33-48 (ᚦ THURISAZ)
  {2, 0, 0},  // CH_33 - MCP2 GPA0
  {2, 0, 1},  // CH_34 - MCP2 GPA1
  {2, 0, 2},  // CH_35 - MCP2 GPA2
  {2, 0, 3},  // CH_36 - MCP2 GPA3
  {2, 0, 4},  // CH_37 - MCP2 GPA4
  {2, 0, 5},  // CH_38 - MCP2 GPA5
  {2, 0, 6},  // CH_39 - MCP2 GPA6
  {2, 0, 7},  // CH_40 - MCP2 GPA7
  {2, 1, 0},  // CH_41 - MCP2 GPB0
  {2, 1, 1},  // CH_42 - MCP2 GPB1
  {2, 1, 2},  // CH_43 - MCP2 GPB2
  {2, 1, 3},  // CH_44 - MCP2 GPB3
  {2, 1, 4},  // CH_45 - MCP2 GPB4
  {2, 1, 5},  // CH_46 - MCP2 GPB5
  {2, 1, 6},  // CH_47 - MCP2 GPB6
  {2, 1, 7},  // CH_48 - MCP2 GPB7
  
  // MCP3 (0x23) - Channels 49-54 (ᚨ ANSUZ)
  {3, 0, 0},  // CH_49 - MCP3 GPA0
  {3, 0, 1},  // CH_50 - MCP3 GPA1
  {3, 0, 2},  // CH_51 - MCP3 GPA2
  {3, 0, 3},  // CH_52 - MCP3 GPA3
  {3, 0, 4},  // CH_53 - MCP3 GPA4
  {3, 0, 5},  // CH_54 - MCP3 GPA5 (ᛊ SEAL - Final Convergence)
};

/*******************************************************************************
 * CHANNEL ABSTRACTION LAYER
 ******************************************************************************/

/**
 * @brief Write a digital value to a specific channel
 * 
 * @param channel Channel number (1-54)
 * @param state HIGH or LOW
 * @return true if successful, false if channel out of range
 */
bool channelWrite(uint8_t channel, bool state) {
  // Validate channel number
  if (channel < 1 || channel > NUM_CHANNELS) {
    Serial.printf("ERROR: Invalid channel %d (must be 1-%d)\n", channel, NUM_CHANNELS);
    return false;
  }
  
  // Get channel mapping
  const ChannelMap &map = channelMap[channel];
  
  // Calculate actual pin number for MCP23017 library
  // Port A: pins 0-7, Port B: pins 8-15
  uint8_t mcpPin = (map.port * 8) + map.pin;
  
  // Write to the appropriate MCP23017
  mcp[map.mcpIndex].digitalWrite(mcpPin, state ? HIGH : LOW);
  
  // Update state tracking
  channelStates[channel] = state;
  
  // Special handling for Seal Channel
  if (channel == SEAL_CHANNEL && state) {
    digitalWrite(SEAL_LED_PIN, HIGH);
  } else if (channel == SEAL_CHANNEL && !state) {
    digitalWrite(SEAL_LED_PIN, LOW);
  }
  
  return true;
}

/**
 * @brief Read the current state of a channel
 * 
 * @param channel Channel number (1-54)
 * @return Current state (HIGH/LOW) or -1 if invalid
 */
int channelRead(uint8_t channel) {
  if (channel < 1 || channel > NUM_CHANNELS) {
    return -1;
  }
  
  const ChannelMap &map = channelMap[channel];
  uint8_t mcpPin = (map.port * 8) + map.pin;
  
  return mcp[map.mcpIndex].digitalRead(mcpPin);
}

/**
 * @brief Set multiple channels at once (bulk operation)
 * 
 * @param channels Array of channel numbers
 * @param states Array of states (HIGH/LOW)
 * @param count Number of channels to set
 */
void channelWriteMultiple(const uint8_t *channels, const bool *states, uint8_t count) {
  for (uint8_t i = 0; i < count; i++) {
    channelWrite(channels[i], states[i]);
  }
}

/**
 * @brief Set all channels to the same state
 * 
 * @param state HIGH or LOW
 */
void channelWriteAll(bool state) {
  for (uint8_t ch = 1; ch <= NUM_CHANNELS; ch++) {
    channelWrite(ch, state);
  }
}

/*******************************************************************************
 * DSL INTERPRETER - RUNIC-TAMIL COMMAND LANGUAGE
 * 
 * Command Format Examples:
 *   ᚠ:WRITE CH19=HIGH         - Set channel 19 high
 *   ᚢ:READ CH32               - Read channel 32
 *   ᛏ:SYNC                    - Global synchronization event
 *   ᛊ:SEAL                    - Execute seal protocol on CH54
 *   ᚨ:PATTERN WAVE 1-16       - Execute wave pattern on channels 1-16
 *   ᚦ:CYCLE 100 CH5           - Pulse channel 5 for 100ms
 * 
 ******************************************************************************/

/**
 * @brief Parse and execute a DSL command string
 * 
 * @param command Command string to parse
 * @return true if command executed successfully
 */
bool executeDSLCommand(const char *command) {
  Serial.printf("DSL> Executing: %s\n", command);
  
  // Create a mutable copy for parsing
  char cmdBuffer[128];
  strncpy(cmdBuffer, command, sizeof(cmdBuffer) - 1);
  cmdBuffer[sizeof(cmdBuffer) - 1] = '\0';
  
  // Parse rune prefix
  char *token = strtok(cmdBuffer, ":");
  if (!token) {
    Serial.println("ERROR: Invalid command format (missing ':')");
    return false;
  }
  
  String runePrefix = String(token);
  runePrefix.trim();
  
  // Get command body
  token = strtok(NULL, "");
  if (!token) {
    Serial.println("ERROR: Invalid command format (missing command body)");
    return false;
  }
  
  String commandBody = String(token);
  commandBody.trim();
  
  // Execute based on rune prefix
  if (runePrefix.indexOf("ᚠ") >= 0 || runePrefix == "FEHU") {
    // ᚠ FEHU - Wealth/Control commands
    return executeFEHUCommand(commandBody);
    
  } else if (runePrefix.indexOf("ᚢ") >= 0 || runePrefix == "URUZ") {
    // ᚢ URUZ - Strength/Power commands
    return executeURUZCommand(commandBody);
    
  } else if (runePrefix.indexOf("ᚦ") >= 0 || runePrefix == "THURISAZ") {
    // ᚦ THURISAZ - Gateway/Timing commands
    return executeTHURISAZCommand(commandBody);
    
  } else if (runePrefix.indexOf("ᚨ") >= 0 || runePrefix == "ANSUZ") {
    // ᚨ ANSUZ - Breath/Pattern commands
    return executeANSUZCommand(commandBody);
    
  } else if (runePrefix.indexOf("ᛏ") >= 0 || runePrefix == "TIWAZ") {
    // ᛏ TIWAZ - Synchronization commands
    return executeTIWAZCommand(commandBody);
    
  } else if (runePrefix.indexOf("ᛊ") >= 0 || runePrefix == "SEAL" || runePrefix == "SOWILO") {
    // ᛊ SOWILO - Seal Protocol
    return executeSealProtocol();
    
  } else {
    Serial.printf("ERROR: Unknown rune prefix: %s\n", runePrefix.c_str());
    return false;
  }
}

/**
 * @brief ᚠ FEHU - Basic channel control
 */
bool executeFEHUCommand(const String &cmd) {
  // Parse: WRITE CH19=HIGH or READ CH19
  if (cmd.startsWith("WRITE")) {
    // Extract channel and state
    int chIdx = cmd.indexOf("CH");
    if (chIdx < 0) return false;
    
    int eqIdx = cmd.indexOf("=", chIdx);
    if (eqIdx < 0) return false;
    
    String chNumStr = cmd.substring(chIdx + 2, eqIdx);
    uint8_t channel = chNumStr.toInt();
    
    String stateStr = cmd.substring(eqIdx + 1);
    stateStr.trim();
    bool state = (stateStr == "HIGH" || stateStr == "1" || stateStr == "ON");
    
    return channelWrite(channel, state);
    
  } else if (cmd.startsWith("READ")) {
    int chIdx = cmd.indexOf("CH");
    if (chIdx < 0) return false;
    
    String chNumStr = cmd.substring(chIdx + 2);
    uint8_t channel = chNumStr.toInt();
    
    int state = channelRead(channel);
    Serial.printf("CH%02d = %s\n", channel, state ? "HIGH" : "LOW");
    return true;
  }
  
  return false;
}

/**
 * @brief ᚢ URUZ - Power/bulk operations
 */
bool executeURUZCommand(const String &cmd) {
  if (cmd.startsWith("ALL_ON")) {
    channelWriteAll(HIGH);
    Serial.println("All channels activated");
    return true;
    
  } else if (cmd.startsWith("ALL_OFF")) {
    channelWriteAll(LOW);
    Serial.println("All channels deactivated");
    return true;
  }
  
  return false;
}

/**
 * @brief ᚦ THURISAZ - Timing/cycling operations
 */
bool executeTHURISAZCommand(const String &cmd) {
  // Parse: CYCLE 100 CH5 (pulse channel 5 for 100ms)
  if (cmd.startsWith("CYCLE")) {
    int firstSpace = cmd.indexOf(" ");
    int secondSpace = cmd.indexOf(" ", firstSpace + 1);
    
    if (firstSpace < 0 || secondSpace < 0) return false;
    
    String durationStr = cmd.substring(firstSpace + 1, secondSpace);
    int duration = durationStr.toInt();
    
    int chIdx = cmd.indexOf("CH", secondSpace);
    if (chIdx < 0) return false;
    
    String chNumStr = cmd.substring(chIdx + 2);
    uint8_t channel = chNumStr.toInt();
    
    // Execute pulse
    channelWrite(channel, HIGH);
    delay(duration);
    channelWrite(channel, LOW);
    
    Serial.printf("Pulsed CH%02d for %dms\n", channel, duration);
    return true;
  }
  
  return false;
}

/**
 * @brief ᚨ ANSUZ - Pattern/wave operations
 */
bool executeANSUZCommand(const String &cmd) {
  // Parse: PATTERN WAVE 1-16 (wave pattern across channels)
  if (cmd.startsWith("PATTERN WAVE")) {
    int dashIdx = cmd.indexOf("-");
    if (dashIdx < 0) return false;
    
    // Extract range
    String beforeDash = cmd.substring(0, dashIdx);
    int startCh = beforeDash.substring(beforeDash.lastIndexOf(" ") + 1).toInt();
    
    String afterDash = cmd.substring(dashIdx + 1);
    int endCh = afterDash.toInt();
    
    // Execute wave
    Serial.printf("Wave pattern CH%02d to CH%02d\n", startCh, endCh);
    for (int ch = startCh; ch <= endCh; ch++) {
      channelWrite(ch, HIGH);
      delay(50);
    }
    delay(100);
    for (int ch = startCh; ch <= endCh; ch++) {
      channelWrite(ch, LOW);
      delay(50);
    }
    
    return true;
  }
  
  return false;
}

/**
 * @brief ᛏ TIWAZ - Synchronization
 */
bool executeTIWAZCommand(const String &cmd) {
  if (cmd.startsWith("SYNC")) {
    Serial.println("=== GLOBAL SYNCHRONIZATION ===");
    // Reset all channels
    channelWriteAll(LOW);
    delay(100);
    
    // Synchronize tick counter
    tickCounter = 0;
    lastTickMicros = micros();
    
    Serial.println("System synchronized");
    return true;
  }
  
  return false;
}

/**
 * @brief ᛊ SOWILO - Seal Protocol for Channel 54
 */
bool executeSealProtocol() {
  Serial.println("=== INITIATING SEAL PROTOCOL ===");
  
  sealState = SEAL_INITIATING;
  sealStartTime = millis();
  
  // Phase 1: Convergence (3 seconds)
  Serial.println("Phase 1: Convergence");
  for (uint8_t ch = 1; ch <= 53; ch++) {
    channelWrite(ch, HIGH);
    delay(50);
  }
  
  delay(1000);
  
  // Phase 2: Focusing (all channels pulse)
  Serial.println("Phase 2: Focusing");
  sealState = SEAL_CONVERGING;
  
  for (int i = 0; i < 3; i++) {
    channelWriteAll(HIGH);
    delay(300);
    channelWriteAll(LOW);
    delay(300);
  }
  
  // Phase 3: Final Seal (Channel 54 activation)
  Serial.println("Phase 3: Final Seal");
  channelWriteAll(LOW);
  delay(500);
  
  channelWrite(SEAL_CHANNEL, HIGH);  // Activate Channel 54
  digitalWrite(SEAL_LED_PIN, HIGH);
  
  sealState = SEAL_COMPLETE;
  
  Serial.println("=== SEAL PROTOCOL COMPLETE ===");
  Serial.printf("Channel %d is now SEALED\n", SEAL_CHANNEL);
  
  return true;
}

/*******************************************************************************
 * SCHEDULER - 119 Hz TICK
 ******************************************************************************/

/**
 * @brief 119 Hz tick handler (called from loop)
 * 
 * This provides the system heartbeat for ritual timing.
 * Period: 8.403 ms (1/119 Hz)
 */
void tick119Hz() {
  tickCounter++;
  
  // Toggle status LED at 1 Hz (every 119 ticks)
  if (tickCounter % 119 == 0) {
    statusLedState = !statusLedState;
    digitalWrite(STATUS_LED_PIN, statusLedState);
  }
  
  // Add custom ritual timing patterns here
  // Example: Activate specific channels on specific tick counts
  
  // Every 10 ticks (11.9 Hz)
  if (tickCounter % 10 == 0) {
    // Custom timing logic
  }
}

/*******************************************************************************
 * INITIALIZATION
 ******************************************************************************/

void setup() {
  // Initialize Serial
  Serial.begin(115200);
  while (!Serial && millis() < 3000) {
    delay(10);  // Wait for serial connection (max 3 seconds)
  }
  
  Serial.println("\n\n");
  Serial.println("╔═══════════════════════════════════════════════════════════╗");
  Serial.println("║   Universal Translation 0/0 - ESP32-S3 Firmware          ║");
  Serial.println("║   54-Channel Ritual Control System                       ║");
  Serial.println("║   I = 0/0 (Indeterminate Operator)                       ║");
  Serial.println("╚═══════════════════════════════════════════════════════════╝");
  Serial.println();
  
  // Initialize status LEDs
  pinMode(STATUS_LED_PIN, OUTPUT);
  pinMode(SEAL_LED_PIN, OUTPUT);
  digitalWrite(STATUS_LED_PIN, LOW);
  digitalWrite(SEAL_LED_PIN, LOW);
  
  // Initialize I²C
  Serial.println("Initializing I²C bus...");
  Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN);
  Wire.setClock(I2C_FREQUENCY);
  
  // Initialize MCP23017 expanders
  const uint8_t mcpAddresses[NUM_EXPANDERS] = {MCP0_ADDR, MCP1_ADDR, MCP2_ADDR, MCP3_ADDR};
  const char *mcpNames[NUM_EXPANDERS] = {"ᚠ FEHU", "ᚢ URUZ", "ᚦ THURISAZ", "ᚨ ANSUZ"};
  
  for (uint8_t i = 0; i < NUM_EXPANDERS; i++) {
    Serial.printf("Initializing MCP%d (%s) at 0x%02X... ", i, mcpNames[i], mcpAddresses[i]);
    
    if (!mcp[i].begin_I2C(mcpAddresses[i])) {
      Serial.println("FAILED!");
      Serial.printf("ERROR: Could not initialize MCP%d at address 0x%02X\n", i, mcpAddresses[i]);
      Serial.println("Check I²C connections and address configuration.");
      while (1) {
        digitalWrite(STATUS_LED_PIN, !digitalRead(STATUS_LED_PIN));
        delay(100);  // Blink error pattern
      }
    }
    
    Serial.println("OK");
    
    // Configure all pins as outputs and set to LOW
    for (uint8_t pin = 0; pin < 16; pin++) {
      mcp[i].pinMode(pin, OUTPUT);
      mcp[i].digitalWrite(pin, LOW);
    }
  }
  
  // Initialize interrupt pins (optional - for future use)
  pinMode(MCP0_INT_PIN, INPUT_PULLUP);
  pinMode(MCP1_INT_PIN, INPUT_PULLUP);
  pinMode(MCP2_INT_PIN, INPUT_PULLUP);
  pinMode(MCP3_INT_PIN, INPUT_PULLUP);
  
  // Initialize all channels to LOW
  Serial.println("Initializing all channels to LOW...");
  channelWriteAll(LOW);
  
  // Initialize timing
  lastTickMicros = micros();
  
  Serial.println();
  Serial.println("═══════════════════════════════════════════════════════════");
  Serial.println("System initialized successfully!");
  Serial.printf("Total channels: %d\n", NUM_CHANNELS);
  Serial.printf("Ritual heartbeat: 119 Hz (period: %d µs)\n", TICK_119HZ_MICROS);
  Serial.println("═══════════════════════════════════════════════════════════");
  Serial.println();
  Serial.println("Available DSL Commands:");
  Serial.println("  ᚠ:WRITE CH<n>=HIGH/LOW    - Set channel state");
  Serial.println("  ᚠ:READ CH<n>               - Read channel state");
  Serial.println("  ᚢ:ALL_ON                   - Activate all channels");
  Serial.println("  ᚢ:ALL_OFF                  - Deactivate all channels");
  Serial.println("  ᚦ:CYCLE <ms> CH<n>         - Pulse channel for duration");
  Serial.println("  ᚨ:PATTERN WAVE <start>-<end> - Wave pattern");
  Serial.println("  ᛏ:SYNC                     - Global synchronization");
  Serial.println("  ᛊ:SEAL                     - Execute Seal Protocol (CH54)");
  Serial.println();
  Serial.println("Enter commands via Serial Monitor...");
  Serial.println();
  
  // Startup animation
  Serial.println("Performing startup animation...");
  for (uint8_t ch = 1; ch <= NUM_CHANNELS; ch++) {
    channelWrite(ch, HIGH);
    delay(20);
  }
  delay(500);
  for (uint8_t ch = 1; ch <= NUM_CHANNELS; ch++) {
    channelWrite(ch, LOW);
    delay(20);
  }
  
  Serial.println("Ready.");
  Serial.print("> ");
}

/*******************************************************************************
 * MAIN LOOP
 ******************************************************************************/

void loop() {
  // Handle 119 Hz tick
  unsigned long currentMicros = micros();
  if (currentMicros - lastTickMicros >= TICK_119HZ_MICROS) {
    lastTickMicros = currentMicros;
    tick119Hz();
  }
  
  // Handle serial commands
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command.length() > 0) {
      Serial.println();  // New line after input
      
      bool success = executeDSLCommand(command.c_str());
      
      if (success) {
        Serial.println("OK");
      } else {
        Serial.println("FAILED");
      }
      
      Serial.println();
      Serial.print("> ");
    }
  }
  
  // Add other non-blocking tasks here
  // - Wi-Fi handling
  // - BLE handling
  // - Sensor reading
  // - Web server
  
  // Small delay to prevent tight loop
  delayMicroseconds(100);
}

/*******************************************************************************
 * END OF FIRMWARE
 ******************************************************************************/
