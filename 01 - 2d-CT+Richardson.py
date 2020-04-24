
'''##### PART 2 #####
Main function to do integration
'''
def integral(func, exact_sol, num_interval, xrange, yrange):
    '''
	DESCRIPTION
		a function to do two dimensional integration by composite trapezoid method (with Richardson extrapolation)
    INPUT 
        func: a real function to be integrated
        exact_sol: the exact solution of integration if available
        num_interval: a array of number of intervals used to partition integrand, which must be a geometric series 
					  (e.g. num_interval = [2, 4, 8, 16, ..., 128]). The purpose is to investigate the effect of numbers of 
					  partitions
        xrange/yrange: the integration range of x/ axis
     OUTPUT
	 	[Qcr_list, Qcr_Rd_list]: val of integration with and without Richardson extrapolation if exact_sol is None
		[error, error_Rd]: error of integration with and without Richardson extrapolation if exact_sol is provided
    '''

    Qcr_list = []
    Qcr_Rd_list = []
    error = []
    error_Rd = []
    for n in num_interval:
        h_x = (xrange[1] - xrange[0]) / n
        h_y = (yrange[1] - yrange[0]) / n
        w_x = np.repeat(h_x, n + 1)
        w_x[0] = h_x / 2
        w_x[-1] = h_x / 2
        w_y = np.repeat(h_y, n + 1)
        w_y[0] = h_y / 2
        w_y[-1] = h_y / 2
        x = np.linspace(xrange[0], xrange[1], n + 1)
        y = np.linspace(yrange[0], yrange[1], n + 1)
        Qcr = 0
        for i in range(n + 1):
            for j in range(n + 1):
                Qcr += w_x[i] * w_y[j] * func(x[i], y[j])
        Qcr_list.append(Qcr)
        if exact_sol is None:
            pass
        else:
            error.append(abs(Qcr - exact_sol))

        # Richardson Extrapolation
        if n > 2:
            Q_cr_Rd = 4 / 3 * Qcr_list[-1] - 1 / 3 * Qcr_list[-2]
            Qcr_Rd_list.append(Q_cr_Rd)
            if exact_sol is None:
                pass
            else:
                error_Rd.append(abs(Q_cr_Rd - exact_sol))

    error = np.array(error)
    error_Rd = np.array(error_Rd)
    Qcr_list = np.array(Qcr_list)
    Qcr_Rd_list = np.array(Qcr_Rd_list)
    if exact_sol is None:
        return [Qcr_list, Qcr_Rd_list]
    else:
        return [error, error_Rd]


'''##### PART 2 #####
Example functions
1. f1 and f2 are common functions for demonstrate
2. f3 and f4 are used to demonstrate measure transformation techniques in
   numerical integration
'''

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
