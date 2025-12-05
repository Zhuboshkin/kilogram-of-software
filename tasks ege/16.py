f={}
for n in range(3000,0,-1):
    if n>=2025:
        f[n]=n
    else:
        f[n]=n*2+f[n+2]
print(f[82]-f[81])

f = {}
for n in range(1,48000):
    if n < 20:
        f[n] = n
    else:
        f[n] = (n - 6) * f[n - 7]
print((f[47872] - 290 * f[47865]) / f[47858])
