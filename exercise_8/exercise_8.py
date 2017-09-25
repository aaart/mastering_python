text_to_format = "{} {} {} {}"

#print(text_to_format.format("a one way")) # yeap, it does not work, we need four arguments here
print(text_to_format.format(1, 2, 3, 4))
print(text_to_format.format("one", "two", "three", "four"))
print(text_to_format.format(text_to_format, text_to_format, text_to_format, text_to_format))
print(text_to_format.format(
    "one",
    "two",
    "three",
    "four"))
