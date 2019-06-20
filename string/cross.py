from tkinter import *

root = Tk()
root.title("Crossword")
root.geometry("1500x1000")
root.resizable(width=True, height=True)

row = []
array=[]

for i in range(1,80):
    row.append(i)
array.append(row)

row=[2]
for i in range(1,80):
    row.append("!!!")
array.append(row)


for j in range(3,80):
    row=[j, "!!!"]
    for i in range(1,80):
        row.append(".")
    array.append(row)
    j+=1

descr = []
coord = []
coordText=[]
directions = []

def printArray(firstRow, secRow):
    #for j in range(len(array)):
    for j in range(0, secRow+1):
        #for i in range(len(array[j])):
        for i in range(0, secRow+1):
            if i<firstRow or j<firstRow:
                fnt = "Arial 6"
                bckgr="#fff"
                frgr="#113f45"
            else:
                fnt="Cambria 11"
                bckgr="#113f45"
                frgr="#fff"

            if array[j][i]!= ".":
                label = Label(text=array[j][i], justify=CENTER, bd="0", font=fnt, background=bckgr, foreground=frgr, width="2",height="1") #893f45 9B5150 pady="0", padx="0",
                label.grid(row=j, column=i)
            else:
                #label = Label(text="", justify=CENTER, bd="0", font="Cambria 11", background="#fff", foreground="#fff", width="2",height="1")
                #label.grid(row=j, column=i)
                if (array[j+1][i] in "ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-" and array[j+2][i] in "ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-")  or (array[j][i+1] in "ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-" and array[j][i+2] in "ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-"):
                    btn = Button(text=str(j+1)+":"+str(i+1),  background="#fff",      foreground="#000",  width="2",height="2", font="Arial 5" , command=clickButton)
                    btn.grid(row=j, column=i)

def clickButton():
    lblText="Here should be word description"
    fldText="Here you could type your assumption"


    label = Label(text=lblText, justify=LEFT, bd="0", width=len(lblText), font="Cambria 16", background="#113f45", foreground="#fff") #893f45 9B5150 pady="0", padx="0",
    label.grid(row=40, column=5, columnspan=25)
    text = Text(width=len(fldText), fg="black", bg='white', height="2", wrap=WORD)
    text.insert(1.0, fldText)
    text.grid(row=42, column=5, columnspan=25)
    btn = Button(text="OK",  background="#ddd",      foreground="black",  width="7",height="3", font="Arial 10" , command=clickOK)
    btn.grid(row=42, column=27, columnspan=6)

def clickOK():

    return("")

def lettNr(nr):
    seq=['aa','ab','ac','ad','ae','af','ag','ah','ai','aj','ak','ba','bb','bc','bd','be','bf','bg','bh','bi','bj','bk','ca','cb','cc','cd','ce','cf','cg','ch','ci','cj','ck','da','db','dc','dd','de','df','dg','dh','di','dj','dk','ea','eb','ec','ed','ee','ef','eg','eh','ei','ej','ek','fa','fb','fc','fd','fe','ff','fg','fh','fi','fj','fk','ga','gb','gc','gd','ge','gf','gg','gh','gi','gj','gk','ha','hb','hc','hd','he','hf','hg','hh','hi','hj','hk','ia','ib','ic','id','ie','if','ig','ih','ii','ij','ik','ja','jb','jc','jd','je','jf','jg','jh','ji','jj','jk','ka','kb','kc','kd','ke','kf','kg','kh','ki','kj','kk']

    return(seq[nr])

