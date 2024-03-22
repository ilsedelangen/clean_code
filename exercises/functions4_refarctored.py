import re


class OperationsQueue:
    """
    A queue that keeps track of the operations performed on a FITS file (our data cube)
    """

    def __init__(self):
        self.queue = []

    def add_from_header(self, header) -> None:
        """
        Extracts all operations that are listed in the FITS header and that
        have a key matching the pattern 'OP\\d{3}_.*'.
        Adds them to the queue.
        """
        for i in range(len(header)):
            if not self._extract_operations(header, i):
                break

    def _extract_operations(self, header, idx) -> bool:
        keys = self._extract_keys(header, idx)
        keys = self._add_internal_names(keys)
        return self._add_operations_to_queue(header, keys)

    @staticmethod
    def _extract_keys(header, idx: int) -> list:
        r = re.compile(r'OP{}_'.format(idx))
        return list(filter(r.match, header.keys()))

    @staticmethod
    def _add_internal_names(keys) -> dict:
        return {re.match(r'OP.*_(.*)', key).group(1).lower(): key for key in keys}

    def _add_operations_to_queue(self, header, keys: dict) -> bool:
        if not keys:
            return False

        self.queue.append({internal_key: header[external_key] for internal_key, external_key in keys.items()})
        return True
