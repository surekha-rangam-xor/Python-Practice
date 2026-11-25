print(f"{'C':>5} {'F':>9} {'K':>9}")
 
for c in range(-20, 41, 10):
    f = c * 9 / 5 + 32
    k = c + 273.15
 
    print(f"{c:>5} {f:>9.1f} {k:>9.2f}")