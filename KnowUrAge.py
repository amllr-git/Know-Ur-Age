from tkinter import*
import datetime as dt
today = dt.date.today()

root = Tk()
root.title("HITUNG UMUR")
# p x l
root.geometry('210x210')

#label
lbl = Label(root, text = "Tanggal lahir ")
lbl.grid(column=0,row=0)
lb2 = Label(root, text = "Bulan lahir ")
lb2.grid(column=0,row=1)
lb3 = Label(root, text = "Tahun lahir ")
lb3.grid(column=0,row=2)
lb4 = Label(root, text = "Umur Anda ")
lb4.grid(column=0,row=4)


#hasil
hasil = Label(root, text="")
hasil.grid(column=1,row=4)

#input text
tglInp = Entry(root, width=20)
tglInp.grid(column=1, row=0)
blnInp = Entry(root, width=20)
blnInp.grid(column=1, row=1)
thnInp = Entry(root, width=20)
thnInp.grid(column=1, row=2)

#button is clicked
def clicked():
    #hitung umur
    hari = int(tglInp.get())
    bulan = int(blnInp.get())
    tahun = int(thnInp.get())

    tanggal_lahir = dt.date(tahun,bulan,hari)
    umur_hari = today - tanggal_lahir 
    umur = umur_hari.days // 365
    umur_sisaBulan = (umur_hari.days % 365) // 30


    res = f"{umur} tahun, {umur_sisaBulan} bulan"
    hasil.configure(text=res)

#hitung button
btn1 = Button(root, text="Hitung",
              fg = "green", command=clicked)
btn1.grid(column=1,row=3)
#execute
root.mainloop()