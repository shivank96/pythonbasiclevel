import re
#splitting operators in string using re.split() method

test_str = "15+22*3-4/2"
print(test_str)
result_str = re.split(r'(\D)',str(test_str))
print(result_str)

#split string on kth occurence

test_str1 = "Life_is_a_game_yo"
splt_chr = "_"
k=3
print(str(test_str1))
tmp = test_str1.split(splt_chr)
#method1
result_str1 = splt_chr.join(tmp[:k]),splt_chr.join(tmp[k:])#returns tuple
print(result_str1)
#method2
tmp1 = [x.start() for x in re.finditer(splt_chr,test_str1)]
res1 = test_str1[0:tmp1[k-1]]
res2 = test_str1[tmp1[k-1]+1:]
res3 = (res1+" "+res2).split(" ")#returns string
print(str(res3))
#format
str1 = "{} {} {}".format('Life','is','game')
print(str1)

str2 = "{1} {0} {2}".format('life','is','game')
print(str2)

str3 = "{i} {l} {g}".format(g='game',l='life',i='is')
print(str3)

#string alignment
str4 = "|{:<10}|{:^10}|{:>10}|".format('Life','is','game')
print(str4)

#logical operators in string

str5 = ' '
str6 = 'life'
#repr is used to print the string along with the quotes
print(repr(str5 and str6))
print(repr(str6 and str5))
print(repr(str5 or str6))
print(repr(str6 or str5))





