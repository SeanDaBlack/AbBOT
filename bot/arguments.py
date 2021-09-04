import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='Increases the verbosity of the output.', action='store_true')
parser.add_argument('-c', '--count', help='Set a maximum number of times to successfully submit to the form.', type=int, default=None)

args = parser.parse_args()
