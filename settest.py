#!/usr/bin/env python3

import sys

set_a = set()

for arg in sys.argv[1:]:
    set_a.add(arg)

print(set_a)
