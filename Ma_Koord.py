modulname = 'Ma_Koord'
'''

In 'scene' and related packages the coordinates are integers counting pixels.
'x'-values have their zero at the left edge and is growing to the right.
'y'-values have their zero at the bottom edge and is growing upwards.

In 'Image', 'ImageDraw' and related packages the coordinates are also integers
and are also counting pixels.
'x'-values have their zero at the left edge and is growing to the right.
'y'-values have their zero at the top edge and is growing downwards.

Because of that you need to know the frame of a picture in order to convert
coordinates from one realm to the other.
'''

class KoordinatenKonverter():
	def __init__(self,breite,hoehe):
		self.breite = breite
		self.hoehe  = hoehe
	
	def sceneX_aus_Image(self,x):
		return x
	
	def ImageX_aus_scene(self,x):
		return x
	
	def sceneY_aus_Image(self,y):
		return self.hoehe - y
	
	def ImageY_aus_scene(self,y):
		return self.hoehe - y
	
	def sceneXY_aus_Image(self,x,y):
		return self.sceneX_aus_Image(x) , self.sceneY_aus_Image(y)
	
	def ImageXY_aus_scene(self,x,y):
		return self.ImageX_aus_scene(x) , self.ImageY_aus_scene(y)
	
	def sceneXYPaare_aus_Image(self,paare):
		'''Listen'''
		erg = []
		for paar in paare:
			erg.append( self.sceneXY_aus_Image(paar[0],paar[1]))
		return erg
	
	def ImageXYPaare_aus_scene(self,paare):
		'''Listen'''
		erg = []
		for paar in paare:
			erg.append( self.ImageXY_aus_scene(paar[0],paar[1]))
		return erg

	def scene6XY_aus_Image(self,x,y,x2,y2,x3,y3):
		return self.sceneX_aus_Image(x) , self.sceneY_aus_Image(y) , self.sceneX_aus_Image(x2) , self.sceneY_aus_Image(y2) , self.sceneX_aus_Image(x3) , self.sceneY_aus_Image(y3)
	
	def Image6XY_aus_scene(self,x,y,x2,y2,x3,y3):
		return self.ImageX_aus_scene(x) , self.ImageY_aus_scene(y) , self.ImageX_aus_scene(x2) , self.ImageY_aus_scene(y2) , self.ImageX_aus_scene(x3) , self.ImageY_aus_scene(y3)

	def scene6XY_aus_ImageTupel(self,t):
		x1,y1,x2,y2,x3,y3 = t
		return self.scene6XY_aus_Image(x1,y1,x2,y2,x3,y3)
	
	def Image6XY_aus_sceneTupel(self,t):
		x1,y1,x2,y2,x3,y3 = t
		return self.Image6XY_aus_scene(x1,y1,x2,y2,x3,y3)
	


#__________main____

print(modulname)

if __name__ == '__main__':
	fine = True
	kk = KoordinatenKonverter(100,200)
	ix20 = kk.ImageX_aus_scene( 20)
	iy20 = kk.ImageY_aus_scene(180)
	sxy20_180 = kk.sceneXY_aus_Image(ix20,iy20)
	print('sxy20_180 =',sxy20_180)
	it = (1,2,3,4,5,6)
	st2 = kk.scene6XY_aus_ImageTupel(it)
	it3 = kk.Image6XY_aus_sceneTupel(st2)
	print('st2=',st2,'   it3=',it3)
	fine = fine and ( it == it3 )
	print('fine=',fine)
