
message = ["b", 16, 12, 18, 6, 20, 6, "b", 20, 30, 19, 6, 12, 18, 6, 20]

code = {"b":"a"}

for key in code:
	for x in message:
		if key == x:
			print(code[key])
