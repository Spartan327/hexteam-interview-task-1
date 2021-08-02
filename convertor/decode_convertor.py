from convertor.abstract_base_convertor import AbstractFileConvertor


class Decoder(AbstractFileConvertor):
    def convert_text(self, input_text: str) -> str:
        for original, replace in self._latter_mapper.items():
            input_text = input_text.replace(original, replace, -1)
        return input_text
