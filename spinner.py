from screeninfo import get_monitors
from mouse import move
from math import pi, cos, sin
from random import randint
from argparse import ArgumentParser


def get_arguments():
    parser = ArgumentParser(description='mouse spinner')
    parser.add_argument(
        '-r', '--radius', type=int, help='radius of the circle that mouse will spin around')
    parser.add_argument('-i', '--interval', type=int,
                        help='interval of smoothness')
    parser.add_argument('-c', '--count', type=int, help='count of full spins')
    parser.add_argument(
        '-s', '--slowness', type=int, help='slowness interval while this argument gets bigger mouse spins slower')
    parser.add_argument(
        '-d', '--direction', type=int, help='direction of spinning "1" for clockwise, "-1" fo counter clockwise')
    return parser.parse_args()


def is_prime(n: int):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**.5)+1):
            if n % i == 0:
                return False
        else:
            return True


def sleep(interval: int):
    x = [randint(100000, 500000) for _ in range(interval)]
    for i in x:
        is_prime(i)


def main(**kwargs):
    defaults = {
        'radius': 300,
        'interval': 180,
        'spin_count': 3,
        'slowness': 300,
        'direction': 1,
    }
    args = {}

    for k, v in defaults.items():
        if not kwargs[k]:
            args[k] = v
        else:
            args[k] = kwargs[k]

    mid = {'x': get_monitors()[0].width//2, 'y': get_monitors()[0].height//2}
    angle = 0
    step = pi / args['interval'] * args['direction']

    for _ in range(args['interval'] * 2 * args['spin_count']):
        x = cos(angle) * args['radius'] + mid['x']
        y = sin(angle) * args['radius'] + mid['y']
        move(x, y)
        angle += step
        sleep(args['slowness'])


if __name__ == '__main__':
    args = get_arguments()

    main(radius=args.radius, interval=args.interval,
         spin_count=args.count, slowness=args.slowness, direction=args.direction)
