import os, sys, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 3
__filename__ = "ImageRenaming"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:urllib.request.urlretrieve("https://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
        except:pass

if connection == True:
    try:script_version = int(urllib.request.urlopen("https://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("https://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("https://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

from datetime import datetime
from tkinter.filedialog import *
from tkinter import *

def start_rename():
    directory = askdirectory()
    if directory:
        if askyesno(__filename__, "Êtes-vous sûr de renommer toutes les images dans ce dossier ? Cette action ne peux pas être annulée !"):
            files1 = [f for f in os.listdir(directory) if f[-4:].lower() in (".jpg",".JPG",".png",".PNG",".jpeg",".JPEG",".bmp",".gif")]
            for (index, filename) in enumerate(files1):
                file = directory + "/" + filename
                extension = os.path.splitext(filename)[1]
                if check_var.get() == 0:
                    time1 = os.path.getctime(file)
                elif check_var.get() == 1:
                    time1 = os.path.getmtime(file)
                time2 = datetime.fromtimestamp(time1)
                time = time2.strftime("%Y%m%d%H%M%S%f")
                newname = time + "_" + str(os.path.getsize(file)) + extension
                os.rename(file, directory + "/" + newname)

            files2 = [f for f in os.listdir(directory) if f[-4:].lower() in (".jpg",".JPG",".png",".PNG",".jpeg",".JPEG",".bmp",".gif")]
            for (index, filename) in enumerate(files2):
                file = directory + "/" + filename
                extension = os.path.splitext(filename)[1]
                newname = "Image-%05d%s" % (index + 1, extension)
                if os.path.exists(newname):
                    continue
                if True:
                    os.rename(file, directory + "/" + newname)
            imagerenaming.destroy()
        os._exit(0)
    else:
        showwarning(__filename__, "Erreur : Aucun dossier n'a été sélectionné !")

imagerenaming = Tk()
width = 800
height = 500
imagerenaming.update_idletasks()
x = (imagerenaming.winfo_screenwidth() - width) // 2
y = (imagerenaming.winfo_screenheight() - height) // 2
imagerenaming.geometry("{}x{}+{}+{}".format(width , height, int(x), int(y)))
imagerenaming.resizable(width=False, height=False)
imagerenaming.configure(bg = "lightgray")
if os.path.exists(__iconpath__):
    imagerenaming.iconbitmap(__iconpath__)
imagerenaming.title(__filename__)
Label(imagerenaming, text="Bienvenue dans le programme de renommage !", font="impact 30", fg="red", bg="lightgray").pack(pady=60)
check_var = IntVar()
check_var.set(0)
Radiobutton(imagerenaming, text="Date de création", variable=check_var, value=0, font="impact 20", bg="lightgray").pack(pady=10)
Radiobutton(imagerenaming, text="Date de modification", variable=check_var, value=1, font="impact 20", bg="lightgray").pack()
Button(imagerenaming, text="Renommer des images", command=start_rename, relief=GROOVE, width=25, font="impact 20", fg="black").pack(pady=50)
imagerenaming.mainloop()
