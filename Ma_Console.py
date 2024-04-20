modulname = 'Ma_Console'
_c_ = '(c) 2024, Matthias Mittelstein, Germany, 23816 Neversdorf, Hauptstraße 23'


import sys
import os
b2 = os.path.realpath(__file__).split("/")
b4 = "/".join(b2[0:-2]) 
b5 = "/".join(b2[0:-1])
# 'import' soll auch in dem Ordner suchen, in dem dises Programm gespeichet ist.
sys.path.insert(1,b5)
# 'import' soll auch in dem umfassenden Ordner suchen, wo es hoffentlich das
# Hilfspaket 'Ma_Util' gibt. Unabhänge davon, wie und von wo aus gestartet wurde.
sys.path.insert(1,b4)

from   Ma_Util.Ma_Plattform                         import Ma_Plattform

try:
	import console
except:
	pass

class Ma_Console():
	
	def __init__(self):
		self.plattform = Ma_Plattform()

		# if self.plattform.auf_iPhone_o_iPad():
		# 	import console
		# 	# Don't import into the namespace of a method.
		# 	# It does not help !
		
	def title1(self,aStr):
		if self.plattform.auf_iPhone_o_iPad():
			console.set_color(0.0,0.0,1.0) #blue
			console.set_font("Menlo-Regular", 18)
		l = len(aStr)
		print('\n',aStr,'\n','='*l,'\n',sep='')
		if self.plattform.auf_iPhone_o_iPad():
			console.set_font()  # back to 14
			console.set_color() # back to black
	
	def title2(self,aStr):
		if self.plattform.auf_iPhone_o_iPad():
			console.set_color(0.0,0.0,1.0) #blue
			console.set_font("Menlo-Regular", 16)
		l = len(aStr)
		print('\n',aStr,'\n','-'*l,sep='')
		if self.plattform.auf_iPhone_o_iPad():
			console.set_font()
			console.set_color()

	def print_red(self,aStr):
		if self.plattform.auf_iPhone_o_iPad():
			console.set_color(1.0,0.0,0.0) #red
			print(aStr)
			console.set_color()
		else:
			print('***')
			print('**** ',aStr)
			print('***')

#end class

if __name__ == '__main__':
	
	print(modulname)
	
	c = Ma_Console()
	c.title1('Überschrift')
	c.title2('Unterkapitel')
	print('normal')
	c.print_red('rot')
	print('normal')
