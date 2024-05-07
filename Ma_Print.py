# -*- coding: utf-8 -*-
modulname = 'Ma_Print'
_c_ = '(c) 2024, Matthias Mittelstein, Germany, 23816 Neversdorf, Hauptstraße 23'

def print_dict(d,title=None,keyWidth=21,ausserSchluessel=(''),sort=False,col=None):
	if title:
		linkerText  = title
		linkeBreite = len(title)
	else:
		linkerText  = '--dict'
		linkeBreite = 6
	#print d.attribute()
	#for pair in d:
	#	print str(pair)
	#	#print d[pair]
	
	if d == None:
		line = '{0:{titW}s} <<None>>'.format(linkerText
					                                    ,titW=linkeBreite) 
		if col:
			col.append(line)
		else:
			print(line)
	elif sort:
		for key, value in sorted(d.items()): #Python 2.x: iteritems()
			if key in ausserSchluessel:
				pass
			else:
				if type(value) == dict:
					titleDisp = title
					subtitle = titleDisp + '.' + key
					print_dict(value,title=subtitle,sort=True,col=col)
				else:
					line = '{2:{titW}s} {0:{keyW}s} : {1}'.format(key,value,linkerText
					                                    ,titW=linkeBreite,keyW=keyWidth)
					if col:
						col.append(line)
					else:
						print(line)
				linkerText = ' '
	else:
		for key, value in        d.items() : #Python 2.x: iteritems()
			if key in ausserSchluessel:
				pass
			else:
				if type(value) == dict:
					titleDisp = title
					subtitle = titleDisp + '.' + key
					print_dict(value,title=subtitle         ,col=col)
				else:
					line = '{2:{titW}s} {0:{keyW}s} : {1}'.format(key,value,linkerText
					                                    ,titW=linkeBreite,keyW=keyWidth)
					if col:
						col.append(line)
					else:
						print(line)
				linkerText = ' '
				

def print_list(l,title=None,col=None):
	if title:
		linkerText  = title
		linkeBreite = len(title)
	else:
		linkerText  = '--list'
		linkeBreite = 6
	for item in iter(l):
		line = '{0:{titW}s} {1}'.format(linkerText, item, titW=linkeBreite)
		if col:
			col.append(line)
		else:
			print(line)
		linkerText = ' '

def print_list_of_dicts(lod,col=None):
	ix = 0
	for item in iter(lod):
		line = '--{}'.format(ix)
		if col:
			col.append(line)
		else:
			print(line)
		print_dict(item,col=col)
		ix = ix+1

def print_label_and_dict(ld,col=None):
	label = ld[0]
	dic   = ld[1]
	line = '>>{}'.format(label)
	if col:
		col.append(line)
	else:
		print(line)
	print_dict(dic,col=col)
		

def print_label_and_list_of_dicts(llod,col=None):
	ix = 0
	label = llod[0]
	lod   = llod[1]
	line = '>>{}'.format(label)
	if col:
		col.append(line)
	else:
		print(line)
	for item in iter(lod):
		line = '--{}'.format(ix)
		if col:
			col.append(line)
		else:
			print(line)
		print_dict(item,col=col)
		ix = ix+1


def print_list_of_label_and_list_dicts(lllod,col=None):
	ix = 0
	for llod in iter(lllod):
		line = '=={}'.format(ix)
		if col:
			col.append(line)
		else:
			print(line)
		print_label_and_list_of_dicts(llod,col=col)
		ix = ix+1
		
		
def print_list_of_label_and_dict(lld,col=None):
	ix = 0
	for ld in iter(lld):
		line = '=={}'.format(ix)
		if col:
			col.append(line)
		else:
			print(line)
		print_label_and_dict(ld,col=col)
		ix = ix+1
		

if __name__ == '__main__':
	print( 'Selbsttest für', modulname )
	d = { 'a':1
	    , 'c':3
	    , 'b':2
	    }
	print_dict(None)
	print_dict(d)
	print_dict(d , keyWidth=1 , title='Test')
	print_dict(d , sort=True , keyWidth=1 , title='sortiert')
	l = ( 'eins', 'zwei', 'drei')
	print_list(l)
	print_list(l,title='Test')

