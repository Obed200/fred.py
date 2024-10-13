
class player:
    formerTeams=[]
    teamName='liverpool'
    def __init__(self,name):
        self.name=name
        
p1=player('mark')
p2=player('steve')

p1=player('mark')
p1.formerTeams.append('barcelona')
p2=player('steve')
p2.formerTeams.append('chelsea')

print('name: ', p1.name)
print('Team name: ',p1.teamName)
print(p1.formerTeams)

print('name: ', p2.name)
print('Team name: ',p2.teamName)
print(p2.formerTeams)

print('   -----transfer------   ')

class player:
    teamName='leverpool'
    def __init__(self,name):
        self.name=name
        self.formerTeams=[]
        
p1=player('mark')
p2=player('steve')

p1=player('mark')
p1.formerTeams.append('barcelona')
p2=player('steve')
p2.formerTeams.append('chelsea')

print('name: ', p1.name)
print('Team name: ',p1.teamName)
print(p1.formerTeams)

print('name: ', p2.name)
print('Team name: ',p2.teamName)
print(p2.formerTeams)
