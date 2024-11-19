  if final_synonyms == []:
        return word
    if word.istitle():
        return random.choice(final_synonyms).title()
    else:
        return random.choice(final_synonyms)
    
def plagiarism_removal(para):
    para_split = word_tokenize(para)
    final_text = []
    for i in para_split:
        final_text.append(plagiarism_remover(i))
    final_text = " ".join(final_text)
    return final_text

import tkinter as tk  
from functools import partial   
def call_result(label_result, n):  
    text = n.get()   
    result = plagiarism_removal(text)
    label_result.config(text="Text after plagiarism removal is:\n %s" % result,wraplength=500)  
    return    
root = tk.Tk()  
root.geometry('1000x1000')    
root.title('Plagiarism Removal')  
number1 = tk.StringVar()  
labelNum1 = tk.Label(root, text="Enter text to remove plagiarism")
labelNum1.grid(row=1, column=0)  
labelResult = tk.Label(root)  
labelResult.grid(row=7, column=2)  
entryNum1 = tk.Entry(root, textvariable=number1)
entryNum1.grid(row=1, column=2)     
call_result = partial(call_result, labelResult, number1)   
buttonCal = tk.Button(root, text="Remove Plagiarism", command=call_result)
buttonCal.grid(row=3, column=0)   
root.mainloop()  
