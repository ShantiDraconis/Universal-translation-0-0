#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MCP23X17.h>

// ESP32-S3 pin plan (matches schematic spec)
constexpr uint8_t PIN_I2C_SDA = 8;
constexpr uint8_t PIN_I2C_SCL = 9;
constexpr uint8_t PIN_INT[4] = {4, 5, 6, 7};

// Heartbeat: 8 ms (~125 Hz). Set to 119 ms for the slower 119 ms ritual cycle if desired.
constexpr uint32_t HEARTBEAT_INTERVAL_MS = 8;

// MCP23017 devices on the shared I2C bus
constexpr uint8_t MCP_COUNT = 4;
constexpr uint8_t MCP_ADDRESSES[MCP_COUNT] = {0x20, 0x21, 0x22, 0x23};
Adafruit_MCP23X17 expanders[MCP_COUNT];

// Channel map (1-based external numbering → expander index + pin number)
struct ChannelMapEntry {
  uint8_t expander;
  uint8_t pin;
};

constexpr uint8_t MIN_CHANNEL = 1;
constexpr uint8_t USED_CHANNELS = 54;
const ChannelMapEntry CHANNEL_MAP[USED_CHANNELS] = {
    {0, 0},  {0, 1},  {0, 2},  {0, 3},  {0, 4},  {0, 5},  {0, 6},  {0, 7},  // CH1–8
    {0, 8},  {0, 9},  {0, 10}, {0, 11}, {0, 12}, {0, 13}, {0, 14}, {0, 15}, // CH9–16
    {1, 0},  {1, 1},  {1, 2},  {1, 3},  {1, 4},  {1, 5},  {1, 6},  {1, 7},  // CH17–24
    {1, 8},  {1, 9},  {1, 10}, {1, 11}, {1, 12}, {1, 13}, {1, 14}, {1, 15}, // CH25–32
    {2, 0},  {2, 1},  {2, 2},  {2, 3},  {2, 4},  {2, 5},  {2, 6},  {2, 7},  // CH33–40
    {2, 8},  {2, 9},  {2, 10}, {2, 11}, {2, 12}, {2, 13}, {2, 14}, {2, 15}, // CH41–48
    {3, 0},  {3, 1},  {3, 2},  {3, 3},  {3, 4},  {3, 5}                                    // CH49–54
};

constexpr uint8_t SEAL_CHANNEL = 54; // Channel dedicated to the seal protocol

unsigned long lastTickMs = 0;

bool resolveChannel(uint8_t channel, ChannelMapEntry &out) {
  if (channel < MIN_CHANNEL || channel > USED_CHANNELS) {
    return false;
  }
  out = CHANNEL_MAP[channel - 1];
  return out.expander < MCP_COUNT && out.pin < 16;
}

void channelWrite(uint8_t channel, bool state) {
  ChannelMapEntry entry{};
  if (!resolveChannel(channel, entry)) {
    Serial.printf("Channel %u is invalid\n", channel);
    return;
  }
  expanders[entry.expander].pinMode(entry.pin, OUTPUT);
  expanders[entry.expander].digitalWrite(entry.pin, state ? HIGH : LOW);
}

bool channelRead(uint8_t channel) {
  ChannelMapEntry entry{};
  if (!resolveChannel(channel, entry)) {
    return false;
  }
  expanders[entry.expander].pinMode(entry.pin, INPUT);
  return expanders[entry.expander].digitalRead(entry.pin) == HIGH;
}

