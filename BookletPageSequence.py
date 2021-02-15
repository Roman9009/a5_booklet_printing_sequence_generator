#Written by Roman Platek
#this is a small program used to help print multiple paged documents as foldable booklets.
#This program generate sequences of page numbers based on n number of pages and what is the first page
#it then creates a sequence that follows this pattern: n,n-1,1,2,n-2,n-3,3,4...n/2
#this sequence allows users to take the sequence input 
#and then copy it into a program where the document can print by custom page number order
#where the pages are printed in a 2 pages per a4 sheet with double sided printing.
#thus the pages can be folded into a booklet from the printing stack and stapled.
#a user facing gui has also been created to take user input and create the main sequence and 
#sequences for the front and back pages.
import copy
import tkinter as tk 
def bookletSeq(x,y):
    if x>y: raise ValueError
    #y is last page and must be greater than the first page
    #ie. y = 22
    Y = copy.copy(y)
    #first page
    #ie. x = 1
    p = 1
    #init lists
    seq=[]#full list
    seq_f=[]#front list
    seq_b=[]#back list
    #init output string
    message=""
    #seqential loop to create message and fill lists.
    while (y!=x):
        message= message +str(y)+','
        seq.append(y)
        y =y-1
        if x == y: break   
        message= message +str(x)+','
        seq.append(x)
        x+=1
        if x == y: break
        message= message +str(x)+','
        seq.append(x)
        x+=1
        if x== y: break   
        message= message+str(y)+','
        seq.append(y)
        y =y-1
        p=p+1
    message= message +str(y)+'\n'
    seq.append(y)
    message= message+str(p)+' pages'+'\n'
    i = 1

    while i-1 != len(seq):
        if(i%4 in [1,2]):
            seq_f.append(seq[i-1])
        else:
            seq_b.append(seq[i-1])
        i=i+1
    message= message +'Front: ' +str(seq_f)+'\n'
    message= message+'Back: '+str(seq_b)+'\n'
    return message
message="Fill in the number of the first and last page number, before computing page sequence"
def present_sequence(output,input1,input2):
    try:
        output.delete("@0,0", 'end')
        x=int(input1.get())
        y=int(input2.get())
        message_final=bookletSeq(x,y)
        output.insert('end',message_final)

    except (ValueError,TypeError):
        output.delete("@0,0", 'end')
        output.insert('end',"Error! \n")
        output.insert('end', message)
m =tk.Tk()
m.title('Booklet Page Sequence Calculator')
f=tk.Frame(m)
f.pack()
tk.Label(f, text='First Page Number').grid(row=0) 
tk.Label(f, text='Last Page Number').grid(row=1)

    
    
e1 = tk.Entry(f) 
e2 = tk.Entry(f) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
canvas_height=100
canvas_width=400
button = tk.Button(m, text='Compute', width=int(canvas_width/9)) 
button.pack()
f1=tk.Frame(m)
f1.pack(fill='both',expand='yes')
scrollbar = tk.Scrollbar(f1)
scrollbar.pack( side = 'right', fill = 'y' )
output = tk.Text(f1, bg='white', width=50,height=10, wrap='word',
                 yscrollcommand=scrollbar.set) 
output.pack(side='left',fill='both',expand='yes')




button.config(command=lambda: present_sequence(output,e1,e2))
output.insert('end', message)
scrollbar.config( command = output.yview )
#button.config(command=clearText(output))
m.mainloop()