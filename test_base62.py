from base62 import encode, decode

def raises(fn, arg) -> bool:
    try:
        fn(arg)
    except ValueError:
        return True
    return False

assert encode(1000) == "g8"
assert encode(61) == "Z"
assert encode(62) == "10"
assert encode(3843) == "ZZ"
assert encode(3844) == "100"
assert encode(0) == "0"
assert raises(encode, -1)

assert decode("g8") == 1000
assert decode("0") == 0
assert decode("100") == 3844
assert raises(decode, "")
assert raises(decode, "g-8")

assert all(decode(encode(num)) == num for num in range(10_000))
assert len(encode(56_800_235_583)) == 6

print("all passed")
