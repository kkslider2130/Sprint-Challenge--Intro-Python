# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [p.name for p in humans if p.name.startswith('D')]
# for i in humans:
#     if i.name.startswith('D'):
#         a.append(i.name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [p.name for p in humans if p.name.endswith('e')]
# for i in humans:
#     if i.name.endswith('e'):
#         b.append(i.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
letters_allowed = 'CDEFG'
c = [p.name for p in humans if any(
    p.name.startswith(x) for x in letters_allowed)]
# for i in humans:
#     if any(i.name.startswith(x) for x in letters_allowed):
#         c.append(i.name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [p.age+10 for p in humans]
# for i in humans:
#     d.append(i.age+10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f'{p.name}-{p.age}' for p in humans]
# for i in humans:
#     e.append(f'{i.name}-{i.age}')
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(p.name, p.age) for p in humans if p.age < 33 and p.age > 27]
# for i in humans:
#     if i.age < 33 and i.age > 27:
#         f.append((i.name, i.age))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(p.name.upper(), p.age+5) for p in humans]
# for i in humans:
#     g.append(Human(i.name.upper(), i.age+5))
print(g)


# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [math.sqrt(p.age) for p in humans]
# for i in humans:
#     h.append(math.sqrt(i.age))

print(h)
