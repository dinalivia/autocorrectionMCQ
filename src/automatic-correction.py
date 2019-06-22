# -------------------------------------
# Automatic correction
# --
# Read original image, adjust perspective,
# extract region of interest, process
# answers, correct them and save results
# in csv file.
#
# Developed by Dina Livia - 21.06.2019
# --------------------------------------

#!/usr/bin/python

# Standard imports
import csv
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

# Non standard imports
#import orb
#import otsu
#import pre_processing
#import process_gabarito
#import correction

'''
main = Tk()

main.title("Correcao automatica")
main.geometry("500x400")
var = StringVar()
label = Label(main, textvariable=var, relief=RAISED)

var.set("Selecione arquivo do gabarito")
label.pack()

doneButton = Tkinter.Button(main, text="botao", width=25, command=main.destroy)
doneButton.pack()

main.mainloop()

# receive path to read images
sec = Tk()
#root.filename = tkFileDialog.asksaveasfilename(initialdir = "/home/pi", title = "Selecione o arquivo de gabarito", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

sec.filename = tkFileDialog.askopenfilename(initialdir = "/home/pi/git/TCC/autocorrectionMCQ", title = "Selecione o arquivo de gabarito")
print (sec.filename)

sec.directory = tkFileDialog.askdirectory()
print (sec.directory)
'''


form = Tkinter.Tk()

getFld = Tkinter.IntVar()

form.wm_title('Correcao Automatica de provas multipla escolha')

# -- Gabarito --
stepOne = Tkinter.LabelFrame(form, text=" 1. Informe o gabarito da prova: ")
stepOne.grid(row=0, columnspan=7, sticky='W', \
             padx=5, pady=5, ipadx=5, ipady=5)

transChk = Tkinter.Checkbutton(stepOne, \
           text="Escrever sequencia", onvalue=1, offvalue=0)
transChk.grid(row=0, column=0, sticky='WE', padx=3, pady=2)

transRwLbl = Tkinter.Label(stepOne, \
                           text=" => Ex. a,b,c,d,e,a,b,c, ...")
transRwLbl.grid(row=0, column=1, columnspan=2, \
                sticky='W', padx=5, pady=2)

transRwTxt = Tkinter.Entry(stepOne)
transRwTxt.grid(row=1, columnspan=5, sticky='WE', padx=5, pady=2)

inFileLbl = Tkinter.Label(stepOne, text="Escolher imagem do gabarito:")
inFileLbl.grid(row=2, column=0, sticky='W ', padx=5, pady=2)

inFileTxt = Tkinter.Entry(stepOne)
inFileTxt.grid(row=2, column=1, columnspan=7, sticky="WE",pady=3)

inFileBtn = Tkinter.Button(stepOne, text="Buscar")
inFileBtn.grid(row=2, column=8, sticky='WE', padx=5, pady=2)

#outFileLbl = Tkinter.Label(stepOne, text="Save File to:")
#outFileLbl.grid(row=2, column=0, sticky='E', padx=5, pady=2)

#outFileTxt = Tkinter.Entry(stepOne)
#outFileTxt.grid(row=2, column=1, columnspan=7, sticky="WE", pady=2)

#outFileBtn = Tkinter.Button(stepOne, text="Browse ...")
#outFileBtn.grid(row=2, column=8, sticky='W', padx=5, pady=2)

#inEncLbl = Tkinter.Label(stepOne, text="Input File Encoding:")
#inEncLbl.grid(row=3, column=0, sticky='E', padx=5, pady=2)

#inEncTxt = Tkinter.Entry(stepOne)
#inEncTxt.grid(row=3, column=1, sticky='E', pady=2)

#outEncLbl = Tkinter.Label(stepOne, text="Output File Encoding:")
#outEncLbl.grid(row=3, column=5, padx=5, pady=2)

#outEncTxt = Tkinter.Entry(stepOne)
#outEncTxt.grid(row=3, column=7, pady=2)

