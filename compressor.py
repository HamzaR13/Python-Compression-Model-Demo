from huffman_tree import Node
from compression_utils import byte_to_bits, bits_to_byte

def build_freq_dict(data: bytes) -> dict:
    freq = {}
    for b in data:
        freq[b] = freq.get(b, 0) + 1
    return freq

def build_tree(freq: dict) -> Node:
    nodes = [Node(sym, f) for sym, f in freq.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left, right = nodes.pop(0), nodes.pop(0)
        parent = Node(None, left.freq + right.freq)
        parent.left, parent.right = left, right
        nodes.append(parent)
    return nodes[0]

def build_codes(node, code='', codes={}):
    if node.is_leaf():
        codes[node.symbol] = code
    else:
        build_codes(node.left, code + '0', codes)
        build_codes(node.right, code + '1', codes)
    return codes

def compress(data: bytes, codes: dict) -> bytes:
    bit_str = ''.join(codes[b] for b in data)
    padding = (8 - len(bit_str) % 8) % 8
    bit_str += '0' * padding
    compressed = bytes([bits_to_byte(bit_str[i:i+8]) for i in range(0, len(bit_str), 8)])
    return compressed
