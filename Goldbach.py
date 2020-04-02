"""
    参数en为输入的N
    奇数(odd number): 指不能被2整除的整数
    素数(prime number): 质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数
    合数(composite number): 指在大于1的整数中除了能被1和本身整除外，还能被其他数（0除外）整除的数
    哥德巴赫猜想(Goldbach)：任何一个大于或等于6的偶数都可以写成两个奇素数之和
"""
import math


def is_composite_or_prime_number(r, x, k):      # 判断奇数X是素数还是合数
    while r < k+1:
        n = (x - (2 * r - 1) ** 2) / (2 * (2 * r - 1)) + 1
        xs, zs = math.modf(n)
        if xs > 0:
            r += 1
        else:
            return "composite"      # 返回合数标识
    return "prime"                  # 返回奇数标识


def is_prime_number(i, en):         # 验证一个偶数是否等于两个奇素数之合
    xi = 2*en - i
    m = int(xi ** 0.5)
    if m % 2 == 0:
        ki = m / 2
    else:
        ki = (m + 1) / 2
    ri = 2

    if is_composite_or_prime_number(ri, xi, ki) == "prime":
        if i < 9:       # 以en为中数，判断待验证偶数2*en的一个加数2*en-i为素数
            ""
            # print("{} 可以写成两个奇素数 {}，{}之和".format(2*en, xi, 2*en-xi))
        else:           # 以en为中数，判断待验证偶数2*en的另一个加数i为素数
            is_left_prime_number(i, en)
    else:
        if i >= en:
            print("{}不能写成两个奇素数之和".format(en))
        else:           # 如果待验证偶数2*en的加数2*en-i不为素数，就判断下一下加数2*en-(i+2)是否为素数，直到找到下一个素数
            i += 2
            is_prime_number(i, en)


def is_left_prime_number(i, en):        # 判断待验证偶数的较小的加数为素数
    yi = i
    f = int(yi ** 0.5)
    if f % 2 == 0:
        ki = f / 2
    else:
        ki = (f + 1) / 2
    ri = 2

    if is_composite_or_prime_number(ri, yi, ki) == "prime":
        ""
        # print("{} 可以写成两个奇素数 {}，{}之和".format(2*en, 2*en-yi, yi))
    else:
        if i >= en:
            print("{}不能写成两个奇素数之和".format(en))
        else:
            i += 2
            is_prime_number(i, en)


def main():
    for j in range(22000000, 22200000):
        eni = j
        ii = 3
        is_prime_number(ii, eni)


main()
