class File:
    def __init__(self):
        self.liste = []
    
    def enfiler(self, block):
        self.liste.append(block)

    def defiler(self):
        self.liste.remove(self.liste[0])
    
    def exposed_file(self):
        return self.liste