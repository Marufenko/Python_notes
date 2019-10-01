import random
import sys

article = ["the", "a"]
noun = ["cat", "dog", "man", "woman"]
verb = ["sang", "run", "jumped"]
adverb = ["loudly", "quitly", "well", "badly"]

try:
    input = int(sys.argv[1])
except:
    input = 5

for i in range(input):
    if random.randint(1, 2) == 1:
        print(
            random.choice(article)
            + " "
            + random.choice(noun)
            + " "
            + random.choice(verb)
            + " "
            + random.choice(adverb)
        )
    else:
        print(
            random.choice(article)
            + " "
            + random.choice(noun)
            + " "
            + random.choice(verb)
        )
