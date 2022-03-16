import getopt, sys
import gensim
from gensim import models, corpora
from gensim.models.ldamodel import LdaModel
from underthesea import word_tokenize

def LDA(texts):
    # Before topic extraction, we remove punctuations and stopwords.
    stopwords_file = 'vietnamese-stopwords.txt'
    with open(stopwords_file, 'r', encoding='utf8') as f:
        lines = f.readlines()
    my_stopwords = []
    for line in lines:
        my_stopwords.append(line.strip())
    punctuations=['.','!',',','?','(',')','"']

    # We prepare a list containing tokens
    all_tokens=[]
    for text in texts:
        tokens=[]
        raw=word_tokenize(text)
        for token in raw:
            if token not in my_stopwords:
                if token not in punctuations:
                    tokens.append(token)
                    all_tokens.append(tokens)

    # Creating a gensim dictionary and the matrix
    dictionary = corpora.Dictionary(all_tokens)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in all_tokens]

    # Building the model and training it with the matrix 
    model = LdaModel(doc_term_matrix, num_topics=5, id2word = dictionary,passes=40)

    return model.show_topics(num_topics=5, num_words=5) #, log=False, formatted=True

if __name__ == '__main__':
    """
        Argument from command line. To run: `python keyword_extraction.py --input_file <input_file> --result <output_file>`
    """

    options = ['input_file=', 'result=']

    try:
        args, vals = getopt.getopt(sys.argv[1:], '', options)
        for arg, val in args:
            if arg == '--input_file':
                input_file_name = str(val)
            if arg =='--result':
                output_file_name = str(val)
        
        with open(input_file_name, 'r', encoding='utf16') as f:
            texts = f.readlines()
        result = LDA(texts)
        with open(output_file_name, 'w', encoding='utf16') as f:
            for i in result:
                f.write(i[1])
                f.write('\n')
        print("Successfully wrote to file.")
    except:
        print("An exception occurred.")