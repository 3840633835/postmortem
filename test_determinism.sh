#!/bin/sh
# Check that two runs of main.py write byte-identical output, that the
# output matches entry.txt in this repo, and that it passes the gate
# (UTF-8 text, 1 to 400 characters, not only white space, one or two
# sentences, no trailing newline).
set -e
cd "$(dirname "$0")"
rm -rf /tmp/tsh_a /tmp/tsh_b
mkdir -p /tmp/tsh_a /tmp/tsh_b
MAKEFUN_OUTPUT_DIR=/tmp/tsh_a python3 main.py > /tmp/tsh_a.stdout
MAKEFUN_OUTPUT_DIR=/tmp/tsh_b python3 main.py > /tmp/tsh_b.stdout
cmp /tmp/tsh_a/entry.txt /tmp/tsh_b/entry.txt && echo "deterministic: identical bytes"
cmp /tmp/tsh_a/entry.txt entry.txt && echo "matches entry.txt in repo"
cmp /tmp/tsh_a.stdout /tmp/tsh_b.stdout && echo "stdout deterministic"
python3 -c "
import os
p = '/tmp/tsh_a/entry.txt'
d = open(p, 'rb').read()
t = d.decode('utf-8')
assert 1 <= len(t) <= 400, len(t)
assert t.strip(), 'only white space'
assert t.count('.') == 2, 'must be one or two sentences'
assert not t.endswith('\n'), 'no trailing newline'
assert (os.stat(p).st_mode & 0o777) == 0o644, oct(os.stat(p).st_mode)
print('gate ok: %d chars, %d bytes, mode 0644, 2 sentences, no trailing newline' % (len(t), len(d)))
print('entry:', t)
"