def printDescr():

    dString=[]
    #descrText=""
    i=0
    for direction, d, c in zip(directions, descr,coord):

        #descrText=descrText+"\n"+i
        if len(str(c[0]))==1:
            crd0="0"+str(c[0])
        else:
            crd0=str(c[0])

        if len(str(c[1]))==1:
            crd1="0"+str(c[1])
        else:
            crd1=str(c[1])

        newText = direction + "   "+lettNr(c[0])+":"+lettNr(c[1])+crd0+":"+crd1+"___("+str(i)+")__"+d+"__"
        dString.append(newText)
        i+=1
    #print(len(dString))
    dString.sort()

    #print(len(dString))
    #print(dString)

    hor="По горизонтали: \n"
    vertB="По вертикали: \n"
    vertR=""

    i=1
    for item in dString:
        if item[0:3]=="hor":
            hor = hor +"(" +str(i) +")" + item[23:62]+">> <"+item[11:16]+">\n"
            i+=1
        else:
            hor = hor +"\n"
            break

    horLen = i
    i=1
    for item in dString[horLen-1:int((len(dString)-3)/2)]:
        #if i < 50 - horLen
        vertB = vertB +"(" +str(i) +")" + item[23:62]+">> <"+item[11:16]+">\n"
        i+=1
        #else:
            #break

    for item in dString[horLen+i-2:len(dString)]:
        vertR = vertR +"(" +str(i) +")" + item[23:62]+">> <"+item[11:16]+">\n"
        i+=1

    descrList1 = hor + vertB
    descrList2 = vertR

    label = Label(text=descrList1, bd="0", justify=LEFT,  font="Arial 8", width=52,background="#fff")#893f45 9B5150 pady="0", padx="0",
    label.grid(row=0, column = 49, columnspan=48,rowspan=70)
    label = Label(text=descrList2, bd="0", justify=LEFT, font="Arial 8", width=55,background="#fff")#893f45 9B5150 pady="0", padx="0",
    label.grid(row=0, column = 97, columnspan=48,rowspan=70)

    #for item in dString:
    #    label = Label(text=item,  justify=LEFT,  bd="0", font="Arial 8", width=int(len(item)),background="#fff")#893f45 9B5150 pady="0", padx="0",
    #    label.grid(row=2+i, column = 52, columnspan=int(len(item))+2)
    #    i+=1





from random import random , sample

with open("/home/sergey/Документы/projects/string/_vocabulary.txt") as file:
   voc = [row.strip() for row in file]


vocabulary=[]
vocabularyRev=[]
descriptions=[]
wordLength=[]
wordLengthRev=[]
for i in range(30):
    a=[]
    wordLength.append(a)

for i in range(30):
    a=[]
    wordLengthRev.append(a)

for item in voc:
    space = item.find(" ")
    word = item[0:space]
    description = item[space+1:len(item)-1]
    vocabulary.append(word)
    vocabularyRev.append(word[::-1])
    descriptions.append(description)
    for i in range(1, len(word)+1):
        wordLength[i].append(word)
        wordLengthRev[i].append(word[::-1])
words = []
for i in range(30):
    a=[]
    for j in range(len("ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-")):
        a.append([])
    words.append(a)

for i in range(15000):
    for j in range(0,len(vocabulary[i])):

        if vocabulary[i][j] in "ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-":

            words[j]["ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-".find(vocabulary[i][j])].append(vocabulary[i])


wordsRev = []
for i in range(30):
    a=[]
    for j in range(len("ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-")):
        a.append([])
    wordsRev.append(a)

for i in range(15000):
    for j in range(0,len(vocabulary[i])):

        if vocabulary[i][::-1][j] in "ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-":

            wordsRev[j]["ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-".find(vocabulary[i][::-1][j])].append(vocabulary[i][::-1])




def goodWords(crossNumbers,crossLetters):
    gW = vocabulary
    if crossNumbers[0]==0:
        gW = words[0]["ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-".find(crossLetters[0])]
    for i in range(len(crossNumbers)):
            gWcut = list(set(gW) - set(wordLength[crossNumbers[i]]))
            gWnew = list(set(words[crossNumbers[i]]["ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-".find(crossLetters[i])]) & set(gW))
            gW = list(set(gWcut) | set(gWnew))
    return(gW)


def goodWordsRev(crossNumbers,crossLetters):
    gW = vocabularyRev
    if crossNumbers[0]==0:
        gW = wordsRev[0]["ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-".find(crossLetters[0])]
    for i in range(len(crossNumbers)):
            gWcut = list(set(gW) - set(wordLengthRev[crossNumbers[i]]))
            gWnew = list(set(wordsRev[crossNumbers[i]]["ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-".find(crossLetters[i])]) & set(gW))
            gW = list(set(gWcut) | set(gWnew))
    return(gW)





