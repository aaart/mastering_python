types_of_people = 10
x = f"there are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?!: {}"

print(joke_evaluation.format(hilarious))

left = "this is a left side of a string"
right = " with a right side"

print(left + right)
