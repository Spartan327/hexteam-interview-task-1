import os

from convertor.abstract_base_convertor import AbstractFileConvertor
import glob


class Encoder(AbstractFileConvertor):
    @staticmethod
    def _file_to_dict(filename) -> dict[str, str]:
        dict_letters = {}
        with open(filename) as file:
            for line in file:
                if line:
                    dict_letters[line[0].lower()] = line[2:].split(',')[0].strip()
        return dict_letters

    def convert_text(self, input_text: str) -> str:
        sorted_keys_len_values = sorted(
            self._latter_mapper,
            key=lambda k: len(self._latter_mapper[k]),
            reverse=True)
        for key in sorted_keys_len_values:
            input_text = input_text.replace(self._latter_mapper[key], key, -1)
        return input_text

    def _create_map(self, file: str, **kwargs) -> dict[str, str]:
        assert file
        return self._file_to_dict(file)

    def convert_files(self, *, input_dir: str, input_mask: str,
                      output_dir: str, input_prefix: str,
                      output_prefix: str):
        os.makedirs(output_dir, exist_ok=True)
        for filename in glob.glob(os.path.join(input_dir, input_mask)):
            output_name = self.output_name_generator(
                filename,
                input_prefix,
                output_prefix,
                output_dir,
            )
            with open(filename) as file:
                with open(output_name, 'w') as outfile:
                    converted_text = self.convert_text(file.read())
                    outfile.write(converted_text)
