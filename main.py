#!/usr/bin/env python
#########################################################
# Convert the text file export of keepassx into org mode
#########################################################

pw = {}
d = {}
comment = False
for line in open('~/keepassx-export.txt').readlines():
    if line.startswith('*** '):
        title = ' '.join(line.split()[2:-1])
        pw[title] = []
        continue

    line = line.strip()

    if line.startswith('Title:'):
        pw[title].append(d)
        d = {
            'Url': ' ',
            'Title': ' ',
        }
        comment = False

    if not line:
        continue

    if comment:
        d['Comment'] += '\n' + line
        continue

    key = line.split(':')[0]
    value = ' '.join(line.split()[1:])

    d[key] = value

    if key == 'Comment':
        comment = True

for title, pw_list in pw.items():
    print "* %s (from Keypassx)" % title
    for pw in pw_list:
        title = ''

        if 'Url' in pw:
            title = pw['Url']

        if 'Title' in pw and pw['Title'] not in title:
            title += ' %s' % pw['Title']

        print "** %s" % title
        for k, v in pw.items():
            if k in ['Url', 'Title']:
                continue
            if not v:
                continue
            print "%s: %s" % (k, v)
