# Overview

Gesture Dial follows a event-driven architecture.

The Backend Engine connects to the hardware, listens for notifications, converts the notifications into gesture events.
These events are broadcasted to the workflow engine, and the workflow engine then calls plugins/ action implementations based on its mapping.

# Components

## BLE Connector & Listener
`/core/ble/`

It is responsible for connecting with the hardware, listening for notifications, processing them, and sending raw packets out.
It is also designed to safely handle any form of disconnection.

### Communication
- Hardware Device: Receive/ Listen
- `/core/gesture/`: Send raw packets

## Gesture Event Interpreter
`/core/gesture`

It is responsible for converting raw packets into proper gesture events, normalizing the data for other components to handle.

### Communication
- `/core/ble`: Receive raw packets
- `/core/event_bus`: Send gesture events

## Event Broadcaster
`/core/event_bus`

It is responsible for broadcasting gesture events internally to all concerned components.
The components may include: logger, analytics.
It will always broadcast to the workflow engine for implementing actions.

### Communication
- `/core/gesture`: Receive gesture events
- `/core/workflow`: Broadcast gesture events

## Workflow Engine
`/core/workflow`

It is responsible for mapping gesture events to actions. It also stores information about the mappings.
It doesn't implement the actions itself, but it invokes the action implementation.

### Communication
- `/core/event_bus`: Receive gesture events
- `/core/plugins`: Invoke action implementations

## Plugins
`/core/plugins`

It is responsible for the implementation of actions.
This contains modules that can be called to implement actions.

### Communication
- Receive invocation
- Execute action implementation

# Data Flow

## Engine

Hardware Device -> Raw Packets -> Gesture Event -> Workflow Engine -> Action Implementation