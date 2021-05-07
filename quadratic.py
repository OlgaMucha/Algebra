import math

def quadratic(a, b, c):
    """Calculates solutions of any quadratic equation"""

    print('Solving quadratic equation {}x2 + {}x + {} = 0'.format(a, b, c))

    if a == 0:
        if b == 0:
            print('Equation {}x2 + {}x + {} = 0 doesnt have any solution'.format(a, b, c))
            return None
        elif c == 0:
            print('Equation {}x2 + {}x + {} = 0 - every x is a solution'.format(a, b, c))
            return
        else:
            solution = -c/b
            print('Equation {}x2 + {}x + {} = 0 has one solution, {}'.format(a, b, c, solution))
            return solution
    else:
        delta = b*b - 4*a*c
        print('delta = ', delta)
        if delta < 0:
            print('Equation {}x2 + {}x + {} = 0 doesnt have any solution'.format(a, b, c))
            return None
        elif delta == 0:
            solution = -b/(2*a)
            print('Equation {}x2 + {}x + {} = 0 has one solution, {}'.format(a, b, c, solution))
            return solution
        else:
            solution1 = (-b - math.sqrt(delta))/(2*a)
            solution2 = (-b + math.sqrt(delta))/(2*a)
            print('Equation {}x2 + {}x + {} = 0 has two solutions, {} and {}'.format(a, b, c, solution1, solution2))
            return solution1, solution2

quadratic(0,0,6)