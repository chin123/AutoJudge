def clean(cont):
	try:
		a = len(cont)
		i = 0
		wh = {b'\r', b' ', b'\t'}
		while i < a:
			if bytes([cont[i]]) == b'\n':
				while i - 1 >= 0:
					if bytes([cont[i - 1]]) not in wh:
						break
					cont = cont[:i - 1] + cont[i:]
					i -= 1
					a -= 1
			i += 1
	except IndexError:
		print("Error at", i)
	return cont
