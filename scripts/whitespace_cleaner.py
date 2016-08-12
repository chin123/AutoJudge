import os
import sys


def run():
	pass


if __name__ == '__main__':
	try:
		src_f_name = sys.argv[1]
		op_f_name = sys.argv[2]

		with open(src_f_name, 'r') as f_src:
			contents = f_src.read()
			with open(op_f_name, 'w') as f_out:
				f_out.write(contents)	

	except IndexError:
		print ''

