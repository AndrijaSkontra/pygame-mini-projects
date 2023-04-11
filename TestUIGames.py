import customtkinter as ctk
from PIL import Image
from gamesStartTest import *

#find high score
maxy = 0
with open("highscores.txt", "r") as f:
    highScores = f.read()
listHS = highScores.split(" ")
for el in range(len(listHS) - 1):
    if int(listHS[el]) > maxy:
        maxy = int(listHS[el])

# ctk.set_appearance_mode("light")
ctk.set_default_color_theme("Assets/myColors.json")
app = ctk.CTk()
app.wm_title("B GAMES")
app.iconbitmap("Assets/joystickIco.ico")
#  app.overrideredirect(True) -> borderless, implement later, use app.kill()

window_width = 700
window_height = 550

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

app.geometry(f"{window_width}x{window_height}+"
             f"{center_x}+{center_y}")
app.resizable(False, False)

bgames_photo = ctk.CTkImage(light_image=Image.open("Assets/BgamesFINAL.png"),
                            dark_image=Image.open("Assets/BgamesFINAL.png"), size=(400, 400))
bgames = ctk.CTkLabel(app, image=bgames_photo, text="")
bgames.place(relx=0.5, rely=0.3, anchor='center')

myCopyright = ctk.CTkLabel(app, text="@shkoki", corner_radius=8,
                           fg_color="#999999", font=('Arial', 12, 'bold'),
                           )
myCopyright.place(relx=0.90, rely=0.93)

wizard = ctk.CTkButton(app, corner_radius=10, border_width=5,
                       border_color="lightblue", text="PLAY WIZARD",
                       font=("font", 20, "bold"), command=Wizard)
wizard.place(relx=0.5, rely=0.5, anchor="center")

cijevi = ctk.CTkButton(app, corner_radius=10, border_width=5,
                       border_color="lightblue", text="PLAY CIJEVI",
                       font=("font", 20, "bold"), command=Cijevi)
cijevi.place(relx=0.5, rely=0.6, anchor="center")

zombie = ctk.CTkButton(app, corner_radius=10, border_width=5,
                       border_color="lightblue", text="PLAY ZOMBIE",
                       font=("font", 20, "bold"), command=Zombie)
zombie.place(relx=0.5, rely=0.7, anchor="center")

hsLabel = ctk.CTkLabel(app, text=f"Wizard high score: {maxy}", corner_radius=10,
                           fg_color="#534789", font=('Arial', 14, 'bold'),
                           )
hsLabel.place(relx=0.7, rely=0.47)

app.mainloop()