def shiftCell(cell, direct, stepsNr):
    if direct == "south":
        return([cell[0]+stepsNr, cell[1]])
    if direct == "north":
        return([cell[0]-stepsNr, cell[1]])
    if direct == "east":
        return([cell[0], cell[1]+stepsNr])
    if direct == "west":
        return([cell[0], cell[1]-stepsNr])

def sides(cell, direct, stepsNr):
    if direct == "south":
        if array[cell[0]+stepsNr][cell[1]+1]!="." or array[cell[0]+stepsNr][cell[1]-1]!=".":
            return("filled")
        else:
            return("empty")

    if direct == "north":
        if array[cell[0]-stepsNr][cell[1]+1]!="." or array[cell[0]-stepsNr][cell[1]-1]!=".":
            return("filled")
        else:
            return("empty")

    if direct == "east":
        if array[cell[0]+1][cell[1]+stepsNr]!="." or array[cell[0]-1][cell[1]+stepsNr]!=".":
            return("filled")
        else:
            return("empty")

    if direct == "west":
        if array[cell[0]+1][cell[1]-stepsNr]!="." or array[cell[0]-1][cell[1]-stepsNr]!=".":
            return("filled")
        else:
            return("empty")

def chOrient(orient):
    if orient == "hor":
        return "ver"
    else:
        return "hor"

def maxLength(cell, direct):
    for i in range(0,25):
        if array[shiftCell(cell, direct, i+1)[0]][shiftCell(cell, direct, i+1)[1]]=="!!!":
            return(i)
        if sides(cell, direct, i+1)=="filled" and array[shiftCell(cell, direct, i+1)[0]][shiftCell(cell, direct, i+1)[1]]==".":
            return(i+1)
        if array[shiftCell(cell, direct, i+1)[0]][shiftCell(cell, direct, i+1)[1]]!="." and array[shiftCell(cell, direct, i+2)[0]][shiftCell(cell, direct, i+2)[1]]!=".":
            return(i+1)
    return(25)


def crossingAndRestriction(cell, direct,length):
    crossPositions=[]
    crossLetters=[]
    restrictedPositions=[]


    for i in range(min(length+1,(maxLength(cell, direct)+1))):
        if array[shiftCell(cell, direct, i)[0]][shiftCell(cell, direct, i)[1]]!=".":
            crossPositions.append(i)
            crossLetters.append(array[shiftCell(cell,direct, i)[0]][shiftCell(cell,direct, i)[1]])
            restrictedPositions.append(i-1)
    return([crossPositions,crossLetters])


def fitWord(cell, direct):
    rand = sample(range( 1, 15000 ) , 1 )[0]
    word = sht_dict.cells(rand,1)
    while checkWord(word, cell, direct)!=1:
        rand = sample(range( 1, 15000 ) , 1 )[0]
        word = sht_dict.cells(rand,1)


    return(word)

def fitWordWithLength(cell, direct, length):

    rand = sample(range( 1, 15000 ) , 1 )[0]
    word = sht_dict.cells(rand,1)
    if len(word)<length:
        while checkWordWithLength(word, cell, direct, length)!=1:
            rand = sample(range( 1, 15000 ) , 1 )[0]
            word = sht_dict.cells(rand,1)


    return(word)



def diction(length):
    if length == 56:
        dic=[]
        for i in range(1,15000):
            if len(sht_dict.cells(i,1))>=5 and len(sht_dict.cells(i,1))<=6:
                dic.append(sht_dict.cells(i,1))
        return(dic)

    else:
        dic=[]
        for i in range(1,15000):
            if len(sht_dict.cells(i,1))>=length:
                dic.append(sht_dict.cells(i,1))
        return(dic)


def dictionRev(length):
    if length == 56:
        dic=[]
        for i in range(1,15000):
            if len(sht_dict.cells(i,1))>=5 and len(sht_dict.cells(i,1))<=6:
                dic.append(sht_dict.cells(i,1)[::-1])
        return(dic)

    else:
        dic=[]
        for i in range(1,15000):
            if len(sht_dict.cells(i,1))>=length:
                dic.append(sht_dict.cells(i,1)[::-1])
        return(dic)

