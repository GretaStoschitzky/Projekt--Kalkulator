from tkinter import *
import sympy


okno = Tk()
okno.title("Kalkulator")




class Kalkulator(Frame):
    def __init__(self, okno):
        self.pripravi_graficni_vmesnik()


    def pripravi_graficni_vmesnik(self):
        self.prikaz = Entry(okno, font=('arial', 16, 'bold'),bg= 'purple',bd = 3, justify=RIGHT, relief = RAISED)
        self.prikaz.insert(0, '0')
        self.prikaz.grid(row=0, column=0, columnspan=4)





        self.gumb0 = Button(okno,padx=10,bd=7, fg='black', font=('arial',16,'bold'),text='0', command= lambda: self.gumb_s_stevilko('0'))
        self.gumb1 = Button(okno,padx=10,bd=7, fg='black', font=('arial',16,'bold'),text='1', command= lambda:self.gumb_s_stevilko('1'))
        self.gumb2 = Button(okno,padx=10,bd=7, fg='black', font=('arial',16,'bold'),text='2', command=lambda: self.gumb_s_stevilko('2'))
        self.gumb3 = Button(okno,padx=10,bd=7, fg='black', font=('arial',16,'bold'),text='3', command= lambda: self.gumb_s_stevilko('3'))
        self.gumb4 = Button(okno,padx=10,bd=7, fg='black', font=('arial',16,'bold'),text='4', command=lambda: self.gumb_s_stevilko('4'))
        self.gumb5 = Button(okno,padx=10,bd=7, fg='black', font=('arial',16,'bold'),text='5', command= lambda:self.gumb_s_stevilko('5'))
        self.gumb6 = Button(okno,padx=10,bd=7, fg='black', font=('arial',16,'bold'),text='6', command=lambda: self.gumb_s_stevilko('6'))
        self.gumb7 = Button(okno,padx=10,bd=7, fg='black', font=('arial',16,'bold'),text='7', command= lambda: self.gumb_s_stevilko('7'))
        self.gumb8 = Button(okno,padx=10,bd=7, fg='black', font=('arial',16,'bold'),text='8', command=lambda: self.gumb_s_stevilko('8'))
        self.gumb9 = Button(okno,padx=10, bd=7, fg='black', font=('arial',16,'bold'),text='9', command=lambda: self.gumb_s_stevilko('9'))
        self.gumb_pika = Button(okno,padx=10,bd=7, fg='black', font=('arial',16,'bold'),text='.', command= lambda: self.gumb_s_stevilko('.'))

        self.plus = Button(okno, padx = 10, bd=7, fg='purple', font=('arial',16,'bold'), text="+",command= lambda: self.gumb_s_stevilko('+'))
        self.minus = Button(okno,padx=10,bd=7, fg='purple', font=('arial',16,'bold'), text="-", command= lambda: self.gumb_s_stevilko('-'))
        self.deljeno = Button(okno,padx=10,bd=7, fg='purple', font=('arial',16,'bold'), text=":",command=lambda: self.gumb_s_stevilko('/'))
        self.krat = Button(okno,padx=10,bd=7, fg='purple', font=('arial',16,'bold'), text="x", command= lambda: self.gumb_s_stevilko('*'))

        self.kvadrat = Button(okno,padx=8,bd=8, fg='purple', font=('arial',10,'bold'), text="x^2", command= lambda: self.gumb_s_stevilko('**2'))
        self.kub = Button(okno,padx=8,bd=7, fg='purple', font=('arial',12,'bold'), text="x^3", command= lambda: self.gumb_s_stevilko('**3'))


        self.enako = Button(okno,padx=100,bd=7, fg='purple', font=('arial',16,'bold'), text="=", command= self.enacba)
        self.izbrisi = Button(okno,padx=100,bd=7, fg='purple', font=('arial',16,'bold'), text="C", command= self.zbrisi)

        self.kvadrat.grid(row=5, column=2)
        #self.kub.grid(row=1, column=1)
        self.enako.grid(row=6, columnspan = 4)
        self.izbrisi.grid(row=1, columnspan =4)
        self.gumb7.grid(row=2, column=0)
        self.gumb8.grid(row=2, column=1)
        self.gumb9.grid(row=2, column=2)
        self.plus.grid(row=2, column=3)
        self.gumb4.grid(row=3, column=0)
        self.gumb5.grid(row=3, column=1)

        self.gumb6.grid(row=3, column=2)
        self.minus.grid(row=3, column=3)

        self.gumb1.grid(row=4, column=0)
        self.gumb2.grid(row=4, column=1)
        self.gumb3.grid(row=4, column=2)
        self.krat.grid(row=4, column=3)
        self.gumb0.grid(row=5, column=0)
        self.gumb_pika.grid(row=5, column=1)
        self.deljeno.grid(row=5, column=3)




    def gumb_s_stevilko(self, stevilka):
        self.stevila = self.prikaz.get()
        self.dolzina = len(self.stevila)

        if self.stevila == '0':
            self.prikaz.delete(0, END)
            self.prikaz.insert(0, stevilka)
        else:
            self.prikaz.insert(self.dolzina, stevilka)



    def enacba(self):
        self.izraz = self.prikaz.get()
        self.rezultat = round(sympy.sympify(self.izraz), 3)
        self.prikaz.delete(0, END)
        self.prikaz.insert(0, self.rezultat)


    def zbrisi(self):
        self.prikaz.delete(0, END)
        self.prikaz.insert(0, '0')


kalkulator1 = Kalkulator(okno)

okno.mainloop()