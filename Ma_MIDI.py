# -*- coding: utf-8 -*-
modulname = "Ma_MIDI.py"
_c_ = '(c) 2024, Matthias Mittelstein, Germany, 23816 Neversdorf, Hauptstraße 23'

'''Generates a MIDI file with ... . The result is then played with the sound.MIDIPlayer class.
If nothing happens, make sure that your device isn't muted.
'''

'''
Bausteine um Melodien aufzuschreiben, die dann nach MIDI umgewandelt
werden können. Auf iPad und iPhone scheint das der einzige Weg zur
Tonausgabe zu sein: Erst eine MIDI-Datei erstellen und sie dann
abspielen.
[ Funktioniert bisher nur auf iPad und iPhone. ]
'''

try:
	import sound
	from midiutil.MidiFile import MIDIFile
except:
	pass

from random import choice, randint
import string



#          international
#          !      MIDI-Nummer
#          !      !   deutsch
#          !      !   !    MIDI-Name
#          !      !   !    !    Sonstiges (als Kommentar)
hoehen = { 'C3':( 48,"c" ,'C2')
        , 'G3':( 55,"g" ,'G2')
        , 'C4':( 60,"c'",'C3')
        , 'D4':( 62,"d'",'D3')
        , 'E4':( 64,"e'",'E3')
        , 'F4':( 65,"f'",'F3')
        , 'G4':( 67,"g'",'G3')
        , 'A4':( 69,"a'",'A3') # Kammerton, 440 Hz
        , 'H4':( 70,"h'",'H3')
        , 'C5':( 72,"c''",'C4')
        , 'D5':( 74,"d''",'D4')
        , 'E5':( 76,"e''",'E4')
        } 

laengen = { 'o' :(16,'o'  ) # ganze Note, 16/16
         , 'h' :( 8,'o!' )
         , 'v' :( 4,'_!' )
         , 'a' :( 2,"_!'")
         , 's' :( 1,'_!"')
         , 'dv':(12,'o!.') # dreiviertel
         , 'zd':(13,'o!+_!+_!"')
         , 'zn':( 9,'o!+_!"')
         , 'zs':( 7,'_!..') # viertel plus achtel plus punkt
         , 'zy':(24,'o.+o.')    # zwei dreiviertel
         , 'zz':(36,'o.+o.+o.') # drei dreiviertel
         , 'da':( 6,'_!.') # dreiachtel
         , 'ds':( 3,"_!'.")
         }

