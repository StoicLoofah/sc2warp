import random
import sys

def main(args):
    text = []
    with open(args[0], 'r') as fin:
        text = fin.read().split()

    mapping = get_mapping(text)

    new_text = [text[0].lower()]
    for i in range(1000):
        new_text.append(random.choice(mapping[new_text[-1]]))
    print(' '.join(new_text))

def get_mapping(text):
    mapping = {}

    last_word = None
    for word in text:
        word = word.lower()
        if last_word:
            if not last_word in mapping:
                mapping[last_word] = []
            mapping[last_word].append(word)
        last_word = word

    return mapping

if __name__ == "__main__":
    main(sys.argv[1:])
