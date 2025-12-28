# ESP32-S3 + MCP23017×4 Schematic Specification for KiCad

**Project:** Universal Translation 0/0 - 54-Channel Ritual Control System  
**Platform:** ESP32-S3 + 4× MCP23017 I²C GPIO Expanders  
**Revision:** 1.0  
**Date:** 2025-12-28  

## Table of Contents

1. [System Overview](#system-overview)
2. [Power Tree Architecture](#power-tree-architecture)
3. [ESP32-S3 MCU Block](#esp32-s3-mcu-block)
4. [MCP23017 GPIO Expander Blocks](#mcp23017-gpio-expander-blocks)
5. [I²C Bus Configuration](#i2c-bus-configuration)
6. [Channel Pin Mapping Table](#channel-pin-mapping-table)
7. [Net Aliases and Bindrunes](#net-aliases-and-bindrunes)
8. [Bill of Materials (BOM)](#bill-of-materials-bom)
9. [Design Notes](#design-notes)

---

## System Overview

### Architecture Summary
- **MCU:** ESP32-S3-WROOM-1 (N16R8) - Handles Wi-Fi/BLE, system control, data processing
- **GPIO Expansion:** 4× MCP23017 I²C GPIO Expanders
  - Each provides 16 digital I/O pins
  - Total: 64 channels (54 used + 10 reserve)
- **Communication:** Single I²C bus (SCL/SDA) connects all expanders to MCU
- **Interrupt Lines:** Optional - 4 interrupt lines from expanders to MCU

### Key Design Principles
1. Use symbolic/ritualistic naming alongside technical net names
2. Map ancient runic/Tamil concepts to hardware signals
3. Maintain electrical integrity while supporting aesthetic design
4. 119 Hz system heartbeat for ritual timing

---

## Power Tree Architecture

### Symbolic Power Grid Mapping

The power distribution follows the symbolic runic framework:

| Symbolic Name | Technical Net | Voltage | Current Capacity | Regulator |
|---------------|--------------|---------|------------------|-----------|
| **ANSUZ** (Divine Breath) | VCC_3V3 | 3.3V | 1.5A | AMS1117-3.3 or XC6220 |
| **JERA** (Harvest Cycle) | VCC_1V8 | 1.8V | 300mA | AP2112K-1.8 |
| **THURISAZ** (Gateway) | GND | 0V | N/A | Power Plane |
| **URUZ** (Primal Power) | VBUS | 5V | 2A | USB-C Input |

### Power Supply Schematic Section

```
[USB-C Connector J1]
  VBUS (5V) ───┬─── [Fuse F1: 2A Polyfuse] ───┬─── URUZ (5V Rail)
               │                               │
               │                               ├─── [C1: 10µF] ──┬─── GND (THURISAZ)
               │                               │                 │
               │                               └─── [Regulator U1: AMS1117-3.3]
               │                                        │
               │                                        ├─── ANSUZ (3.3V Rail)
               │                                        │
               │                                        ├─── [C2: 10µF, C3: 100nF] ─── GND
               │                                        │
               │                                        └─── [Regulator U2: AP2112K-1.8]
               │                                                 │
               │                                                 ├─── JERA (1.8V Rail)
               │                                                 │
               │                                                 └─── [C4: 10µF, C5: 100nF] ─── GND
               │
               └─── [Protection Diode D1: Schottky]
```

### Power Distribution

- **ANSUZ (3.3V)** supplies:
  - ESP32-S3 VDD (3.3V)
  - All 4× MCP23017 VDD pins
  - I²C pull-up resistors
  - General digital logic

- **JERA (1.8V)** supplies:
  - ESP32-S3 VDDA (analog power) - Optional, can also use 3.3V
  - Future analog sensors if needed

- **THURISAZ (GND)** - Common ground plane

### Decoupling Capacitors
Each IC requires local decoupling:
- **100nF ceramic** close to each VDD pin
- **10µF tantalum/ceramic** at each IC power entry point
- Power planes with ground stitching vias

---

## ESP32-S3 MCU Block

### ESP32-S3-WROOM-1 Module (U3)

**Package:** Surface Mount Module  
**Memory:** 16MB Flash (N16R8 variant)

### Pin Assignments

#### Power Pins
| Pin | Net Name | Voltage | Description |
|-----|----------|---------|-------------|
| 3V3 | ANSUZ | 3.3V | Main power supply |
| GND | THURISAZ | 0V | Ground (multiple pins) |

#### I²C Bus Pins
| Pin | Net Name | Bindrune | Description |
|-----|----------|----------|-------------|
| GPIO8 | I2C_SDA | ᚱ RAIDHO | I²C Data line (journey/pathway) |
| GPIO9 | I2C_SCL | ᚲ KENAZ | I²C Clock line (torch/knowledge) |

**Note:** Internal pull-ups available, but external 4.7kΩ pull-ups to ANSUZ recommended for reliability.

#### Interrupt Lines (Optional)
| Pin | Net Name | Bindrune | Connected To |
|-----|----------|----------|--------------|
| GPIO10 | MCP_INT0 | ᛁ ISA | MCP23017 #0 INTA |
| GPIO11 | MCP_INT1 | ᛏ TIWAZ | MCP23017 #1 INTA |
| GPIO12 | MCP_INT2 | ᛒ BERKANO | MCP23017 #2 INTA |
| GPIO13 | MCP_INT3 | ᛗ MANNAZ | MCP23017 #3 INTA |

#### Status/Debug LEDs
| Pin | Net Name | Description |
|-----|----------|-------------|
| GPIO2 | LED_STATUS | System heartbeat (119 Hz blink pattern) |
| GPIO3 | LED_SEAL | Channel 54 seal protocol indicator |

#### Bootstrap/Programming Pins
| Pin | Net Name | Description |
|-----|----------|-------------|
| GPIO0 | BOOT | Boot mode select (pull-up, button to GND) |
| EN | nRST | Reset line (pull-up, button to GND) |
| TXD0 | UART_TX | Serial debug output |
| RXD0 | UART_RX | Serial debug input |

#### Reserved/Unused Pins
All other GPIO pins available for future expansion:
- GPIO4-7, GPIO14-48 (check datasheet for strapping pins)
- Some pins have special boot-time requirements

### ESP32-S3 Connections Summary

```
ESP32-S3-WROOM-1 (U3)
┌─────────────────────────────────┐
│                                 │
│  3V3 ◄─────── ANSUZ (3.3V)     │
│  GND ◄─────── THURISAZ (GND)   │
│                                 │
│  GPIO8 (SDA) ─────► I2C_SDA    │
│  GPIO9 (SCL) ─────► I2C_SCL    │
│                                 │
│  GPIO10 ◄───── MCP_INT0        │
│  GPIO11 ◄───── MCP_INT1        │
│  GPIO12 ◄───── MCP_INT2        │
│  GPIO13 ◄───── MCP_INT3        │
│                                 │
│  GPIO2 ─────► LED_STATUS       │
│  GPIO3 ─────► LED_SEAL         │
│                                 │
│  GPIO0 ◄───── BOOT (button)    │
│  EN ◄───────── nRST (button)   │
│                                 │
│  TXD0 ─────► UART_TX           │
│  RXD0 ◄───── UART_RX           │
│                                 │
└─────────────────────────────────┘
```

---

## MCP23017 GPIO Expander Blocks

### MCP23017 Overview
- **Package:** 28-pin DIP or SOIC
- **Interface:** I²C
- **Supply Voltage:** 3.3V (ANSUZ)
- **I/O Ports:** Port A (GPA0-7), Port B (GPB0-7)
- **Interrupt:** INTA, INTB (can be tied together)

### Address Configuration

Each MCP23017 has a unique I²C address set by A0, A1, A2 pins:

| Chip # | Symbol | A2 | A1 | A0 | I²C Address (7-bit) | Hex |
|--------|--------|----|----|----|--------------------|-----|
| MCP0 | ᚠ FEHU (Cattle/Wealth) | GND | GND | GND | 0b0100000 | 0x20 |
| MCP1 | ᚢ URUZ (Aurochs/Strength) | GND | GND | 3V3 | 0b0100001 | 0x21 |
| MCP2 | ᚦ THURISAZ (Thorn/Gate) | GND | 3V3 | GND | 0b0100010 | 0x22 |
| MCP3 | ᚨ ANSUZ (God/Breath) | GND | 3V3 | 3V3 | 0b0100011 | 0x23 |

### MCP23017 Chip #0 (U4) - 0x20

```
MCP23017 (U4) - Address 0x20
┌────────────────────────────────┐
│ Pin  Signal    Channel         │
├────────────────────────────────┤
│ VDD  ◄─────── ANSUZ (3.3V)    │
│ VSS  ◄─────── THURISAZ (GND)  │
│                                │
│ SCL  ◄─────── I2C_SCL         │
│ SDA  ◄──┬──── I2C_SDA         │
│         └──── [4.7kΩ to ANSUZ]│
│                                │
│ A2   ◄─────── GND             │
│ A1   ◄─────── GND             │
│ A0   ◄─────── GND             │
│                                │
│ nRESET ◄───── ANSUZ via 10kΩ  │
│                                │
│ INTA ─────► MCP_INT0          │
│ INTB ─────► (tied to INTA)    │
│                                │
│ === Port A (Output) ===        │
│ GPA0 ─────► CH_01             │
│ GPA1 ─────► CH_02             │
│ GPA2 ─────► CH_03             │
│ GPA3 ─────► CH_04             │
│ GPA4 ─────► CH_05             │
│ GPA5 ─────► CH_06             │
│ GPA6 ─────► CH_07             │
│ GPA7 ─────► CH_08             │
│                                │
│ === Port B (Output) ===        │
│ GPB0 ─────► CH_09             │
│ GPB1 ─────► CH_10             │
│ GPB2 ─────► CH_11             │
│ GPB3 ─────► CH_12             │
│ GPB4 ─────► CH_13             │
│ GPB5 ─────► CH_14             │
│ GPB6 ─────► CH_15             │
│ GPB7 ─────► CH_16             │
└────────────────────────────────┘
```

**Decoupling:** 100nF ceramic capacitor between VDD and VSS, close to IC.

### MCP23017 Chip #1 (U5) - 0x21

```
MCP23017 (U5) - Address 0x21
┌────────────────────────────────┐
│ Address: A2=0, A1=0, A0=1     │
│                                │
│ GPA0-7 ─────► CH_17 to CH_24  │
│ GPB0-7 ─────► CH_25 to CH_32  │
│                                │
│ INTA ─────► MCP_INT1          │
└────────────────────────────────┘
```

### MCP23017 Chip #2 (U6) - 0x22

```
MCP23017 (U6) - Address 0x22
┌────────────────────────────────┐
│ Address: A2=0, A1=1, A0=0     │
│                                │
│ GPA0-7 ─────► CH_33 to CH_40  │
│ GPB0-7 ─────► CH_41 to CH_48  │
│                                │
│ INTA ─────► MCP_INT2          │
└────────────────────────────────┘
```

### MCP23017 Chip #3 (U7) - 0x23

```
MCP23017 (U7) - Address 0x23
┌────────────────────────────────┐
│ Address: A2=0, A1=1, A0=1     │
│                                │
│ GPA0-5 ─────► CH_49 to CH_54  │
│ GPA6-7 ─────► RESERVE_01, 02  │
│ GPB0-7 ─────► RESERVE_03-10   │
│                                │
│ INTA ─────► MCP_INT3          │
└────────────────────────────────┘
```

**Special Note:** Channel 54 (GPA5 on U7) is the **Seal Protocol Channel** - the final convergence point in the ritual system.

---

## I²C Bus Configuration

### Bus Topology

```
       ESP32-S3 (U3)
          │   │
      SDA │   │ SCL
          │   │
    ┌─────┴───┴─────┬─────────┬─────────┬─────────┐
    │               │         │         │         │
    │               │         │         │         │
  MCP0 (U4)      MCP1 (U5)  MCP2 (U6)  MCP3 (U7)  [Pull-ups]
  0x20           0x21       0x22       0x23       4.7kΩ → ANSUZ
```

### I²C Specifications
- **Speed:** 400 kHz (Fast Mode) recommended
- **Pull-up Resistors:** 4.7kΩ (R1, R2) from SDA and SCL to ANSUZ (3.3V)
- **Bus Length:** Keep traces short (<30cm) for reliability
- **Termination:** None required at this speed

### Signal Integrity
- Use ground planes
- Route I²C traces away from noisy signals (PWM, switching)
- Add series resistors (22Ω-47Ω) if needed for ringing/overshoot

---

## Channel Pin Mapping Table

### Complete Channel to Pin Mapping

| Channel | Symbolic Name | MCP Chip | Port | Pin | I²C Addr | Description |
|---------|---------------|----------|------|-----|----------|-------------|
| CH_01 | ᚠ Fehu-01 | MCP0 (U4) | A | 0 | 0x20 | Wealth Gateway 1 |
| CH_02 | ᚠ Fehu-02 | MCP0 (U4) | A | 1 | 0x20 | Wealth Gateway 2 |
| CH_03 | ᚠ Fehu-03 | MCP0 (U4) | A | 2 | 0x20 | Wealth Gateway 3 |
| CH_04 | ᚠ Fehu-04 | MCP0 (U4) | A | 3 | 0x20 | Wealth Gateway 4 |
| CH_05 | ᚠ Fehu-05 | MCP0 (U4) | A | 4 | 0x20 | Wealth Gateway 5 |
| CH_06 | ᚠ Fehu-06 | MCP0 (U4) | A | 5 | 0x20 | Wealth Gateway 6 |
| CH_07 | ᚠ Fehu-07 | MCP0 (U4) | A | 6 | 0x20 | Wealth Gateway 7 |
| CH_08 | ᚠ Fehu-08 | MCP0 (U4) | A | 7 | 0x20 | Wealth Gateway 8 |
| CH_09 | ᚠ Fehu-09 | MCP0 (U4) | B | 0 | 0x20 | Wealth Gateway 9 |
| CH_10 | ᚠ Fehu-10 | MCP0 (U4) | B | 1 | 0x20 | Wealth Gateway 10 |
| CH_11 | ᚠ Fehu-11 | MCP0 (U4) | B | 2 | 0x20 | Wealth Gateway 11 |
| CH_12 | ᚠ Fehu-12 | MCP0 (U4) | B | 3 | 0x20 | Wealth Gateway 12 |
| CH_13 | ᚠ Fehu-13 | MCP0 (U4) | B | 4 | 0x20 | Wealth Gateway 13 |
| CH_14 | ᚠ Fehu-14 | MCP0 (U4) | B | 5 | 0x20 | Wealth Gateway 14 |
| CH_15 | ᚠ Fehu-15 | MCP0 (U4) | B | 6 | 0x20 | Wealth Gateway 15 |
| CH_16 | ᚠ Fehu-16 | MCP0 (U4) | B | 7 | 0x20 | Wealth Gateway 16 |
| CH_17 | ᚢ Uruz-01 | MCP1 (U5) | A | 0 | 0x21 | Strength Channel 1 |
| CH_18 | ᚢ Uruz-02 | MCP1 (U5) | A | 1 | 0x21 | Strength Channel 2 |
| CH_19 | ᚢ Uruz-03 | MCP1 (U5) | A | 2 | 0x21 | Strength Channel 3 |
| CH_20 | ᚢ Uruz-04 | MCP1 (U5) | A | 3 | 0x21 | Strength Channel 4 |
| CH_21 | ᚢ Uruz-05 | MCP1 (U5) | A | 4 | 0x21 | Strength Channel 5 |
| CH_22 | ᚢ Uruz-06 | MCP1 (U5) | A | 5 | 0x21 | Strength Channel 6 |
| CH_23 | ᚢ Uruz-07 | MCP1 (U5) | A | 6 | 0x21 | Strength Channel 7 |
| CH_24 | ᚢ Uruz-08 | MCP1 (U5) | A | 7 | 0x21 | Strength Channel 8 |
| CH_25 | ᚢ Uruz-09 | MCP1 (U5) | B | 0 | 0x21 | Strength Channel 9 |
| CH_26 | ᚢ Uruz-10 | MCP1 (U5) | B | 1 | 0x21 | Strength Channel 10 |
| CH_27 | ᚢ Uruz-11 | MCP1 (U5) | B | 2 | 0x21 | Strength Channel 11 |
| CH_28 | ᚢ Uruz-12 | MCP1 (U5) | B | 3 | 0x21 | Strength Channel 12 |
| CH_29 | ᚢ Uruz-13 | MCP1 (U5) | B | 4 | 0x21 | Strength Channel 13 |
| CH_30 | ᚢ Uruz-14 | MCP1 (U5) | B | 5 | 0x21 | Strength Channel 14 |
| CH_31 | ᚢ Uruz-15 | MCP1 (U5) | B | 6 | 0x21 | Strength Channel 15 |
| CH_32 | ᚢ Uruz-16 | MCP1 (U5) | B | 7 | 0x21 | Strength Channel 16 |
| CH_33 | ᚦ Thurisaz-01 | MCP2 (U6) | A | 0 | 0x22 | Gateway Channel 1 |
| CH_34 | ᚦ Thurisaz-02 | MCP2 (U6) | A | 1 | 0x22 | Gateway Channel 2 |
| CH_35 | ᚦ Thurisaz-03 | MCP2 (U6) | A | 2 | 0x22 | Gateway Channel 3 |
| CH_36 | ᚦ Thurisaz-04 | MCP2 (U6) | A | 3 | 0x22 | Gateway Channel 4 |
| CH_37 | ᚦ Thurisaz-05 | MCP2 (U6) | A | 4 | 0x22 | Gateway Channel 5 |
| CH_38 | ᚦ Thurisaz-06 | MCP2 (U6) | A | 5 | 0x22 | Gateway Channel 6 |
| CH_39 | ᚦ Thurisaz-07 | MCP2 (U6) | A | 6 | 0x22 | Gateway Channel 7 |
| CH_40 | ᚦ Thurisaz-08 | MCP2 (U6) | A | 7 | 0x22 | Gateway Channel 8 |
| CH_41 | ᚦ Thurisaz-09 | MCP2 (U6) | B | 0 | 0x22 | Gateway Channel 9 |
| CH_42 | ᚦ Thurisaz-10 | MCP2 (U6) | B | 1 | 0x22 | Gateway Channel 10 |
| CH_43 | ᚦ Thurisaz-11 | MCP2 (U6) | B | 2 | 0x22 | Gateway Channel 11 |
| CH_44 | ᚦ Thurisaz-12 | MCP2 (U6) | B | 3 | 0x22 | Gateway Channel 12 |
| CH_45 | ᚦ Thurisaz-13 | MCP2 (U6) | B | 4 | 0x22 | Gateway Channel 13 |
| CH_46 | ᚦ Thurisaz-14 | MCP2 (U6) | B | 5 | 0x22 | Gateway Channel 14 |
| CH_47 | ᚦ Thurisaz-15 | MCP2 (U6) | B | 6 | 0x22 | Gateway Channel 15 |
| CH_48 | ᚦ Thurisaz-16 | MCP2 (U6) | B | 7 | 0x22 | Gateway Channel 16 |
| CH_49 | ᚨ Ansuz-01 | MCP3 (U7) | A | 0 | 0x23 | Breath Channel 1 |
| CH_50 | ᚨ Ansuz-02 | MCP3 (U7) | A | 1 | 0x23 | Breath Channel 2 |
| CH_51 | ᚨ Ansuz-03 | MCP3 (U7) | A | 2 | 0x23 | Breath Channel 3 |
| CH_52 | ᚨ Ansuz-04 | MCP3 (U7) | A | 3 | 0x23 | Breath Channel 4 |
| CH_53 | ᚨ Ansuz-05 | MCP3 (U7) | A | 4 | 0x23 | Breath Channel 5 |
| **CH_54** | **ᛊ SEAL (Sowilo)** | **MCP3 (U7)** | **A** | **5** | **0x23** | **Final Convergence** |
| RESERVE_01 | - | MCP3 (U7) | A | 6 | 0x23 | Reserved for expansion |
| RESERVE_02 | - | MCP3 (U7) | A | 7 | 0x23 | Reserved for expansion |
| RESERVE_03-10 | - | MCP3 (U7) | B | 0-7 | 0x23 | Reserved for expansion |

### Firmware Access Pattern

```c
// Example: To control Channel 19 (ᚢ Uruz-03)
// Chip: MCP1 (0x21), Port A, Pin 2
channelWrite(19, HIGH);  // Translates to MCP1.writeGPIO(GPIOA, 2, HIGH)
```

---

## Net Aliases and Bindrunes

### Symbolic Signal Names

KiCad allows double-labeling of nets. Each critical signal has both a technical name and a bindrune symbol:

| Technical Net | Bindrune | Symbol Meaning | Purpose |
|---------------|----------|----------------|---------|
| I2C_SDA | ᚱ RAIDHO | Journey, Pathway | Data travels this path |
| I2C_SCL | ᚲ KENAZ | Torch, Knowledge | Clock illuminates timing |
| MCP_INT0 | ᛁ ISA | Ice, Stillness | Interrupt freeze point |
| MCP_INT1 | ᛏ TIWAZ | Victory, Justice | Interrupt for action |
| MCP_INT2 | ᛒ BERKANO | Birth, Growth | Interrupt for emergence |
| MCP_INT3 | ᛗ MANNAZ | Humanity | Interrupt for human intervention |
| ANSUZ | ᚨ | Divine Breath | 3.3V power - life force |
| THURISAZ | ᚦ | Thorn, Gateway | Ground - return path |
| JERA | ᛃ | Harvest, Cycle | 1.8V - cyclical processes |
| URUZ | ᚢ | Primal Strength | 5V - raw power |

### KiCad Implementation

In the KiCad schematic editor, nets can have custom labels that appear as text annotations:

1. Technical name as the primary net label (e.g., `I2C_SDA`)
2. Bindrune symbol as a text field placed near the trace with the same net property
3. Both names electrically equivalent - purely visual distinction

**Example Net Label:**
```
I2C_SDA / ᚱ RAIDHO
```

This appears on the schematic as both the functional name and symbolic meaning.

---

## Bill of Materials (BOM)

### Core Components

| Ref Des | Qty | Part Number | Description | Package | Notes |
|---------|-----|-------------|-------------|---------|-------|
| U3 | 1 | ESP32-S3-WROOM-1-N16R8 | ESP32-S3 MCU Module | SMD Module | Wi-Fi/BLE, 16MB Flash |
| U4, U5, U6, U7 | 4 | MCP23017-E/SP | 16-bit I²C GPIO Expander | DIP-28 or SOIC-28 | I²C address configurable |
| U1 | 1 | AMS1117-3.3 | 3.3V LDO Regulator | SOT-223 | 1A output |
| U2 | 1 | AP2112K-1.8TRG1 | 1.8V LDO Regulator | SOT-23-5 | 600mA output |
| J1 | 1 | USB4110-GF-A | USB Type-C Connector | SMD | Power + Data |
| F1 | 1 | 0ZCG0200FF2G | Polyfuse 2A | 1206 SMD | Overcurrent protection |
| D1 | 1 | SS34 | Schottky Diode 3A 40V | DO-214AC | Reverse polarity protection |

### Passives

| Type | Qty | Value | Package | Application |
|------|-----|-------|---------|-------------|
| C1, C2, C4 | 3 | 10µF | 0805/1206 | Bulk decoupling (tantalum or ceramic X7R) |
| C3, C5 | 2 | 100nF | 0603 | HF decoupling at regulators |
| C6-C13 | 8 | 100nF | 0603 | Decoupling for MCP23017 (one per chip × 2) |
| C14 | 1 | 100nF | 0603 | ESP32-S3 decoupling |
| R1, R2 | 2 | 4.7kΩ | 0603 | I²C pull-ups |
| R3, R4 | 2 | 10kΩ | 0603 | BOOT and EN pull-ups |
| R5-R8 | 4 | 10kΩ | 0603 | MCP23017 nRESET pull-ups |
| R9, R10 | 2 | 330Ω | 0603 | LED current limiting |

### Indicators & Switches

| Ref Des | Qty | Part | Description |
|---------|-----|------|-------------|
| LED1 | 1 | LED | Status indicator (119 Hz heartbeat) |
| LED2 | 1 | LED | Seal protocol indicator |
| SW1 | 1 | Tactile Switch | BOOT button |
| SW2 | 1 | Tactile Switch | RESET button |

### Optional Components

| Ref Des | Part | Purpose |
|---------|------|---------|
| J2 | 6-pin header | UART debug/programming |
| J3-J6 | 2×8 pin headers | Channel breakout for MCP0-3 |
| TP1-TP10 | Test points | For probing I²C, power rails, interrupts |

---

## Design Notes

### Layout Recommendations

#### Component Placement Zones

Following the "Tablet Harappan" aesthetic:

1. **Core Zone (Center)**
   - ESP32-S3 module (U3)
   - Power regulators (U1, U2)
   - Decoupling capacitors

2. **Ring Zone (Middle)**
   - Four MCP23017 chips arranged in cardinal directions
   - MCP0 (North/ᚠ), MCP1 (East/ᚢ), MCP2 (South/ᚦ), MCP3 (West/ᚨ)

3. **Border Zone (Perimeter)**
   - Channel output connectors/headers
   - LED indicators
   - USB connector
   - Programming header

#### Trace Routing

- **I²C Bus:** Route as a differential-style pair, equal lengths, ground plane underneath
- **Power Planes:** Solid 3.3V (ANSUZ) and GND (THURISAZ) planes with thermal relief for soldering
- **Channel Outputs:** Keep traces short if driving external loads; consider series resistors for protection
- **Silkscreen:** Add bindrune symbols near each major IC for aesthetic/symbolic alignment

#### Grounding Strategy

- Single-point ground connection at USB connector
- Star ground topology for analog/digital separation if using JERA (1.8V)
- Ground stitching vias every 5-10mm around board perimeter
- Ground pour on both top and bottom layers

### Thermal Considerations

- ESP32-S3 can draw up to 500mA during Wi-Fi transmission
- AMS1117 may require heatsinking if input voltage is high (>7V USB source)
- Keep thermal vias under ESP32-S3 shield for better heat dissipation

### Ritual Timing Design

The system is designed around a **119 Hz** base frequency:

- 119 Hz = 8.4ms period (1/119)
- Or alternatively: 119ms cycle (slower ritual cadence)
- Timer interrupt in firmware generates this heartbeat
- Can be used for synchronized channel activation patterns

### Firmware-Hardware Interface

The firmware (Deliverable 2) will:
1. Initialize I²C at 400 kHz
2. Configure all 4 MCP23017 chips
3. Map logical channels (1-54) to physical pins via lookup table
4. Implement DSL interpreter for commands like `ᚠ:WRITE CH19=HIGH`
5. Execute Seal Protocol sequence on Channel 54

### Future Expansion Paths

- 10 reserved channels for additional capabilities
- Unused ESP32-S3 GPIOs for sensors, additional I²C devices
- Add SPI devices if needed (displays, SD card)
- Bluetooth BLE for wireless ritual commands
- Wi-Fi for remote monitoring/control

---

## KiCad Schematic Workflow

### Step-by-Step Implementation

1. **Create New Project**
   - New KiCad project: `Universal_Translation_ESP32_S3.kicad_pro`

2. **Symbol Library Setup**
   - Add ESP32-S3-WROOM-1 symbol (create custom if needed)
   - Add MCP23017 symbols (available in standard libraries)
   - Add regulator symbols
   - Create custom bindrune text symbols for annotations

3. **Schematic Pages**

   **Page 1: Power Supply**
   - Draw USB-C input
   - Add fuse and protection diode
   - Draw AMS1117 regulator circuit for 3.3V
   - Draw AP2112K regulator circuit for 1.8V
   - Label nets: URUZ, ANSUZ, JERA, THURISAZ

   **Page 2: ESP32-S3 MCU**
   - Place ESP32-S3-WROOM-1 symbol
   - Connect power pins
   - Connect I²C pins (GPIO8, GPIO9)
   - Connect interrupt pins (GPIO10-13)
   - Connect UART, BOOT, RESET
   - Add status LEDs on GPIO2, GPIO3

   **Page 3: MCP23017 Expanders**
   - Place all 4 MCP23017 symbols
   - Configure I²C addresses (A0, A1, A2 pins)
   - Connect I²C bus (parallel to all chips)
   - Connect power and reset
   - Connect interrupt lines
   - Label all GPA/GPB pins with channel numbers

   **Page 4: Channel Mapping**
   - Create hierarchical sheet or table showing channel mapping
   - Can be implemented as text table or connector symbols
   - Add bindrune annotations for each channel group

4. **Net Naming**
   - Use consistent net names across all pages
   - Add global labels for I2C_SDA, I2C_SCL
   - Add power symbols: ANSUZ (+3V3), THURISAZ (GND), JERA (+1V8), URUZ (+5V)

5. **Design Rule Check (DRC)**
   - Verify all pins connected
   - Check for net conflicts
   - Verify power connections

6. **Generate Netlist**
   - Export netlist for PCB layout
   - Generate BOM from schematic

7. **Annotations & Documentation**
   - Add title block with project info, revision, date
   - Add notes on each page explaining the symbolic framework
   - Include reference to this specification document

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-28 | Universal Translation Project | Initial schematic specification for ESP32-S3 + MCP23017×4 architecture |

---

## References

- ESP32-S3 Technical Reference Manual: https://www.espressif.com/sites/default/files/documentation/esp32-s3_technical_reference_manual_en.pdf
- MCP23017 Datasheet: https://ww1.microchip.com/downloads/en/devicedoc/20001952c.pdf
- KiCad Documentation: https://docs.kicad.org/
- Elder Futhark Runes: Traditional Norse runic alphabet
- Tamil Script: Classical Tamil linguistic elements

---

**End of Schematic Specification Document**

This document provides the complete blueprint for creating the electrical schematic in KiCad. An engineer can use this specification to directly implement the circuit, place components, route nets, and prepare for PCB layout while maintaining both technical accuracy and symbolic/aesthetic alignment.
