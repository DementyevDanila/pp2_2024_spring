from time import sleep


def sqrt_mls(n, time):
    sleep(time / (1000))
    print(f"Square root of {n} after {time} miliseconds is {n ** 0.5}")

sqrt_mls(int(input()), int(input()))