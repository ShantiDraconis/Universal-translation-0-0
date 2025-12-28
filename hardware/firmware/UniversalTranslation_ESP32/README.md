# Arduino Project Configuration
# This is a standard Arduino sketch for ESP32-S3

# Board Configuration:
# - Board: ESP32S3 Dev Module
# - Upload Speed: 921600
# - USB Mode: Hardware CDC and JTAG
# - USB CDC On Boot: Enabled
# - Flash Size: 16MB (128Mb)
# - Partition Scheme: Default 4MB with spiffs
# - PSRAM: QSPI PSRAM

# Required Libraries:
# - Adafruit MCP23X17 (install via Library Manager)

# Installation Steps:
# 1. Install Arduino IDE 2.x or PlatformIO
# 2. Add ESP32 board support: https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html
# 3. Install "Adafruit MCP23X17" library from Library Manager
# 4. Open UniversalTranslation_ESP32.ino
# 5. Select "ESP32S3 Dev Module" from Tools > Board
# 6. Connect ESP32-S3 via USB
# 7. Upload sketch
# 8. Open Serial Monitor at 115200 baud
