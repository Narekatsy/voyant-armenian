import string
from collections import Counter
import pandas as pd
import filter_words as fw
#import io
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from matplotlib.figure import Figure

def sort_word_freqs(book, minimum_frequency = 5):
    with open(book, 'r', encoding='utf-8') as file:
        text = file.read()

    #Remove punctuation and convert all characters to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation + '՛՝՞՜–―—֊․։։'))
    text = text.lower()

    #Split the text into words and count the frequency of each word
    words = text.split()
    word_counts = Counter(words)

    #Sort the words based on their frequency
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse = True)
    
    #Exclude the unnecessary words    
    filtered_words = [(word, count) for word, count in sorted_words if count > minimum_frequency
                      and len(word) > 1
                      and all(word not in lst for lst in [fw.shaghkapner, fw.ojandak_bayer, fw.kaper,
                                                          fw.andznakan_deranun, fw.cucakan_deranun,
                                                          fw.harcakan_deranun, fw.voroshyal_deranun,
                                                          fw.ayl_deranun, fw.armenian_symbols])]
    #Return words and frequencies
    for word, count in filtered_words:
        words = [word for word, count in filtered_words]
        counts = [count for word, count in filtered_words]
        return words, counts
    
'''
def sort_voyant(book, minimum_frequency = 5):
    with open(book, 'r', encoding='utf-8') as file:
        text = file.read()

    #Remove punctuation and convert all characters to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation + '՛՝՞՜–―—֊․։։'))
    text = text.lower()

    #Split the text into words and count the frequency of each word
    words = text.split()
    word_counts = Counter(words)

    #Sort the words based on their frequency
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse = True)
    
    #Exclude the unnecessary words    
    filtered_words = [(word, count) for word, count in sorted_words if count > minimum_frequency
                      and len(word) > 1]
    #Return words and frequencies
    for word, count in filtered_words:
        words = [word for word, count in filtered_words]
        counts = [count for word, count in filtered_words]
        return words, counts
'''

if __name__ == "__main__":
    book = "book_name.txt"
    words, counts = sort_word_freqs(book, 50)
    
    #Creating dataframes from words and frequencies
    df = pd.DataFrame(list(zip(words, counts)), columns =['Words', 'Counts'])
    
    #Plotting barplot
    #df.plot.bar(x = "Words", y ="Counts", figsize = (14, 6))    
    
    #Armenian df
    df01 = pd.DataFrame(list(zip(words1, counts1)), columns =['Բառեր', 'Քանակ'])
    
    #Plotting barplot
    #df01.plot.bar(x = "Բառեր", y ="Քանակ", figsize = (14, 6), title = "Հեղինակ - վերնագիր")

    #Real voyant data
    '''
    voyant_words1, voyant_counts1 = sort_voyant(book1, 8)
    voyant_df01 = pd.DataFrame(list(zip(voyant_words1, voyant_counts1)), columns =['Բառեր', 'Քանակ'])
    
    voyant_df01.plot.bar(x = "Բառեր", y ="Քանակ", figsize = (14, 6), title = "-Voyant- Հեղինակ - վերնագիր")
    '''
    
