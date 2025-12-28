# Getting Started - Building Your First Prototype

## Quick Start Guide for the 54-Channel Ritual Control System

This guide will walk you through building a minimal working prototype of the Universal Translation 0/0 hardware platform.

---

## 🎯 Goal

Build a working prototype with:
- 1× ESP32-S3 development board
- 1× MCP23017 GPIO expander
- Control of 16 channels (expandable to 54)
- Functional DSL command interpreter

**Time Required:** 2-3 hours  
**Skill Level:** Intermediate (basic electronics & Arduino experience)

---

## 📦 Bill of Materials (Minimal Prototype)

### Core Components

| Item | Quantity | Approx. Cost | Source |
|------|----------|--------------|--------|
| ESP32-S3 DevKit | 1 | $8-15 | AliExpress, Amazon, Adafruit |
| MCP23017 | 1 | $1-3 | Mouser, DigiKey, eBay |
| Breadboard (830 points) | 1 | $3-5 | Amazon, local electronics |
| Jumper wires (M-M) | 20+ | $3-8 | Amazon, local electronics |
| USB-C cable | 1 | $3-8 | Amazon, local electronics |

### Resistors

| Value | Quantity | Purpose |
|-------|----------|---------|
| 4.7kΩ | 2 | I²C pull-ups |
| 330Ω | 2 | LED current limiting |

### LEDs

| Type | Quantity | Purpose |
|------|----------|---------|
| Red LED | 1 | Status/heartbeat |
| Green LED | 1 | Seal indicator |
| Any color LEDs | 8-16 | Channel outputs (optional) |

### Optional Components

| Item | Purpose |
|------|---------|
| Logic analyzer | Debug I²C communication |
| Multimeter | Verify voltages |
| Oscilloscope | Verify 119 Hz timing |

**Total Cost:** ~$20-40 USD (excluding optional items)

---

## 🔧 Hardware Assembly

### Step 1: Understand the Pin Mapping

#### ESP32-S3 Connections

```
ESP32-S3 DevKit
┌─────────────────┐
│                 │
│  GPIO8  ────────┼──── I2C SDA (to MCP23017)
│  GPIO9  ────────┼──── I2C SCL (to MCP23017)
│  GPIO2  ────────┼──── Status LED (via 330Ω)
│  GPIO3  ────────┼──── Seal LED (via 330Ω)
│  3.3V   ────────┼──── Power (+3.3V rail)
│  GND    ────────┼──── Ground (GND rail)
│                 │
└─────────────────┘
```

#### MCP23017 Pinout (28-pin DIP)

```
       MCP23017
    ┌────────────┐
GPB0│1        28 │GPA7
GPB1│2        27 │GPA6
GPB2│3        26 │GPA5
GPB3│4        25 │GPA4
GPB4│5        24 │GPA3
GPB5│6        23 │GPA2
GPB6│7        22 │GPA1
GPB7│8        21 │GPA0
VDD │9        20 │INTA
VSS │10       19 │INTB
 NC │11       18 │RESET (active low)
SCL │12       17 │A2 (address)
SDA │13       16 │A1 (address)
 NC │14       15 │A0 (address)
    └────────────┘
```

### Step 2: Breadboard Layout

```
Power Rails (Red = +3.3V, Blue/Black = GND)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                              
    [4.7kΩ]       [4.7kΩ]                    Pull-up resistors
       │             │                         to +3.3V
       ├─────────────┤                        
       │             │                        
   ═══╪═════════════╪═══ +3.3V Rail          
       │             │                        
     SDA           SCL   ← I²C bus            
       │             │                        
   ┌───┴─────────────┴───┐                   
   │   ESP32-S3 DevKit   │                   
   │                     │                   
   │  GPIO8→SDA  GPIO2→  │──[330Ω]──[LED]──GND  Status
   │  GPIO9→SCL  GPIO3→  │──[330Ω]──[LED]──GND  Seal
   │  3.3V       GND     │                   
   └─┬────────────┬──────┘                   
     │            │                           
     │   ┌────────┴────────┐                 
     │   │    MCP23017     │                 
     │   │                 │                 
     └───│9 (VDD)   28(GPA7)│──[LED]──GND   Optional: LED on
         │10(VSS)   27(GPA6)│──[LED]──GND   each output to
         │12(SCL)←  26(GPA5)│──[LED]──GND   visualize channel
         │13(SDA)←  25(GPA4)│──[LED]──GND   states
         │15(A0)    ...     │                
         │16(A1)    21(GPA0)│──[LED]──GND   
         │17(A2)    ...     │                
         │18(RST)←  8(GPB7) │                
         └──┬───────────────┘                
            │                                 
          ═══════════════════ GND Rail        
```

