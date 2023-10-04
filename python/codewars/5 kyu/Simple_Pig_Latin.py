"""
Move the first letter of each word to the end of it, then add "ay" \
to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    new_text = []
    text = text.split()
    for x in text:
        if x in '?!.,:;':
            new_text.append(x)
        else:
            word = x[1:] + x[0] + "ay"
            new_text.append(word)
    return ' '.join(new_text)


    





print(pig_it('Hello world !'))   #'igPay atinlay siay oolcay