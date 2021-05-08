def set_of_equations(a, b, c, d, e, f):
    print('''solving set of equations: 
    {}x + {}y = {}
    {}x + {}y = {}'''.format(a, b, c, d, e, f))

    w = a*e - b*d
    wx = c*e - b*f
    wy = a*f - c*d

    if w == 0:
        if wx != 0 or wy != 0:
            print('this set of equations doesnt have any solution')
            return None
        else:
            print('every set (x, y) is a solution of this equation')
            return None
    else:
        x = wx / w
        y = wy / w
        print('solution of this equation is ({}, {})'.format(x, y))
        return x, y



set_of_equations(1, 3, 5, 8, 0, 2)
print('------------------------------------------------------------------')
set_of_equations(1, 1, 2, 1, 1, 3)
print('-------------------------------------------------------------------')
set_of_equations(1, 1, 2, 2, 1, 3)
