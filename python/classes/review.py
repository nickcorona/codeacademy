class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
    
    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)

    def get_average(self):
        average_score = sum(self.grades) / float(len(self.grades))
        return average_score


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score
    
    def is_passing(self):
        is_passing = self.score > self.minimum_passing
        return is_passing


roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

pieter.add_grade(Grade(100))
pieter.get_average()