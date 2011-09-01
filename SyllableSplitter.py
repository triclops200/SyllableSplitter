lettergroups = ["bl","br","ch","cl","cr","ck",
	"dr","ci","fl","fr","gh","gl","gr","kl","kr","mn","nc","ng",
	"py","ss","ou","io","th","sc","ps","ee","ph","pr","qu","pt","st",
	"sh","tr","to","ly","gy","wh", "ry", "ky","oo"]
specials = ["io","tio","sio","sci","psy","ee","cio","eo","fly","y","why","cry","try", "dry", "ank"]
vowels = ["a","e","o","i","u"]
cons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
import sys
def containedIn(st,li):
	for i in range(0,len(li)):
		if(st == li[i]):
			return True
	return False
def remStringItem(st,i):
	return st[0:i]+st[i+1:]
def breakIntoGroups(st):
	fin = []
	x=0
	for i in range(0,len(st)-1):
		gro = ""
		gr = False
		vl = False
		if(x<len(st)):
			for ii in range(0,len(vowels)):
				if st[x] == vowels[ii]:
					if(x<len(st)-1):
						if(not containedIn(st[x]+st[x+1],lettergroups)):
							gro+=st[x]
						if(not containedIn(st[x+1],vowels)):
								vl = True
								x+=1
						else:
							for ii in range(0,len(lettergroups)):
								if st[x]+st[x+1] == lettergroups[ii]:
									gro += lettergroups[ii]
									gr = True
			if(containedIn(gro,specials) or containedIn(st[x],specials)):
				if(gro == ""):
					gro = st[x]
				if (len(fin)>0):
					if(containedIn(fin[len(fin)-1]+gro,specials)):
						gro = fin[len(fin)-1]+gro
						fin[len(fin)-1] = gro
						gro = ""
						x+=1
				if(x<=len(st)-2):
					if(containedIn(gro+st[x+1],specials)):
						gro = st[x-1]+gro
						fin[len(fin)-1] = remStringItem(fin[len(fin)-1],len(fin[len(fin)-1])-1)
				try:
					gro += st[x+2]
				except:
					asdsad=0
			if(x<len(st)-1 and not gr):
				for ii in range(0,len(lettergroups)):
					if st[x]+st[x+1] == lettergroups[ii]:
						gro += lettergroups[ii]
						gr = True
			if(not x<len(st)):
				for ind in range(0,len(fin)):
					if(fin[ind][0] == "o" and fin[ind][1] == "g" and ind !=0):
						fin[ind] = remStringItem(fin[ind],0)
						fin = fin[0:ind] + ["o"]+fin[ind:]
				return fin
			if(not gr and not vl):
				fin += [st[x]]
			elif(gr and not vl):
				fin += [gro];
				x+=len(gro)-1
			elif(vl and not gr):
				fin += [gro+st[x]]
			else:
				fin += [gro]
				x+=len(gro)-2
			x+=1			
		else:
			for ind in range(0,len(fin)):
				try:
					if(fin[ind][0] == "o" and fin[ind][1] == "g" and ind !=0):
						fin[ind] = remStringItem(fin[ind],0)
						fin = fin[0:ind] + ["o"]+fin[ind:]
				except:
					hsdkjsahdkj=0
			return fin
	for ind in range(0,len(fin)):
		if(fin[ind][0] == "o" and fin[ind][1] == "g" and ind !=0):
			fin[ind] = remStringItem(fin[ind],0)
			fin = fin[0:ind] + ["o"]+fin[ind:]
	return fin
def breakIntoSyllables(stli):
	fin = []
	x = 0
	for i in range(0,len(stli)):
		gro = ""
		if(x<len(stli)-1):
			if(containedIn(stli[x+1][0],vowels) and gro == "" and not containedIn(stli[x][0],vowels)):
				gro = stli[x]+stli[x+1]
				x+=1
			else:
				gro = stli[x] 
		elif(x==len(stli)-1):
			gro = stli[x] 
		if(gro != ""):
			fin +=[gro]
		x+=1
	if(fin[len(fin)-1] == "e"):
		del fin[len(fin)-1]
		fin[len(fin)-1]+="e"
	if(fin[len(fin)-1] == "t"):
		del fin[len(fin)-1]
		fin[len(fin)-1]+="t"
	if(fin[len(fin)-1] == "k"):
		del fin[len(fin)-1]
		fin[len(fin)-1]+="k"	
	return fin
k = breakIntoGroups(sys.argv[1])
print k
print breakIntoSyllables(k)
