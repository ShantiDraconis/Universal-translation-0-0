# Universal Translation 0/0 - Hardware Implementation

This directory contains hardware schematics and firmware for the **54-Channel Ritual Control System** based on ESP32-S3 microcontroller and MCP23017 I²C GPIO expanders.

## Overview

The hardware platform implements the "Runic-Tamil" symbolic framework as physical electronics, bridging ancient symbolic concepts with modern IoT technology.

### Key Features

- **54 Digital Channels** for ritual control
- **ESP32-S3** MCU with Wi-Fi/BLE connectivity
- **4× MCP23017** I²C GPIO expanders (64 total channels, 54 used + 10 reserve)
- **119 Hz Ritual Heartbeat** for synchronized timing
- **Domain-Specific Language (DSL)** interpreter for symbolic commands
- **Seal Protocol** for Channel 54 (final convergence point)
- **Runic/Tamil symbolic naming** alongside technical specifications

## Directory Structure

```
hardware/
├── schematic/
│   └── ESP32-S3_SCHEMATIC_SPECIFICATION.md  # Complete KiCad schematic specification
├── firmware/
│   └── UniversalTranslation_ESP32/
│       └── UniversalTranslation_ESP32.ino   # Arduino firmware skeleton
└── README.md                                # This file
```

## Deliverable 1: Schematic Specification

**File:** `schematic/ESP32-S3_SCHEMATIC_SPECIFICATION.md`

A comprehensive, human-readable text-based specification document that an engineer can use to directly create the electrical schematic in KiCad.

### Contents:
- **Power Tree** - Maps symbolic power grid (ANSUZ/3.3V, JERA/1.8V, THURISAZ/GND, URUZ/5V) to regulators
- **ESP32-S3 MCU Block** - Pin assignments, I²C configuration, interrupt lines
- **4× MCP23017 Blocks** - GPIO expander configuration with unique I²C addresses
- **I²C Bus** - Signal routing, pull-ups, topology
- **Channel Pin Mapping** - Complete table mapping Channels 1-54 to physical pins
- **Net Aliases with Bindrunes** - Symbolic signal names (e.g., I2C_SDA / ᚱ RAIDHO)
- **Bill of Materials (BOM)** - Component list with part numbers
- **Layout Recommendations** - Guidance for PCB design following "Tablet Harappan" aesthetic

### Design Philosophy:
The schematic maintains electrical integrity while incorporating symbolic/ritualistic naming conventions. Each major signal carries both a technical name and a bindrune symbol, allowing the hardware to function as both practical electronics and symbolic artifact.

## Deliverable 2: Firmware Skeleton

**File:** `firmware/UniversalTranslation_ESP32/UniversalTranslation_ESP32.ino`

Ready-to-compile Arduino C++ firmware implementing the complete 54-channel control system.

### Key Components:

#### 1. Channel Abstraction Layer
```cpp
bool channelWrite(uint8_t channel, bool state);  // Write to any channel 1-54
int channelRead(uint8_t channel);                 // Read channel state
void channelWriteAll(bool state);                 // Set all channels at once
```

The firmware automatically translates logical channel numbers (1-54) to the correct MCP23017 chip, port, and pin.

#### 2. DSL Interpreter
Parses and executes Runic-Tamil command strings:

| Command | Description | Example |
|---------|-------------|---------|
| `ᚠ:WRITE CH<n>=HIGH/LOW` | Set channel state | `ᚠ:WRITE CH19=HIGH` |
| `ᚠ:READ CH<n>` | Read channel state | `ᚠ:READ CH32` |
| `ᚢ:ALL_ON` | Activate all channels | `ᚢ:ALL_ON` |
| `ᚢ:ALL_OFF` | Deactivate all channels | `ᚢ:ALL_OFF` |
| `ᚦ:CYCLE <ms> CH<n>` | Pulse channel | `ᚦ:CYCLE 100 CH5` |
| `ᚨ:PATTERN WAVE <start>-<end>` | Wave pattern | `ᚨ:PATTERN WAVE 1-16` |
| `ᛏ:SYNC` | Global synchronization | `ᛏ:SYNC` |
| `ᛊ:SEAL` | Execute Seal Protocol | `ᛊ:SEAL` |

