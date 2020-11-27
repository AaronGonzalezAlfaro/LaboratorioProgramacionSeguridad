import tkinter

ventana = tkinter.Tk()
ventana.geometry("300x200")

#Ingresar Palabra a Cifrar
etiqueta1 = tkinter.Label(ventana, text = "Mensaje a Cifrar")
etiqueta1.pack(fill = tkinter.X)

cajatexto1 = tkinter.Entry(ventana)
cajatexto1.pack()

#Clave a para crifrar la Palabra
etiqueta2 = tkinter.Label(ventana, text = "Clave (Palabra)")
etiqueta2.pack(fill = tkinter.X)

cajatexto2 = tkinter.Entry(ventana)
cajatexto2.pack()

#Etiqueta que muestra el resultado
resultado = tkinter.Label(ventana)
resultado.pack()

def Cifrar():
    mensaje = cajatexto1.get()
    clave = cajatexto2.get()
    mensaje = str(mensaje)
    espacios = 1
    while espacios > 0:
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in mensaje:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    translated = "Palabra Cifrada: " + translated
    resultado["text"] = translated


buton1 = tkinter.Button(ventana, text = "Cifrar", padx = 20, pady = 10, \
                        command = Cifrar, bg = "lavender")
buton1.pack(expand = True)

ventana.mainloop()
