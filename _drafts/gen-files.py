#!/usr/bin/env python
text = open('list', 'r')
content = text.read()
lines = content.split('\n')
for line in lines:
    line = line.strip()
    file = open('2014-01-19-' + line + '.markdown', 'w')
    file.write("""\
---
layout: post
title: """ + line + """
---

dummy text here for entry: """ + line)
    file.close()