#### 3. Scheduler & Ritual Timing
- **119 Hz tick** (8.403ms period) for system heartbeat
- Configurable ritual timing patterns
- Non-blocking tick handler in main loop

#### 4. Seal Protocol
Multi-phase sequence for Channel 54 (final convergence):
1. **Convergence Phase** - Sequential activation of channels 1-53
2. **Focusing Phase** - Synchronized pulsing of all channels
3. **Final Seal** - Activation of Channel 54 with LED indicator

### Hardware Requirements:
- ESP32-S3-WROOM-1 module (or compatible)
- 4× MCP23017 GPIO expanders
- Adafruit MCP23X17 library
- Arduino IDE or PlatformIO

### Pin Configuration:
| GPIO | Function | Symbol |
|------|----------|--------|
| 8 | I2C SDA | ᚱ RAIDHO |
| 9 | I2C SCL | ᚲ KENAZ |
| 10 | MCP0 Interrupt | ᛁ ISA |
| 11 | MCP1 Interrupt | ᛏ TIWAZ |
| 12 | MCP2 Interrupt | ᛒ BERKANO |
| 13 | MCP3 Interrupt | ᛗ MANNAZ |
| 2 | Status LED | Heartbeat |
| 3 | Seal LED | Channel 54 |

## Getting Started

### Phase 1: Breadboard Prototype (Recommended)

Start with a minimal prototype to validate the core design:

1. **Components Needed:**
   - 1× ESP32-S3 development board
   - 1× MCP23017 (start with just one)
   - Breadboard and jumper wires
   - 2× 4.7kΩ resistors (I²C pull-ups)
   - 2× LEDs and resistors

2. **Connections:**
   ```
   ESP32-S3        MCP23017
   GPIO8  ────────  SDA
   GPIO9  ────────  SCL
   3.3V   ────────  VDD
   GND    ────────  VSS, A0, A1, A2
   ```

3. **Upload Firmware:**
   - Install Arduino IDE
   - Install ESP32 board support
   - Install Adafruit MCP23X17 library
   - Open `UniversalTranslation_ESP32.ino`
   - Select board: "ESP32S3 Dev Module"
   - Upload to board

4. **Test Commands:**
   Open Serial Monitor (115200 baud) and try:
   ```
   ᚠ:WRITE CH1=HIGH
   ᚠ:READ CH1
   ᚢ:ALL_OFF
   ```

### Phase 2: Full System Assembly

Once the prototype is validated:

1. Create the full schematic in KiCad using the specification document
2. Design PCB layout following "Tablet Harappan" aesthetic guidelines
3. Order components from BOM
4. Assemble and test
5. Upload firmware and verify all 54 channels

### Phase 3: Expansion

- Add Wi-Fi connectivity for remote control
- Implement BLE interface for mobile apps
- Add sensors for environmental feedback
- Create custom ritual sequences
- Integrate with web dashboard

## KiCad Workflow

To implement the schematic in KiCad:

1. **Read the Specification:**
   Study `ESP32-S3_SCHEMATIC_SPECIFICATION.md` thoroughly

2. **Create Symbol Libraries:**
   - Add ESP32-S3-WROOM-1 symbol
   - Add MCP23017 symbols (4×)
   - Create custom bindrune annotation symbols

3. **Draw Schematic Pages:**
   - Page 1: Power supply circuit
   - Page 2: ESP32-S3 MCU connections
   - Page 3: MCP23017 expanders
   - Page 4: Channel mapping reference

4. **Label Nets:**
   - Use technical names as primary labels
   - Add bindrune symbols as text annotations
   - Create hierarchical labels for key signals

5. **Generate Outputs:**
   - Run Electrical Rules Check (ERC)
   - Generate netlist for PCB
   - Export BOM

## PCB Layout Guidelines

### Component Placement Zones

Following the "Tablet Harappan" aesthetic:

```
┌─────────────────────────────────────┐
│    BORDER ZONE                      │
│  ┌─────────────────────────────┐   │
│  │   RING ZONE                 │   │
│  │  ┌───────────────────────┐  │   │
│  │  │   CORE ZONE           │  │   │
│  │  │   ┌─────────────┐     │  │   │
│  │  │   │   ESP32-S3  │     │  │   │
│  │  │   │   Regulators│     │  │   │
│  │  │   └─────────────┘     │  │   │
│  │  └───────────────────────┘  │   │
│  │   MCP0  MCP1  MCP2  MCP3    │   │
│  └─────────────────────────────┘   │
│   Connectors, LEDs, USB             │
└─────────────────────────────────────┘
```

