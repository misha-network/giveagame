from tkinter import *
from tkinter import messagebox
import webbrowser

class GUI:
	def __init__(self, root, game):
		self.tk = root
		self.mainMenu = Menu(self.tk)
		self.index = 0
		self.game = game
		self.tk.config(menu=self.mainMenu)
		self.settingsMenu = Menu(self.mainMenu, tearoff=0)
		self.settingsMenu.add_command(label="Пауза.", command=self.com_PauseGame, accelerator="Ctrl+P")
		self.settingsMenu.add_separator()
		self.settingsMenu.add_command(label="Выход.", command=self.com_Exit, accelerator="Ctrl+Q")
		self.helpMenu = Menu(self.mainMenu, tearoff=0)
		self.helpMenu.add_command(label="README файл.", command=self.com_OpenReadmeFile, accelerator="Ctrl+H")
		self.helpMenu.add_separator()
		self.helpMenu.add_command(label="О программе.", command=self.com_OpenAboutProgram)
		self.mainMenu.add_cascade(label="Настройки", menu=self.settingsMenu)
		self.mainMenu.add_cascade(label="Справка", menu=self.helpMenu)

		self.tk.bind_all("<Control-q>", self.com_Exit)
		self.tk.bind_all("<Control-p>", self.com_PauseGame)
		self.tk.bind_all("<Control-h>", self.com_OpenReadmeFile)

	def com_Exit(self):
		self.tk.destroy()
		quit()

	def com_OpenReadmeFile(self):
		webbrowser.open_new_tab('README.html')

	def com_OpenAboutProgram(self):
		messagebox.showinfo(title="О программе.", message="Мистер Рука-Палка бежит до выхода! Версия: 0.4bf.")

	def com_PauseGame(self):
		self.index = not self.index

		if self.index:
			self.game.running = False
		else:
			self.game.running = True