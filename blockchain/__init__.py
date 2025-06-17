import hashlib as HL

__hasher__ = {"sha256": HL.sha256(), "sha512": HL.sha512()}
__initial_digest__ = "DEADBEEF"