def voc(cell, direct, length):
    vocab= []
    for word in diction():
        if checkWordWithLength(word, cell, direct, length)>0:
            vocab.append(word)
    return(vocab)

def goodLetters(word, gL):
    for i in gL:
        if (word[i] in "КЕНГВАПРОЛДСМИТБ") != True:
            return(0)
    return(1)

def findWord(cell, direct, lengthMin, lengthMax, goodLett):
    if maxLength(cell, direct)<lengthMin:
        return("no match")
    if crossingAndRestriction(cell, direct, lengthMax)[0]==[]  or crossingAndRestriction(cell, direct, lengthMax)[0][0]>lengthMax:
        new_dict = vocabulary
    else:
        new_dict = goodWords(crossingAndRestriction(cell, direct, lengthMax)[0],crossingAndRestriction(cell, direct, lengthMax)[1])

    new_dict = list(set(new_dict)&set(wordLength[lengthMin])-set(wordLength[lengthMax+1]))
    new_dict = sample(new_dict, len(new_dict))
    for word in new_dict:
        #print(word)
        if (len(word) in  crossingAndRestriction(cell, direct, lengthMax)[0])!=True or crossingAndRestriction(cell, direct, lengthMax)[0]==[]:
            if len(word)<=lengthMax and len(word)>=lengthMin:
                if goodLetters(word, goodLett) == 1:
                    if len(word)<= maxLength(cell, direct):
                        return(word)
    return("no match")

def findWordRev(cell, direct, lengthMin, lengthMax, goodLett):
    if maxLength(cell, direct)<lengthMin:
        return("no match")
    if crossingAndRestriction(cell, direct, lengthMax)[0]==[] or crossingAndRestriction(cell, direct, lengthMax)[0][0]>lengthMax:
        new_dict = vocabularyRev
    else:
        new_dict = goodWordsRev(crossingAndRestriction(cell, direct, lengthMax)[0],crossingAndRestriction(cell, direct, lengthMax)[1])

    new_dict = list(set(new_dict)&set(wordLengthRev[lengthMin])-set(wordLengthRev[lengthMax+1]))
    new_dict = sample(new_dict, len(new_dict))
    for word in new_dict:
        #print(word)
        if (len(word) in  crossingAndRestriction(cell, direct, lengthMax)[0])!=True or crossingAndRestriction(cell, direct, lengthMax)[0]==[]:
            if len(word)<=lengthMax and len(word)>=lengthMin:
                if goodLetters(word, goodLett) == 1:
                    if len(word)<= maxLength(cell, direct):
                        return(word)
    return("no match")

def badLetter():
    return("ЦФЫЯЧШЩХЪЖЭЬЮ-")

def square(cell, length,  tale):
    #north

    word=findWord(cell, "east", length, 11, [2,6])

    lenNorth=len(word)
    i=0
    for lett in word:
        array[cell[0]][cell[1]+i]=lett
        i=i+1
    #west
    cell = shiftCell(cell, "east", tale)
    cell = shiftCell(cell, "north", tale)
    #print(cell)
    word=findWord(cell, "south", length, 11, [2,6])
    if word == "no match":
        return("west - no match")
    lenWest=len(word)
    i=0
    for lett in word:
        array[cell[0]+i][cell[1]]=lett
        i=i+1
    #sourh
    cell = shiftCell(cell, "south", length-tale-1)
    cell = shiftCell(cell, "west", tale)
    #print(cell)
    word=findWord(cell, "east", length, 11, [2, 4, 6])
    if word == "no match":
        return("south - no match")
    lenSouth=len(word)
    i=0
    for lett in word:
        array[cell[0]][cell[1]+i]=lett
        i=i+1
    #east
    cell = shiftCell(cell, "north", length-tale-1)
    cell = shiftCell(cell, "east", length-tale-1)
    #print(cell)
    word=findWord(cell, "south", length, 11, [2,6])
    if word == "no match":
        return("east - no match")
    lenEast=len(word)
    i=0
    for lett in word:
        array[cell[0]+i][cell[1]]=lett
        i=i+1

    return(lenNorth, lenEast, lenSouth, lenWest)




