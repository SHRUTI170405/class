class Player:
    def __init__(self, jn, name, runs, team, wickets):
        self.jersey_no = jn
        self.name = name
        self.runs = runs
        self.team = team
        self.wickets = wickets

    def display(self):
        print(self.jersey_no, self.name, self.runs, self.team, self.wickets)

p1 = Player(45, "Rohit Sharma", 5000, "MI", 10)
p2 = Player(63, "Suryakumar Yadav", 3200, "MI", 5)
p3 = Player(98, "Jasprit Bumrah", 200, "MI", 150)
p4 = Player(33, "Hardik Pandya", 2500, "MI", 80)
p5 = Player(99, "Ishan Kishan", 2200, "MI", 2)
p6 = Player(18, "Virat Kohli", 7000, "RCB", 5)
p7 = Player(19, "Mohammed Siraj", 100, "RCB", 120)
p8 = Player(7, "MS Dhoni", 5000, "CSK", 1)
p9 = Player(8, "Ravindra Jadeja", 2500, "CSK", 130)
p10 = Player(77, "Shubman Gill", 2800, "GT", 2)
p11 = Player(2, "KL Rahul", 4000, "LSG", 1)

mi_team = []
mi_team.append(p1)
mi_team.append(p2)
mi_team.append(p3)
mi_team.append(p4)
mi_team.append(p5)
print("MI Team:")
mi_team[0].display()
mi_team[1].display()
mi_team[2].display()
mi_team[3].display()
mi_team[4].display()
