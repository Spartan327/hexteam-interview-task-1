import glob
import os
from pathlib import Path

from convertor.abstract_base_convertor import AbstractFileConvertor


class Trasher(AbstractFileConvertor):
    def convert_text(self, input_text: str) -> str:
        return input_text

    def _create_map(self, file: str, **kwargs) -> dict[str, str]:
        assert not file
        return {}

    def convert_files(self, *, input_dir: str, input_mask: str,
                      output_dir: str, input_prefix: str,
                      output_prefix: str) -> list[str]:
        os.makedirs(output_dir, exist_ok=True)
        result = []
        for filename in glob.glob(os.path.join(input_dir, input_mask)):
            output_name = self.output_name_generator(filename, input_prefix,
                                                     output_prefix, output_dir)
            Path(output_name).touch(exist_ok=True)
            result.append('')
        return result
