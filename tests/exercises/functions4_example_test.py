from ...exercises.functions4 import fits_parse_op_keywords
from ...exercises.functions4_refarctored import OperationsQueue

# -------------------- Original Test Harness --------------------


def test_legacy_single_complex():
    queue = fits_parse_op_keywords([], {'OP0_FOO': 'Test step 1', 'OP0_BAR': 'Test step 2', 'OP1_Test': 'BAZ'})
    assert queue == [{'foo': 'Test step 1', 'bar': 'Test step 2'}, {'test': 'BAZ'}]


def test_legacy_multiple():
    queue = fits_parse_op_keywords([], {'OP0_FOO': 'Test step 1'})
    queue = fits_parse_op_keywords(queue, {'OP0_FOO': 'Test step 2'})
    queue = fits_parse_op_keywords(queue, {'OP0_BAR': 'Test step 3', 'OP1_BAZ': 'Test step 4'})
    assert queue == [{'foo': 'Test step 1'}, {'foo': 'Test step 2'}, {'bar': 'Test step 3'}, {'baz': 'Test step 4'}]

# -------------------- Refactored Tests --------------------
# Same tests for the refactored version, just to prove that we didn't break anything.
# In real life one would change the existing code and tests, instead of creating new ones.
# Here we only keep it to make the process visible...


def test_operations_queue_complex():
    oq = OperationsQueue()
    oq.add_from_header({'OP0_FOO': 'Test step 1', 'OP0_BAR': 'Test step 2', 'OP1_Test': 'BAZ'})
    assert oq.queue == [{'foo': 'Test step 1', 'bar': 'Test step 2'}, {'test': 'BAZ'}]


def test_operations_queue_multiple():
    oq = OperationsQueue()
    oq.add_from_header({'OP0_FOO': 'Test step 1'})
    oq.add_from_header({'OP0_FOO': 'Test step 2'})
    oq.add_from_header({'OP0_BAR': 'Test step 3', 'OP1_BAZ': 'Test step 4'})
    assert oq.queue == [{'foo': 'Test step 1'}, {'foo': 'Test step 2'}, {'bar': 'Test step 3'}, {'baz': 'Test step 4'}]
