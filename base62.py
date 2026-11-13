ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(ALPHABET)

def encode(num: int) -> str:
    if num < 0:
        raise ValueError('input must be nonnegative')
    if num == 0:
        return '0'
    
    res = []
    while num > 0:
        num, d = divmod(num, BASE)
        res.append(ALPHABET[d])
    return ''.join(reversed(res))
        
        
def decode(code: str) -> int:
    if not code:
        raise ValueError('must be a valid string')
    
    res = 0
    for ch in code:
        d = ALPHABET.index(ch)
        res = res * BASE + d
    return res
