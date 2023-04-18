'''
How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

Examples:
- h = 3, bounce = 0.66, window = 1.5, result is 3
'''

def bouncing_ball(h, bounce, window):
    if not (h > 0 and (bounce > 0 and bounce < 1) and window < h):
        return -1
    else:
        return 1 if h < window else 2 + bouncing_ball((h * bounce), bounce, window)
        # return 1 if the bounce doesn't reach the window
        # return 2 + the new parameters for the function, i.e: new height of drop from rebound