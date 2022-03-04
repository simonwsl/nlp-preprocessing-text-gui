
#CORE PACKAGES - allow us to do the tabs and scrollable

import tkinter as tk #---acronym is added so that app structures will be more aesthetic
from tkinter import * #---import all modules defined in  tkinter
from tkinter import ttk #---provide access to Tk-themed widget set
from tkinter.scrolledtext import * #---provides a scrollable widget 

#NLP PACKAGES - to do text preprocessing

import nltk #---import the lirbaries for natural language processing
from textblob import TextBlob #---this is a python libraryfor processing textual data
from nltk.corpus import stopwords 
from nltk import PorterStemmer #---a package that performs stemming using different classes(i.e. porter stemmer)
from nltk.stem import WordNetLemmatizer #---group together different inflected forms of a word so they can be analyzed as a single item






#---create a window for the program
window = Tk()
window.title("NLP Preprocessing")
window.geometry("700x400") #width*height


#TAB LAYOUT - add 3 tab frames(windows)
tab_control = ttk.Notebook(window) #manage a collection of windows and displays a single one, at a time
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)


#ADD TAB TO NOTEBOOK
tab_control.add(tab1, text="Text Processor") #add a new tab to the window
tab_control.add(tab2, text="File Processor") 
tab_control.add(tab3, text="about") 

tab_control.pack(expand = 1, fill='both') #to display the tab


#TAB - ADD LABELS INSIDE THE TAB
label1 = Label(tab1, text='Welcome!', padx = 5, pady = 5) #the padding will move the position of the name 
label1.grid(column = 0, row = 0)

label2 = Label(tab2, text='Hello!', padx = 5, pady = 5) 
label2.grid(column = 0, row = 0)

label3 = Label(tab3, text='About', padx = 5, pady = 5) 
label3.grid(column = 0, row = 0)






#FUNCTION FOR NLP TAB1


#tokenization function
def get_tokens():
    raw_text = str(raw_entry.get()) #convert to string the raw text entered in box(named as raw entry)
    new_text = TextBlob(raw_text)
    final_text = new_text.words
    result = '\n Tokens: {}'.format(final_text)
    
    tab1_display.insert(tk.END, result) #display the final text


#POS Tagging function
def get_pos_tags():
    raw_text = str(raw_entry.get()) #convert to string the raw text entered in box(raw entry)
    new_text = TextBlob(raw_text)
    final_text = new_text.tags
    result = '\n Part of Speech(POS): {}'.format(final_text)
    
    tab1_display.insert(tk.END, result) #display the final text


#stopword removal function
def get_stopword_removal():
    raw_text = str(raw_entry.get()) #convert to string the raw text entered in box(raw entry)
    text = TextBlob(raw_text)
    tokens = set(text.words)
    stop = set(stopwords.words("english"))
    
    final_text = tokens-stop
    result = '\n Stopword removal: {}'.format(final_text)
    
    tab1_display.insert(tk.END, result) #display the final text


#porter stemmer function
def get_stemmer():
    raw_text = str(raw_entry.get()) #convert to string the raw text entered in box(raw entry)
    new_text = TextBlob(raw_text)
    
    ps = PorterStemmer() #---create a new name for PorterStemmer()
    final_text = new_text.words
    
    stemmed_text1 = [] #---an empty list
    for token in final_text:
        stemmed_text1.append(ps.stem(token)) #---add to empty list


    result = '\n Porter Stemmer: {}'.format(stemmed_text1)
    
    tab1_display.insert(tk.END, result) #display the final text


#lemmatization function
def get_lemmatize():
    raw_text = str(raw_entry.get()) #convert to string the raw text entered in box(raw entry)
    new_text = TextBlob(raw_text)
        
    lemmatizer = WordNetLemmatizer()
    final_text = new_text.words

    lemmatize_text1 = []
    for token in final_text:
        lemmatize_text1.append(lemmatizer.lemmatize(token))


    result = '\n Lemmatization: {}'.format(lemmatize_text1)
    
    tab1_display.insert(tk.END, result) #display the final text


