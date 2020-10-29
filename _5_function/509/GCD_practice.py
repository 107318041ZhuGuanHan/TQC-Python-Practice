def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

gcd_value = gcd(12, 16)  # 隨便擺數字進去開debug模式來理解

print(gcd_value)