# ESP32-S3 + 4× MCP23017 Schematic Specification (KiCad-ready)

This document is a direct handoff for schematic capture in KiCad. It defines the nets, pin-by-pin connectivity, power tree, and channel allocation for a 54-channel system built around an ESP32-S3 and four MCP23017 I²C expanders. Net labels include dual naming (engineering + bindrune) so the runic layer can be placed as graphical symbols on the schematic.

## Core architecture
- **MCU:** ESP32-S3-WROOM-1 (or equivalent ESP32-S3 module).
- **GPIO expansion:** 4× MCP23017 on a single I²C bus, giving 64 GPIOs (54 used, 10 reserved).
- **Bus:** I²C at 3.3 V with shared SCL/SDA and individual address pins.
- **Interrupts:** One interrupt line per expander to the MCU for change notification.

## Power tree (symbolic grid → electrical nets)
- **5 V input (VBUS):** from USB-C or external header.
- **3.3 V rail (`NET_3V3` / ᚨ ANSUZ):** LDO regulator from VBUS (e.g., AP2112K-3.3 or TLV75533). Place 10 µF + 0.1 µF at regulator IN/OUT, plus 0.1 µF close to every IC VDD.
- **1.8 V rail (`NET_1V8` / ᛃ JERA):** optional LDO for peripherals needing 1.8 V. Keep separate net label even if unpopulated.
- **Ground (`NET_GND` / ᚦ THURISAZ):** single ground plane. Tie shield of USB connector to GND via RC/ESD network per connector vendor guidance.
- **ESP32-S3 EN:** 10 kΩ pull-up to ANSUZ; momentary pushbutton to THURISAZ for reset.
- **Boot strap:** GPIO0 10 kΩ pull-up to ANSUZ, optional momentary button to THURISAZ for download mode.

## MCU pin plan (ESP32-S3)
- **I²C:** `NET_I2C_SDA` / ᛟ OTHALA → GPIO8; `NET_I2C_SCL` / ᚱ RAIDHO → GPIO9. 4.7 kΩ pull-ups from both lines to ANSUZ on the MCU sheet.
- **Expander interrupts:**  
  - `NET_INT_U1` / ᚾ NAUTHIZ → GPIO4  
  - `NET_INT_U2` / ᛇ EIHWAZ → GPIO5  
  - `NET_INT_U3` / ᛃ JERA → GPIO6  
  - `NET_INT_U4` / ᛗ MANNAZ → GPIO7  
  Configure INT pins as open-drain with 10 kΩ pull-ups to ANSUZ.
- **UART0 for programming:** U0TXD → GPIO43, U0RXD → GPIO44 routed to USB-UART bridge or header.
- **Seal trigger (optional redundancy):** `NET_SEAL_CH54` / ᛝ INGWAZ also broken out to a test pad.
- Keep unused GPIOs on a test header for future features; label with electrical and bindrune names.

## MCP23017 blocks (U1–U4)
- **Addresses (A2..A0):**
  - U1 @ `0x20`: A2=0, A1=0, A0=0
  - U2 @ `0x21`: A2=0, A1=0, A0=1
  - U3 @ `0x22`: A2=0, A1=1, A0=0
  - U4 @ `0x23`: A2=0, A1=1, A0=1
- **Power:** VDD to ANSUZ; VSS to THURISAZ. 0.1 µF decoupling at each VDD.
- **RESET:** tie to ANSUZ through 10 kΩ; optional test pad for manual reset.
- **INTA/INTB:** tie together per device and route to the MCU pins listed above.
- **I²C:** all share NET_I2C_SCL/NET_I2C_SDA.

## Channel pin mapping (54 used + 10 reserve)
All channels default to push-pull outputs driven low at boot. Ports are MCP23017 `GPAx/GPBx`.