#CLEANING TEXT/RESET
def clear_entry_text():
    entry1.delete(0, END) #---delete characters starting from index 0 until END

#CLEAR DISPLAY SCREEN
def clear_display_result():
    tab1_display.delete('1.0', END) #---delete chars starting from index 1(1st char) until END






#MAIN NLP TAB1
l1 = Label(tab1, text="Enter text to analyze")
l1.grid(row = 1, column = 0) #---position the label according to row and column

#create an empty box - to be passed into one of the functions to be pre-process
raw_entry = StringVar()
entry1 = Entry(tab1, textvariable = raw_entry, width = 50) #---set the length of the empty box
entry1.grid(row = 1, column = 1)



#BUTTONS
button1 = Button(tab1, text = 'tokenize', width = 15, bg='#03A9F4', fg='#FFF', command=get_tokens) #i want this button to be in tab1; thats why '..(tab1)'
button1.grid(row=4, column=0, padx=10, pady=10) #---position the button according to row and column; add padding on x-axis and y-axis

button2 = Button(tab1, text = 'pos tagging', width = 15, bg='#03A9F4', fg='#FFF', command=get_pos_tags) 
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab1, text = 'stopword removal', width = 15, bg='#03A9F4', fg='#FFF', command=get_stopword_removal) 
button3.grid(row=4, column=2, padx=10, pady=10)

button4 = Button(tab1, text = 'porter stemmer', width = 15, bg='#03A9F4', fg='#FFF', command=get_stemmer) 
button4.grid(row=5, column=0, padx=10, pady=10)

button5 = Button(tab1, text = 'lemmatization', width = 15, bg='#03A9F4', fg='#FFF', command=get_lemmatize) 
button5.grid(row=5, column=1, padx=10, pady=10)

button6 = Button(tab1, text = 'reset text', width = 15, bg='#03A9F4', fg='#FFF', command=clear_entry_text) 
button6.grid(row=5, column=2, padx=10, pady=10)

button7 = Button(tab1, text = 'clear result', width = 15, bg='#03A9F4', fg='#FFF', command=clear_display_result) 
button7.grid(row=6, column=1, padx=10, pady=10)



#Display screen for result
tab1_display = ScrolledText(tab1, height=10) #---use ScrolledText so that can scroll through the result
tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5) 


"""===========FILE PROCESSING TAB==============================="""


#FUNCTIONS FOR TAB2 --- 
#similar functions, except the 1st line of code of each function

def open_file():
    file1 = tk.filedialog.askopenfilename(filetypes=(("Text Files", ".txt"), ("All files","*"))) #the "*" means to receive and be able to open all types of files; will displayed as options once the button is pressed on the bottom right corner
    read_text = open(file1).read() #display the content of the file
    displayed_file.insert(tk.END, read_text) #end operation after displaying file


#tokenization function
def get_file_tokens():
    raw_text = displayed_file.get('1.0', tk.END) #take all characters starting with index 1(1st char), until END
    new_text = TextBlob(raw_text)
    final_text = new_text.words
    result = '\n Tokens: {}'.format(final_text)
    
    tab2_display_text.insert(tk.END, result) #display the final text


#POS Tagging function
def get_file_pos_tags():
    raw_text = displayed_file.get('1.0', tk.END) #take all characters starting with index 1(1st char), until END
    new_text = TextBlob(raw_text)
    final_text = new_text.tags #tag the word
    result = '\n POS of Speech: {}'.format(final_text)

    tab2_display_text.insert(tk.END, result) #display the final text


#stopword removal function
def get_file_stopword_removal():
    raw_text = displayed_file.get('1.0', tk.END) #take all characters starting with index 1(1st char), until END
    text = TextBlob(raw_text)
    tokens = set(text.words)
    stop = set(stopwords.words("english"))
    
    final_text = tokens-stop
    result = '\n Stopword removal: {}'.format(final_text)
    

    tab2_display_text.insert(tk.END, result) #display the final text


