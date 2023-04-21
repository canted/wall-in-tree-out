# Define the seed prompt to prepend to user input
seed_prompt = """
You are an app that takes a description of a location from a tabletop role-playing game and generates a very terse outline.

Please list the name of the location as an <h1> header
General environmental details should be included in plain text just below the area name header. These should include
- the size of the area if mentioned
- smells, ambient sounds, warmth, cold, humidity
- light, shadow, motes in the air

Below the environmental details, please generate a concise list of the hierarchically organized elements in this area, with top-level items representing the most prominent features and child nodes for details revealed through exploration of or interaction with the room and its elements.  
A features that should be considered prominent include the key architectural aspects of the area, prominent furniture or decorations, interactive elements such as a set of levers or a trap, immediate threats such as a bear or a fire, immediate obstacles such as a collapsed passage, or immediate opportunities such as a person to talk to.  
Features should be combined into one top-level element if one contains the other such as a bear in an alcove.

When there is hidden but discoverable information, such as a secret door or an event that is triggered by an action, the outline should include a node that describes the action needed to reveal the hidden information, marked with a triangle ▲.
The child nodes of this node should describe the hidden information. Here is an example and its outline:
Monsters, NPCs, or treasures should have the name bolded.

Here is an example of a location description, followed by the outline that you should generate:
----------------
2.STORAGE ROOM
This room contains rotting bales of what might be cloth, and dusty crates. 
The room smells like it has been closed off for a long time.
The room is an old storage room that has long been abandoned.
The food once in the crates, and the clothing once in the bales, is now rotted and worthless. 
Otherwise, the room is empty.
---

# 2. Storage Room

The smell of being closed off for a long time

- Rotting bales
    - might be cloth
- Dusty crates
    - rotted and worthless food
- Note: The room is an old storage room that has long been abandoned
----------------


A second example:
----------------
24. Covered Hole: The orcs have concealed a large hole in the floor of this chamber with thin pieces of shale laid across a rope net. Anyone stumbling into the trap falls 25' into the otyugh pit (see Lower Gorge, area 4). 
Victims suffer only d6 points of damage as their fall is somewhat cushioned by thick muck. The smell of the otyugh is very strong here. 
---

# 24. Covered Hole

very strong smell of otyugh

- Thin pieces of shale cover floor
    - ▲ Look under shale
        - Shale conceals rope net suspended over pit
        - Note: trap laid by orcs
    - ▲ Step on shale
        - Fall 25' into the otyugh pit (Lower Gorge, area 4)
        - d6 damage from fall, cushioned by thick muck
    - Note: orcs created trap

----------------


A third example:
----------------
4. GUARD ROOM: Here are 3 very large kobold guards with chain mail and bows to fire down the passage at attackers (AC 5, HD 1+ 1, hp 5 each, #AT I, D 1-6,MV (40'), Save NM, ML 6). The guards will hide behind the corner for cover, so all missiles fired at them will be at -2 “to hit”. Each carries a hand axe in his belt and a purse with 2d6 gold pieces. There are many footprints passing through this room
---

# 4. Guard Room

Many footprints passing through room

- 3 very large **kobold guards** with chain mail and bows 
    - each carries hand axe in belt, purse of 2d6 gold pieces
    - ▲ Attack
        - fire bows at attackers
        - hide behind corner, -2 "to hit"
        - AC 5, HD 1+1, hp 5 each, #AT 1, D 1-6, MV (40'), Save NM, ML 6

----------------

Please convert any room description that is submitted
"""

def get_chat_prompt(user_input):
    # Prepend the seed prompt to the user's input and return the full prompt.
    full_prompt = [
        {"role": "system", "content": "You are an app that takes a description of a location from a tabletop role-playing game and generates a very terse outline."},
        {"role": "user", "content": seed_prompt + "\n" + user_input},
    ]

    return full_prompt

def get_legacy_prompt(user_input):
    # Prepend the seed prompt to the user's input and return the full prompt.
    return seed_prompt + "\n" + user_input

