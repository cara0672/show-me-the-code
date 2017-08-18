import collections

def count(text_name,word):
    with open(text_name,'r') as f:
        text = f.read()
        text = text.split()
        c = collections.Counter(text)
        print(c[word])

count('0004.txt','want')

if __name__ == '__main__':
    count('0004.txt','the')