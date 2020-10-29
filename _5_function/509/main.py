# 自己寫的
def compute(x, y, m, n):
    p = (x * n) + (y * m)  # 分子的部分(直接乘起來相加)
    q = (y * n)            # 分母的部分(直接相乘)

    gcd = 0   # 1.用變數
    cds = []  # 2.用list
    for n in range(1, min(p, q)):
        if (p % n == 0) and (q % n == 0):
            gcd = n             # 1.用變數
            cds.append(n)       # 2.用list

    p_var = p / gcd             # 1.用變數
    q_var = q / gcd             # 1.用變數
    p_list = p / (max(cds))     # 2.用list
    q_list = q / (max(cds))     # 2.用list
    return p_var, q_var, p_list, q_list


x, y = eval(input("請輸入第一個分數(x/y)的分子(x)與分母(y)，以逗號隔開: "))
m, n = eval(input("請輸入第二個分數(m/n)的分子(m)與分母(n)，以逗號隔開: "))

var_p, var_q, list_p, list_q = compute(x=x, y=y, m=m, n=n)

print("Var: (%d / %d) + (%d / %d) = (%d / %d)"
      % (x, y, m, n, var_p, var_q))     # 1.用變數

print("List: (%d / %d) + (%d / %d) = (%d / %d)"
      % (x, y, m, n, list_p, list_q))   # 2.用list

# ★參考答案直接用遞迴的方式




# ----------------------------------------------------------------------
# 網路上找的
def gcd(m, n):  #   最大公因數
    return m if n == 0 else gcd(n, m % n)


def lcm(m, n):  #   最小公倍數
    return m * n // gcd(m, n)


m = int(input("輸入 m："))
n = int(input("輸入 n："))
print("Gcd: ", gcd(m, n))
print("Lcm: ", lcm(m, n))

# ----------------------------------------------------------------------
# 自己練習用遞迴寫輾轉相除法
def gcd(p, q):
    return p if q == 0 else gcd(q, p % q)


x, y = eval(input("請輸入第一個分數(x/y)的分子(x)與分母(y)，以逗號隔開: "))
m, n = eval(input("請輸入第一個分數(m/n)的分子(m)與分母(n)，以逗號隔開: "))

p = (x * n) + (y * m)
q = y * n

gcd_value = gcd(p, q)  # 得到最大公因數

p_out = p / gcd_value  # 化到最簡分數
q_out = q / gcd_value  # 化到最簡分數

print("(%d / %d) + (%d / %d) = (%d / %d)" % (x, y, m, n, p_out, q_out))