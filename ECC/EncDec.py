from ecc.curve import (
    P256, secp256k1, Curve25519, M383, E222, E382
)
from ecc.cipher import ElGamal
from ecc.key import gen_keypair

CURVES = [P256, secp256k1, Curve25519, M383, E222, E382]
PLAINTEXT = b"MBC laboratory"

# Generate key pair
pri_key, pub_key = gen_keypair(E382)
print("Private key\t: ",pri_key)
print("Public key\t: ",pub_key)

# Initiate ElGamal
cipher_elg = ElGamal(E382)

# Encrypt
C1, C2 = cipher_elg.encrypt(PLAINTEXT, pub_key)

# Decrypt
plaintext = cipher_elg.decrypt(pri_key, C1, C2)
print("Plaintext\t: ",plaintext)
