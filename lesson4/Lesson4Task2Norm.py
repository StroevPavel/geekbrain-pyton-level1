# coding: utf-8

"""
Вывести символы в верхнем регистре, слева от которых находятся
два символа в нижнем регистре, а справа - два символа в верхнем регистре.
Т.е. из строки 
"GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
нужно получить список строк: ['AY', 'NOGI', 'P']
Решить задачу двумя способами: с помощью re и без.
"""
import re

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# Используем функцию RE
print("Используем функцию RE: ")
print(re.findall('[a-z]{2}([A-Z]+)[A-Z]{2}',line_2))

# НЕ Используем функцию RE
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

res = []
line2 = list(line_2[:])

i = 0
j = -1
k = 0
while i < len(line2):
	# ищем кейс {aaBCD}
	if len(line2) > (i+4): # остаток массива >= 5
		if (line2[i] in low)&(line2[i+1] in low)&(line2[i+2] in upper)&(line2[i+3] in upper)&(line2[i+4] in upper): # найден кейс {aaBCD}
			#print(line2[i] + line2[i+1] + line2[i+2] + line2[i+3] + line2[i+4])
			i += 2
			res.append('')
			j += 1
			while i < len(line2):
				if (len(line2) < (i+2)): # если остаток массива < 3
					break
				elif ((line2[i] in upper)&(line2[i+1] in upper)&(line2[i+2] in upper)): # найден {BCD}
					#print(line2[i] + line2[i+1] + line2[i+2])
					res[j] = res[j] + line2[i]
					i += 1
				else: # найден {BCD}
					i += 1
					break
	else:
		break
	i += 1
print("НЕ Используем функцию RE: ")
print(res)