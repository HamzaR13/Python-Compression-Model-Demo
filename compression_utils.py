def byte_to_bits(byte: int) -> str:
    return bin(byte)[2:].rjust(8, '0')

def bits_to_byte(bits: str) -> int:
    return int(bits.ljust(8, '0'), 2)

def get_bit(byte: int, pos: int) -> int:
    return (byte >> pos) & 1
