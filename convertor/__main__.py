import argparse
import re
import string
KEY_FILE = 'key'


def prepare_text_source(text: str):
    return re.sub(string.punctuation, '', text.lower())


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_text',
                        type=str,
                        help='Returns encoded or decode text')
    return parser.parse_args()


def decode():
    # use a prepare_text_source function for preparing!
    # TODO: need to implement this functionality [4]
    print('Opps... The decode function is not implemented')


def encode():
    # TODO: need to implement this functionality [5]
    print('Opps... The encode function is not implemented')
