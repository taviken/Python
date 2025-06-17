class Linker:
    def __init__(self, payload: str, prev_hash: str, hash_name: str = "sha256"):
        self.payload = payload
        self.prev_hash = prev_hash
        self.hash_name = hash_name
