# -*- coding: utf-8 -*-
modulname = 'Ma_DebugPrint'
_c_ = '(c) 2024, Matthias Mittelstein, Germany, 23816 Neversdorf, Hauptstraße 23'

import time
import sys # for flush()

class DebugPrint():
	def __init__(self,warnstufe=0):
		self._anfZeitKlasse = time.time()
		self._anfZeitKurz   = self._anfZeitKlasse
		self._wichtigkeit   = warnstufe
		self._einrueck      = 0
		self._tabBreite     = 2
		self._vorspann      = ''

	def neueWarnstufe(self,ws):
		self._wichtigkeit = ws

	def restart(self,title=None):
		self._anfZeitKurz = time.time()
		if title:
			self.print(title)

	def print(self,*args):
		now = time.time()
		timediff = now - self._anfZeitKlasse
		if self._anfZeitKurz == self._anfZeitKlasse:
			print( format(timediff  , "10f" #, "{:12f}"
			             )
			     , self._vorspann, *args )
			sys.stdout.flush()
		else:
			timediff2 = now - self._anfZeitKurz
			print( format(timediff,"10f"), format(timediff2 ,"10f")
			     , self._vorspann, *args )
			sys.stdout.flush()

	def print1(self,*args):
		if self._wichtigkeit >= 1:
			self.print(*args)

	def print2(self,*args):
		if self._wichtigkeit >= 2:
			self.print(*args)

	def print3(self,*args):
		if self._wichtigkeit >= 3:
			self.print(*args)

	def einruecken(self):
		self._einrueck += self._tabBreite
		for i in range(self._tabBreite):
			self._vorspann += ' '

	def ausruecken(self):
		self._einrueck -= self._tabBreite
		if self._einrueck == 0:
			self._vorspann = ''
		elif self._einrueck < 0:
			self._einrueck = 0
		else:
			n = self._einrueck * self._tabBreite
			self._vorspann = self._vorspann[0:n]
