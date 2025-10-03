s = 1

for n in range(1, 21):
    s *= ((25 * n**2) + 16*n + 21) / (n**3 + (15 * n**2 + 30))

print(s)
