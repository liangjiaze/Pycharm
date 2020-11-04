some_sentences = '''\
I love learning python
because python is fun
and also easy to use
'''

f = open('Five_Two_sentences.txt', 'w')

f.write(some_sentences)
f.close()

# f = open('Five_Two_sentences.txt')
# while True:
#     line = f.readline()
#     if len(line) == 0:
#         break
#     print(line)
# f.close()