#porter stemmer function
def get_file_stemmer():
    raw_text = displayed_file.get('1.0', tk.END) #take all characters starting with index 1(1st char), until END
    new_text = TextBlob(raw_text)
    
    ps = PorterStemmer()
    final_text = new_text.words
    
    stemmed_text1 = []
    for token in final_text:
        stemmed_text1.append(ps.stem(token))


    result = '\n Porter Stemmer: {}'.format(stemmed_text1)

    tab2_display_text.insert(tk.END, result) #display the final text


#lemmatization function
def get_file_lemmatize():
    raw_text = displayed_file.get('1.0', tk.END) #take all characters starting with index 1(1st char), until END
    new_text = TextBlob(raw_text)
        
    lemmatizer = WordNetLemmatizer()
    final_text = new_text.words

    lemmatize_text1 = []
    for token in final_text:
        lemmatize_text1.append(lemmatizer.lemmatize(token))


    result = '\n Lemmatization: {}'.format(lemmatize_text1)
    
    tab2_display_text.insert(tk.END, result) #display the final text



#CLEANING TEXT/RESET
def clear_text_file():
    displayed_file.delete('1.0', END) #---delete chars starting from index 1(1st char) until END


#CLEAR THE DISPLAY RESULT SCREEN
def clear_result():
    tab2_display_text.delete('1.0', END) #---delete chars starting from index 1(1st char) until END






l1 = Label(tab2, text='Open File to Process', padx = 5, pady = 5) #the padding will move the position of the name 
l1.grid(column = 1, row = 1)

displayed_file = ScrolledText(tab2, height=10)
displayed_file.grid(row=2, column=0, columnspan=3, padx=5, pady=3)



#BUTTONS
b0 = Button(tab2, text = 'open file', width = 12, command=open_file, bg='#03A9F4', fg='#FFF') #i want this button to be in tab1; thats why '..(tab1)'
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text = 'tokenize', width = 12, command=get_file_tokens, bg='#03A9F4', fg='#FFF') 
b1.grid(row=3, column=1, padx=10, pady=10)

b2 = Button(tab2, text = 'pos tagger', width = 12, command=get_file_pos_tags, bg='#03A9F4', fg='#FFF') 
b2.grid(row=3, column=2, padx=10, pady=10)

b3 = Button(tab2, text = 'stopword removal', width = 12, command=get_file_stopword_removal, bg='#03A9F4', fg='#FFF') 
b3.grid(row=4, column=0, padx=10, pady=10)

b4 = Button(tab2, text = 'porter stemmer', width = 12, command=get_file_stemmer, bg='#03A9F4', fg='#FFF') 
b4.grid(row=4, column=1, padx=10, pady=10)

b5 = Button(tab2, text = 'lemmatization', width = 12, command=get_file_lemmatize, bg='#03A9F4', fg='#FFF') 
b5.grid(row=4, column=2, padx=10, pady=10)

b6 = Button(tab2, text = 'reset', width = 12, command=clear_text_file, bg='#03A9F4', fg='#FFF') 
b6.grid(row=5, column=0, padx=10, pady=10)


b6 = Button(tab2, text = 'clear result', width = 12, command=clear_result, bg='#03A9F4', fg='#FFF') 
b6.grid(row=5, column=1, padx=10, pady=10)


#DISPLAY RESULT SCREEN 
tab2_display_text = ScrolledText(tab2, height=10) #---use ScrolledText so that can scroll through the result
tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)


"""==========ABOUT TAB======================"""
about_label = Label(tab3, text="You are here", padx=5, pady=5)
about_label.grid(column=0, row=1)



#everything before the following code must be inside in order for them to be displayed on the window
window.mainloop()