from ...examples.liskov import LiskovExample


class LiskovTestExample(LiskovExample):
    """
    We subclass the IospContainer such that we can intercept which conditions are checked.
    The original implementation stops, as soon as the first condition is true.
    We want to replicate and test this pattern.
    """

    def __init__(self, char):
        super().__init__(char)
        self.conditions_checked = []

    def _matches(self, condition):
        #: overwritten method, to intercept calls...
        self.conditions_checked.append(condition)
        return super()._matches(condition)


abc = ['A', 'B', 'C', 'D', 'E']
xyz = ['X', 'Y', 'Z']


def test_original():
    iosp_container = LiskovTestExample('C')
    assert iosp_container.meets_condition(abc)
    assert "B" in iosp_container.conditions_checked
    assert "D" not in iosp_container.conditions_checked

    assert not iosp_container.meets_condition(xyz)
    assert "Z" in iosp_container.conditions_checked


def test_refactored():
    iosp_container = LiskovTestExample('C')
    assert iosp_container.meets_condition_refactored(abc)
    assert "B" in iosp_container.conditions_checked
    assert "D" not in iosp_container.conditions_checked

    assert not iosp_container.meets_condition_refactored(xyz)
    assert "Z" in iosp_container.conditions_checked
