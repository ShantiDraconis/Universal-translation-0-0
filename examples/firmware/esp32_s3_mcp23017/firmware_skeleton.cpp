#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MCP23X17.h>
#include <limits.h>

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
constexpr uint8_t PIN_MODE_UNKNOWN = 0xFF;
uint8_t pinModeCache[MCP_COUNT][16];

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
struct SealController {
  bool active;
  unsigned long startMs;
} sealController{false, 0};

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
  if (pinModeCache[entry.expander][entry.pin] != OUTPUT) {
    expanders[entry.expander].pinMode(entry.pin, OUTPUT);
    pinModeCache[entry.expander][entry.pin] = OUTPUT;
  }
  expanders[entry.expander].digitalWrite(entry.pin, state ? HIGH : LOW);
}

bool channelRead(uint8_t channel) {
  ChannelMapEntry entry{};
  if (!resolveChannel(channel, entry)) {
    return false;
  }
  if (pinModeCache[entry.expander][entry.pin] != INPUT) {
    expanders[entry.expander].pinMode(entry.pin, INPUT);
    pinModeCache[entry.expander][entry.pin] = INPUT;
  }
  return expanders[entry.expander].digitalRead(entry.pin) == HIGH;
}

void initializeExpanders() {
  Wire.begin(PIN_I2C_SDA, PIN_I2C_SCL);
  Wire.setClock(400000); // 400 kHz fast mode
  for (uint8_t i = 0; i < MCP_COUNT; ++i) {
    for (uint8_t pin = 0; pin < 16; ++pin) {
      pinModeCache[i][pin] = PIN_MODE_UNKNOWN;
    }
  }

  for (uint8_t i = 0; i < MCP_COUNT; ++i) {
    if (!expanders[i].begin_I2C(MCP_ADDRESSES[i])) {
      Serial.printf("Failed to init MCP23017 at 0x%02X (check power, SDA/SCL pull-ups, and address pins)\n",
                    MCP_ADDRESSES[i]);
      continue;
    }
    // Default all pins to output-low for deterministic startup
    for (uint8_t pin = 0; pin < 16; ++pin) {
      expanders[i].pinMode(pin, OUTPUT);
      expanders[i].digitalWrite(pin, LOW);
      pinModeCache[i][pin] = OUTPUT;
    }
  }

  for (uint8_t i = 0; i < MCP_COUNT; ++i) {
    pinMode(PIN_INT[i], INPUT_PULLUP);
  }
}

void setInitialChannelStates() {
  for (uint8_t ch = MIN_CHANNEL; ch <= USED_CHANNELS; ++ch) {
    ChannelMapEntry entry{};
    if (!resolveChannel(ch, entry)) {
      continue;
    }
    expanders[entry.expander].digitalWrite(entry.pin, LOW);
    pinModeCache[entry.expander][entry.pin] = OUTPUT;
  }
}

void performSealProtocol() {
  // Minimal placeholder: begin a non-blocking pulse on the seal channel.
  if (sealController.active) {
    return;
  }
  sealController.startMs = millis();
  sealController.active = true;
  channelWrite(SEAL_CHANNEL, true);
}

void serviceSealProtocol() {
  if (!sealController.active) {
    return;
  }
  if (static_cast<unsigned long>(millis() - sealController.startMs) >= HEARTBEAT_INTERVAL_MS) {
    channelWrite(SEAL_CHANNEL, false);
    sealController.active = false;
  }
}

void handleSyncEvent() {
  // Hook for ᛏ:SYNC ritual alignment. Extend with your synchronization or broadcast logic.
}

void heartbeatTick() {
  // Called every HEARTBEAT_INTERVAL_MS. Extend with scheduled rituals or timed channel updates.
  serviceSealProtocol();
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
    int keywordPos = cmd.indexOf("WRITE");
    int chIdx = keywordPos >= 0 ? cmd.indexOf("CH", keywordPos) : -1;
    int eqIdx = chIdx >= 0 ? cmd.indexOf('=', chIdx) : -1;
    if (keywordPos < 0 || chIdx < 0 || eqIdx <= chIdx) {
      Serial.println("WRITE command format invalid. Use WRITECH##=HIGH|LOW");
      return;
    }
    {
      String channelToken = cmd.substring(chIdx + 2, eqIdx);
      if (channelToken.isEmpty()) {
        Serial.println("Channel token missing in WRITE command");
        return;
      }
      unsigned long channelLong = 0;
      bool overflowed = false;
      for (size_t i = 0; i < channelToken.length(); ++i) {
        const char c = channelToken[i];
        if (c < '0' || c > '9') {
          Serial.printf("Channel token '%s' is not numeric\n", channelToken.c_str());
          return;
        }
        const uint8_t digit = static_cast<uint8_t>(c - '0');
        if (channelLong > (ULONG_MAX - digit) / 10) {
          overflowed = true;
          break;
        }
        channelLong = (channelLong * 10) + digit;
      }
      if (overflowed) {
        Serial.printf("Channel token '%s' is too large\n", channelToken.c_str());
        return;
      }
      if (channelLong < MIN_CHANNEL || channelLong > USED_CHANNELS) {
        Serial.printf("Channel %lu out of range (%u-%u)\n", channelLong, MIN_CHANNEL, USED_CHANNELS);
        return;
      }
      const uint8_t channelId = static_cast<uint8_t>(channelLong);
      String value = cmd.substring(eqIdx + 1);
      bool high = false;
      if (value.startsWith("HIGH") || value.startsWith("ON") || value == "1") {
        high = true;
      } else if (value.startsWith("LOW") || value.startsWith("OFF") || value == "0") {
        high = false;
      } else {
        Serial.printf("Value '%s' not recognized. Use HIGH/LOW.\n", value.c_str());
        return;
      }
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
  if (static_cast<unsigned long>(now - lastTickMs) >= HEARTBEAT_INTERVAL_MS) {
    lastTickMs = now;
    heartbeatTick();
  }
}
