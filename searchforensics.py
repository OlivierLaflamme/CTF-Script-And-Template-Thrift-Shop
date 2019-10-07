#!/usr/bin/env python
import glob, re
for f in glob.iglob('.git/objects/*/*'):
  m = re.search('([0-9a-f]{2})/([0-9a-f]+)', f)
  if m:
    g = m.groups()
    print("{}{}".format(g[0],g[1]))
