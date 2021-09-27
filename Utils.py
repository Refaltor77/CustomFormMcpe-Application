from tkinter import *
import json


def launchApplication():
    root = Tk()
    root.title('Modificateur de form MCPE')
    root.geometry("1080x720")
    root.minsize(1080, 720)
    root.config(background='#2ec57f')
    root.iconbitmap('img/icon.ico')
    frame = Frame(root, bg='#2ec57f')
    width = 300
    height = 300
    image = PhotoImage(file='img/icon.png').zoom(11).subsample(32)
    canvas = Canvas(frame, width=width, height=height, bg='#2ec57f', bd=0, highlightthickness=0)
    canvas.create_image(width / 2, height / 2, image=image)
    canvas.grid(row=0, column=0, sticky=W)
    frame2 = Frame(frame, bg='#2ec57f')
    title = Label(frame2, text="Entrez le chemin d'accées de votre pack.", font=("Helvetica", 20), bg='#2ec57f',
                  fg='white')
    title.pack()
    entry = Entry(frame2, font=("Helvetica", 20), bg='#2ec57f', fg='white')
    entry.pack(fill=X)
    button = Button(frame2, text="Commencez la création !", font=("Helvetica", 20), bg='#2ec57f', fg='white',
                    command=lambda: [launchFrameTwo(entry.get())])
    button.pack(fill=X)
    frame2.grid(row=0, column=1, sticky=W)
    frame.pack(expand=YES)
    root.mainloop()


def launchFrameTwo(path):
    root = Tk()
    root.title("path: " + path)
    root.geometry("1080x720")
    root.minsize(1080, 720)
    root.config(background='#2ec57f')
    root.iconbitmap('img/icon.ico')
    frame = Frame(root, bg='#2ec57f')

    title = Label(frame, text="Entrez la taille X", font=("Helvetica", 20), bg='#2ec57f', fg='white')
    title.pack(fill=X)
    entry = Entry(frame, font=("Helvetica", 20), bg='#2ec57f', fg='white')
    entry.pack(fill=X)

    title2 = Label(frame, text="Entrez la taille Z", font=("Helvetica", 20), bg='#2ec57f', fg='white')
    title2.pack(fill=X)
    entry2 = Entry(frame, font=("Helvetica", 20), bg='#2ec57f', fg='white')
    entry2.pack(fill=X)
    button = Button(frame, text="Envoyez !", font=("Helvetica", 20), bg='#2ec57f', fg='white',
                    command=lambda: [writeJson(entry.get(), entry2.get(), path)])
    button.pack(fill=X)

    frame.pack(expand=YES)
    root.mainloop()


def writeJson(x, z, path):
    file = open('json/server_form.json', 'r')
    content = file.read()
    file.close()
    array = json.loads(content)
    array['custom_form@common_dialogs.main_panel_no_buttons']['size'][0] = int(x)
    array['custom_form@common_dialogs.main_panel_no_buttons']['size'][1] = int(z)
    path = path.replace('\\', '/')
    file = open(path + '/ui/server_form.json', 'w')
    file.write(json.dumps(array, sort_keys=True, indent=4))
