#!/usr/bin/env python3
import os
from pathlib import Path

import convertor
from convertor.decode_convertor import Decoder
from convertor.trash_generator import Trasher

ROOT_PATH = Path(__file__).parent
KEY_FILE = Path(os.path.dirname(convertor.__file__)) / 'key'
SOURCE_DIR = ROOT_PATH / 'source'
DECODED_DIR = ROOT_PATH / 'decoded_sources'
ENCODED_DIR = ROOT_PATH / 'encoded_sources'


def assert_source_files():
    assert SOURCE_DIR.exists() and os.listdir(SOURCE_DIR)


def decode_source():
    decoder = Decoder(KEY_FILE)
    return decoder.convert_files(input_dir=SOURCE_DIR,
                                 input_mask='source*',
                                 output_dir=DECODED_DIR,
                                 input_prefix='source',
                                 output_prefix='decoded')


def generate_trash_files():
    trasher = Trasher()
    return trasher.convert_files(input_dir=DECODED_DIR,
                                 input_mask='decoded*',
                                 output_dir=DECODED_DIR,
                                 input_prefix='decoded',
                                 output_prefix='')


def encode_decoded_source():
    # TODO: need to implement this functionality [3]
    raise NotImplementedError('Not implemented [3]')


def main():
    assert_source_files()
    decode_source()
    generate_trash_files()
    # encode_decoded_source()


if __name__ == '__main__':
    main()