# -- Respostas dos docentes --
stepTwo = Tkinter.LabelFrame(form, text=" 2. Informe as respostas dos docentes: ")
stepTwo.grid(row=3, columnspan=7, sticky='W', \
             padx=5, pady=5, ipadx=5, ipady=5)

inFileLb2 = Tkinter.Label(stepTwo, text="Escolher diretorio de imagens:")
inFileLb2.grid(row=4, column=0, sticky='WE', padx=5, pady=2)

inFileTxt2 = Tkinter.Entry(stepTwo)
inFileTxt2.grid(row=4, column=1, columnspan=7, sticky="WE", pady=3)

inFileBtn2 = Tkinter.Button(stepTwo, text="Buscar")
inFileBtn2.grid(row=4, column=8, sticky='W', padx=5, pady=2)

#outTblLbl = Tkinter.Label(stepTwo, \
#      text="Enter the name of the table to be used in the statements:")
#outTblLbl.grid(row=3, column=0, sticky='W', padx=5, pady=2)

#outTblTxt = Tkinter.Entry(stepTwo)
#outTblTxt.grid(row=3, column=1, columnspan=3, pady=2, sticky='WE')

#fldLbl = Tkinter.Label(stepTwo, \
#                       text="Enter the field (column) names of the table:")
#fldLbl.grid(row=5, column=0, padx=5, pady=2, sticky='W')

#getFldChk = Tkinter.Checkbutton(stepTwo, \
#                       text="Get fields automatically from input file",\
#                       onvalue=1, offvalue=0)
#getFldChk.grid(row=5, column=1, columnspan=3, pady=2, sticky='WE')

#fldRowTxt = Tkinter.Entry(stepTwo)
#fldRowTxt.grid(row=6, columnspan=5, padx=5, pady=2, sticky='WE')


# -- Processando e salvando resultados --
stepThree = Tkinter.LabelFrame(form, text=" 3. Resultado das correcoes ")
stepThree.grid(row=5, columnspan=7, sticky='W', \
               padx=5, pady=5, ipadx=5, ipady=5)

inFileLb3 = Tkinter.Label(stepThree, text="Escolher diretorio de imagens:")
inFileLb3.grid(row=4, column=0, sticky='WE', padx=5, pady=2)

inFileTxt3 = Tkinter.Entry(stepThree)
inFileTxt3.grid(row=4, column=1, columnspan=7, sticky="WE", pady=3)

inFileBtn3 = Tkinter.Button(stepThree, text="Buscar")
inFileBtn3.grid(row=4, column=8, sticky='W', padx=5, pady=2)

'''
transChk = Tkinter.Checkbutton(stepThree, \
           text="Enable Transaction", onvalue=1, offvalue=0)
transChk.grid(row=6, sticky='W', padx=5, pady=2)

transRwLbl = Tkinter.Label(stepThree, \
             text=" => Specify number of rows per transaction:")
transRwLbl.grid(row=6, column=2, columnspan=2, \
                sticky='W', padx=5, pady=2)

transRwTxt = Tkinter.Entry(stepThree)
transRwTxt.grid(row=6, column=4, sticky='WE')
'''


# -- Help section --
helpLf = Tkinter.LabelFrame(form, text=" Ajuda ")
helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, \
            sticky='WE', \
             padx=5, pady=5, ipadx=5, ipady=5)
helpLbl = Tkinter.Label(helpLf, text="Este e o programa de correcao automatica de provas de multipla escolha. Para efetuar as correcoes, preencha os campos  ao lado. \n Passo 1. Definir sequencia de respostas corretas do gabarito ou informar imagem do gabarito correto preenchido \n Passo 2. Informar diretorio com imagens de respostas dos alunos. \n Passo 3. Escolher diretorio para salvar o resultado dos alunos")
helpLbl.grid(row=0)


form.mainloop()


# read all images from pi_cam folder and
# correct perspective and save in im_aligned folder
#
# orb for all files in folder

#pre-processing images