def squareReverse(cell, length,  tale):
    #north
    word=findWordRev(cell, "west", length, 11, [2,6])

    lenNorth=len(word)
    i=0
    for lett in word:
        array[cell[0]][cell[1]-i]=lett
        i=i+1
    #east
    cell = shiftCell(cell, "west", tale)
    cell = shiftCell(cell, "north", tale)
    #print(cell)
    word=findWord(cell, "south", length, 11, [2,6])
    if word == "no match":
        return("east - no match")
    lenEast=len(word)
    i=0
    for lett in word:
        array[cell[0]+i][cell[1]]=lett
        i=i+1
    #south
    cell = shiftCell(cell, "south", length-tale-1)
    cell = shiftCell(cell, "east", tale)
    #print(cell)
    word=findWordRev(cell, "west", length, 11, [2, 4, 6])
    if word == "no match":
        return("south - no match")
    lenSouth=len(word)
    i=0
    for lett in word:
        array[cell[0]][cell[1]-i]=lett
        i=i+1
    #west
    cell = shiftCell(cell, "north", length-tale-1)
    cell = shiftCell(cell, "west", length-tale-1)
    #print(cell)
    word=findWord(cell, "south", length, 11, [2,6])
    if word == "no match":
        return("west - no match")
    lenWest=len(word)
    i=0
    for lett in word:
        array[cell[0]+i][cell[1]]=lett
        i=i+1

    return(lenNorth, lenEast, lenSouth, lenWest)



def vocLength(length):
    vocabulary = []
    for word in diction():
        if len(word)>=9:
            vocabulary.update(word)
    return(vocabulary)


def goodStartFromEmptyCell(cell, direct):
    if direct=="north" and ((array[cell[0]+1][cell[1]]!=".")    or (array[cell[0]][cell[1]-1]!=".") or (array[cell[0]][cell[1]+1]!=".")):
        return(0)
    if direct=="south" and ((array[cell[0]-1][cell[1]]!=".")    or (array[cell[0]][cell[1]-1]!=".") or (array[cell[0]][cell[1]+1]!=".")):
        return(0)
    if direct=="west" and ((array[cell[0]][cell[1]+1]!=".")    or (array[cell[0]-1][cell[1]]!=".") or (array[cell[0]+1][cell[1]]!=".")):
        return(0)
    if direct=="east" and ((array[cell[0]][cell[1]-1]!=".")    or (array[cell[0]-1][cell[1]]!=".") or (array[cell[0]+1][cell[1]]!=".")):
        return(0)
    return(1)

def goodStartFromFilledCell(cell, direct):
    if direct=="north" and (array[cell[0]+1][cell[1]]!=".") :
        return(0)
    if direct=="south" and (array[cell[0]-1][cell[1]]!=".")  :
        return(0)
    if direct=="west" and (array[cell[0]][cell[1]+1]!="." or (array[cell[0]][cell[1]-1]!="." and array[cell[0]][cell[1]-2]!=".")):
        return(0)
    if direct=="east" and (array[cell[0]][cell[1]-1]!="."):
        return(0)
    return(1)

def goodStart(cell, direct):
    if array[cell[0]][cell[1]]==".":
        return(goodStartFromEmptyCell(cell, direct))
    else:
        return(goodStartFromFilledCell(cell, direct))

def cross3(cell, direct):
    if direct=="north":
        return(array[cell[0]-2][cell[1]])
    if direct=="east":
        return(array[cell[0]][cell[1]+2])
    if direct=="south":
        return(array[cell[0]+2][cell[1]])
    if direct=="west":
        return(array[cell[0]][cell[1]-2])


