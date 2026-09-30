import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    a = 1.0
    b = 1.0 / math.sqrt(2.0)
    t = 0.25
    p = 1.0

    for i in range(1000):
        a_temp = (a + b) / 2.0
        b_temp = math.sqrt(a * b)
        t_temp = t - p * (a - a_temp) ** 2
        p_temp = 2.0 * p

        a = a_temp
        b = b_temp
        t = t_temp
        p = p_temp
        pi_estimate = (a + b) ** 2 / (4 * t)

        if abs(pi_estimate - math.pi) < target_error:
            return pi_estimate

    return pi_estimate


desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
