#
#  https://stackoverflow.com/questions/30764296/algorithm-to-find-the-minimum-value-point-of-a-function
#
#  you can do a simple binary search on your domain to find a point k that satisfies 
#  f'(k-e) * f'(k+e) < 0 the smaller you pick e.
#
#  doing the search let [a,b] be the interval and k=(a+b)/2 
#  you would select left if f'(k)*f'(a) < 0 and right otherwise.
#  Having f(x), f'(x) = (f(x+e)-f(x))/e, again smaller you pick e, better the precision of the derivative.
#
# NOTE:
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=577877&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3088%5D%5Bvalue%5D%3D12%26searchoption%5B3088%5D%5Btype%5D%3Dradio%26searchoption%5B3046%5D%5Bvalue%5D%3D6%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
# 二分的时候一共有4个点当前左边界（a）当前右边界（b）中点（x）和 x+delta_x. delta_x一定是正值x和x+delta_x是用来求gradient的
# 规则是这样右边界（b）只能移动到x+delta_x左边界（a）只能移动到x
# 这是近似于二分但不是严格的二分但是可以保证每次循环理论最低点都在当前左边界（a）和当前右边界（b）之间
#
# stop condition is either f'(k-e) * f'(k+e) < 0, or f'(k) = 0, or (b-a) > 2*e
#


def func(x):
    ''' minimum of f(x) = 2*x^2 + 3*x -5 is at -3/4'''
    a, b, c = 2, 3, -5
    return a*x*x + b*x + c

# def func(x):
#     ''' minimum of f(x) = 2*x^4 + 8/3*x^3 - 5*x^2 -10*x + 20 '''
#     a, b, c, d, e = 2, 8.0/3, -5, -10, 20
#     return a*(x**4) + b*(x**3) + c*(x**2) +d*x + e


def differential(x, epsilon = 0.0001):
    return (func(x+epsilon) - func(x))/epsilon

def minimum_convex(a, b, epsilon = 0.0001):

    search, iter = True, 0
    while search and iter <= 100:
        mid = 0.5*(a+b)
        g_mid = differential(mid)
        # print (iter, a, mid, b, ", G(mid):", g_mid, b-a)
        g_mid_1, g_mid_2 = differential(mid+epsilon), differential(mid-epsilon)

        if g_mid_1*g_mid_1 < 0 or g_mid == 0 or b-a < 2*epsilon: 
            search = False
        else:
            g_a, g_b = differential(a), differential(b)
            if g_a * g_mid < 0:
                b = mid + epsilon
            elif g_b * g_mid < 0:
                a = mid
        iter += 1

    return mid


a, b, c = 2, 3, -5
print (minimum_convex(-3, 5))





