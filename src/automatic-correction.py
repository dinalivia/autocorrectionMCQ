#!/usr/local/bin/python
# coding: latin-1
import os, sys

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

from tkFileDialog   import askopenfilename, askdirectory

gab_img = ''
ans_dir = ''
res_dir = ''

def open_gab():
    gab_img = askopenfilename()
    inFileTxt.insert(INSERT,gab_img)


def open_dir1():
    ans_dir = askdirectory()
    inFileTxt2.insert(INSERT,ans_dir)

def open_dir2():
    res_dir = askdirectory()
    inFileTxt3.insert(INSERT,res_dir)

def Autocorrect():
    os.system("./test.sh")
    
form = Tkinter.Tk()
getFld = Tkinter.IntVar()

form.wm_title('Correção Automática de provas múltipla escolha')

# ----- Gabarito -----

# Titulo
stepOne = Tkinter.LabelFrame(form, text=" 1. Informe o gabarito da prova: ")
stepOne.grid(row=0, columnspan=7, sticky='W', \
             padx=5, pady=5, ipadx=5, ipady=5)

#checkbox
transChk = Tkinter.Checkbutton(stepOne, \
           text="Escrever sequência", onvalue=1, offvalue=0)
transChk.grid(row=0, column=0, sticky='WE', padx=3, pady=2)
transRwLbl = Tkinter.Label(stepOne, \
                           text=" => Ex. a,b,c,d,e,a,b,c, ...")
transRwLbl.grid(row=0, column=1, columnspan=2, \
                sticky='W', padx=5, pady=2)

# Entrada gabarito
transRwTxt = Tkinter.Entry(stepOne)
transRwTxt.grid(row=1, columnspan=5, sticky='WE', padx=5, pady=2)


# Buscar gabarito
inFileLbl = Tkinter.Label(stepOne, text="Escolher imagem do gabarito:")
inFileLbl.grid(row=2, column=0, sticky='W ', padx=5, pady=2)

inFileTxt = Tkinter.Text(stepOne,width = 10, height=1)
inFileTxt.grid(row=2, column=1, columnspan=7, sticky="WE",pady=3)

inFileBtn = Tkinter.Button(stepOne, text="Buscar", command = open_gab)
inFileBtn.grid(row=2, column=8, sticky='WE', padx=5, pady=2)


#inFileTxt.insert(INSERT, )


# ------- Respostas dos discentes -------

stepTwo = Tkinter.LabelFrame(form, text=" 2. Informe as respostas dos discentes: ")
stepTwo.grid(row=3, columnspan=7, sticky='W', \
             padx=5, pady=5, ipadx=5, ipady=5)

inFileLb2 = Tkinter.Label(stepTwo, text="Escolher diretório de imagens:")
inFileLb2.grid(row=4, column=0, sticky='WE', padx=5, pady=2)

inFileTxt2 = Tkinter.Text(stepTwo,width = 23, height=1)
inFileTxt2.grid(row=4, column=1, columnspan=7, sticky="WE",pady=3)

inFileBtn2 = Tkinter.Button(stepTwo, text="Buscar", command = open_dir1)
inFileBtn2.grid(row=4, column=8, sticky='W', padx=5, pady=2)


# ------- Processando e salvando resultados -------

stepThree = Tkinter.LabelFrame(form, text=" 3. Resultado das correções ")
stepThree.grid(row=5, columnspan=7, sticky='W', \
               padx=5, pady=5, ipadx=5, ipady=5)

inFileLb3 = Tkinter.Label(stepThree, text="Escolher diretório de imagens:")
inFileLb3.grid(row=4, column=0, sticky='WE', padx=5, pady=2)

inFileTxt3 = Tkinter.Text(stepThree,width = 23, height=1)
inFileTxt3.grid(row=4, column=1, columnspan=7, sticky="WE",pady=3)

inFileBtn3 = Tkinter.Button(stepThree, text="Buscar", command = open_dir2)
inFileBtn3.grid(row=4, column=8, sticky='W', padx=5, pady=2)

# ------- Help section -------

helpLf = Tkinter.LabelFrame(form, text=" Ajuda ")
helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, \
            sticky='NWE', \
             padx=5, pady=5, ipadx=5, ipady=5)

helpText = Tkinter.Text(helpLf,width = 30, height=10)

scrollbar = Scrollbar(helpLf, command=helpText.yview, orient=VERTICAL)
scrollbar.grid(row=0, column=9, columnspan=2, rowspan=8, \
            sticky='NSWE', \
             padx=5, pady=5, ipadx=5, ipady=5)

scrollbar.config(command=helpText.yview)

helpText.insert(INSERT, "\nEste e o programa de correção automatica de provas de múltipla escolha. Para efetuar as correções, preencha os campos  ao lado. \n\n -> Passo 1. \nDefinir sequência de respostas corretas do gabarito ou informar imagem do gabarito correto preenchido \n\n -> Passo 2. \nInformar diretório com imagens de respostas dos alunos. \n\n -> Passo 3. \nEscolher diretorio para salvar o resultado dos alunos\n")

helpText.configure(yscrollcommand=scrollbar.set, state='disable')

helpText.grid(row=0, column=0, columnspan=2, rowspan=8, \
            sticky='W', \
             padx=5, pady=5, ipadx=5, ipady=5)


# ------- Iniciar correcao -------

stepFour = Tkinter.LabelFrame(form, text=" 4. Realizar correção ")
stepFour.grid(row=1, column=9, columnspan=2, rowspan=8, \
            sticky='SWE', \
             padx=5, pady=5, ipadx=5, ipady=5)

inFileBtn3 = Tkinter.Button(stepFour, text="Iniciar correção", width=25, command= Autocorrect)
inFileBtn3.grid(row=1, column=9, \
            sticky='WE', \
             padx=5, pady=5, ipadx=5, ipady=5)


form.mainloop()



