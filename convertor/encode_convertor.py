from convertor.abstract_base_convertor import AbstractFileConvertor


class Encoder(AbstractFileConvertor):
    def convert_text(self, input_text: str) -> str:
        sorted_keys_len_values = sorted(
            self._latter_mapper,
            key=lambda k: len(self._latter_mapper[k]),
            reverse=True)
        for key in sorted_keys_len_values:
            input_text = input_text.replace(self._latter_mapper[key], key, -1)
        return input_text
