def welches_pissoir(pissoir):
    if pissoir.count(1) == 0:
        print("Gehe in die Ecke...")
    if pissoir.count(1) == 1:
        if pissoir.index(1) < pissoir.length() / 2:
            print("Gehe in rechte Ecke...")
        else:
            print("Gehe in linke Ecke...")

pissoir1 = [0, 0, 0, 0, 0]
welches_pissoir(pissoir1)

#var1 = 0
#grSlot = 0
#grSlots = {}
#for i in list:
#   if i == 0:
#       var1 += 1
#   elif i == 1:
#       if var1 > grSlot
    #       grSlot = var1
    #       grSlots[i-1] = var1
    #       var1 = 0
    #   elif var1 == grSlot
