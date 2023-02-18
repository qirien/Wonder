label chapter1:
    scene city-night
    "It's been a long time since my last case."
    "Had to take some side gigs -- delivery jobs, tutoring, that sort of thing."
    "So it feels good to be on a real mystery again."

    "Not so sure about the client, but at least I know he can pay..."

    scene mansion
    show q with dissolve
    q "You understand that your quarry is arcane, elusive, and unconventional?"
    you "That's why you're hiring me, isn't it?"
    q "Yes... and you say you're fully human? No nixie ancestors on your mother's side or kitsune possession or anything?"
    you "No."
    q "Interesting... Would you mind demonstrating your abilities for me? I believe you, of course, I'm just immensely curious how they work."
    you "..."
    "I didn't want to use it like that, like some cheap magic trick. But he was paying me an awful lot of money, and he had a good point. Powers like mine were rare, and in humans, practically nonexistent."
    #show light-ball or something
    "I opened my senses to the otherworldly... and a cacophony of scents rushed in. His scent was charcoal and vellum, but coming from the open window were the smells of hyacinth and pine."
    "The room itself exuded the scents of Wonder, a rich, earthy smell like fresh dirt and cinnamon."
    q "Hmmm, yes! I can feel the Wonder flowing through you with even this small demonstration. Fascinating."
    #hide light-ball
    q "I apologize; that was quite rude of me to ask this of you."
    you "You want to make sure you get what you're paying for."
    q "You have a unique gift; I look forward to your quick resolution to this matter."

    scene city-night
    "I'm looking for a murderer."
    "Not just any murderer; a fae murderer."
    "I need capture them alive and bring them back to Q."
    "My friend J works at the library and can help if I need to do any research. I should also check out the crime scene and question anyone who might have seen something."

label investigation_loop:
    scene city-night
    menu:
        "Where should I go next?"
        "Library":
            jump library
        "Crime Scene":
            jump crimescene1
        "Morgue":
            jump morgue
        "Q's Mansion":
            jump mansion
        "Fight the [selected_creature]" if (selected_creature != ""):
            jump fight

    return

label library:
    scene library
    show j
    if (ch1.met_j):
        j "Hello again!"
    else:
        j "Welcome! Oh, it's you. I didn't know you were in town."
        you "Just started a new case."
        j "Ooh, is it about that poor girl that was murdered last week?"
        you "Yeah, you heard about it?"
        j "Oh yes, nasty business. Strange, too -- the fae have never bothered anyone here before."
        you "Are there a lot of fae here?"
        j "I mean, how would we know? They're so good at hiding... but I do get a few coming in for books every once in a while."
        you "Interesting."
        $ ch1.met_j = True

    j "Here to look something up?"
    #clue notebook bestiary screen
    menu ch1_library:
        "Bestiary":
            call screen bestiary(ch1.clues)
        "Leave":
            jump investigation_loop
    jump ch1_library

label crimescene1:
    scene park
    if (not ch1.met_crimescene):
        "I ducked under the flimsy tape barrier to look at where the murder took place."
    $ ch1.met_crimescene = True

    # TODO: Have better graphics where you click on what you want to examine
    menu ch1_crimescene:
        "What should I examine?"
        "Riverbank":
            "Footprints seemed to come out of the water, lead to a dark stain, and then return to the water."
            $ ch1.clues["Water"]["found"] = True
        "Footprints" if ch1.clues["Water"]["found"]:
            "The footprints looked human but small and light, almost like a child."
            $ ch1.clues["Footprints"]["found"] = True
        "Dark stain" if ch1.clues["Water"]["found"]:
            "The dark stain seemed like blood. Looking closer, I could see smaller stains of a different color nearby."
            "Opening my senses to the fae realm, I could sense two separate auras emitting from these stains."
            if (ch1.clues["Body"]["found"]):
                "The large, dark one smelled mundane and matched the victim I had seen earlier."
            else:
                "The large, dark one smelled mundane."
            "The smaller stains smelled frightened, desperate, and crazed. They dripped with the scent of fae."
        "Leave":
            jump investigation_loop
    jump ch1_crimescene

label morgue:
    scene morgue
    if (not ch1.met_morgue):
        "I expected them to be suspicious, but as soon as I mentioned Q's name they nodded. I was expected."
        "They took me back to where the body lay. It was pale and bloated and grotesque from its time underwater."
    $ ch1.met_morgue = True
    menu ch1_morgue:
        "What should I examine?"
        "Smell":
            "I didn't really want to smell the body, but I had to in order to learn more."
            "I tried to smell past the decaying body stench and into the realm of the fae. However, this body was mundane and had no otherworldly smell."
            $ ch1.clues["Body"]["found"] = True
        "Throat":
            "While the body was bloated with water, it appeared that the victim died before sinking in the river."
        "Abdomen":
            "The skin was perforated multiple times around the chest with something small and sharp. Looked like someone was aiming for the heart but wasn't sure exactly where it was."
            $ ch1.clues["Wound"]["found"] = True
        "Feet":
            "There was no mud under the toenails. The report says she was found with shoes on."
        "Leave":
            jump investigation_loop
    jump ch1_morgue

label mansion:
    scene mansion
    show q
    q "Finished already?"
    if (ch1.victory):
        you "Yes, I've brought the guilty fae."
        q "Excellent. I knew my trust in you was warranted."
    else:
        if (selected_creature != ""):
            you "No, but I think it's a [selected_creature]."
            q "Really? Well, I wish you the best of luck bringing it in. Alive, remember."
            you "I'm on it."
        else:
            you "Not yet..."
        q "I expect to see you soon."
        jump investigation_loop

    return

label fight:
    scene park
    "Now that I knew what it was, I could make use of its weaknesses..."
    menu fight_loop:
        "What should I do?"
        "Lure it with music.":
            "I really hoped no one was listening."
            "Taking a deep breath, I sang, quietly at first, then louder as nothing happened."
            "I sang of the sea, of empty seashells and rushing water and silvery fish."
            "Nothing happened."
            jump fight_loop
        "Lure it with food.":
            "I placed some tantalizing treats on the ground near the river."
            "I waited a long time..."
            jump fight_loop
        "Lure it with loneliness.":
            "I looked around. Good, I was alone."
            "I sat and pondered my solitude."
            you "A friend would sure be nice. Or, maybe even an acquaintance. I'd settle for J or Q even."
            you "But no, I'm alone... not just right now, but all the time..."
            "I heard water dripping but made sure not to turn around."
            you "Surely no one has been as lonely as I am right now."
            "The kelpie was getting closer."
            "Zap! I managed to stun it with the MacGuffin I acquired earlier."
            $ ch1.victory = True
    jump mansion
