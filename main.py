import argparse
import sys


def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description='Bio-Evolution Simulator')
    parser.add_argument('--init', type=str, help='Initialization parameters for the simulation')
    parser.add_argument('--visualize', action='store_true', help='Enable visualization options')

    args = parser.parse_args()

    # Simulation initialization
    if args.init:
        print(f'Initializing simulation with parameters: {args.init}')
    else:
        print('No initialization parameters provided.')

    # Visualization options
    if args.visualize:
        print('Visualization enabled.')
    else:
        print('Running simulation without visualization.')


if __name__ == '__main__':
    main()