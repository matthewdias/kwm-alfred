import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--path')
parser.add_argument('--command')
args = parser.parse_args()

if args.path:
	file_ = open('path', 'w')
	file_.write(args.path)
	file_.close()

if args.command:
	file_ = open('path', 'r')
	kwm = file_.read() + 'kwmc'
	print kwm
	os.system(kwm + ' ' + args.command)
