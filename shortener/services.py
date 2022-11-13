import random
import string

from shortener.models import Url


def alias_generator():
    """
    generate a unique 10-element-long string composed of:
    - 2-7 upper or lower case letters
    - at least 3 digits
    - the last element is always a digit, which indicates a total number of letters within this string

    :return: string
    """
    while True:
        elements = []
        letters_num = random.randint(2, 7)
        for i in range(letters_num):
            elements.append(random.choice(string.ascii_letters))
        while len(elements) < 9:
            elements.append(str(random.randint(0, 9)))
        random.shuffle(elements)
        elements.append(str(letters_num))
        result = ''.join(elements)
        if len(Url.objects.filter(alias=result)) == 0:
            return result

