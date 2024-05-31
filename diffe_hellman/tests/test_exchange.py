from diffe_hellman import DiffeHellman, MODP_1024_160, MODP_2048_224, MODP_2048_256
import pytest


@pytest.mark.parametrize("modp", [MODP_1024_160, MODP_2048_224, MODP_2048_256])
def test_keyswap(modp):
    alice = DiffeHellman(prime=modp.p, g_root=modp.g)
    bob = DiffeHellman.from_modp(modp)

    alice_public = alice.generate_public_key()
    bob_public = bob.generate_public_key()

    alice.generate_secret_key(bob_public)
    bob.generate_secret_key(alice_public)

    assert alice.keys.secret == bob.keys.secret
