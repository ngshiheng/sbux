from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, config


@dataclass
class BaseSBUXDataClassJsonMixin(DataClassJsonMixin):
    """A base model for storing and serializing data using the dataclasses_json library.

    Inherit from a DataClassJsonMixin instead of using a class decorator for better static analysis tools support.

    To change casing at class level with mixin, see: https://github.com/lidatong/dataclasses-json/issues/272.
    """

    dataclass_json_config = config(letter_case=LetterCase.PASCAL)["dataclasses_json"]
