from dataclasses import dataclass

@dataclass
class A:
    a: int

class B:
    def __init__(self, b: int):
        self.b = b

l1 = [A(1), A(2), A(1)]
l2 = [B(1), B(2), B(1)]

print(l1[0] == l1[0])
print(l1[0] == l1[1])
print(l1[0] == l1[2])
print(l2[0] == l2[0])
print(l2[0] == l2[1])
print(l2[0] == l2[2])