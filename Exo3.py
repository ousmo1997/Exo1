n1=int(input("Saisir la 1ère note: "))
n2=int(input("Saisir la 2ème note: "))
n3=int(input("Saisir la 3ème note: "))
moy=(n1+n2+n3)/3
if moy>16:
    print(moy," Trèb bien")
elif moy>14:
    print(moy," Bien")
elif moy>12:
    print(moy," Assez bien")
elif moy>10:
    print(moy," Passable")
else:
    print(moy, " Insuffisant")