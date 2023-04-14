def xor(x, s):
    print(x, 'xor', s, '=', s ^ x)
    print(bin(x), 'xor', bin(s), '=', bin(s ^ x))
    print('\n')

xor(4,0)
xor(4,4)
xor(255,1)
xor(255,128)

