from effect import Effect

class RTModel:
    def __init__(self):
        self.effects = []
        self.load()

    def effects_to_strings(self):
        return [e.to_string() for e in self.effects]

    def add_effect(self, name, rounds):
        e = Effect(name, rounds)
        self.effects.append(e)
    
    def remove_effect(self, index):
        del self.effects[index]

    def tick_effects(self, rounds):
        for effect in self.effects:
            effect.mod_rounds(rounds)
    
    def save(self):
        with open("./roundtracker_save.txt","w") as f:
            for effect in self.effects:
                f.write(effect.name + '|' + str(effect.rounds) + '\n')

    def load(self):
        try:
            with open("./roundtracker_save.txt","r") as f:
                for line in f:
                    name, rounds = line[:-1].split('|')
                    self.add_effect(name, int(rounds))
        except:
            print("Unable to find file. Skipping load step.")