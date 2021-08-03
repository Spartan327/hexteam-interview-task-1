import argparse
import re
import string

from convertor.decode_convertor import Decoder
from convertor.encode_convertor import Encoder

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
    input_text = prepare_text_source(parse_args().source_text)
    decode = Decoder('convertor/' + KEY_FILE)
    output_text = decode.convert_text(input_text)
    return print(output_text)


def encode():
    # TODO: need to implement this functionality [5]
    input_text = parse_args().source_text
    encoder = Encoder('convertor/' + KEY_FILE)
    output_text = encoder.convert_text(input_text)
    return print(output_text)
