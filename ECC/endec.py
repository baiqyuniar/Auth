from ecc.curve import (
    P256, secp256k1, Curve25519, M383, E222, E382
)
from ecc.cipher import ElGamal
from ecc.key import gen_keypair


CURVES = [P256, secp256k1, Curve25519, M383, E222, E382]
PLAINTEXT = b"Rini yang cantiiik"

# Generate key pair
pri_key, pub_key = gen_keypair(E382)

# Initiate ElGamal
cipher_elg = ElGamal(E382)

# Encrypt
C1, C2 = cipher_elg.encrypt(PLAINTEXT, pub_key)
print(pri_key)
print(pub_key)

# Decrypt
plaintext = cipher_elg.decrypt(pri_key, C1, C2)
print(plaintext)
