#pragma once

#include <cstdint>

struct RawPacket {
    uint16_t value;
    uint64_t timestamp;
};