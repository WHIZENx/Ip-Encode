def convert_to_dec(n):
	result = 0
	for count in n:
		result = result << 1 | (count == '1')

	return result

def convert_to_bin(n, mode):
	result = ""
	if mode == 1:
		while len(result) < 2 << 2:
			result = str(n & 1) + result
			n >>=  1
	elif mode == 2:
		while len(result) < 2 << 4:
			result = str(n & 1) + result
			n >>=  1
	return result

def split_point(text):
	text = text.split(".")

	return text[0], text[1], text[2], text[3]