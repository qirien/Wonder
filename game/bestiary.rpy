screen bestiary(clues):
    frame:
        xfill True
        yfill True
        vbox:
            hbox:
                # Clues on the left
                vbox:
                    style_prefix "check"
                    for n in clues:
                        if clues[n]["found"]:
                            textbutton n tooltip clues[n]["description"] action ToggleDict(clues[n],"selected")

                # Attributes in the middle
                vbox:
                    style_prefix "check"
                    for m in attributes:
                        textbutton m action ToggleDict(attributes,m)

                # Monsters on the right
                vbox:
                    style_prefix "radio"
                    for k in bestiary:
                        if bestiary[k]["unlocked"]:
                            textbutton k:
                                sensitive matches_attributes(k)
                                selected (k==selected_creature)
                                action SelectCreature(k)
                                tooltip bestiary[k]["description"]

            $ tooltip = GetTooltip()
            if tooltip:
                text tooltip

            textbutton "Return" xalign 1.0 yalign 1.0 action Return()



init python:
    # Does this creature match all the selected attributes?
    def matches_attributes(creature):
        global bestiary, attributes
        for m in attributes:
            if attributes[m]:
                if m not in bestiary[creature]["attributes"]:
                    return False
        return True


    def select_creature(creature):
        global selected_creature
        selected_creature = creature
        return
    SelectCreature = renpy.curry(select_creature)
