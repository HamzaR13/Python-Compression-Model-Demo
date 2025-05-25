from compressor import build_freq_dict, build_tree, build_codes, compress

def test_freq_dict():
    data = b'hello'
    freq = build_freq_dict(data)
    assert freq[ord('h')] == 1
    assert freq[ord('e')] == 1
    assert freq[ord('l')] == 2
    assert freq[ord('o')] == 1

def test_build_tree_and_codes():
    data = b'abab'
    freq = build_freq_dict(data)
    tree = build_tree(freq)
    codes = build_codes(tree)
    assert set(codes.keys()) == {ord('a'), ord('b')}

def test_compression():
    data = b'abc'
    freq = build_freq_dict(data)
    tree = build_tree(freq)
    codes = build_codes(tree)
    compressed = compress(data, codes)
    assert isinstance(compressed, bytes)
    assert len(compressed) <= len(data)
