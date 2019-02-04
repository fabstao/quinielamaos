# ***********************
# (C) 2019 Fabs
# Quiniela Maos
# ***********************
import math
import operator

prams=17
ppats=16

pats={'rulo': 30,'r2': 24,'robert': 38,'elin': 27,'ahumada': 35,'fer': 27,'fabs': 38}
rams={'rulo': 27,'r2': 21,'robert': 45,'elin': 30,'ahumada': 28,'fer': 35,'fabs': 40}
diff={'rulo': 0,'r2': 0,'robert': 0,'elin': 0,'ahumada': 0,'fer': 0,'fabs': 0}

print("Quiniela Maos")
print()
print("Marcador real")
print("Rams: ",prams,", Pats: ",ppats)
print()

ggana="rams"
for llave in rams:
   if pats[llave] > rams[llave]:
      ggana="pats"
   print(llave+": dice que gana "+ggana+", puntos Rams: ",rams[llave]," , Pats: ",pats[llave])
   diff[llave]=math.fabs(prams-rams[llave])+math.fabs(ppats-pats[llave])

print()
print(diff)
print()
print("Ganador:")
print(min(diff.items(), key=operator.itemgetter(1))[0])
print()