### Step 3: Detailed Wiring Instructions

#### Power & Ground
1. Connect ESP32-S3 **3.3V** pin to breadboard **positive (+) rail**
2. Connect ESP32-S3 **GND** pin to breadboard **negative (-) rail**
3. Connect MCP23017 **pin 9 (VDD)** to **+3.3V rail**
4. Connect MCP23017 **pin 10 (VSS)** to **GND rail**

#### I²C Bus
5. Connect ESP32-S3 **GPIO8** to MCP23017 **pin 13 (SDA)**
6. Connect ESP32-S3 **GPIO9** to MCP23017 **pin 12 (SCL)**
7. Connect **4.7kΩ resistor** from SDA to **+3.3V rail**
8. Connect **4.7kΩ resistor** from SCL to **+3.3V rail**

#### MCP23017 Configuration
9. Connect MCP23017 **pin 15 (A0)** to **GND** (address 0x20)
10. Connect MCP23017 **pin 16 (A1)** to **GND** (address 0x20)
11. Connect MCP23017 **pin 17 (A2)** to **GND** (address 0x20)
12. Connect MCP23017 **pin 18 (RESET)** to **+3.3V** (always active)

#### Status LEDs
13. Connect ESP32-S3 **GPIO2** → **330Ω resistor** → **Red LED (+)** → **GND**
14. Connect ESP32-S3 **GPIO3** → **330Ω resistor** → **Green LED (+)** → **GND**

#### Channel Output LEDs (Optional)
15. For each MCP23017 output you want to visualize:
    - Connect **GPA0-7** or **GPB0-7** → **LED (+)** → **GND**
    - Or use a LED bar graph module
    - Note: MCP23017 can source up to 25mA per pin (enough for LED)

### Step 4: Visual Inspection Checklist

Before powering on:
- [ ] All power connections correct (3.3V and GND)
- [ ] I²C pull-up resistors installed (4.7kΩ to 3.3V)
- [ ] SDA and SCL connected correctly
- [ ] MCP23017 address pins (A0, A1, A2) all connected to GND
- [ ] MCP23017 RESET pin connected to 3.3V
- [ ] No short circuits between power rails
- [ ] LED polarity correct (long leg = +, short leg = -)

---

## 💻 Software Setup

### Step 1: Install Arduino IDE

1. Download Arduino IDE 2.x from: https://www.arduino.cc/en/software
2. Install and launch Arduino IDE

### Step 2: Install ESP32 Board Support

1. Open **File → Preferences**
2. In "Additional Boards Manager URLs", add:
   ```
   https://espressif.github.io/arduino-esp32/package_esp32_index.json
   ```
3. Click **OK**
4. Open **Tools → Board → Boards Manager**
5. Search for "esp32"
6. Install **"esp32" by Espressif Systems** (latest version)

### Step 3: Install Required Library

1. Open **Tools → Manage Libraries**
2. Search for "Adafruit MCP23017"
3. Install **"Adafruit MCP23X17"** library
4. Click **Install All** if prompted for dependencies

### Step 4: Open the Firmware

1. Navigate to: `hardware/firmware/UniversalTranslation_ESP32/`
2. Open: `UniversalTranslation_ESP32.ino`
3. Or use **File → Open** in Arduino IDE

