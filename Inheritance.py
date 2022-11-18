#My Hero Academia
#One for all quirk users

class Yoichi(object):#Founder of one for all
    def __init__(self, stockpiling):#quirk
        self.stockpiling = stockpiling

    def getStockpiling(self):
        return self.stockpiling
 
class Scar(Yoichi):
 
    def __init__(self, stockpiling, bind):
        Yoichi.__init__(self, stockpiling)
        self.bind = bind
        
    def getBind(self):
        return self.bind
 
class Sidekick(Scar):
 
    def __init__(self, stockpiling, bind, fajin):
        Sidekick.__init__(self, stockpiling, bind)
        self.fajin = fajin
        
    def getFajin(self):
        return self.fajin

class Hikage(Sidekick):
 
    def __init__(self, stockpiling, bind, fajin, danger_sense):
        Hikage.__init__(self, stockpiling, bind, fajin)
        self.danger_sense = danger_sense
        
    def getDanger_sense(self):
        return self.danger_sense
        
class Lariat(Hikage):
 
    def __init__(self, stockpiling, bind, fajin, danger_sense,
                 blackwhip):
        Lariat.__init__(self, stockpiling, bind, fajin, danger_sense)
        self.blackwhip = blackwhip
        
    def getBlackwhip(self):
        return self.blackwhip

class En(Lariat):
 
    def __init__(self, stockpiling, bind, fajin, danger_sense,
                 blackwhip, smokescreen):
        En.__init__(self, stockpiling, bind, fajin, danger_sense, 
                         blackwhip)
        self.smokescreen = smokescreen
        
    def getSmokescreen(self):
        return self.smokescreen
        
class Nana(En):
 
    def __init__(self, stockpiling, bind, fajin, danger_sense,
                 blackwhip, smokescreen, levitate):
        Nana.__init__(self, stockpiling, bind, fajin, danger_sense, 
                         blackwhip, smokescreen)
        self.levitate = levitate
        
    def getLevitate(self):
        return self.levitate
        
class AllMight(Nana):
 
    def __init__(self, stockpiling, bind, fajin, danger_sense,
                 blackwhip, smokescreen, levitate, smash):
        AllMight.__init__(self, stockpiling, bind, fajin, danger_sense, 
                         blackwhip, smokescreen, levitate)
        self.smash = smash
        
    def getSmash(self):
        return self.smash 
        
class Deku(AllMight):#current one for all holder
 
    def __init__(self, stockpiling, bind, fajin, danger_sense,
                 blackwhip, smokescreen, levitate, smash, multi):#quirkless
        Deku.__init__(self, stockpiling, bind, fajin, danger_sense, 
                         blackwhip, smokescreen, levitate, smash)
        self.multi = multi
        
    def getMulti(self):
        return self.multi             
        
        
      
    #currently can use quirks   
d = Deku("DangerSense", "FaJin", "Smokescreen", "Levitate", "Blackwhip")
print(d.getDanger_sense(), d.getFajin(), d.getSmokescreen, d.getLevitate, d.getBlackwhip())

