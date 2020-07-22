
'''
pip install nltk
pip install slate
pip install slate3k
pip install pdfminer
#may be unnecessary 
pip install PyPDF2
#for scanned PDF - not yet in use.
pip install textract
'''

from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords
import pdfminer

'''need section for calling folder and iterating through files - sending them 
to different functions depending on what type of file
Here's a draft 
if file_name.endswith('jpg'):
    print('The file is a JPEG')
'''

filename = 'sample_for_cleaning/r1.pdf' 


#function to get text chunk from pdf file using PDFMINER and Slate3

import slate3k as slate

text = []

'''First option keeps pages so don't delete yet
def create_text_chunk(filename):
    with open(filename, 'rb') as f:
        global doc
        doc = slate.PDF(f)
        '''


def create_text_chunk(filename):
    with open(filename, 'rb') as f:
        global doc
        doc = slate.PDF(f) 
    global text
    text = ' '.join(doc)
        
    
create_text_chunk(filename)
'''This explains the output of the function that retains pages above
doc
#prints the full document as a list of strings
#each element of the list is a page in the document
doc[0]
#prints the first page of the document'''


#tokenise and get rid of '\n'
tokens = word_tokenize(text)

tokens_clean = []

#Clean special characters divided by white space
def clean_punc(some_list):
        #we'll create a new list which contains punctuation we wish to clean
    global tokens_clean
    punctuations = ['*','**','***','****','*****','"','“','”']
    tokens_clean = [word for word in tokens if not word in punctuations]
    
clean_punc(tokens)

'''This is not working (yet!)
#Clean special characters which are part of the word string

words_clean = []

def clean_word_strings(a_list):
    global words_clean
    for word in a_list:
        word = word.rstrip('*')
        word = word.lstrip('*')
    words_clean = a_list

clean_word_strings(tokens_clean)
'''

'''Not yet sure that this will be helpful or necessary
#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
#stop_words = stopwords.words('english')

#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
#keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

#don't use stop_words
keywords = [word for word in tokens if not word in punctuations]'''

'''
#function for Indonesian hyphen issue
for index, word in enumerate(keywords):
    # Skip if first or last word is hyphen (as that would cause an index error)
    if word == '-' and index and index != len(keywords) - 1:  
        keywords[index] = keywords[index - 1] + keywords[index] + keywords[index + 1]
        keywords.pop(index - 1)
        keywords.pop(index)

'''





'''PyPDF2 method was not as successful as PDFminer

import PyPDF2 
import textract
#open allows you to read the file
pdfFileObj = open(filename,'rb')

text = ''

#function to get text chunk from pdf file using PyPDF2
def create_file_obj(pdfFileObj):
        #The pdfReader variable is a readable object that will be parsed
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        #discerning the number of pages will allow us to parse through all the pages
    num_pages = pdfReader.numPages
    count = 0
    global text
    text = ""

        #The while loop will read each page
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
            #This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
        if text != "":
           text = text
            #need to add else statement once computer updated and tesseract is working.
    return text

create_file_obj(pdfFileObj)







#filename = '2translation.pdf' 
filename = '2reading.pdf' 
#filename = '2grammar.pdf' 

#open allows you to read the file

pdfFileObj = open(filename,'rb')

#The pdfReader variable is a readable object that will be parsed

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#discerning the number of pages will allow us to parse through all #the pages

num_pages = pdfReader.numPages

count = 0
text = ""

#The while loop will read each page

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
    
#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.

if text != "":
   text = text
   
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text

else:
   text = textract.process(fileurl, method='tesseract', language='eng')
   
# Now we have a text variable which contains all the text derived 
#from our PDF file. Type print(text) to see what it contains. It 
#likely contains a lot of spaces, possibly junk such as '\n' etc.'''




'''This section may be useful to clean for Elpis
# Now, we will clean our text variable, and return it as a list of keywords.

#The word_tokenize() function will break our text phrases into 
#individual words
tokens = word_tokenize(text)

#Attempt to modify tokenize to have 'undang-undang' stay together
#tokens_regexp = regexp_tokenize(text, '\w+(?:-\w+)*')

#we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',','*','?']

#needs rules
# to keep 'duplicated-redup' type words as one string. 
# delete numbers?

#We initialize the stopwords variable which is a list of words like 
#"The", "I", "and", etc. that don't hold much value as keywords
#stop_words = stopwords.words('english')

#We create a list comprehension which only returns a list of words 
#that are NOT IN stop_words and NOT IN punctuations.
#keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

#don't use stop_words
keywords = [word for word in tokens if not word in punctuations]'''



'''#From Nic
prac_words = ['eat', 'undang', '-', 'undang', 'dance', 'kira', '-', 'kira', 'makan', 'go', 'final']

for index, word in enumerate(prac_words):
    # Skip if first or last word is hyphen (as that would cause an index error)
    if word == '-' and index and index != len(prac_words) - 1:  
        prac_words[index] = prac_words[index - 1] + prac_words[index] + prac_words[index + 1]
        prac_words.pop(index - 1)
        prac_words.pop(index)
   '''     
        
'''#For merging items from token list
for index, word in enumerate(keywords):
    # Skip if first or last word is hyphen (as that would cause an index error)
    if word == '-' and index and index != len(keywords) - 1:  
        keywords[index] = keywords[index - 1] + keywords[index] + keywords[index + 1]
        keywords.pop(index - 1)
        keywords.pop(index)
'''        

'''#to convert numbers to int and then delete?

prac_words = ['eat', '2', 'undang', 'dance', 'kira', '-', 'kira', '3', 'go', 'final']

def int_filter( someList ):
    for v in someList:
        try:
            int(v)
            continue # Skip these
        except ValueError:
            yield v # Keep these

keywords_2 = list( int_filter(keywords))
'''



'''#Zara attempt to solve hyphen issue - works but index errors will happen if '-' is prac_words[0]
prac_words = ['eat', 'undang', '-', 'undang', 'dance', 'kira', '-', 'kira', 'makan', 'go', 'final']
 
x = -1

for word in prac_words:
    x = x + 1
    if word == '-':
        prac_words[x] = prac_words[x-1] + prac_words[x] + prac_words[x+1]
        prac_words.pop(x-1)
        prac_words.pop(x)
        x = x - 1  
'''
        