void initializeExpanders() {
  Wire.begin(PIN_I2C_SDA, PIN_I2C_SCL);
  Wire.setClock(400000); // 400 kHz fast mode

  for (uint8_t i = 0; i < MCP_COUNT; ++i) {
    if (!expanders[i].begin_I2C(MCP_ADDRESSES[i])) {
      Serial.printf("Failed to init MCP23017 at 0x%02X (check power, SDA/SCL pull-ups, and address pins)\n",
                    MCP_ADDRESSES[i]);
    }
    // Default all pins to output-low for deterministic startup
    for (uint8_t pin = 0; pin < 16; ++pin) {
      expanders[i].pinMode(pin, OUTPUT);
      expanders[i].digitalWrite(pin, LOW);
    }
  }

  for (uint8_t i = 0; i < MCP_COUNT; ++i) {
    pinMode(PIN_INT[i], INPUT_PULLUP);
  }
}

void setInitialChannelStates() {
  for (uint8_t ch = MIN_CHANNEL; ch <= USED_CHANNELS; ++ch) {
    channelWrite(ch, false);
  }
}

void performSealProtocol() {
  // Minimal placeholder: pulse the seal channel HIGH for one heartbeat.
  // This blocks for one interval; replace with a non-blocking state machine if concurrent work is required.
  channelWrite(SEAL_CHANNEL, true);
  delay(HEARTBEAT_INTERVAL_MS);
  channelWrite(SEAL_CHANNEL, false);
}

void handleSyncEvent() {
  // Hook for ᛏ:SYNC ritual alignment. Extend with your synchronization or broadcast logic.
}

void heartbeatTick() {
  // Called every HEARTBEAT_INTERVAL_MS. Extend with scheduled rituals or timed channel updates.
}

void processDslCommand(const String &rawCommand) {
  String cmd = rawCommand;
  cmd.trim();
  if (cmd.isEmpty()) {
    return;
  }
  cmd.replace(" ", "");
  cmd.toUpperCase();

  if (cmd.startsWith("ᛏ:SYNC") || cmd.startsWith("SYNC")) {
    handleSyncEvent();
    return;
  }

  if (cmd.startsWith("ᚢ:SEAL") || cmd.startsWith("SEAL")) {
    performSealProtocol();
    return;
  }

  if (cmd.startsWith("ᚠ:WRITE") || cmd.startsWith("WRITE")) {
    int chIdx = cmd.indexOf("CH");
    int eqIdx = cmd.indexOf('=');
    if (chIdx >= 0 && eqIdx > chIdx) {
      String channelToken = cmd.substring(chIdx + 2, eqIdx);
      if (channelToken.isEmpty()) {
        Serial.println("Channel token missing in WRITE command");
        return;
      }
      for (size_t i = 0; i < channelToken.length(); ++i) {
        const char c = channelToken[i];
        if (c < '0' || c > '9') {
          Serial.printf("Channel token '%s' is not numeric\n", channelToken.c_str());
          return;
        }
      }
      long channelLong = channelToken.toInt();
      if (channelLong == 0 && channelToken != "0") {
        Serial.printf("Channel token '%s' could not be parsed\n", channelToken.c_str());
        return;
      }
      int channel = static_cast<int>(channelLong);
      String value = cmd.substring(eqIdx + 1);
      if (channel < MIN_CHANNEL || channel > USED_CHANNELS) {
        Serial.printf("Channel %d out of range (%u-%u)\n", channel, MIN_CHANNEL, USED_CHANNELS);
        return;
      }
      const uint8_t channelId = static_cast<uint8_t>(channel);
      bool high = value.startsWith("HIGH") || value.startsWith("ON") || value == "1";
      channelWrite(channelId, high);
    }
    return;
  }

  Serial.printf("Unrecognized DSL command: %s\n", cmd.c_str());
}

void processSerialInput() {
  while (Serial.available()) {
    String line = Serial.readStringUntil('\n');
    processDslCommand(line);
  }
}

void setup() {
  Serial.begin(115200);
  initializeExpanders();
  setInitialChannelStates();
  Serial.println("Runic-Tamil DSL skeleton ready.");
}

void loop() {
  processSerialInput();

  const unsigned long now = millis();
  if (now - lastTickMs >= HEARTBEAT_INTERVAL_MS) {
    lastTickMs = now;
    heartbeatTick();
  }
}