| Channel | Expander (Addr) | Port.Pin | Net Alias (engineering / bindrune) | Notes |
|---------|-----------------|----------|------------------------------------|-------|
| 1  | U1 (0x20) | GPA0 | NET_CH01 / ᚠ FEHU | |
| 2  | U1 (0x20) | GPA1 | NET_CH02 / ᚢ URUZ | |
| 3  | U1 (0x20) | GPA2 | NET_CH03 / ᚦ THURISAZ | |
| 4  | U1 (0x20) | GPA3 | NET_CH04 / ᚨ ANSUZ | |
| 5  | U1 (0x20) | GPA4 | NET_CH05 / ᚱ RAIDHO | |
| 6  | U1 (0x20) | GPA5 | NET_CH06 / ᚲ KAUNAN | |
| 7  | U1 (0x20) | GPA6 | NET_CH07 / ᚷ GEBO | |
| 8  | U1 (0x20) | GPA7 | NET_CH08 / ᚹ WUNJO | |
| 9  | U1 (0x20) | GPB0 | NET_CH09 / ᚺ HAGALAZ | |
| 10 | U1 (0x20) | GPB1 | NET_CH10 / ᚾ NAUTHIZ | |
| 11 | U1 (0x20) | GPB2 | NET_CH11 / ᛁ ISA | |
| 12 | U1 (0x20) | GPB3 | NET_CH12 / ᛃ JERA | |
| 13 | U1 (0x20) | GPB4 | NET_CH13 / ᛇ EIHWAZ | |
| 14 | U1 (0x20) | GPB5 | NET_CH14 / ᛈ PERTHRO | |
| 15 | U1 (0x20) | GPB6 | NET_CH15 / ᛉ ALGIZ | |
| 16 | U1 (0x20) | GPB7 | NET_CH16 / ᛊ SOWILO | |
| 17 | U2 (0x21) | GPA0 | NET_CH17 / ᛏ TIWAZ | |
| 18 | U2 (0x21) | GPA1 | NET_CH18 / ᛒ BERKANO | |
| 19 | U2 (0x21) | GPA2 | NET_CH19 / ᛖ EHWAZ | |
| 20 | U2 (0x21) | GPA3 | NET_CH20 / ᛗ MANNAZ | |
| 21 | U2 (0x21) | GPA4 | NET_CH21 / ᛚ LAGUZ | |
| 22 | U2 (0x21) | GPA5 | NET_CH22 / ᛜ INGWAZ | |
| 23 | U2 (0x21) | GPA6 | NET_CH23 / ᛞ DAGAZ | |
| 24 | U2 (0x21) | GPA7 | NET_CH24 / ᛟ OTHALA | |
| 25 | U2 (0x21) | GPB0 | NET_CH25 / ᚠ FEHU2 | |
| 26 | U2 (0x21) | GPB1 | NET_CH26 / ᚢ URUZ2 | |
| 27 | U2 (0x21) | GPB2 | NET_CH27 / ᚦ THURISAZ2 | |
| 28 | U2 (0x21) | GPB3 | NET_CH28 / ᚨ ANSUZ2 | |
| 29 | U2 (0x21) | GPB4 | NET_CH29 / ᚱ RAIDHO2 | |
| 30 | U2 (0x21) | GPB5 | NET_CH30 / ᚲ KAUNAN2 | |
| 31 | U2 (0x21) | GPB6 | NET_CH31 / ᚷ GEBO2 | |
| 32 | U2 (0x21) | GPB7 | NET_CH32 / ᚹ WUNJO2 | |
| 33 | U3 (0x22) | GPA0 | NET_CH33 / ᚺ HAGALAZ2 | |
| 34 | U3 (0x22) | GPA1 | NET_CH34 / ᚾ NAUTHIZ2 | |
| 35 | U3 (0x22) | GPA2 | NET_CH35 / ᛁ ISA2 | |
| 36 | U3 (0x22) | GPA3 | NET_CH36 / ᛃ JERA2 | |
| 37 | U3 (0x22) | GPA4 | NET_CH37 / ᛇ EIHWAZ2 | |
| 38 | U3 (0x22) | GPA5 | NET_CH38 / ᛈ PERTHRO2 | |
| 39 | U3 (0x22) | GPA6 | NET_CH39 / ᛉ ALGIZ2 | |
| 40 | U3 (0x22) | GPA7 | NET_CH40 / ᛊ SOWILO2 | |
| 41 | U3 (0x22) | GPB0 | NET_CH41 / ᛏ TIWAZ2 | |
| 42 | U3 (0x22) | GPB1 | NET_CH42 / ᛒ BERKANO2 | |
| 43 | U3 (0x22) | GPB2 | NET_CH43 / ᛖ EHWAZ2 | |
| 44 | U3 (0x22) | GPB3 | NET_CH44 / ᛗ MANNAZ2 | |
| 45 | U3 (0x22) | GPB4 | NET_CH45 / ᛚ LAGUZ2 | |
| 46 | U3 (0x22) | GPB5 | NET_CH46 / ᛜ INGWAZ2 | |
| 47 | U3 (0x22) | GPB6 | NET_CH47 / ᛞ DAGAZ2 | |
| 48 | U3 (0x22) | GPB7 | NET_CH48 / ᛟ OTHALA2 | |
| 49 | U4 (0x23) | GPA0 | NET_CH49 / ᚠ FEHU3 | |
| 50 | U4 (0x23) | GPA1 | NET_CH50 / ᚢ URUZ3 | |
| 51 | U4 (0x23) | GPA2 | NET_CH51 / ᚦ THURISAZ3 | |
| 52 | U4 (0x23) | GPA3 | NET_CH52 / ᚨ ANSUZ3 | |
| 53 | U4 (0x23) | GPA4 | NET_CH53 / ᚱ RAIDHO3 | |
| 54 | U4 (0x23) | GPA5 | NET_CH54 / ᛜ INGWAZ3 (Seal) | Seal protocol channel |
| R1 | U4 (0x23) | GPA6 | NET_RES1 / ᛞ DAGAZ3 | Reserve |
| R2 | U4 (0x23) | GPA7 | NET_RES2 / ᛟ OTHALA3 | Reserve |
| R3–R10 | U4 (0x23) | GPB0–GPB7 | NET_RES3–NET_RES10 | Reserve bank |

## Sheet and net labeling guidance
- Use a hierarchical sheet for each MCP23017 block; reuse a symbol with fields for address and reference.
- Apply the dual labels (e.g., `NET_I2C_SCL` and ᚱ RAIDHO) to the same net in KiCad. The bindrune can be added via a graphic text on the sheet.
- Place test pads on I²C, INT lines, and the seal channel (CH54).
- Keep I²C traces short and routed as a bus; place pull-ups near the MCU.

## Minimal bring-up sequence
1. Power rails up (ANSUZ 3.3 V stable), then EN released.
2. MCU boots, configures I²C @ 400 kHz.
3. Probe expanders at 0x20–0x23; set all GPIOs as outputs LOW.
4. Assert Seal channel (CH54) only after DSL/ritual logic is ready.

## Notes for PCB layout
- Group expanders physically by channel ranges (CH1–16, 17–32, 33–48, 49–54 + reserve).
- Keep decoupling capacitors adjacent to each MCP23017 VDD pin.
- Maintain a continuous GND plane; avoid splitting under the I²C bus.
- Use the top silkscreen for Harappan tablet artwork; ensure DRC clearance from copper.
