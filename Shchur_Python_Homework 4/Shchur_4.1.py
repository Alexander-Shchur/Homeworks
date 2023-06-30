'''
1. Отделом исследований было получена записка:
ʺABBABAABAB AABBBAAABAAABABABBABABAAA ABABAABABBBBBBABABBBAAAAAABBAAABAAA ABBBABAABA BAABAAAAAAABAABABBABʺ

'''

print("Добрый день. Это домашняя работа по курсу Python,\nвыполненная студентом группы Python23 академии ТОР, Челябинск\n"
	  "Щур Александром Николаевичем.\nПреподаватель Андрей Комаров\n"
	  "________________________________________________________________________________________________________________")

#message = [["ABBAB","AABAB"],["AABBB","AAABA","AABAB","ABBAB","ABAAA"],["ABABA","ABABB","BBBBA","BABBB","AAAAA","ABBAA","ABAAA"],
#	["ABBBA","BAABA"],["BAABA","AAAAA","ABAAB","ABBAB"]]

message = "1"
key = {"а":"AAAAA","б":"ААААВ","в":"АААВА","г":"АААВВ","д":"ААВАА","е":"ААВАВ",
	"ж":"ААВВА","з":"ААВВВ","и":"АВААА","й":"АВААВ","к":"АВАВА","л":"АВАВВ",
	"м":"АВВАА","н":"ABBAB","о":"АВВВА","п":"АВВВВ","р":"ВАААА","с":"ВАААВ",
	"т":"ВААВА","у":"ВААВВ","ф":"ВАВАА","х":"ВАВАВ","ц":"ВАВВА","ч":"ВАВВВ",
	"ш":"ВВААА","щ":"ВВААВ","ъ":"ВВАВА","ы":"ВВАВВ","ь":"ВВВАА","э":"ВВВАВ",
	"ю":"ВВВВА","я":"ВВВВВ"}

descripted_message = []
'''
for x in message:
	word_1 = message[0] # ["ABBAB", "AABAB"]
	word_2 = message[1]
	word_3 = message[2]
	word_4 = message[3]
	word_5 = message[4]
print(word_1)
for y in key:
	letter_code = key.values()
	letter = key.keys()
print(letter_code)
'''


for value in key:
	if message == value:
		print("yes")
		descripted_message.append(1)

print(descripted_message)




print("________________________________________________________________________________________________________________\n"
	  "Благодарю вас за пользование моей программой.\n"
      "Направляйте свои замечания на электронную почту alexandershchoor@gmail.com.\n"
      "Спасибо за внимание.")