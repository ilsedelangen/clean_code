from dataclasses import dataclass
from datetime import datetime
import re


@dataclass
class ConfigContainer:
    VERSION_PATTERN = "\\d{1,2}\\.\\d{1,2}\\.\\d{1,2}\\.\\d{1,4}"

    name: str = None
    target: str = None
    version: str = None
    creation_date: datetime = None
    comment: str = None
    approved: bool = False
    body: object = None

    def is_valid(self):
        valid = True
        valid &= _is_present(self.name)
        valid &= _is_present(self.target)
        valid &= _is_present(self.comment)
        valid &= self._version_is_valid()
        valid &= self.creation_date is not None
        valid &= self.body is not None
        return valid

    def _version_is_valid(self) -> bool:
        return self.version is not None and bool(re.match(ConfigContainer.VERSION_PATTERN, self.version))


def _is_present(value: str) -> bool:
    return value is not None and not value.isspace()
