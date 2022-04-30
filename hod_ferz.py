'''
      0    1    2    3    4    5    6    7
 0  ['0', '0', '0', '+', '0', '0', '0', '0']   8
 1  ['0', '0', '0', '+', '0', '0', '0', '+']   7
 2  ['+', '0', '0', '+', '0', '0', '+', '0']   6
 3  ['0', '+', '0', '+', '0', '+', '0', '0']   5
 4  ['0', '0', '+', '+', '+', '0', '0', '0']   4
 5  ['+', '+', '+', 'W', '+', '+', '+', '+']   3
 6  ['0', '0', '+', '+', '+', '0', '0', '0']   2
 7  ['0', '+', '0', '+', '0', '+', '0', '0']   1
      1    2    3    4    5    6    7    8
'''

y = int(input('x>>> ')) - 1
x = 8 - int(input('y>>> '))
sym = '🟢'
# pos = input('position 🐴: ')
pos = '👑'

mass = [['❎'] * 8 for k in range(8)]
if 0 <= x < 8 and 0 <= y < 8:
    for i in range(1, 8):
        d = f'{x}:{y + i}'  # right
        d1 = f'{x + i}:{y + i}'  # downright
        d2 = f'{x}:{y - i}'  # left
        d3 = f'{x - i}:{y - i}'  # upleft
        d4 = f'{x + i}:{y - i}'  # downleft
        d5 = f'{x - i }:{y + i}'  # upright
        d6 = f'{x-i}:{y}'  # up
        d7 = f'{x+i}:{y}'  # down
        s = d.split(':')
        s1 = d1.split(':')
        s2 = d2.split(':')
        s3 = d3.split(':')
        s4 = d4.split(':')
        s5 = d5.split(':')
        s6 = d6.split(':')
        s7 = d7.split(':')
        if 0 <= int(s[0]) < 8 and 0 <= int(s[-1]) < 8:
            mass[int(s[0])][int(s[-1])] = sym
        if 0 <= int(s1[0]) < 8 and 0 <= int(s1[-1]) < 8:
            mass[int(s1[0])][int(s1[-1])] = sym
        if 0 <= int(s2[0]) < 8 and 0 <= int(s2[-1]) < 8:
            mass[int(s2[0])][int(s2[-1])] = sym
        if 0 <= int(s3[0]) < 8 and 0 <= int(s3[-1]) < 8:
            mass[int(s3[0])][int(s3[-1])] = sym
        if 0 <= int(s4[0]) < 8 and 0 <= int(s4[-1]) < 8:
            mass[int(s4[0])][int(s4[-1])] = sym
        if 0 <= int(s5[0]) < 8 and 0 <= int(s5[-1]) < 8:
            mass[int(s5[0])][int(s5[-1])] = sym
        if 0 <= int(s6[0]) < 8 and 0 <= int(s6[-1]) < 8:
            mass[int(s6[0])][int(s6[-1])] = sym
        if 0 <= int(s7[0]) < 8 and 0 <= int(s7[-1]) < 8:
            mass[int(s7[0])][int(s7[-1])] = sym
        mass[x][y] = pos
else:
    print('only from 0 to 9')
for l in mass:
    for f in l:
        print(f, end='\t')
    print()
