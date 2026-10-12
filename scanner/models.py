
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Protocol(str, Enum):
    TCP = "tcp"
    UDP = "udp"


class PortState(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    FILTERED = "filtered"
    OPEN_FILTRED = "open|filtered"
    UNKNOWN = "unknown"

@dataclass
class PortResult:
    port: int
    state: PortState
    service: Optional[str] = None
    banner: Optional[str] = None
    latency_ms: Optional[float] = None

