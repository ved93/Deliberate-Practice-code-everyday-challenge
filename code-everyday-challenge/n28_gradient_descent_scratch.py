


import random
import tqdm

num_friends = [100.0,49,41,40,25,21,21,19]
daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4 ]

outlier = num_friends.index(100)    # index of outlier

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]


def predict(alpha: float, beta: float, x_i: float) -> float:
    return beta * x_i + alpha

def error(alpha: float, beta: float, x_i: float, y_i: float) -> float:
    """
    The error from predicting beta * x_i + alpha
    when the actual value is y_i
    """
    return predict(alpha, beta, x_i) - y_i


def sum_of_sqerrors(alpha: float, beta: float, x, y) -> float:
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))

def gradient_step(v, gradient, step_size: float) :
    """Moves `step_size` in the `gradient` direction from `v`"""
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)

def scalar_multiply(c: float, v) :
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]

def add(v, w) :
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


num_epochs= 10000
random.seed(0)

#choose random value to start
guess = [random.random(), random.random()] 

learning_rate = 0.001

with tqdm.trange(num_epochs) as t:
    for _ in t:
        alpha, beta = guess
    
        # Partial derivative of loss with respect to alpha
        grad_a = sum(2 * error(alpha, beta, x_i, y_i)
                        for x_i, y_i in zip(num_friends_good,
                                            daily_minutes_good))


        # Partial derivative of loss with respect to beta
        grad_b = sum(2 * error(alpha, beta, x_i, y_i) * x_i
                        for x_i, y_i in zip(num_friends_good,
                                            daily_minutes_good))

        # Compute loss to stick in the tqdm description
        loss = sum_of_sqerrors(alpha, beta,
                                num_friends_good, daily_minutes_good)
        t.set_description(f"loss: {loss:.3f}")

 # Finally, update the guess
        guess = gradient_step(guess, [grad_a, grad_b], -learning_rate)

    # We should get pretty much the same results:
alpha, beta = guess
assert 22.9 < alpha < 23.0
assert 0.9 < beta < 0.905


print(alpha, beta)
