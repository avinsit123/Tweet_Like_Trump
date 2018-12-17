

import preprocessor as p
import re


def unicodetoascii(text):

    TEXT = (text.
    		replace('\\xe2\\x80\\x99', "'").
            replace('\\xc3\\xa9', 'e').
            replace('\\xe2\\x80\\x90', '-').
            replace('\\xe2\\x80\\x91', '-').
            replace('\\xe2\\x80\\x92', '-').
            replace('\\xe2\\x80\\x93', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x98', "'").
            replace('\\xe2\\x80\\x9b', "'").
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9d', '"').
            replace('\\xe2\\x80\\x9e', '"').
            replace('\\xe2\\x80\\x9f', '"').
            replace('\\xe2\\x80\\xa6', '...').#
            replace('\\xe2\\x80\\xb2', "'").
            replace('\\xe2\\x80\\xb3', "'").
            replace('\\xe2\\x80\\xb4', "'").
            replace('\\xe2\\x80\\xb5', "'").
            replace('\\xe2\\x80\\xb6', "'").
            replace('\\xe2\\x80\\xb7', "'").
            replace('\\xe2\\x81\\xba', "+").
            replace('\\xe2\\x81\\xbb', "-").
            replace('\\xe2\\x81\\xbc', "=").
            replace('\\xe2\\x81\\xbd', "(").
            replace('\\xe2\\x81\\xbe', ")").
            replace('\\xe2\\x80\\x99', "'")

                 )
    return TEXT
if __name__=="__main__":
    row = []
    crimefile = open('Tweets of Trump.txt', 'r')
    for line in crimefile.readlines():
        row.append([line])
        for i in line.split(","):
            row[-1].append(i)
    #a=p.clean("Thank you to @tim_cook for agreeing to expand operations in the U.S. and thereby creating thousands of jobs! https://t.co/2zOVxp9nTF']\n")
    #print(row[19])
    cleaned_tweets=[]
    for tweet in row:
        print(type(tweet))
        ar = str(tweet)
        gody = ar.split("'")
        gody = gody[1]
        gody = p.clean(gody)
        cleaned_tweets.append(gody)

            #print(cleaned_tweets[i])

    with open('Cleaned Tweets of Trump.txt', 'w') as f:
        for item in cleaned_tweets:
            f.write("%s\n" % item)