### Step 5: Configure Board Settings

1. **Tools → Board** → Select **"ESP32S3 Dev Module"**
2. **Tools → Upload Speed** → **921600**
3. **Tools → USB CDC On Boot** → **Enabled**
4. **Tools → Port** → Select your ESP32-S3 port (COM3, /dev/ttyUSB0, etc.)

### Step 6: Compile and Upload

1. Click **Verify** (✓) button to compile
2. Check for any errors in the output window
3. If compilation succeeds, click **Upload** (→) button
4. Wait for upload to complete (~30 seconds)

### Step 7: Open Serial Monitor

1. Click **Serial Monitor** button (top-right)
2. Set baud rate to **115200**
3. Set line ending to **Newline** or **Both NL & CR**
4. You should see the startup banner:

```
╔═══════════════════════════════════════════════════════════╗
║   Universal Translation 0/0 - ESP32-S3 Firmware          ║
║   54-Channel Ritual Control System                       ║
║   I = 0/0 (Indeterminate Operator)                       ║
╚═══════════════════════════════════════════════════════════╝

Initializing I²C bus...
Initializing MCP0 (ᚠ FEHU) at 0x20... OK
...
System initialized successfully!
```

---

## ✅ Testing & Verification

### Test 1: I²C Communication

**Expected Result:** MCP23017 initialization should show "OK"

**Troubleshooting:**
- If "FAILED" appears:
  - Check I²C wiring (SDA, SCL)
  - Verify pull-up resistors installed
  - Check MCP23017 power (VDD, VSS)
  - Verify address pins (A0, A1, A2) all at GND

### Test 2: LED Heartbeat

**Expected Result:** Red LED blinks at ~1 Hz

**Command:** (automatic on startup)

**Troubleshooting:**
- If no blink: Check LED polarity and 330Ω resistor
- If blink too fast/slow: Normal, timing may vary slightly

### Test 3: Basic Channel Control

**Commands to try:**
```
FEHU:WRITE CH1=HIGH
FEHU:READ CH1
FEHU:WRITE CH1=LOW
```

**Expected Result:**
- "OK" response after each command
- If channel LED connected: should turn on/off

### Test 4: All Channels Test

**Commands:**
```
URUZ:ALL_ON
(wait 2 seconds)
URUZ:ALL_OFF
```

**Expected Result:**
- All connected channel LEDs turn on, then off
- Status messages in serial monitor

### Test 5: Wave Pattern

**Command:**
```
ANSUZ:PATTERN WAVE 1-8
```

**Expected Result:**
- Sequential activation of channels 1-8
- If LEDs connected: cascading light effect

### Test 6: Pulse Test

**Command:**
```
THURISAZ:CYCLE 1000 CH1
```

**Expected Result:**
- Channel 1 pulses for 1 second
- Returns to OFF state

---

## 🐛 Troubleshooting Common Issues

### Issue: MCP23017 Not Detected

**Symptoms:** "FAILED" during initialization

**Solutions:**
1. Run I²C scanner sketch (Examples → Wire → i2c_scanner)
2. Verify address 0x20 appears
3. Check wiring: SDA, SCL, VDD, VSS, A0-A2
4. Verify pull-up resistors installed (4.7kΩ)
5. Try different I²C speed: Change `I2C_FREQUENCY` to `100000` (100 kHz)

### Issue: Serial Monitor Shows Garbage

**Solutions:**
1. Set baud rate to exactly **115200**
2. Try different USB cable
3. Check board selection (must be ESP32S3 Dev Module)
4. Press RESET button on ESP32-S3

### Issue: Upload Fails

**Symptoms:** "Failed to connect" or timeout errors

**Solutions:**
1. Hold **BOOT** button on ESP32-S3 while uploading
2. Press **RESET** after upload completes
3. Try different USB port
4. Reduce upload speed: **Tools → Upload Speed → 115200**
5. Install CH340/CP2102 USB drivers if needed

