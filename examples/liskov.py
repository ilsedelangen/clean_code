class LiskovExample:

    def __init__(self, char):
        self._char = char

    def meets_condition(self, conditions: list) -> bool:
        for i in range(len(conditions)):
            if self._matches(conditions[i]):
                return True
        return False

    def meets_condition_refactored(self, conditions: list) -> bool:
        return any(self.meets_condition(c) for c in conditions)

    def _matches(self, condition):
        return condition == self._char
