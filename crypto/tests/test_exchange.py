from crypto.diffie_hellman import (
    DiffieHellman,
    MODP_1024_160,
    MODP_2048_224,
    MODP_2048_256,
)
import pytest


@pytest.mark.parametrize("modp", [MODP_1024_160, MODP_2048_224, MODP_2048_256])
def test_keyswap(modp):
    alice = DiffieHellman(prime=modp.p, g_root=modp.g, seed=1)
    bob = DiffieHellman.from_modp(modp, seed=2)

    alice_public = alice._generate_public_key()
    bob_public = bob._generate_public_key()

    alice.generate_secret_key(bob_public)
    bob.generate_secret_key(alice_public)

    assert alice.keys.secret == bob.keys.secret
