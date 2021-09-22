import random
import string


def random_username():
    return "".join(random.choices(string.ascii_lowercase, k=32))
