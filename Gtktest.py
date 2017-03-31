# coding: utf-8

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import Pessoas

class MinhaJanela(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Gera Pessoas")
		self.set_border_width(6)
		self.p = Pessoas.Pessoa()

		self.listbox = Gtk.ListBox()
		self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        
		self.buttons()
		self.boxes()
		self.grid()
		self.add(self.grid1)


	def grid(self):
		self.grid1 = Gtk.Grid()
		self.grid1.add(self.box1)
		self.grid1.add(self.box2)
		self.grid1.attach(self.box1,1,0,2,1)
		self.grid1.attach_next_to(self.box1,self.box2,Gtk.PositionType.BOTTOM,2,1)


	def boxes(self):
		self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
		self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
		
        self.box2.pack_start(self.button2, True, True, 0)
		self.box1.pack_start(self.button1, True, True, 0)
		self.box1.pack_start(self.button2, True, True, 0)
		
		self.box2.pack_start(self.button_close, True, True, 0)

	def buttons(self):
		self.button1 = Gtk.Button(label="Clique Aqui")
		self.button1.connect("clicked", self.on_button1_click)
		
		self.button2 = Gtk.Button(label="Cria Pessoa!")
		self.button2.connect("clicked", self.gera_pessoa)
		
		self.button_close = Gtk.Button(label="Fechar")
		self.button_close.connect("clicked", Gtk.main_quit)

	def on_button1_click(self,widget):
		print "Isso funciona!"

	def gera_pessoa(self,widget):
		print "o"



win = MinhaJanela()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()