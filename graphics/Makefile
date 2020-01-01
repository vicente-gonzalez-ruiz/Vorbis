window.dat:	window.py
		./window.py

spectrum.dat:

TMPs += spectrum_window.dat
spectrum_window.dat:	window.dat
			./spectrum.py window

default:	window.dat spectrum_window.dat

include $(HOME)/Makefile_templates/Makefile
