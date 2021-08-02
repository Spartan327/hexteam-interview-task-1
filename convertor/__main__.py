import argparse
import re
import string
KEY_FILE = 'key'


def prepare_text_source(text: str):
    return re.sub(re.escape(string.punctuation), '', text.lower())


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_text',
                        type=str,
                        help='Returns encoded or decode text')
    return parser.parse_args()


def file_to_dict(filename) -> dict[str, str]:
    dict_letters = {}
    with open(filename) as file:
        for line in file:
            if line:
                dict_letters[line[0].lower()] = line[2:].split(',')[0].strip()
    return dict_letters


def decode():
    # use a prepare_text_source function for preparing!
    # TODO: need to implement this functionality [4]
    input_text = prepare_text_source(parse_args().source_text)
    dict_letters = file_to_dict('convertor/' + KEY_FILE)
    for original, replace in dict_letters.items():
        input_text = input_text.replace(original, replace, -1)
    return print(input_text)


def encode():
    # TODO: need to implement this functionality [5]
    input_text = parse_args().source_text
    dict_letters = file_to_dict('convertor/' + KEY_FILE)
    sorted_keys_len_values = sorted(
            dict_letters,
            key=lambda k: len(dict_letters[k]),
            reverse=True)
    for key in sorted_keys_len_values:
        input_text = input_text.replace(dict_letters[key], key, -1)
    return print(input_text)