def fourCorners():
    cell=[10,10]
    a=square(cell,9, 2)
    #print(a)
    #print(cell)

    newCell = [cell[0]+2,cell[1]+4]
    word = findWord(newCell,"south",12, 15, [])
    lenJoinWord = len(word)
    i=0
    for lett in word:
        array[newCell[0]+i][newCell[1]]=lett
        i=i+1

    newCell=[newCell[0]+len(word)-2,newCell[1]-4]
    cell2 = newCell
    #print(newCell)

    b=square(newCell,9,2)
    #print(b)



    newCellRev=[cell[0],cell[1]+max(a[0],a[2],b[0],b[2])+15]
    c=squareReverse(newCellRev,9,2)
    #print(c)
    #print(cell)

    newCellRev = [newCellRev[0]+2,newCellRev[1]-4]


    word = findWord(newCellRev,"south",11, lenJoinWord, [])
    while len(word)!=lenJoinWord:
        word = findWord(newCellRev,"south",11, 15, [])

    i=0
    for lett in word:
        array[newCellRev[0]+i][newCellRev[1]]=lett
        i=i+1

    newCellRev=[newCellRev[0]+len(word)-2,newCellRev[1]+4]
    #print(newCellRev)

    d=squareReverse(newCellRev,9,2)
    #print(d)


    newCell = [14,18]
    #print(newCell)
    newLenSouth = lenJoinWord-5
    word = findWord(newCell,"south", newLenSouth, newLenSouth, [newLenSouth-1])
    while word == "no match":
        newCell = shiftCell(newCell, "north", 1)
        newLenSouth = newLenSouth + 1
        word = findWord(newCell,"south", newLenSouth, newLenSouth, [newLenSouth-1])
    i=0
    for lett in word:
        array[newCell[0]+i][newCell[1]]=lett
        i=i+1

    newCell=[newCell[0]+newLenSouth-1,18]
    #print(newCell)
    newLenEast = max(a[0],a[2],b[0],b[2])-2
    word = findWord(newCell,"east", newLenEast, newLenEast, [newLenEast-1])
    i=0
    for lett in word:
        array[newCell[0]][newCell[1]+i]=lett
        i=i+1


    newCell=[newCell[0]+2,18+max(a[0],a[2],b[0],b[2])-1]
    #print(newCell)
    newLenNorth = lenJoinWord-5
    word = findWordRev(newCell,"north", newLenNorth, newLenNorth, [newLenNorth-1])
    while word == "no match":
        newCell = shiftCell(newCell, "south", 1)
        newLenNorth = newLenNorth + 1
        word = findWordRev(newCell,"north", newLenNorth, newLenNorth, [newLenNorth-1])
    i=0
    for lett in word:
        array[newCell[0]-i][newCell[1]]=lett
        i=i+1



    newCell=[newCell[0]-newLenNorth+1,18+max(a[0],a[2],b[0],b[2])-1]
    #print(newCell)
    newLenWest = max(a[0],a[2],b[0],b[2])-2
    word = findWordRev(newCell,"west", newLenWest, newLenWest, [newLenWest-1])

    i=0
    for lett in word:
        array[newCell[0]][newCell[1]-i]=lett
        i=i+1


    ## vertical junctions - direct

    newCell = [cell[0]+6,cell[1]+10]
    #print(newCell)




    while array[newCell[0]+1][newCell[1]]==".":
        word = findWord(newCell, "south", (lenJoinWord-7),(lenJoinWord-7),[])
        if word == "no match" or goodStart(newCell, "south")==0:
            newCell=shiftCell(newCell, "east", 1)
        else:
            i=0
            for lett in word:
                array[newCell[0]+i][newCell[1]]=lett
                i=i+1
            newCell=shiftCell(newCell, "east", 2)

def printWord(cell, direct, lenMin, lenMax, goodLett):

    if goodStart(cell,direct)==0:
        return("no match")
    if direct in ('north', 'west'):
        word = findWordRev(cell, direct, lenMin, min(maxLength(cell, direct),lenMax), goodLett)
    else:
        word = findWord(cell, direct, lenMin, min(maxLength(cell, direct),lenMax), goodLett)
    #print(word)
    if word!="no match" and word!=None:
        i = 0
        for lett in word:
            array[shiftCell(cell, direct, i)[0]][shiftCell(cell, direct, i)[1]]=lett
            i=i+1
        if direct in ('west','north'):
            newWord = word[::-1]
        else:
            newWord = word
        for v in range(len(vocabulary)):
            if vocabulary[v]==newWord:
                break
        descr.append(descriptions[v][1:len(descriptions[v])])
        if direct in ("south", "east"):
            crdn=[cell[0]+1,cell[1]+1]
        else:
               crdn=[shiftCell(cell, direct, len(word)-1)[0]+1,shiftCell(cell, direct, len(word)-1)[1]+1]
        coord.append(crdn)
        coordText.append(str(crdn[0])+":"+str(crdn[1]))
        #print(crdn)


        if direct in ("south", "north"):
            directions.append("ver")
        else:
            directions.append("hor")
        return(word)
    else:
        return("no match")



