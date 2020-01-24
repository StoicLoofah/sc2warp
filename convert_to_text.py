import sys
import xml.etree.ElementTree as ET

def main(args):
    tree = ET.parse(args[0])
    root = tree.getroot()
    full_text = []
    for elem in root.iter():
        if elem.text:
            cur_text = elem.text.strip()
            if cur_text:
                full_text.append(cur_text)

    with open('{}.txt'.format(args[0]), 'w') as fout:
        fout.write(' '.join(full_text))


if __name__ == "__main__":
    main(sys.argv[1:])
