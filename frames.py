import customtkinter as ctk
from settings import *


class TypingFrame(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(master=parent)

        self.place(relx=0.5, rely=0.4, anchor="center", relwidth=0.8, relheight=0.7)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.time_label = ctk.CTkLabel(self, text='Waiting', font=R_FONT)
        self.time_label.grid(row=0, column=0, pady=6)
        self.text_box = ctk.CTkTextbox(self, font=T_FONT, width=W_WIDTH - W_W_PAD, height=W_HEIGHT - W_H_PAD)
        self.text_box.grid(row=1, column=0)
        self.words_counter = ctk.CTkLabel(self, text=f'Words: ---/{GOAL}', font=R_FONT)
        self.words_counter.grid(row=2, column=0, pady=6)

        self.word_goal = GOAL


    def count_words(self):

        self.words = len(self.text_box.get('1.0', 'end').strip().split())
        self.words_counter.configure(text=f'Words: {self.words}/{GOAL}')


    def clean_box(self):

        self.text_box.delete('1.0', 'end')


    def check_goal(self):

        if self.words == self.word_goal:
            return True
        else:
            return False


    def prepare_text(self):

        text_to_export = self.text_box.get('1.0', 'end').strip()
        return text_to_export


class Timer(ctk.CTkLabel):

    def __init__(self, parent):

        super().__init__(master=parent)
        self.seconds = SECONDS
        self.timer_running = False
        self.color_fading = FADING
        self.color = 0


    def start(self, time_over, time_label, text_box):

        if not self.timer_running:
            return

        if self.seconds < 10:
            seconds = f'0{self.seconds}'
        else:
            seconds = f'{str(self.seconds)}'

        time_label.configure(text=seconds)

        if self.seconds > 0:
            self.seconds -= 1
            text_box.configure(text_color=self.color_fading[self.color])
            self.color += 1
            self.after(1000, lambda: self.start(time_over, time_label, text_box))
        else:
            time_label.configure(text='Time Over! Your Text is Dead! ☠️', text_color='#F44336')
            time_over()


    def reset(self):

        self.seconds = SECONDS


class FileTypePanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(master=parent)
        self.configure(fg_color='transparent')
        self.place(relx=0.70, rely=0.85, anchor='center')

        self.name_string = ctk.StringVar()

        self.entry = ctk.CTkEntry(self, textvariable= self.name_string, placeholder_text='file name')
        self.entry.configure(state='disabled')
        self.entry.grid(row=0, column=0, columnspan=3, sticky='nsew', pady=5)

        self.txt_var = ctk.StringVar(value="")
        self.doc_var = ctk.StringVar(value="")
        self.pdf_var = ctk.StringVar(value="")

        self.txt_check = ctk.CTkCheckBox(
            self, text='txt',
            variable=self.txt_var, onvalue="txt", offvalue="",
            command=self.update_to_txt
        )
        self.txt_check.configure(state='disabled')
        self.txt_check.grid(row=1, column=0)

        self.doc_check = ctk.CTkCheckBox(
            self, text='doc',
            variable=self.doc_var, onvalue="doc", offvalue="",
            command=self.update_to_doc
        )
        self.doc_check.configure(state='disabled')
        self.doc_check.grid(row=1, column=1)

        self.pdf_check = ctk.CTkCheckBox(
            self, text='pdf',
            variable=self.pdf_var, onvalue="pdf", offvalue="",
            command=self.update_to_pdf
        )
        self.pdf_check.configure(state='disabled')
        self.pdf_check.grid(row=1, column=2)


    def update_to_txt(self):

        self.doc_var.set("")
        self.pdf_var.set("")


    def update_to_doc(self):

        self.txt_var.set("")
        self.pdf_var.set("")


    def update_to_pdf(self):

        self.txt_var.set("")
        self.doc_var.set("")


    def enable_frame(self):

        self.entry.configure(state='normal')
        self.txt_check.configure(state='normal')
        self.doc_check.configure(state='normal')
        self.pdf_check.configure(state='normal')


    def disable_frame(self):

        self.entry.configure(state='disabled')
        self.txt_check.configure(state='disabled')
        self.doc_check.configure(state='disabled')
        self.pdf_check.configure(state='disabled')