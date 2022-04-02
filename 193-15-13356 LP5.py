class Person:

    def __init__(self, name, jersynumber,age):
        self.name = name
        self.jersynumber = 11
        self.age = 20


person = Person(
    "Jane",
    "12",
    "20"
)

print(person.name)
print(person.jersynumber)
print(person.age())