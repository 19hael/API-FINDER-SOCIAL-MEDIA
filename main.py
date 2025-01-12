import requests
from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu

def buscar_numero(numero):
    api_key = "62a06875222c20f9d33d766d561af408"
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={numero}"
    response = requests.get(url).json()
    if response.get("valid"):
        return f"Número: {response['number']}\nPaís: {response['country_name']}\nLocalización: {response['location']}\nTipo: {response['line_type']}"
    return "Número inválido o no encontrado."

def buscar_email(email):
    api_key = "1d113cc02f93309c36084af3928c3bf93758b3cd"
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"
    response = requests.get(url).json()
    if "data" in response and response["data"]:
        return f"Email: {response['data']['email']}\nEstado: {response['data']['status']}"
    return "Email no válido o no encontrado."

def realizar_busqueda():
    entrada = entrada_texto.get()
    if opcion_seleccionada.get() == "Búsqueda de Número":
        resultado.set(buscar_numero(entrada))
    elif opcion_seleccionada.get() == "Búsqueda de Email":
        resultado.set(buscar_email(entrada))
    else:
        resultado.set("Funcionalidad de búsqueda de username no implementada.")

app = Tk()
app.title("HAEL LEGION")
app.geometry("500x400")
app.configure(bg="black")

titulo = Label(app, text="H A E L  L E G I O N", font=("Courier", 20), fg="white", bg="black")
titulo.pack(pady=20)

opcion_seleccionada = StringVar()
opcion_seleccionada.set("Búsqueda de Número")
opciones = ["Búsqueda de Número", "Búsqueda de Email", "Búsqueda de Username"]
menu_opciones = OptionMenu(app, opcion_seleccionada, *opciones)
menu_opciones.config(font=("Arial", 12), fg="white", bg="gray", width=20)
menu_opciones.pack(pady=10)

entrada_texto = StringVar()
entrada = Entry(app, textvariable=entrada_texto, font=("Arial", 14), width=30)
entrada.pack(pady=10)

boton_buscar = Button(app, text="Buscar", command=realizar_busqueda, font=("Arial", 14), bg="green", fg="white")
boton_buscar.pack(pady=10)

resultado = StringVar()
etiqueta_resultado = Label(app, textvariable=resultado, font=("Arial", 12), fg="white", bg="black", wraplength=450, justify="left")
etiqueta_resultado.pack(pady=20)

app.mainloop()