"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
Notes:

the returned string should only contain lowercase letters
"""


def kebabize(st):
    new_st = ''
    for x in st:
        if x.isalpha():
            if x == x.upper():
                new_st = new_st + '-' + x.lower()
            else:
                new_st += x
    return new_st.lstrip('-')


print(kebabize('42'))   # 'my-camel-cased-string'
