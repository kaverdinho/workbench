# reinforced glass window
def reinforcedglasswindow(a):
    cost = 125
    #print("Reinforced Glass Window = " + str(cost) + " Scrap")
    return cost + a

# Armored door
def armoreddoor(a):
    cost = 500
    #print("Armored Door = " + str(cost) + " Scrap")
    return reinforcedglasswindow(a + cost)

# armored double door
def armoreddoubledoor():
    cost = 500
    #print("Armored Double Door = " + str(cost) + " Scrap")
    return armoreddoor(cost)

# mp5a4
def mp5a4(a):
    cost = 125
    #print("Mp5a4 = " + str(cost) + " Scrap")
    return reinforcedglasswindow(a + cost)

# weapon lasersight
def weaponlasersight(a):
    cost = 125
    #print("Weapon Lasersight = " + str(cost) + " Scrap")
    return mp5a4(a + cost)

# hv rifle ammo
def hvrifleammo(a):
    cost = 125
    #print("HV 5.56 Rifle Ammo = " + str(cost) + " Scrap")
    return weaponlasersight(a + cost)

# explosive riffle ammo
def explosiverifleammo(a):
    cost = 125
    #print("Explosive Riffle Ammo = " + str(cost) + " Scrap")
    return hvrifleammo(a + cost)

# explosives
def explosives(a):
    cost = 500
    #print("Explosives = " + str(cost) + " Scrap")
    return explosiverifleammo(a + cost)

# timed explosive charge
def timedexplosivecharge(a):
    cost = 500
    #print("Timed Explosive Charge = " + str(cost) + " Scrap")
    return explosives(a + cost)

# rocket
def rocket():
    cost = 500
    #print("Rocket = " + str(cost) + " Scrap")
    return timedexplosivecharge(cost)

# metal chest plate
def metalchestplate(a):
    cost = 500
    #print("Metal Chest Plate = " + str(cost) + " Scrap")
    return explosiverifleammo(a + cost)

# metal facemask
def metalfacemask(a):
    cost = 500
    #print("Metal Facemask = " + str(cost) + " Scrap")
    return explosiverifleammo(a + cost)

# assault rifle
def assaultrifle(a):
    cost = 500
    #print("Assault Rifle = " + str(cost) + " Scrap")
    return metalchestplate(a + cost)

# bolt action rifle
def boltactionrifle(a):
    cost = 500
    #print("Bolt Action Rifle = " + str(cost) + " Scrap")
    return assaultrifle(a + cost)

# eightx zoom scope
def eightxzoomscope():
    cost = 125
    #print("8x Scope = " + str(cost) + " Scrap")
    return boltactionrifle(cost)






