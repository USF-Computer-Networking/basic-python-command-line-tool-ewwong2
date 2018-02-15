# Function: This program demonstrates the use
#           of command line tools. 
# 

import argparse
import sys

def greet():
	print "Hello, Welcome to commandLineTools.py!"

def closing():
	print "Bye!"

def compute(args):
	if args.writeTo:
		with open(args.writeTo, 'w') as file:
			file.write("{}".format(args.x**args.y))

	if args.simple:
		print args.x**args.y
	elif args.explain:
		sys.stdout.write(("{}*").format(args.x)*(args.y-1))
		sys.stdout.write("{}={}\n".format(args.x,args.x**args.y))
		sys.stdout.flush()
	else:
		print "{} to the power of {} is {}".format(args.x,args.y,args.x**args.y)

if __name__=='__main__':
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	parser.add_argument("x", type=int, help="the base")
	parser.add_argument("y", type=int, help="the exponent")
	parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="count", default=0)
	parser.add_argument("-g", "--greet", help="prints greeting", action="store_true")
	parser.add_argument("-c", "--closing", help="prints closing", action="store_true")
	group.add_argument("-w", "--writeTo", help="write simple answer to file")
	group.add_argument("-s", "--simple", help="only print answer of compute", action="store_true")
	group.add_argument("-e", "--explain", help="show work of compute", action="store_true")
	args = parser.parse_args()

	if not args.simple and args.greet:
		greet()

	compute(args)

	if not args.simple and args.verbosity >= 1:
		print "{} verbosity".format(args.verbosity)

	if not args.simple and args.closing:
		closing()