- **Core:** ESP32-S3, power regulators
- **Ring:** 4× MCP23017 in cardinal directions
- **Border:** I/O connectors, indicators, USB

### Silkscreen Artwork

Add Harappan tablet design to top silkscreen layer:
- Does not interfere with electrical copper traces
- Can include bindrune symbols near major ICs
- Aesthetic integration with functional design

## Development Recommendations

### Iterative Approach

1. **Minimal Prototype** - 1 ESP32 + 1 MCP23017 on breadboard
2. **Core Logic** - Get basic channel control working
3. **DSL Interpreter** - Test command parsing
4. **Full Assembly** - All 4 expanders, 54 channels
5. **Ritual Sequences** - Implement specific patterns
6. **Connectivity** - Add Wi-Fi/BLE features

### Testing Strategy

- Test each MCP23017 individually before parallel connection
- Verify I²C addresses with scanner sketch
- Test channel mapping with LED array
- Validate DSL commands one at a time
- Measure timing accuracy of 119 Hz tick
- Test Seal Protocol sequence

### Expansion Opportunities

- Use 10 reserve channels for sensors, relays, etc.
- Add SPI devices (LCD display, SD card)
- Implement MQTT for IoT integration
- Create web-based ritual control interface
- Add audio feedback (speaker/buzzer)
- Interface with external lighting or actuators

## Technical Support

### Common Issues

**Problem:** MCP23017 not detected  
**Solution:** Check I²C connections, verify address pins, test with I²C scanner

**Problem:** Channels not responding  
**Solution:** Verify power supply, check MCP23017 initialization, test individual pins

**Problem:** Serial commands not working  
**Solution:** Check baud rate (115200), verify Serial Monitor settings, test simple commands

**Problem:** Timing drift  
**Solution:** Use hardware timers instead of delay(), verify ESP32-S3 clock source

### Library Dependencies

- **Adafruit MCP23X17** - For MCP23017 control  
  Install via Arduino Library Manager: "Adafruit MCP23017"

- **Wire** - Built-in I²C library  
  Included with Arduino IDE

### Resources

- [ESP32-S3 Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/)
- [MCP23017 Datasheet](https://www.microchip.com/en-us/product/MCP23017)
- [KiCad Tutorial](https://docs.kicad.org/master/en/getting_started_in_kicad/getting_started_in_kicad.html)
- [Adafruit MCP23017 Guide](https://learn.adafruit.com/mcp230xx-gpio-expander-on-raspberry-pi)

## License

MIT License - See main repository LICENSE file

Copyright (c) 2025 Universal Translation Project

---

## Symbolic Framework

### Runic Correspondences

The hardware design maps ancient Norse runes to modern electronic functions:

| Rune | Name | Voltage/Signal | Meaning |
|------|------|----------------|---------|
| ᚨ ANSUZ | Divine Breath | 3.3V Power | Life force of the system |
| ᚦ THURISAZ | Thorn/Gateway | Ground | Return path, gateway |
| ᛃ JERA | Harvest/Cycle | 1.8V Power | Cyclical processes |
| ᚢ URUZ | Primal Strength | 5V Input | Raw power source |
| ᚱ RAIDHO | Journey | I2C Data | Data travels this path |
| ᚲ KENAZ | Torch | I2C Clock | Clock illuminates timing |
| ᛊ SOWILO | Sun/Seal | Channel 54 | Final convergence point |

### Tamil Integration

Future revisions will incorporate Tamil script symbols alongside Norse runes, creating a unified symbolic language that bridges Norse, Tamil, and modern technical terminology.

### The 119 Hz Heartbeat

The number 119 carries symbolic significance:
- Prime number (indivisible, fundamental)
- 7 × 17 (combining sacred seven with transformative seventeen)
- Close to 120 (number of completeness in many traditions)
- Creates visible ~1 Hz LED blink (119 ticks = 1 second)

---

**"From ancient symbols to modern silicon, the pathway remains unbroken."**

*Universal Translation 0/0 Hardware Platform*
