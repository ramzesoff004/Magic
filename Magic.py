class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person: {self.name}, Age: {self.age}'

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

class Collection:
    def __init__(self, people: list):
        self.people = people

    def __add__(self, other):
        self.people.append(other)
        return self

    def __len__(self):
        return len(self.people)

    def __getitem__(self, index):
        return self.people[index]

    def __call__(self):
        return [x.name for x in self.people]

    def __contains__(self, name):
        return any(x.name == name for x in self.people)
