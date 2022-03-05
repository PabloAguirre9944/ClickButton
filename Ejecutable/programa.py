import tkinter

#Configuracion de la pagina
window=tkinter.Tk()
window.title('Pagina')
window.geometry("300x200+10+10")

#Varibales
texto="Aquí hay un boton"

#Eventos
def botonPulsado():
    texto="Hijole si se pudo"
    global label
    label["text"]=texto

#Codigo



#Configuracion conponentes
btn=tkinter.Button(window, text="This is Button widget", fg='blue',command = lambda: botonPulsado())
btn.pack()
label=tkinter.Label(window,text=texto, fg='red', font=("Helvetica", 16))
label.pack()

#Posiciones
label.place(x=55, y=60)
btn.place(x=80, y=100)


#Loop
window.mainloop()