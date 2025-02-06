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


# p1 = Person("Alice", 25)
# p2 = Person("Bob", 30)
# p3 = Person("Alice", 25)
# print(p1 == p3)
# print(p1 == p2)
# print(p1 < p2)
# print(p1 > p2)
# print(p2 > p1)


# p = Person("Alice", 25)
# print(p)

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


# c = Collection([Person("Alice", 25), Person("Bob", 30)])
# print(len(c))
# c = c + Person("Charlie", 22)
# print(len(c))