geraete = [ (  0,'Klavier 1')
         , (  1,'Klavier 2')
         , (  3,'Klavier mit Sinus')
         , (  6,'nakter Ton')
         , ( 17,'Hammondorgel (etwas)')
         , ( 19,'Kirchenorgel')
         , ( 20,'nakte Töne (Melodika?)')
         , ( 25,'Cembalo 1')
         , ( 28,'Cembalo 2')
         , ( 29,'Melodika')
         , ( 31,'piepsiges Summen')
         , ( 32,'Hammondorgel (etwas)')
         , ( 33,'einfacher Ton')
         , ( 34,'einfacher Ton')
         , ( 40,'Geige')
         , ( 43,'Klavier nicht alle Töne')
         , ( 44,'Synt mit Schnarren')
         , ( 45,'geschlagene Seiten?')
         , ( 57,'Posaune')
         , ( 58,'Synt')
         , ( 60,'Synt posaunig')
         , ( 63,'Synt')
         , ( 65,'Synt, trompetig')
         , ( 74,'Bassflöte')
         , ( 75,'Flöte mit Anlaut')
         , ( 76,'Flöte')
         , ( 77,'Orgelflöte?')
         , ( 81,'Hammondorgel (etwas)')
         , ( 82,'Orgel (etwas) nur schwacher Anlaut')
         , ( 84,'Hupe mit Klavier')
         , ( 99,'Synt')
         , (103,'Synt zweistimmig')
         , (105,'Chembalo-synt')
         , (108,'Xylophon')
         , (110,'Synt')
         , (111,'Synt mit zugehaltener Nase')
         , (112,'Glocken')
         , (113,'Holzklöppel auf Blechglocken')
         , (114,'weiche Klöppel auf Metallrohr')
         , (117,'weiche Trommel (nicht mehrstimmig?)')
         , (118,'klopfen')
         , (119,'leises Bellen?')
         , (120,'feilen')
         , (122,'Regen (ohne Tonhöhenänderung)')
         , (124,'Gockenläuten')
         , (125,'-')
         , (127,'Rauschen mit Anlaut')
         , (128,'Klavier o Chembalo')
         , (140,'Xylophon')
         , (142,'Kirchenglocken')
         , (143,'gezupfte Gitarre')
         , (147,'Orgel')
         , (159,'Flöte (synt)')
         , (151,'Synt trocken')
         , (154,'schlichter Orgelton')
         , (157,'einfacher Ton')
         , (161,'einfacher Ton')
         , (168,'Cello')
         , (172,'Synt mit Schnarren')
         , (173,'gezupfte Geige')
         , (176,'Synt zweistimmig')
         , (180,'Synt, mehrstimmig')
         , (181,'Xylophon, etwas glasig')
         , (182,'Orgel oder Säge')
         , (183,'Klavier und Bläser und Hall')
         , (188,'trompetige Orgel')
         , (190,'summender Synt')
         , (193,'Blechbläser')
         , (194,'weiche Trompete')
         , (202,'Bassflöte mit Hammond-Anschlag')
         , (203,'Bassflöte mit Anblaston')
         , (206,'tiefe, weiche Orgelflöte')
         , (220,'Synt zweistimmig')
         , (221,'Synt (Teppich) 2')
         , (222,'Synt (Teppich) 2')
         , (229,'Synt mit Hall 1')
         , (231,'Synt mit Hall 3')
         , (234,'holziges Cembalo')
         , (243,'klopfen auf Holz')
         , (244,'Trommel mit Handballen')
         , (245,'Trommeln')
         , (246,'klopfen o klatschen')
         , (247,'Rauschen?')
         , (248,'sägen')
         ]


# Melodie-Format 1
#-================
# 1: Liste von Anschlägen, die nacheinander gespielt werden sollen.
# 2: Liste (oft nur Einer) von Tönen, die gleichzeitig gespielt werden sollen.
#    Falls die Töne unterschiedlich lang sein sollten, muss der
#    erste Ton der längste sein.
# 3: Paar aus Dauer und Tonhöhe.
# 4: zwei Strings mit Dauer resp. Tonhöhe.
#
takt9_1l = [ [ ('v','C4' ) ]
          , [ ('v','D4' ), ('v','E4') ]
          , [ ('v','C4' ) ]
          , [ ('v','D4' ) ]
          ]
takt8_1l = [[('v','C4')]
          ,[('v','D4'), ('v','E4')]
          ,[('v','C4')]
          ,[('v','D4')]
          ]

# Melodie-Format 2
#-================
# 1: Liste von Anschlägen, die nacheinander gespielt werden sollen.
# 2: Liste (oft nur Einer) von Tönen, die gleichzeitig gespielt werden sollen.
# 3: String konkateniert aus Dauer und Tonhöhe.
#
takt10_1l = [ [ 'vC4' ]
           , [ 'vD4','vE4']
           , [ 'vC4' ]
           , [ 'vD4' ]
           ]

# Melodie-Format 3
#-================
# 1: String, der sich an White-Space in Anschläge trennen lässt,
#    die nacheinander gespielt werden sollen.
# 2: Strings, die sich an '/' pder '|' trennen lassen in Töne,
#    die gleichzeitig gespielt werden sollen.
# 3: Strings, die sich in Dauer und Tonhöhe trennen lassen.
#
takt5_1l = 'vC4  vD4/vE4  vC4  vD4'
takt6_1l = 'vC4  vD4|vE4  vC4  vD4'


