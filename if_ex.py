a = 0
if a == 10:
    print('a=10')
if a > 10:
    print('a>10')
if a < 10:
    print('a<10')

if a == 10:
    print('a=10')
elif a > 10:
    print('a>10')
else:
    print('Sorry ')

s = 'python'
if 'th' in s:
    print('Substring exists')

if not s.startswith('java'):
    print('Not there!')

if s != 'c++':
    print('Not C++')

if s[1:3] == 'yt':
    print('Wohoo')

l1 = [10, 20]
l2 = l1
l3 = l1.copy()

if 20 in l1:
    print('20 found!')
if l1 is l2:  # is compares the IDs of l1 and l2
    print('Both refer to the same object')
if id(l1) == id(l2):
    print('Same ID!')
if l1 == l3:
    print('Same Contents.')

d = {'a': 10, 'b': 20}
if 'b' in d:
    print('Key B found!')
if 'b' in d.keys():
    print('Key B FOund')
if 20 in d.values():
    print('20 found')
if ('a', 10) in d.items():  # D.items() gives the k:v tuples
    print('Found')
# if you want to keep any block empty then use a 'pass'. it doesnt do anything.
if a == 10:
    pass
