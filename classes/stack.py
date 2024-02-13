class Stack:
    def __init__(self):
        self.liste = []
    
    def empiler(self, block):
        self.liste.append(block)

    def depiler(self):
        self.liste.pop()
    
    def exposed_stack(self):
        return self.liste