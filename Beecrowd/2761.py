import struct  # https://docs.python.org/3/library/struct.html
inteiro, real, char, string = input().split(maxsplit=3)
inteiro = int(inteiro)
real = struct.unpack('f', struct.pack('f', float(real)))[0] 
print(f"{inteiro}{real:.6f}{char}{string}")
print(f"{inteiro}\t{real:.6f}\t{char}\t{string}")
print(f"{inteiro:>10}{real:>10.6f}{char:>10}{string:>10}")