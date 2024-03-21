import re


# 01. Answer: Why is this method not clean?
# 02. Create a test-harness
# 03. Refactor towards cleaner method
def fits_parse_op_keywords(queue, hdr):
    """
    Parses keywords 'OP123_KEY' from a given FITS header.
    Those keywords are used to store the operations performed on the data-cube.
    """
    i = 0
    while True:
        r = re.compile(r'OP{}_'.format(i))
        op_keys = list(filter(r.match, hdr.keys()))
        if not op_keys:
            break

        op = {}
        for op_key in op_keys:
            key = re.match(r'OP.*_(.*)', op_key).group(1).lower()
            op[key] = hdr[op_key]
        queue.append(op)
        i += 1

    return queue


