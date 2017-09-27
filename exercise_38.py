# I do anly a part of it bacuase I just want to manipulate list elements

list = []

counter = 0
while len(list) is not 10:
    list.append(counter)
    counter += 1
    print(list)

while len(list) != 0:
    list.pop()
    counter -= 1
    print(list)

counter = 0
while len(list) is not 10:
    list.append(counter)
    counter += 1
    print(list)

while len(list) != 0:
    del list[0]
    counter -= 1
    print(list)
