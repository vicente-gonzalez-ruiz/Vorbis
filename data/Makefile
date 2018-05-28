include $(HOME)/Makefile_templates/Makefile

window.dat:	window.py
		./window.py

spectrum_window.dat:	window.dat
			./spectrum.py window

default:	window.dat spectrum_window.dat