def fillColumnHoriz(cell, direct, rows):
    i=0
    word = printWordWithShift(cell, direct, firstCross(cell, direct)+1,20,[],2)
    while i<=rows:
        if word!="no match":
            cell = shiftCell(cell, "south", 2)
            i+=2
        else:
            cell = shiftCell(cell, "south", 1)
            i+=1
        word = printWordWithShift(cell, direct, firstCross(cell, direct)+1,20,[],2)

def printWordWithShift(cell, direct, lenMin, lenMax, goodLett, shift):
    word = printWord(cell, direct, max(firstCross(cell, direct)+1,lenMin),maxLength(cell,direct)+1,[])
    newCell=cell
    for i in range(1,shift):
        if word == "no match":
            newCell=shiftCell(newCell, direct, -i)
            word = printWord(newCell, direct, max(firstCross(cell, direct)+i+1,lenMin),maxLength(cell,direct)+1,[])
    return(word)

def fillColumn2sides(cell, rows):
    i=0
    direct = "west"
    word = printWord(cell, direct, firstCross(cell, direct)+1,20,[])
    while i<=rows:
        if word!="no match":
            cell = shiftCell(cell, "south", 2)
            i+=2
            if direct == "west":
                direct = "east"
                #print(direct)
            else:
                direct = "west"
        else:
            cell = shiftCell(cell, "south", 1)
            i+=1
        word = printWord(cell, direct, firstCross(cell, direct)+1,20,[])


def fillColumnVert(cell, rows):
    i=0
    word = printWord(cell, "south", firstCross(cell, "south")+1,20,[])
    while i<=rows-4:
        if word!="no match":
            cell = shiftCell(cell, "south", len(word)+1)
            i+=len(word)+1
        else:
            cell = shiftCell(cell, "south", 1)
            i+=1
        word = printWord(cell, "south", firstCross(cell, "south")+1,20,[])
        #print(cell)

def fillVert(cell, height):
    i=0
    startRow = cell[0]
    word = printWordWithCrossN(cell,"south", height+startRow-cell[0]-1,[], 2)
    while cell[0] < startRow + height:
        if word!="no match":
            cell = shiftCell(cell, "south", len(word)+1)
            i+=len(word)+1
        else:
            cell = shiftCell(cell, "south", 1)
            i+=1
        word = printWordWithCrossN(cell,"south", height+startRow-cell[0]-1,[], 2)
        #print(cell)

def printWordWithCrossN(cell,direct, maxLen,goodLett, N):
    if array[cell[0]][cell[1]]==".":
        firstPos = 0
    else:
        firstPos = 1

    if len(crossingAndRestriction(cell, direct, 20)[0])>=N:
        minLen=crossingAndRestriction(cell, direct, 20)[0][N-1-firstPos]
    else:
        minLen = 100
    word = printWord(cell, direct, minLen,maxLen,goodLett)
    return(word)

def fillVert20(cell, height):
    word = printWord(cell, "south", 15,min(height, 20),[])
    restHeight = height - len(word)
    cell = shiftCell(cell, "south", height)
    word = printWord(cell, "north", restHeight,min(restHeight, 20),[])


def fillMiddle(cell, width, height):
    #for i in range(0, width):
        #fillColumnVert(shiftCell(cell,"east",i), height)


    return("")

def firstCross(cell, direct):
    i=1
    while array[shiftCell(cell,direct,i)[0]][shiftCell(cell,direct,i)[1]]=="." and i<(min(30, maxLength(cell,direct))):
        i+=1
    return(i)

