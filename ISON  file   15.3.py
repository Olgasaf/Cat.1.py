#myfile = open('17-4.txt', 'r')
#f = myfile.read()
#print(f)
#myfile.close()

#with open('17-4.txt') as somefile:
#    a = somefile.readlines()
#    b = list(map(int, a))
#    print(b)

#
#with open('17-4.txt') as somefile:
#    s = somefile.readlines()
#    a = list(map(int, s))
#    res = []
#    for i in a:
#        if str(i).count('0') >= 2 and i % 7 == 0:
#            res.append(i)
#print(max(res), len(res))

#подсчитать количество слов
#file = open('17-4.txt')
#data = file.read()
#words = data.split()
#print(len(words))
#file.close()



#with open('17-4.txt') as f:
#    s = [int(x) for x in f]
#    res = []
#    for i in range(1, len(s)):
#        if (abs(s[i]) % 10 == 7 or abs(s[i-1]) % 10 == 7) and (s[i] + s[i-1]) % 12 == 0:
#            res.append(s[i] + s[i-1])
#print(len(res), max(res))
#print(s[i], ' ', s[i-1])

#ISON
#import json
#data = {
#    "name":"Ivan",
#    "age": 26
#}
#with open('data_file.json', 'w') as f:
#    json.dump(data, f)





