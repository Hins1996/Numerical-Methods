# Example functions
# 1. f1 and f2 are common functions to demonstrate the CT method
# 2. f3 and f4 are used to demonstrate measure transformation techniques in
#    numerical integration
def f1(x, y):
    # function f = e^(x+y)
    return np.exp(x+y)


def f2(x, y):
    # function f = e^(x*y)
    return np.exp(x*y)


def f3(r, theta):
    # function f = e^(x*y) * r, where x = r*cos(theta) and y = r*sin(theta)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return np.exp(x*y)*r


def f4(r, theta):
    # function f = (x+y) * r, where x = r*cos(theta) and y = r*sin(theta)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return (x+y)*r