class Uhr():
	def __init__(self,name='',zeige=1):
		'''
		zeige == 0 : nichts
		      == 1 : print wenn sync etwas unerwartet ändern muss
		      == 2 : print jeden sync
		      == 3 : print jede Aktion
		'''
		self.uhr   = 0
		self.name  = name
		self.zeige = zeige
		
	def ist(self):
		return self.uhr
	
	def tick(self,mal=1):
		self.uhr += mal
		if self.zeige >= 3:
			print(('Die Uhr',self.name,'ist', self.uhr, '.'))
	
	def sync(self,uhr2):
		t2 = uhr2.ist()
		if t2 == self.uhr:
			if self.zeige >= 2:
				print('Die zwei Uhren gehen gleich.')
		elif t2 > self.uhr:
			if self.zeige >= 1:
				print(('Stelle Uhr',self.name,'von', self.uhr, 'auf', t2, '.'))
			self.uhr = t2
		else:
			if self.zeige >= 1:
				print(('Uhr',self.name,'ist weiter. Stelle andere Uhr.'))
			uhr2.sync(self)

	def vorstellen(self,uhr2):
		''' Die eigene Uhr vorstellen
		'''
		t2 = uhr2.ist()
		if t2 == self.uhr:
			if self.zeige >= 2:
				print('Die zwei Uhren gehen gleich.')
		elif t2 > self.uhr:
			if self.zeige >= 2:
				print(('Stelle Uhr',self.name,'von', self.uhr, 'auf', t2, 'vor.'))
			self.uhr = t2
		else:
			if self.zeige >= 1:
				print(('Uhr',self.name,'ist weiter. Vorstellen wäre sinnlos.'))

	def zurueckstellen(self,uhr2):
		''' Die eigene Uhr zurückstellen
		'''
		t2 = uhr2.ist()
		if t2 == self.uhr:
			if self.zeige >= 2:
				print('Die zwei Uhren gehen gleich.')
		elif t2 > self.uhr:
			if self.zeige >= 1:
				print(('Uhr',self.name
				     ,'ist sowieso schon hinterher. Zurückstellen wäre sinnlos.'))
		else:
			if self.zeige >= 2:
				print(('Stelle Uhr',self.name,'von', self.uhr, 'zurück auf', t2, '.'))
			self.uhr = t2

#-end-of-class Uhr