### Issue: Commands Not Recognized

**Symptoms:** "ERROR: Invalid command format"

**Solutions:**
1. Check command syntax exactly (case-sensitive)
2. Ensure colon (`:`) separator present
3. Use ASCII names if rune characters don't work: `FEHU:WRITE CH1=HIGH`
4. Check line ending in Serial Monitor (Newline or Both)

### Issue: Channels Don't Respond

**Solutions:**
1. Verify MCP23017 initialized successfully
2. Check channel number is 1-16 for single MCP
3. Measure MCP23017 output pins with multimeter
4. Try reading channel state: `FEHU:READ CH1`

---

## 📈 Next Steps - Expanding to 54 Channels

Once your prototype is working:

### Add Second MCP23017 (Channels 17-32)

1. Insert second MCP23017 on breadboard
2. Wire power, I²C, and RESET same as first
3. Configure address pins:
   - A0 = **3.3V** (different from first)
   - A1 = **GND**
   - A2 = **GND**
   - This sets address to 0x21
4. Upload firmware (already supports 4× MCP23017)
5. Test: `FEHU:WRITE CH17=HIGH`

### Add Third MCP23017 (Channels 33-48)

Address configuration:
- A0 = **GND**
- A1 = **3.3V**
- A2 = **GND**
- Address: 0x22

### Add Fourth MCP23017 (Channels 49-54)

Address configuration:
- A0 = **3.3V**
- A1 = **3.3V**
- A2 = **GND**
- Address: 0x23

### Design Custom PCB

Follow instructions in:
- `schematic/ESP32-S3_SCHEMATIC_SPECIFICATION.md`
- Use KiCad to create schematic and PCB layout
- Order from PCB manufacturer (JLCPCB, PCBWay, etc.)

---

## 📚 Additional Resources

### Documentation
- Hardware Overview: `hardware/README.md`
- DSL Command Reference: `firmware/DSL_COMMAND_REFERENCE.md`
- Schematic Spec: `schematic/ESP32-S3_SCHEMATIC_SPECIFICATION.md`

### Datasheets
- [ESP32-S3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)
- [MCP23017 Datasheet](https://ww1.microchip.com/downloads/en/devicedoc/20001952c.pdf)

### Libraries
- [Adafruit MCP23X17 Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)
- [ESP32 Arduino Core](https://github.com/espressif/arduino-esp32)

---

## 🎓 Learning Resources

### Arduino & ESP32
- [Arduino Getting Started](https://www.arduino.cc/en/Guide)
- [ESP32 Tutorial](https://randomnerdtutorials.com/getting-started-with-esp32/)

### I²C Communication
- [I²C Tutorial](https://learn.sparkfun.com/tutorials/i2c)
- [Understanding Pull-up Resistors](https://learn.sparkfun.com/tutorials/pull-up-resistors)

### Electronics Basics
- [Breadboard Tutorial](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [LED Basics](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

---

## 💡 Tips for Success

1. **Start Simple:** Get one channel working before expanding
2. **Test Incrementally:** Verify each connection before powering on
3. **Use Serial Monitor:** Watch for initialization messages
4. **Check Voltages:** Use multimeter to verify 3.3V supply
5. **Document Changes:** Keep notes on any modifications
6. **Join Community:** Share your progress on GitHub issues

---

## 🎉 Congratulations!

You now have a working prototype of the Universal Translation 0/0 hardware platform!

**What you've achieved:**
- ✅ Built functional ESP32-S3 + MCP23017 system
- ✅ Installed and compiled firmware
- ✅ Controlled digital channels via DSL commands
- ✅ Established foundation for 54-channel system

**Next:**
- Experiment with ritual sequences
- Add more MCP23017 chips for full 54 channels
- Design custom PCB with symbolic artwork
- Integrate Wi-Fi/BLE connectivity
- Create your own DSL commands

---

**"Every great system begins with a single channel."**

*Universal Translation 0/0 - Getting Started Guide v1.0*
