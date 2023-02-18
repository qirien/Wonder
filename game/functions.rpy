init python:
    def generate_attributes():
        global bestiary, attributes
        for b in bestiary:
            attr = bestiary[b]["attributes"]
            for a in attr:
                attributes[a] = False #need to add "selected" attribute
                #"crazy":{"selected":False}
