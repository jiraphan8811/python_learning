from imghdr import what


def sentence_maker(phrase):
    captilalized = phrase.capitalize()
    if phrase.startswith(("how","what","why")):
        return "{}?".format(captilalized)

    else:
        return "{}.".format(captilalized)

l1 = []

while True:
    x = input("Say something: ")
    if x == '\end':
        
        print(' '.join(l1))
        break

    else:
        l1.append(sentence_maker(x))

print(l1)