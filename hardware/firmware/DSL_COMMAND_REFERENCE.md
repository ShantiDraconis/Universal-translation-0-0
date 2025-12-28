# Runic-Tamil DSL Command Reference Card

## Quick Reference for 54-Channel Control System

### Command Format
```
<RUNE_PREFIX>:<COMMAND> [ARGUMENTS]
```

### Available Rune Prefixes

| Rune | ASCII | Domain | Purpose |
|------|-------|--------|---------|
| ᚠ | FEHU | Control | Basic channel operations |
| ᚢ | URUZ | Power | Bulk/power operations |
| ᚦ | THURISAZ | Timing | Timing and cycling |
| ᚨ | ANSUZ | Pattern | Patterns and waves |
| ᛏ | TIWAZ | Sync | Synchronization |
| ᛊ | SEAL/SOWILO | Ritual | Seal protocol (CH54) |

---

## ᚠ FEHU Commands - Basic Control

### Write Channel State
```
ᚠ:WRITE CH<n>=HIGH
ᚠ:WRITE CH<n>=LOW
FEHU:WRITE CH<n>=HIGH
```

**Examples:**
- `ᚠ:WRITE CH1=HIGH` - Turn on channel 1
- `ᚠ:WRITE CH19=LOW` - Turn off channel 19
- `FEHU:WRITE CH54=HIGH` - Activate seal channel

### Read Channel State
```
ᚠ:READ CH<n>
FEHU:READ CH<n>
```

**Examples:**
- `ᚠ:READ CH32` - Read state of channel 32
- `FEHU:READ CH54` - Check seal channel status

---

## ᚢ URUZ Commands - Power Operations

### Activate All Channels
```
ᚢ:ALL_ON
URUZ:ALL_ON
```

**Effect:** Sets all 54 channels to HIGH state simultaneously.

### Deactivate All Channels
```
ᚢ:ALL_OFF
URUZ:ALL_OFF
```

**Effect:** Sets all 54 channels to LOW state simultaneously.

---

## ᚦ THURISAZ Commands - Timing & Cycling

### Pulse Channel
```
ᚦ:CYCLE <duration_ms> CH<n>
THURISAZ:CYCLE <duration_ms> CH<n>
```

**Examples:**
- `ᚦ:CYCLE 100 CH5` - Pulse channel 5 for 100ms
- `ᚦ:CYCLE 500 CH20` - Pulse channel 20 for 500ms
- `THURISAZ:CYCLE 1000 CH54` - Pulse seal channel for 1 second

**Behavior:** Activates channel, waits for specified duration, then deactivates.

---

## ᚨ ANSUZ Commands - Patterns & Waves

### Wave Pattern
```
ᚨ:PATTERN WAVE <start>-<end>
ANSUZ:PATTERN WAVE <start>-<end>
```

**Examples:**
- `ᚨ:PATTERN WAVE 1-16` - Wave across channels 1-16
- `ᚨ:PATTERN WAVE 17-32` - Wave across channels 17-32
- `ANSUZ:PATTERN WAVE 1-54` - Wave across all channels

**Behavior:** 
1. Sequential activation from start to end (50ms per step)
2. Brief pause (100ms)
3. Sequential deactivation from start to end (50ms per step)

---

## ᛏ TIWAZ Commands - Synchronization

### Global Sync
```
ᛏ:SYNC
TIWAZ:SYNC
```

**Effect:**
- Resets all channels to LOW
- Resets tick counter to 0
- Synchronizes system timing

**Use Case:** Reset system to known state before starting ritual sequences.

---

## ᛊ SEAL Commands - Ritual Protocol (Channel 54)

### Execute Seal Protocol
```
ᛊ:SEAL
SEAL:SEAL
SOWILO:SEAL
```

**Effect:** Executes three-phase convergence ritual:

**Phase 1: Convergence (3 seconds)**
- Sequential activation of channels 1-53
- Each channel turns on with 50ms delay

**Phase 2: Focusing (1.8 seconds)**
- 3× synchronized pulses of all channels
- 300ms ON, 300ms OFF pattern

**Phase 3: Final Seal**
- All channels OFF
- 500ms pause
- Channel 54 activated (SEALED state)
- Seal LED illuminated

**Total Duration:** ~8-10 seconds

---

## Example Ritual Sequences

### Morning Activation Sequence
```
ᛏ:SYNC                        # Reset system
ᚨ:PATTERN WAVE 1-16          # Wake channels 1-16
ᚨ:PATTERN WAVE 17-32         # Wake channels 17-32
ᚨ:PATTERN WAVE 33-48         # Wake channels 33-48
ᚨ:PATTERN WAVE 49-54         # Wake final channels
ᚢ:ALL_OFF                     # Clear all
```

