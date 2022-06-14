from ast import Return


def checkInfoClass(instance):
    ID = instance.ID[0:2]
    if ID == '10' or ID == '11' or ID == '12' : 
        return True
    return False
