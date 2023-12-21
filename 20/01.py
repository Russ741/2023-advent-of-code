import re
from dataclasses import dataclass, astuple, field
from queue import SimpleQueue
from enum import Enum, global_enum

@global_enum
class Type(Enum):
    BROADCASTER = 1
    FLIPFLOP = 2
    CONJUNCTION = 3

    def get(type_str):
        if type_str == '':
            return BROADCASTER
        elif type_str == '%':
            return FLIPFLOP
        elif type_str == '&':
            return CONJUNCTION

@dataclass
class Gate:
    name: str
    outputs: tuple

    def notify_outputs(self):
        for output in self.outputs:
            if output in gates:
                gates[output].add_input(self.name)

    def add_input(self, name):
        pass

@dataclass
class Broadcaster(Gate):
    def recv(self, _, high):
        return [Packet(self.name, output, high) for output in self.outputs]

@dataclass
class FlipFlop(Gate):
    state: bool = False

    def recv(self, _, high):
        if high:
            return []
        else:
            self.state = not self.state
            return [Packet(self.name, output, self.state) for output in self.outputs]

@dataclass
class Conjunction(Gate):
    state: dict = field(default_factory=dict)

    def recv(self, src, high):
        self.state[src] = high
        out_high = not all(self.state.values())
        return [Packet(self.name, output, out_high) for output in self.outputs]

    def add_input(self, input):
        self.state[input] = False

@dataclass(frozen=True)
class Packet:
    src: str
    dst: str
    high: bool

    def __iter__(self):
        return iter(astuple(self))

def push_button():
    packets = SimpleQueue()
    packets.put(Packet("button", "broadcaster", False))

    packet_ct = 0
    high_ct = 0
    while not packets.empty():
        packet_ct += 1
        src, dst, high = packets.get()
        # print(src, dst, high)
        if high:
            high_ct += 1
        if not dst in gates:
            continue
        gate = gates[dst]
        for out_packet in gate.recv(src, high):
            packets.put(out_packet)
    low_ct = packet_ct - high_ct
    print(f"{low_ct=} {high_ct=} {low_ct * high_ct}")
    return low_ct, high_ct


with open("input.txt") as infile:
    lines = infile.read().splitlines()

gates = {}
for line in lines:
    type, gate_name, output_str = re.match(r"^([%&]?)(\w+) -> (.*)$", line).groups()
    outputs = output_str.split(", ")
    gate = None
    if type == "":
        gate = Broadcaster(gate_name, outputs)
    elif type == "%":
        gate = FlipFlop(gate_name, outputs)
    elif type == "&":
        gate = Conjunction(gate_name, outputs)
    gates[gate_name] = gate

for gate in gates.values():
    gate.notify_outputs()

sum_low = 0
sum_high = 0
for i in range(1000):
    low, high = push_button()
    sum_low += low
    sum_high += high

print(f"{sum_low=} {sum_high=} {sum_low * sum_high}")