def butterfly(iniRow=4, iniCol=4):
    leftWing(iniRow, iniCol)
    #printArray(2,55)
    rightWing(iniRow, iniCol+40)
    #printArray(2,55)

    fillVert20([iniRow, iniCol+18], 30)
    #printArray(2,55)
    fillColumnHoriz([iniRow, iniCol+18], "west", 30)
    #printArray(2,55)
    fillVert20([iniRow, iniCol+22], 30)
    #printArray(2,55)
    fillColumnHoriz([iniRow, iniCol+22], "east", 30)
    #printArray(2,55)
    fillColumnHoriz([iniRow, iniCol+18], "east", 30)
    #printArray(2,55)
    fillColumnHoriz([iniRow, iniCol+22], "west", 30)
    #printArray(2,55)
    fillColumnHoriz([iniRow, iniCol+18], "west", 30)
    #printArray(2,55)
    fillColumnHoriz([iniRow, iniCol+22], "east", 30)
    fillVert([iniRow-1, iniCol+6], 33)
    fillVert([iniRow-1, iniCol+8], 33)
    fillVert([iniRow-1, iniCol+32], 33)
    fillVert([iniRow-1, iniCol+34], 33)
    fillVert([iniRow-1, iniCol+15], 33)
    fillVert([iniRow-1, iniCol+16], 33)
    fillVert([iniRow-1, iniCol+24], 33)
    fillVert([iniRow-1, iniCol+25], 33)
    fillColumnHoriz([iniRow, iniCol+18], "west", 30)
    fillColumnHoriz([iniRow, iniCol+22], "east", 30)
    printArray(2,45)
    printDescr()


def leftWing(iniRow, iniCol):
    cell=[iniRow,iniCol]#10 10
    word = printWord(cell,'east',15,17,[])
    #(2,55)
    lenPrev = len(word)
    cell = shiftCell(cell, "south", 3)#13 10

    for i in range(10):
        iniCell=cell#13 10
        #print(cell)
        word = printWord(cell,'east',15,17,[])
        #(2,55)
        cellEnd = shiftCell(cell, "east", min(len(word),lenPrev))#13 end
        lenPrev = len(word)
        #print(cell)
        gLett = []
        #print(cell)
        cell = shiftCell(cell,'north',4)#9 10
        #print(cell)
        word = printWord(cell,"south",5,6,gLett)
        #2,55)
        #print(cell)
        while word=="no match":
            cell = shiftCell(cell,"east",1)
            word = printWord(cell,"south",5,6,gLett)
        #(2,55)
        cell = shiftCell(cellEnd, "north", 4)#9 end
        #print(cell)

        word = printWord(cell,"south",5,6,gLett)
        while word=="no match":
            cell = shiftCell(cell,"west",1)
            word = printWord(cell,"south",5,6,gLett)

        #(2,55)
        cell = shiftCell(iniCell,'south',3)#16 10
        #print(cell)

def rightWing(iniRow, iniCol):
    cell=[iniRow,iniCol]#10 10
    word = printWord(cell,'west',15,17,[])
    #(2,55)
    lenPrev = len(word)
    cell = shiftCell(cell, "south", 3)#13 10

    for i in range(10):
        iniCell=cell#13 10
        #print(cell)
        word = printWord(cell,'west',15,17,[])
        #(2,55)
        cellEnd = shiftCell(cell, "west", min(len(word),lenPrev))#13 end
        lenPrev = len(word)
        #print(cell)
        gLett = []
        #print(cell)
        cell = shiftCell(cell,'north',4)#9 10
        #print(cell)
        word = printWord(cell,"south",5,6,gLett)
        #(2,55)
        #print(cell)
        while word=="no match":
            cell = shiftCell(cell,"west",1)
            word = printWord(cell,"south",5,6,gLett)
        #(2,55)
        cell = shiftCell(cellEnd, "north", 4)#9 end
        #print(cell)

        word = printWord(cell,"south",5,6,gLett)
        while word=="no match":
            cell = shiftCell(cell,"east",1)
            word = printWord(cell,"south",5,6,gLett)

        #(2,55)
        cell = shiftCell(iniCell,'south',3)#16 10
        #print(cell)




butterfly()
