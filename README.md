!!! Work In Progress !!!

# Gesture Dial

GestureDial is an open-source, cross-platform automation platform that transforms wearable BLE gestures into programmable system actions and workflows.

# Folder Structure

```
gestureDial
|--core/            # Engine
|   |--ble/         # BLE Listener
|   |--event_bus/   # Internal Event Broadcaster
|   |--gesture/     # Interpret Gesture into Event
|   |--plugins/     # Action implementation
|   |--workflow/    # Maps Gesture to Action
|--desktop/         # Desktop App 
|--docs/            # Detailed Documentation
|--examples/        # Example Setups
|--firmware/        # Firmware for Supported Devices
|   |--arduino/     # Supports: Arduino Nano 33 BLE Sense Rev2
|--old_code/        # Legacy code (Soon to be archived)
|--tests/           # Tests for core/
|--LICENSE
|--README.md        # you're here! :p
```

# Maintainer

[Vishesh Agarwal](https://github.com/not-wish)

# Milestones

02-07-2026 : Started the core planning and work 