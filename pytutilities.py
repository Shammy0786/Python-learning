import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    if args.o == 'sub':
        return args.x - args.y

    if args.o == 'mul':
        return args.x * args.y

    if args.o == 'div':
        return args.x / args.y

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument_group('--x', type=float, default=1.0,
                    help="Enter first number. This is a utility for calculation.")

    parser.add_argument_group('--y', type=float, default=3.0,
                          help="Enter second number. This is a utility for calculation.")

    parser.add_argument_group('--o', type=float, default=1.0,
                    help="This is a utility for calculation.")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args))) #This will write on cmd line