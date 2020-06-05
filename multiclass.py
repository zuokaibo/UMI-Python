class PartyAnimials:
    x = 0
    name = ""

    def _init_(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count: ", self.x)


class FootballFan(PartyAnimials):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points: ", self.points)




s = PartyAnimials("Sally")
s.party()

j = FootballFan("Jim")
j.party()
s.party()
j.touchdown()