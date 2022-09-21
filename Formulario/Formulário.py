from tkinter import *
cor1 = 'white'
janela = Tk()
janela.title('Formulário Principal')
janela.geometry('600x500')
cor = '#fddc5e'
janela.title('Formulário de Cadastro de Cliente')
janela.config(bg=cor)


codigo = Label(janela, width=20,height=2, text='Código:',font='Arial 12', relief='solid', fg='black', bg='#fcd231')
codigo.place(x=1, y=80)

nome = Label(janela, width=20,height=2, text='Nome:',font='Arial 12', relief='solid', fg='black', bg='#fcd231')
nome.place(x=1, y=120)

estado = Label(janela, width=20,height=2, text='Estado:',font='Arial 12', relief='solid', fg='black', bg='#fcd231')
estado.place(x=1, y=160)

cidade = Label(janela, width=20,height=2, text='Cidade:',font='Arial 12', relief='solid', fg='black', bg='#fcd231')
cidade.place(x=1, y=200)

bairro = Label(janela, width=20,height=2, text='Bairro:',font='Arial 12', relief='solid', fg='black', bg='#fcd231')
bairro.place(x=1, y=240)

logradouro = Label(janela, width=20,height=2, text='Logradouro:',font='Arial 12', relief='solid', fg='black', bg='#fcd231')
logradouro.place(x=1, y=280)

complemento = Label(janela, width=20,height=2, text='Complemento:',font='Arial 12', relief='solid', fg='black', bg='#fcd231')
complemento.place(x=1, y=320)


cadastro = Label(janela, width=20,height=2, text='Cadastro de Cliente', font= 'Arial 15', relief='flat', bg='#fddc5e')
cadastro.place(x=200, y=0)

#estilos botao - groove-solid-flat-sunken-ridge
consultar = Button(janela, width=10, text="Consultar", relief='solid', fg='black', bg='#fcd231')
consultar.place(x=496, y=65)

novo = Button(janela, width=10, text="Novo", relief='solid', fg='black', bg='#fcd231')
novo.place(x=300, y=450)

salvar = Button(janela, width=10, text="Salvar", relief='solid', fg='black', bg='#fcd231')
salvar.place(x=496, y=450)

apagar = Button(janela, width=10, text="Apagar", relief='solid', fg='black', bg='#fcd231')
apagar.place(x=400, y=450)


codigo = Entry(janela, width=20,  font = "arial 15", relief='solid')
codigo.place(x=200, y=87)

nome = Entry(janela, width=34,  font = "arial 15", relief='solid')
nome.place(x=200, y=128)

estado = Entry(janela, width=23,  font = "arial 15", relief='solid')
estado.place(x=200, y=170)

cidade = Entry(janela, width=34,  font = "arial 15", relief='solid')
cidade.place(x=200, y=205)

bairro = Entry(janela, width=34,  font = "arial 15", relief='solid')
bairro.place(x=200, y=247)

logradouro = Entry(janela, width=34,  font = "arial 15", relief='solid')
logradouro.place(x=200, y=285)

complemento = Entry(janela, width=23,  font = "arial 15", relief='solid')
complemento.place(x=200, y=327)






janela.mainloop()