class MelodieStueck:
	def __init__(self,zeige=0):
		'''
		zeige == 0 : nichts
		      == 2 : print jede Note
		'''
		self.stueck1 = None
		self.stueck2 = None
		self.stueck3 = None
		self.zeige = zeige

	def lade1(self,st1):
		self.stueck1 = st1
		self.stueck2 = None
		self.stueck3 = None
	
	def lade2(self,st2):
		self.stueck1 = None
		self.stueck2 = st2
		self.stueck3 = None
		
	def lade3(self,st3):
		self.stueck1 = None
		self.stueck2 = None
		self.stueck3 = st3
		
	def mach2aus3(self):
		self.stueck1 = None
		self.stueck2 = []
		anschlaege = self.stueck3.split() # at white space
		for anschlag in anschlaege:
			#print('anschlag',anschlag)
			anschlaegeListe = []
			toene = anschlag.split('/')
			if len(toene) == 1:
				toene = anschlag.split('|')
			for ton in toene:
				#print('.                  ton',ton)
				anschlaegeListe.append(ton)
			self.stueck2.append(anschlaegeListe)
				
	
	def mach1aus2(self):
		self.stueck1 = []
		for anschlag in self.stueck2:
			#print('A',anschlag)
			#print(type(anschlag))
			if type(anschlag) == str:
				lh = self.mach1aus2ton(anschlag) # ton = anschlag
				self.stueck1.append([lh])
			else:
				gl = []
				for ton in anschlag:
					lh = self.mach1aus2ton(ton)
					gl.append(lh)
				self.stueck1.append(gl)
		#print( self.stueck1)
	
	def mach1aus2ton(self,tonStr):
		#print('.         T',tonStr)
		l = str.rstrip(tonStr,'AHCDEFGB#bP1234567890') #p2to3: string --> str
		h = str.lstrip(tonStr,'ohvasdzyn')             #p2to3: string --> str
		#print('l',l,'  h',h)
		sechszehntel,bild = laengen[l]
		if h == 'P':
			pass #Pause
		else:
			midinr,deutsch,midiname = hoehen[h]
		#print(sechszehntel,'/16 MIDI-Nr',midinr)
		return ( l,h )
	
	def verbindeMIDI(self,midi,track,chan,uhr,dura16, laut=100):
		'''
		midi : MIDIfile to append to
		track : int
		chan  : int
		startTime : float
		dura16 : float? : duration of 1/16 note
		'''
		self.midi   = midi
		self.track  = track
		self.chan   = chan
		self.uhr    = uhr
		self.dura16 = dura16
		self.laut   = laut
	
	def lauter(self,um=10):
		self.laut += 10
		if self.laut > 100:
			self.laut  = 100
		
	def leiser(self,um=10):
		self.laut -= 10
		if self.laut < 0:
			self.laut  = 0
		
	def machMIDI(self):
		if self.stueck1 == None:
			if self.stueck2 == None:
				self.mach2aus3()
			self.mach1aus2()
		startTime = self.uhr.ist()
		for anschlag in self.stueck1:
			dura = 0
			for ton in anschlag:
				lStr,hStr = ton
				sechszehntel,bild = laengen[lStr]
				if dura == 0:
					dura = sechszehntel
				if hStr == 'P':
					pass # Pause
				else:
					midinr,deutsch,midiname = hoehen[hStr]
					self.midi.addNote( self.track, self.chan
					                 , midinr
					                 , self.uhr.ist(), sechszehntel*self.dura16
					                 , self.laut )
					if self.zeige >= 2:
						print(( self.uhr.ist(),deutsch,bild \
						     , '.     ',midinr,'(',sechszehntel,')' ))
			dura *= self.dura16
			self.uhr.tick(dura)



# Allgemeine Doku über MIDI-Benutzung
#-===================================


""" Add notes to the MIDIFile object

       Use:
           MyMIDI.addNotes(track,channel,pitch,time, duration, volume)

       Arguments:
           track: The track to which the note is added.
           channel: the MIDI channel to assign to the note. [Integer, 0-15]
           pitch: the MIDI pitch number [Integer, 0-127].
           time: the time (in beats) at which the note sounds [Float].
           duration: the duration of the note (in beats) [Float].
           volume: the volume (velocity) of the note. [Integer, 0-127].
       """

"""
       Add a track name to a MIDI track.

       Use:
           MyMIDI.addTrackName(track,time,trackName)

       Argument:
           track: The track to which the name is added. [Integer, 0-127].
           time: The time at which the track name is added, in beats [Float].
           trackName
           """

"""
       Add a tempo event.

       Use:
           MyMIDI.addTempo(track, time, tempo)

       Arguments:
           track: The track to which the event is added. [Integer, 0-127].
           time: The time at which the event is added, in beats. [Float].
           tempo: The tempo, in Beats per Minute. [Integer]
       """

"""
       Add a MIDI controller event.

       Use:
           MyMIDI.addControllerEvent(track, channel, time, eventType, parameter1)

       Arguments:
           track: The track to which the event is added. [Integer, 0-127].
           channel: The channel the event is assigned to. [Integer, 0-15].
           time: The time at which the event is added, in beats. [Float].
           eventType: the controller event type.
           parameter1: The event's parameter. The meaning of which varies by event type.
       """



if __name__ == '__main__':
	
	print(modulname)
	print("Hier gibt es bisher weder eine Demo noch einen Selbsttest.")
