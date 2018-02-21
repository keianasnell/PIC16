sample = "Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in \
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia \
deserunt mollit anim id est laborum."

lorem_list = sample.split() 

#Using dict comprehension method (algorithm 1)
d = {word: lorem_list.count(word) for word in lorem_list}
print d
#Calculating number of unique words
unique_words = len(d) #64 words


#Using counting algorithm (algorithm 2)
a = {}
for word in lorem_list:
    if word not in a:
        a[word] = 1
    else:
        a[word] += 1



f = open('/Users/keianarei/Desktop/Assignment 1/a_christie.txt', 'r')
agatha = f.read()
f.close()

#using algorithm 1
agatha_list = agatha.split()
x = {word: agatha_list.count(word) for word in agatha_list}
print x

#using algorithm 2
b = {}
for word in agatha_list:
    if word not in b:
        b[word] = 1
    else:
        b[word] += 1
        
print b['found'] #50 times
    