### Focused Channel Test
```
ᛏ:SYNC                        # Reset
ᚠ:WRITE CH1=HIGH             # Test channel 1
ᚦ:CYCLE 1000 CH1             # Pulse for 1 second
ᚠ:READ CH1                    # Verify state
```

### Full System Test
```
ᛏ:SYNC                        # Reset
ᚢ:ALL_ON                      # All channels on
ᚢ:ALL_OFF                     # All channels off
ᚨ:PATTERN WAVE 1-54          # Wave across all
```

### Convergence Ritual (Full Seal)
```
ᛏ:SYNC                        # Reset system
ᚨ:PATTERN WAVE 1-16          # Quadrant 1
ᚨ:PATTERN WAVE 17-32         # Quadrant 2
ᚨ:PATTERN WAVE 33-48         # Quadrant 3
ᚠ:WRITE CH49=HIGH            # Prepare convergence
ᚠ:WRITE CH50=HIGH
ᚠ:WRITE CH51=HIGH
ᚠ:WRITE CH52=HIGH
ᚠ:WRITE CH53=HIGH
ᛊ:SEAL                        # Execute final seal
```

---

## Channel Mapping Quick Reference

### Channel Groups by Rune

| Channels | MCP Chip | Rune | Symbol |
|----------|----------|------|--------|
| 1-16 | MCP0 (0x20) | FEHU | ᚠ |
| 17-32 | MCP1 (0x21) | URUZ | ᚢ |
| 33-48 | MCP2 (0x22) | THURISAZ | ᚦ |
| 49-53 | MCP3 (0x23) | ANSUZ | ᚨ |
| **54** | **MCP3 (0x23)** | **SEAL** | **ᛊ** |

### Special Channels

- **Channel 54** - Final convergence point (Seal Protocol)
- **Channels 1-16** - Wealth Gateway (Foundation layer)
- **Channels 17-32** - Strength Layer (Power core)
- **Channels 33-48** - Gateway Layer (Threshold zone)
- **Channels 49-53** - Breath Layer (Convergence preparation)

---

## Timing Reference

### System Heartbeat
- **Frequency:** 119 Hz
- **Period:** 8.403 ms per tick
- **Status LED:** Blinks at 1 Hz (every 119 ticks)

### Pattern Timing
- **Wave step:** 50 ms per channel
- **Wave pause:** 100 ms between activation/deactivation
- **Pulse duration:** User-defined (CYCLE command)
- **Seal protocol:** ~8-10 seconds total

---

## Error Messages

| Message | Meaning | Solution |
|---------|---------|----------|
| `ERROR: Invalid channel <n>` | Channel number out of range | Use 1-54 only |
| `ERROR: Invalid command format` | Missing `:` or command body | Check syntax |
| `ERROR: Unknown rune prefix` | Unrecognized rune/command | Use valid prefix |
| `FAILED` | Command execution failed | Check hardware, retry |

---

## Serial Monitor Setup

- **Baud Rate:** 115200
- **Line Ending:** Newline (NL) or Carriage Return (CR+LF)
- **Encoding:** UTF-8 (for rune characters)

### Testing Commands

1. Start with simple commands: `FEHU:WRITE CH1=HIGH`
2. Verify with read: `FEHU:READ CH1`
3. Try bulk operations: `URUZ:ALL_OFF`
4. Test patterns: `ANSUZ:PATTERN WAVE 1-16`
5. Execute seal when ready: `SEAL:SEAL`

---

## Tips & Best Practices

### Command Entry
- Rune characters (ᚠᚢᚦᚨᛏᛊ) or ASCII names (FEHU, URUZ, etc.) both work
- Commands are case-sensitive (use uppercase)
- Spaces in commands matter (e.g., `CYCLE 100 CH5`)

### Ritual Design
- Always start with `ᛏ:SYNC` to establish known state
- Use wave patterns for gradual activation
- Reserve Channel 54 for final convergence only
- Test individual channels before full sequences

### Debugging
- Use `ᚠ:READ CH<n>` to verify channel states
- Start with single channels before bulk operations
- Monitor serial output for error messages
- Check Status LED for 1 Hz heartbeat (system alive)

---

**"From symbol to silicon, the ancient pathways illuminate the modern circuit."**

*Universal Translation 0/0 - DSL Command Reference v1.0*
