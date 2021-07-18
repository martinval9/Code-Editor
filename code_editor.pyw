from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from colorama import init,Fore,Back
from io import open
import os

#---BACKEND---
#---FUNCIONES PARA INTERACTUAR CON LOS ARCHIVOS---

ruta = ""

def nuevo():
    global ruta

    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0 , "end")
    root.title("Mi editor")

def abrir():
	try:
	    global ruta

	    mensaje.set("Abrir fichero")
	    ruta = FileDialog.askopenfilename(
	        initialdir='.', 
	        filetypes=(("Ficheros de texto" , "*"),),
	        title="Abrir un fichero de texto")

	    if ruta != "":
	        fichero = open(ruta , 'r')
	        contenido = fichero.read()
	        texto.delete(1.0 , 'end')
	        texto.insert('insert', contenido)
	        fichero.close()
	        mensaje.set(ruta + " - Mi editor")

	except UnicodeDecodeError:
		MessageBox.showerror("Error de decodificado" , "Error:\nFormato de archivo no compatible")

def guardar():
    mensaje.set("Guardar fichero")

    if ruta != "":
        contenido = texto.get(1.0 , 'end-1c')
        fichero = open(ruta , 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")

    else:
        guardar_como()

def guardar_como():
    global ruta
    
    mensaje.set("Guardar fichero como")
    fichero = FileDialog.asksaveasfile(
    	title = "Guardar fichero",
    	mode = "w",
    	defaultextension = "*")

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0 , 'end-1c')
        fichero = open(ruta , 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")

    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

#---FUNCIONES DE LA BARRA SUPERIOR---

def terminal():
	os.system("kitty")

def fzf():
	fzf = os.system("kitty fzf")

def gplv2():
	MessageBox.showinfo("GNU GENERAL PUBLIC LICENSE Version 2" , "GNU GENERAL PUBLIC LICENSE\nVersion 2, June 1991\n\nCopyright (C) 1989, 1991 Free Software Foundation, Inc.,\n51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA\nEveryone is permitted to copy and distribute verbatim copies\nof this license document, but changing it is not allowed.\nPreamble\n\n\nThe licenses for most software are designed to take away your\nfreedom to share and change it.  By contrast, the GNU General Public\nLicense is intended to guarantee your freedom to share and change free\nsoftware--to make sure the software is free for all its users.  This\nGeneral Public License applies to most of the Free Software\nFoundation's software and to any other program whose authors commit to\nusing it.  (Some other Free Software Foundation software is covered by\nthe GNU Lesser General Public License instead.)  You can apply it to\nyour programs, too.")

def lgplv2():
	MessageBox.showinfo("GNU LESSER GENERAL PUBLIC LICENSE Version 2.1" , "GNU LESSER GENERAL PUBLIC LICENSE\nVersion 2.1, February 1999\nCopyright (C) 1991, 1999 Free Software Foundation, Inc.\n51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA\nEveryone is permitted to copy and distribute verbatim copies\nof this license document, but changing it is not allowed.\n[This is the first released version of the Lesser GPL.  It also counts\nas the successor of the GNU Library Public License, version 2, hence\nthe version number 2.1].")

def pagina_web():
	#os.system("firefox Pagina_Web/index.html")
	#os.system("firefox-developer-edition index.html") Si tienes el navegador firefox-developer-edition quitale el comentario (#)
	#os.system("chrome index.html") Si tienes el navegador chrome quitale el comentario (#)
	os.system("kitty brave-beta file:///home/martin/code_editor/Pagina_Web/index.html") #Si tienes el navegador brave quitale el comentario (#)

#---FUNCIONES DEL SUBMENU DE EJECUCION---


def ejecutar_en_python():
	os.system("kitty python3 " + ruta + "&& sleep 5")

def ejecutar_en_cpp():
	os.system("kitty g++ " + ruta + " -o test")
	os.system("kitty ./test" + " && sleep 5")

def ejecutar_en_c():
	os.system("kitty gcc " + ruta + " -o test_c")
	os.system("kitty ./test_c" + " && sleep 5")

def ejecutar_en_node():
	os.system("kitty node " + ruta + " && sleep 5")

def ejecutar_en_ruby():
	os.system("kitty ruby " + ruta + " && sleep 5")

def ejecutar_en_java():
	os.system("kitty javac " + ruta + " && java test_java" + " && sleep 5")

def ejecutar_en_go():
	os.system("kitty go run " + ruta + " && sleep 5")

#---RANDOM---

def salir():
	resultado = MessageBox.askquestion("Salir","¿Está seguro que desea salir?")

	if resultado == "yes":
		root.destroy()

#---FUNCIONES DEL SUBMENU DE ABRIR EN EL NAVEGADOR---

def abrir_en_firefox():
	os.system("firefox " + ruta)

def abrir_en_chromium():
	os.system("chromium " + ruta)

def abrir_en_chrome():
	os.system("chrome " + ruta)

def abrir_en_brave():
	os.system("brave-beta " + ruta)

root = Tk()
root.title("Programming Editor")

#---Menú superior---

menubar = Menu(
	root, 
	bg = "#090909",
	fg = "#FFFFFF",
	activebackground = "#1E1E1E",
	activeforeground = "#FF0000",
	border = 0,
	font = "JetBrainsMonoMedium 9")

filemenu = Menu(
	menubar,
	tearoff=0,
	bg = "#090909",
	fg = "#FFFFFF",
	activebackground = "#1E1E1E",
	activeforeground = "#FF0000",
	border = 0,
	font = "JetBrainsMonoMedium 9")

abrir_en = Menu(
	menubar,
	tearoff = 0,
	bg = "#090909",
	fg = "#FFFFFF",
	activebackground = "#1E1E1E",
	activeforeground = "#FF0000",
	border = 0,
	font = "JetBrainsMonoMedium 9")

ejecutar_en = Menu(
	menubar,
	tearoff = 0,
	bg = "#090909",
	fg = "#FFFFFF",
	activebackground = "#1E1E1E",
	activeforeground = "#FF0000",
	border = 0,
	font = "JetBrainsMonoMedium 9")

ayuda = Menu(
	menubar,
	tearoff = 0,
	bg = "#090909",
	fg = "#FFFFFF",
	activebackground = "#1E1E1E",
	activeforeground = "#FF0000",
	border = 0,
	font = "JetBrainsMonoMedium 9")

filemenu.add_command(label = "Nuevo" , command = nuevo)
filemenu.add_command(label = "Abrir" , command = abrir)
filemenu.add_command(label = "Guardar" , command = guardar)
filemenu.add_command(label = "Guardar como" , command = guardar_como)
filemenu.add_separator()
filemenu.add_command(label = "Salir" , command = salir)
menubar.add_cascade(menu = filemenu , label = "Archivo")

menubar.add_command(label="Terminal" , command = terminal)
menubar.add_command(label="FZF" , command = fzf)

menubar.add_cascade(menu = ejecutar_en , label="Ejecutar en")
ejecutar_en.add_command(label = "Python" , command = ejecutar_en_python)
ejecutar_en.add_command(label = "C++" , command = ejecutar_en_cpp)
ejecutar_en.add_command(label = "C" , command = ejecutar_en_c)
ejecutar_en.add_command(label = "Node (console)" , command = ejecutar_en_node)
ejecutar_en.add_command(label = "Ruby" , command = ejecutar_en_ruby)
ejecutar_en.add_command(label = "Java" , command = ejecutar_en_java)
ejecutar_en.add_command(label = "Go" , command = ejecutar_en_go)

menubar.add_cascade(menu = abrir_en , label = "Abrir en el Navegador")
abrir_en.add_command(label = "Firefox" , command = abrir_en_firefox)
abrir_en.add_command(label = "Chrome" , command = abrir_en_chrome)
abrir_en.add_command(label = "Chromium" , command = abrir_en_chromium)
abrir_en.add_command(label = "Brave" , command = abrir_en_brave)

menubar.add_cascade(menu = ayuda , label = "Ayuda")
ayuda.add_command(label = "Pagina Web" , command = pagina_web)
ayuda.add_command(label = "Licencia GPLv2" , command = gplv2)
ayuda.add_command(label = "Licencia LGPLv2.1" , command = lgplv2)

Scrollbar(root=None)
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

texto = Text(root , yscrollcommand=scrollbar.set)

texto.config(bg = "#030303",
	fg = "#00FF4A",
	bd=0, padx=6,
	pady=4,
	font="JetBrainsMonoMedium 11",
	insertbackground="#FF0000")

texto.pack(fill = "both" , expand = 1)

scrollbar.config(command=texto.yview , bg = "#444444" , border = 0 , activebackground = "#00ff4a")

# Monitor inferior
mensaje = StringVar()

mensaje.set("Sientate,escribe algo de codigo y demuestra lo mejor que sabes hacer :) | Version 3.2")
monitor = Label(root, textvar = mensaje, justify = 'left')
monitor.pack(side = "left")

monitor.config(
	bg = "#00171B",
	fg = "#fff",
	font = "JetBrainsMonoMedium 9")

root.config(menu = menubar , bg = "#00171B")

root.update()
root.mainloop()
