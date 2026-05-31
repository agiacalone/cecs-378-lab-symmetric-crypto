"""The Vault's four wards, as black-box oracles.

Students import these and attack them. Do not read past this docstring if you
want the challenge intact — the internals are the answer key.
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from oracle import _seed

BS = 16


class WardI:
    """The Wisp — ECB detection.

    ``challenge()`` returns five hex ciphertexts of the same repeated-block
    plaintext. Exactly one was sealed in ECB mode (deterministic → repeated
    plaintext blocks become repeated cipher blocks). ``unlock(index)`` yields
    the flag if you name the ECB one.
    """

    _NUM = 5
    _PLAIN = b"the same block!!" * 4  # four identical 16-byte blocks

    def __init__(self):
        self._key = _seed.ward_key("ward1")
        self._ecb_index = _seed.ward_index("ward1", self._NUM)

    def challenge(self):
        out = []
        for i in range(self._NUM):
            if i == self._ecb_index:
                ct = AES.new(self._key, AES.MODE_ECB).encrypt(self._PLAIN)
            else:
                iv = _seed.ward_iv(f"ward1-{i}")
                ct = AES.new(self._key, AES.MODE_CBC, iv).encrypt(self._PLAIN)
            out.append(ct.hex())
        return out

    def unlock(self, index):
        return _seed.ward_flag("ward1") if index == self._ecb_index else None


class WardII:
    """The Rune Golem — ECB byte-at-a-time.

    ``encrypt(data)`` returns ``AES-ECB(pad(data || SECRET))`` under a fixed
    per-student key, where SECRET is the per-student flag. Recover SECRET one
    rune (byte) at a time; the recovered SECRET *is* the flag.
    """

    def __init__(self):
        self._key = _seed.ward_key("ward2")
        self._secret = _seed.ward_flag("ward2").encode()

    def encrypt(self, data: bytes) -> bytes:
        return AES.new(self._key, AES.MODE_ECB).encrypt(pad(data + self._secret, BS))


class WardIII:
    """The Mirror Knight — CBC bit-flipping.

    ``make_token(userdata)`` wraps your data between a fixed prefix and suffix,
    escapes ``;`` and ``=`` so you cannot inject them directly, then CBC-encrypts
    under a fixed per-student key+IV. ``is_admin(token)`` decrypts and yields the
    flag if the plaintext contains ``;admin=true;``. Forge it by tampering
    ciphertext, not input.
    """

    _PRE = b"comment1=cooking%20MCs;userdata="   # exactly 32 bytes (2 blocks)
    _POST = b";comment2=%20like%20a%20pound%20of%20bacon"

    def __init__(self):
        self._key = _seed.ward_key("ward3")
        self._iv = _seed.ward_iv("ward3")

    def make_token(self, userdata: bytes) -> bytes:
        ud = userdata.replace(b";", b"%3B").replace(b"=", b"%3D")
        plain = self._PRE + ud + self._POST
        return AES.new(self._key, AES.MODE_CBC, self._iv).encrypt(pad(plain, BS))

    def is_admin(self, token: bytes):
        raw = AES.new(self._key, AES.MODE_CBC, self._iv).decrypt(token)
        try:
            plain = unpad(raw, BS)
        except ValueError:
            plain = raw  # tampering may break padding; we only care about the body
        return _seed.ward_flag("ward3") if b";admin=true;" in plain else None


class WardIV:
    """OMEGA WARD — CBC padding oracle.

    ``challenge()`` returns ``(iv_hex, ct_hex)`` of the per-student flag,
    CBC-encrypted with PKCS7 padding under a fixed per-student key.
    ``has_valid_padding(iv_hex, ct_hex)`` leaks one bit: whether the decryption
    ends in valid PKCS7 padding. That leak is enough to unmake the seal.
    """

    def __init__(self):
        self._key = _seed.ward_key("ward4")
        self._secret = _seed.ward_flag("ward4").encode()

    def challenge(self):
        iv = _seed.ward_iv("ward4")
        ct = AES.new(self._key, AES.MODE_CBC, iv).encrypt(pad(self._secret, BS))
        return iv.hex(), ct.hex()

    def has_valid_padding(self, iv_hex, ct_hex) -> bool:
        iv, ct = bytes.fromhex(iv_hex), bytes.fromhex(ct_hex)
        raw = AES.new(self._key, AES.MODE_CBC, iv).decrypt(ct)
        try:
            unpad(raw, BS)
            return True
        except ValueError:
            return False
