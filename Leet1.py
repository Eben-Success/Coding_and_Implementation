voted = {}
def check_voter(name):
    if voted.get(name):
        print("Kick them out")
    else:
        voted[name] = True
        print("Let them vote!")
        
        
check_voter('ebenezer')
check_voter('ebenezer')
        
        
        
        
        