
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def freqDist(text):
    """
    function calculates frequency distribution of words in text using nltk package
    input: text
    output: dictionary of frequency distribution

    """



    tokenized=word_tokenize(text)
    result = FreqDist(tokenized)

    return  dict(result)


def freqDistNew(text):
    """
     function calculates frequency distribution of words in text using  for cycle
     input: text
     output: dictionary of frequency distribution

     """
    tokenized=word_tokenize(text)
    result={}
    for word in tokenized:
        if word in result.keys():
            result[word]+=1
        else:
            result[word]=1

    return  dict(result)

