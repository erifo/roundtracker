class Effect:
    def __init__(self, name, rounds):
        self.name = name
        self.rounds = rounds
    
    def mod_rounds(self, rounds):
        self.rounds += rounds
    
    def to_string(self):
        h = self.rounds//600
        m = (self.rounds%600)//10
        r = (self.rounds%600%10)
        return str(h).ljust(8) + str(m).ljust(8) + str(r).ljust(8) + self.name