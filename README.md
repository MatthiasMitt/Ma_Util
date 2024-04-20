Ma_Util
=======

Ein Repository, dass diejenigen Hilfsmoduln und -funktionen enthält,
die in verschiedenen Nachbar-Repositories mehrfach gebraucht werden 
können.

Ma_Plattform
------------

Ermittle, wo ein Python-Programm läuft.
z.Z. sind bekannt:
* iPad   mit iOS    und mit Pythonista
* iPhone mit iPadOS und mit Pythonista
* iMac   mit macOS  und mit python3

Ma_Console
----------

Schreibe Überschriften etc. je nach Plattfrom
farbig oder anderes hervorgehoben.

Ma_Koord
--------

In 'scene' and related packages the coordinates are integers counting pixels.
'x'-values have their zero at the left edge and is growing to the right.
'y'-values have their zero at the bottom edge and is growing upwards.

In 'Image', 'ImageDraw' and related packages the coordinates are also integers
and are also counting pixels.
'x'-values have their zero at the left edge and is growing to the right.
'y'-values have their zero at the top edge and is growing downwards.

Dieser Modul hilft beim Konvertieren. Das ist zwar nicht schwierig,
aber sehr fehleranfällig.

Ma_MIDI
-------

Bausteine um Melodien aufzuschreiben, die dann nach MIDI umgewandelt
werden können. Auf iPad und iPhone scheint das der einzige Weg zur
Tonausgabe zu sein: Erst eine MIDI-Datei erstellen und sie dann
abspielen.
[ Funktioniert bisher nur auf iPad und iPhone. ]
