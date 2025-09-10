class emp:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def inc(self, p):
        self.s += self.s * p / 100

    def add_bonus(self, bonus):
        self.s += bonus

    def pr(self):
        print("emp:", self.n, "salary:", self.s)

e = emp("RAJU", 5000)
e.inc(10)        
e.add_bonus(500) 
e.pr()          