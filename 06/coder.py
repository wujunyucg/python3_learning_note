class Coder:
    def __init__(self, name):
        self.name = name
        self.skills = []

    def mastering_skill(self, skill):
        self.skills.append(skill)

    def show_skills(self):
        for skill in self.skills:
            print(skill)



