import customtkinter as ctk
from settings import *


class ExportButton(ctk.CTkButton):

    def __init__(self, parent, export):

        super().__init__(master=parent,
                         text = 'Export',
                         font = R_FONT,
                         command = export,
                         width = 70,
                         height = 40,
                         text_color = "white",
                         corner_radius = 10
                         )
        self.disable()
        self.place(relx=0.87, rely=0.84, anchor='center')


    def disable(self):
        self.configure(state='disabled', fg_color='#CCCCCC', text_color='#888888', hover_color='#CCCCCC')


    def enable(self):
        self.configure(state='normal', fg_color=EXPORT_B_FG, text_color='white', hover_color=EXPORT_B_HV)



class InstructionsButton(ctk.CTkButton):

    def __init__(self, parent, instructions):

        super().__init__(master=parent,
                         text = 'Instructions',
                         font = R_FONT,
                         command = instructions,
                         width = 60,
                         height = 40,
                         fg_color = INSTRO_B_FG,
                         hover_color = INSTRO_B_HV,
                         text_color = "white",
                         corner_radius = 10
                         )
        self.place(relx=0.15, rely=0.85, anchor='center')


class BrowseButton(ctk.CTkButton):

    def __init__(self, parent, path):

        super().__init__(master=parent,
                         text = 'Browse',
                         font = B_FONT,
                         command = path,
                         width = 60,
                         height = 40,
                         text_color = "white",
                         corner_radius = 10
                         )
        self.place(relx=0.87, rely=0.91, anchor='center')
        self.disable()

    def disable(self):
        self.configure(state='disabled', fg_color='#CCCCCC', text_color='#888888', hover_color='#CCCCCC')

    def enable(self):
        self.configure(state='normal', fg_color=BROWSE_FG, text_color='white', hover_color=BROWSE_HV)


class ResetButton(ctk.CTkButton):

    def __init__(self, parent, reset):

        super().__init__(master=parent,
                         text='Reset',
                         font=B_FONT,
                         command=reset,
                         width=60,
                         height=40,
                         text_color="white",
                         corner_radius=10
                         )
        self.place(relx=0.50, rely=0.80, anchor='center')
        self.enable()

    def disable(self):
        self.configure(state='disabled', fg_color='#CCCCCC', text_color='#888888', hover_color='#CCCCCC')

    def enable(self):
        self.configure(state='normal', fg_color=RESET_FG, text_color='white', hover_color=RESET_HV)
