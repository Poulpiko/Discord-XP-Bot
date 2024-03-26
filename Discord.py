from operator import itemgetter
import re

if __name__ == "__main__":

  llist = []
  sepX = ' XP: '
  sep = '@'

  with open('./TOP.txt') as f:
    lines = f.readlines()
  
  with open('./FINAL.txt') as f:
    flines = f.readlines()

  for l in lines:
    flag = False
    x = ['x','x']
    if l.startswith("#") and "!209830507179933696>" not in l and "!192300665173704704>" not in l and "Poulpiko" not in l:# and "GoultarChief Le SalÃ©" not in l and "DADDY CHOKE" not in l and "Goultardos" not in l :
      x[0] = l.split(sepX,1)[0]
      x[0] = x[0].split(sep,1)[1]
  
      x[1] = l.split(sepX,1)[1]
      x[1] = int(x[1][:len(x[1]) - 1])

      for i in range(len(llist)):
        if x[0] in llist[i][0]:
          llist[i][1] += x[1]
          flag = True
      
      if not flag:
        llist.append(x)

  llist.append(['Poulpiko',801057])
      

  llist.sort(key=itemgetter(1),reverse=True)

  roi = llist[0]
  gduc = llist[1]
  ducs = llist[2:5]
  comte = llist[5]
  vicomtes = llist[6:11]
  banneret = llist[11]
  barons = llist[12:27]

  final = ""

  # for i in royaute:
  #   final += "ROYAUTE:\t\t" + str(i[1]) +" - "+i[0]+ "\n"
  # final += "\n"

  final += "ROI:\t\t"+str(roi[1])+" - "+roi[0]+"\n\n\n"

  final += "GRAND DUC:\t"+str(gduc[1])+" - "+gduc[0]+"\n\n"

  for i in ducs:
    final += "DUCS:\t\t" + str(i[1]) +" - "+i[0]+ "\n"
  final += "\n\n"

  final += "COMTE:\t\t"+str(comte[1])+" - "+comte[0]+"\n\n"

  for i in vicomtes:
    final += "VICOMTES:\t" + str(i[1]) +" - "+i[0]+ "\n"
  final += "\n\n"

  final += "BANNERET:\t"+str(banneret[1])+" - "+banneret[0]+"\n\n"

  for i in barons:
    final += "BARONS:\t\t" + str(i[1]) +" - "+i[0]+ "\n"

  print(final)
  print("\n-------------------\n")

  # plines = final.splitlines()

  # fchar = ["\n", " ", "\t"]

  # pnotes = []
  # fnotes = []

  # for i in range(len(plines)):
  #   plines[i] = re.sub(r"[^ -~]", "", plines[i])
  #   flines[i] = re.sub(r"[^ -~]", "", flines[i])

  #   for c in fchar:
  #     plines[i] = plines[i].replace(c,"")
  #     flines[i] = flines[i].replace(c,"")

  #   if plines[i] != "":

  #     pnote = ['x','x','x']
  #     fnote = ['x','x','x']

  #     pnote[0] = plines[i].split(':',1)[0]
  #     pnote[1] = plines[i].split('-',1)[1]
  #     pnote[2] = int(plines[i].split('-',1)[0].split(':',1)[1])

  #     fnote[0] = flines[i].split(':',1)[0]
  #     fnote[1] = flines[i].split('-',1)[1]
  #     fnote[2] = int(flines[i].split('-',1)[0].split(':',1)[1])
      
  #     pnotes.append(pnote)
  #     fnotes.append(fnote)

  # pnotes.sort(key=itemgetter(2))
  # fnotes.sort(key=itemgetter(2))

  # tmpp = []
  # tmpf = []

  # for i in range(len(pnotes)):
  #   tmpp.append(pnotes[i][1])
  #   tmpf.append(fnotes[i][1])

  # pdiff = list(set(tmpp) - set(tmpf))
  # fdiff = list(set(tmpf) - set(tmpp))

  # # for i in range(len(pnotes)):
  # #   if str(pnotes[i]) != str(fnotes[i]):
  # #     if pnotes[i][1] in pdiff:
  # #       print(up.format("@"+pnotes[i][1], "un Bourgeois"))
  # #     if fnotes[i][1] in fdiff:
  # #       print(down.format("@"+fnotes[i][1], "un Gueux"))
  # #     if pnotes[i][0] == "LEDUC" and (fnotes[i][0] == "NOBLES" or fnotes[i][0] == "BOURGEOIS" or fnotes[i][0] == "x"):
  # #       print(up.format("@"+pnotes[i][1], "le Duc"))
  # #     if pnotes[i][0] == "NOBLES" and (fnotes[i][0] == "BOURGEOIS" or fnotes[i][0] == "x"):
  # #       print(up.format("@"+pnotes[i][1], "un Noble"))
  # #     if pnotes[i][0] == "NOBLES" and (fnotes[i][0] == "LEDUC"):
  # #       print(down.format("@"+pnotes[i][1], "un Noble"))
  # #     if pnotes[i][0] == "BOURGEOIS" and (fnotes[i][0] == "x"):
  # #       print(up.format("@"+pnotes[i][1], "un Bourgeois"))
  # #     if pnotes[i][0] == "BOURGEOIS" and (fnotes[i][0] == "LEDUC" or fnotes[i][0] == "NOBLES"):
  # #       print(down.format("@"+pnotes[i][1], "un Bourgeois"))

  # with open('G:/Mon Drive/Codes/Autres/Discord Bot/FINAL.txt', 'w') as f:
  #   f.write(final)