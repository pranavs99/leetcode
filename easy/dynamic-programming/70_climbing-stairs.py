def climbStairs(self, n: int) -> int:
    # store the solutions to the previous two values of n
    # for n = 0 and n = 1, there's only one way to climb stairs
    previous = [1, 1]
    for i in range(2, n + 1):
        # the number of ways to climb n stairs is equal
        # to the number of ways to climb n - 1 stairs (by tacking on
        # one more step) + n - 2 stairs (by skipping a step)
        current = previous[0] + previous[1]
        previous[0] = previous[1]
        previous[1] = current
    return previous[-1]