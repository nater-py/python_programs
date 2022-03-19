# 'Madlibs' is a game that generates a sentence and fills in the blanks of that sentence with words given by the user
# 'Nouns', 'Adjectives', and 'Verbs' are typically the three types of words given by the user

noun = input("Input a noun: \n")
adjective = input("Input an adjective: \n")
verb = input("Input a verb: \n")

# Using f-strings to substitute the noun, adjective, and verb into the sentences
print(f"The {adjective} {noun} is currently burning. {verb.capitalize()} the water to put the fire out!")
