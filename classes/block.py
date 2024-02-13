import hashlib
import time

class Block:
    def __init__(self, index, name, previous_hash, timestamp, data, hash):
        self.index = index
        self.name = name
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash(index, name, previous_hash, timestamp, data)

    @staticmethod
    def calculate_hash(index, name, previous_hash, timestamp, data):
        value = str(index) + str(name) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()
    
    def genesis_block(name, data):
        index = 0
        timestamp = int(time.time())
        hash = Block.calculate_hash(index, name, "0", timestamp, data)
        return Block(index, name, 0, timestamp, data, hash)
    
    def create_block(name, previous_block, data):
        index = previous_block.index + 1
        timestamp = int(time.time())
        hash = Block.calculate_hash(index, name, previous_block.hash, timestamp, data)
        return Block(index, name, previous_block.hash, timestamp, data, hash)

    def exposed_block(self):
        return self.index, self.name, self.previous_hash, self.timestamp, self.data, self.hash