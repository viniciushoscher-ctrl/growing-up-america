import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 74 · ANGLE TEST: kindness story (poor woman shelters strangers in a storm, the next day they come back)
# Model from the 10/11 research: "A Poor Old Grandma Sheltered 13 Freezing Bikers" (636k, 15 min).
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Christmas Eve, nineteen fifty-eight. A blizzard was burying Mansfield, Ohio. My father was snowed in at the plant, the power was out, and we had one stove, one pot of soup, and nine dollars until payday. And at ten o'clock that night, somebody pounded on our front door so hard the whole house shook. I was fourteen years old, and I have never been so scared in my life.""",
   "blizzard night small house window light", "CHRISTMAS EVE, 1958")
sc("""When my mother opened that door, there were twelve men standing in the snow, in black leather jackets, with motorcycles half buried in the drifts behind them. Tonight I'm going to tell you what my mother did, what the whole street said about her, and what happened the next morning, which nobody on Elm Street ever forgot. Stay with me, sweetheart, because the ending still makes me cry.""",
   "motorcycles buried in snow at night", "TWELVE MEN AT THE DOOR")

ch("The storm")
sc("""That winter was a hard one for us, honey. The plant had cut my father's hours in the fall, and my mother was taking in ironing to pay the coal man. There were no presents under our little tree that year except two oranges and a pair of mittens she had knitted from an old sweater. Danny and I knew not to ask for anything.""",
   "1950s poor family small Christmas tree", "NINE DOLLARS")
sc("""The storm started in the afternoon. By supper, the snow was up to the porch rail, and the wind was screaming down Elm Street like a freight train. The lights went out at seven. My mother lit the kerosene lamp, put the last of the potatoes and an onion in a pot of soup, and told us to put on every sweater we owned.""",
   "kerosene lamp kitchen 1950s night", "THE LIGHTS WENT OUT")
sc("""At ten o'clock, we were all three sitting by the stove in blankets, when we heard engines. Loud ones. A whole row of them, coughing and dying in the snow out on the street. Then voices, men shouting to each other. Then boots on our porch. Then that pounding. My mother put her finger to her lips, and she picked up the fireplace poker.""",
   "boots on snowy porch at night", "BOOTS ON THE PORCH")

ch("The door")
sc("""She opened the door about four inches, with the chain on. A huge man stood there, with a red beard full of ice and a face burned raw by the wind. He took off his hat, which surprised her, and he said, ma'am, I'm sorry to scare you. Our bikes froze up. We've got two boys out here who can't feel their hands. Can we just stand in your hallway for an hour?""",
   "bearded biker in snow at door night", "CAN WE JUST STAND HERE?")
sc("""Now, sweetheart, you have to understand what bikers meant in nineteen fifty-eight. There'd been stories in all the papers. Gangs. Fights. Towns torn up. Our neighbor, Mrs. Hadley, was watching from her window across the street, and I saw her curtain twitch, and I saw her light a candle and pull that curtain shut tight. Every other house on the street went dark.""",
   "neighbor closing curtain at night", "EVERY HOUSE WENT DARK")
sc("""My mother looked at that man for a long time. Then she looked past him, at a skinny boy in the snow, maybe eighteen, shaking so hard his teeth were clicking. In a minute I'll tell you what she said to me afterward about that boy. But right then, she took the chain off the door, and she said, take your boots off. All of you. And wipe your feet.""",
   "young man shivering in snow", "TAKE YOUR BOOTS OFF")

ch("Twelve strangers")
sc("""Twelve grown men came into our little front room, honey, one by one, stomping and dripping and apologizing. They filled every inch. I stood in the kitchen door with my heart pounding, and I watched my mother, five foot two, hand a towel to each one of them like they were boys come in from sledding.""",
   "crowded small living room 1950s lamplight", "TWELVE GROWN MEN")
sc("""The two youngest couldn't feel their fingers. My mother sat them by the stove and put their hands in a pan of warm water, never hot, because Grandma Pearl had taught her that hot water on frozen hands does terrible damage. The big man with the red beard watched her, and he didn't say a word.""",
   "hands in pan of water by stove", "WARM WATER, NEVER HOT")
sc("""Then she went into the kitchen, and I followed her. She looked at that one pot of potato soup, meant to last us three days. She looked at me. And she said, Ruthie, get every bowl and every cup in this house. And she put in more water, and the last of the onions, and a whole box of crackers, and she said, it'll stretch. It always stretches.""",
   "pot of potato soup on old stove", "IT ALWAYS STRETCHES")

ch("The soup")
sc("""If you're enjoying this story, sweetheart, tap the like button for me. It helps more people find Grandma's stories. Twelve men ate that thin potato soup out of coffee cups and jelly glasses and Danny's cereal bowl. Nobody said it was thin. The red-bearded man washed his cup at our sink and dried it.""",
   "men eating soup from cups lamplight", "NOBODY SAID IT WAS THIN")
sc("""His name was Frank. He told my mother they were a club from Pittsburgh, riding to a funeral in Indiana. One of their members had been killed in a factory accident, and they'd promised his widow they'd be there. They knew the storm was coming. They rode anyway. My mother asked him why, and he said, because we told her we would, ma'am.""",
   "biker club riding on winter highway", "BECAUSE WE PROMISED")
sc("""Then Frank noticed our tree, honey. The little bare tree with two oranges under it. He looked at it for a long time, and then he looked at my mother's hands, red and cracked from the ironing, and at the stack of other people's shirts folded on the table. He didn't say anything. But I saw his face change, and I didn't understand why until the next morning.""",
   "small bare Christmas tree two oranges", "TWO ORANGES")

ch("The longest night")
sc("""That night, twelve men slept on our floor, on our couch, in the hallway, and one on the kitchen table. My mother kept the stove going until three in the morning, feeding it the last of our coal, and then the kindling, and then two old chairs from the cellar. I heard her, sweetheart. I heard her breaking up those chairs so those boys wouldn't freeze.""",
   "men sleeping on floor by stove night", "SHE BROKE UP THE CHAIRS")
sc("""Around midnight, I came downstairs for water, and the skinny boy was awake by the stove. His name was Eddie. He was eighteen, and he had run away from a bad home in West Virginia two years before. He told me he hadn't had a Christmas Eve inside a house since he was eleven. Then he asked me, is your mama always like this? And I said, yes. She is.""",
   "teenage boy awake by stove at night", "IS SHE ALWAYS LIKE THIS?")
sc("""And here's what my mother told me later about Eddie, the thing I promised you. She said, Ruthie, when I opened that door, I didn't see twelve bikers. I saw one shaking boy who was somebody's son. And I thought, if Danny was ever out in the snow, I'd pray to God some woman would open her door. That's all it was. One boy.""",
   "mother and daughter talking kitchen 1950s", "ONE SHAKING BOY")

ch("Christmas morning")
sc("""In the morning, the storm was over, and the sun came up on three feet of snow. My mother woke up, and the house was quiet. The men were gone. Their blankets were folded in a neat stack by the door, every single one. The floor was swept. The cups were washed and lined up on the counter. And there was a note on the kitchen table, held down with my mother's own salt shaker.""",
   "folded blankets stack by door morning", "THE MEN WERE GONE")
sc("""The note said, thank you, Mrs. Dorothy. You didn't have to, and you did. We won't forget it. Frank. That was all. My mother read it twice, and then she put it in her apron pocket, and she said, well. And she said, that's that, children. Merry Christmas. Nobody even mentioned that the coal was gone.""",
   "handwritten note on kitchen table", "WE WON'T FORGET IT")
sc("""By nine o'clock, the whole street knew. Mrs. Hadley was out on her porch in her housecoat telling everybody that Dorothy had let a gang into her house with two children inside. She said it right where we could hear it. She said, mark my words, they cased that house. They'll be back. And she was right, honey. They came back. But not the way she thought.""",
   "gossiping neighbor on snowy porch", "THEY'LL BE BACK")

ch("The next day")
sc("""At two o'clock on Christmas afternoon, Danny was at the window, and he yelled, Mom! Mom, they're back! And we heard it. Engines. Not twelve this time. It sounded like a hundred. My mother went white as the snow. She told us to get upstairs. And then she went to the front door, alone, and she opened it, and she just stood there with her hand over her mouth.""",
   "row of motorcycles on snowy street", "THEY CAME BACK")
sc("""Coming down Elm Street were Frank's twelve, and behind them a coal truck, and behind that, a pickup truck from the Pittsburgh club piled so high with boxes it was swaying. And behind that, more motorcycles, from a club in Columbus that Frank had called from a gas station that morning. Every single house on Elm Street had its curtains open now, honey. Every single one.""",
   "coal truck and pickup on snowy street 1950s", "EVERY CURTAIN OPEN")
sc("""The coal truck backed up to our cellar window and poured in a full ton of coal. A whole winter. The boxes came off the pickup one by one. A ham. A turkey. Flour, sugar, coffee, canned peaches. A sled for Danny. A pair of real store-bought ice skates for me. And a long flat box for my mother, wrapped in newspaper, which she didn't open until everybody was gone.""",
   "boxes of groceries and sled on porch", "A WHOLE TON OF COAL")
sc("""Eddie, the skinny boy, came up the steps last. He was carrying two new kitchen chairs, one on each shoulder. He set them down in our kitchen, right where the old ones had been, and he said, Mrs. Dorothy, I heard you in the night. Then he hugged her, and that tough little runaway cried like a baby on my mother's shoulder. And so did she.""",
   "young man carrying kitchen chairs", "I HEARD YOU")

ch("The neighbor")
sc("""So far, the storm, the soup, the chairs, and the coal. But there's one more thing, and it's the part people never believe. While the men were unloading, Mrs. Hadley came across the street, in her good coat now, smiling, and she said, well, isn't this lovely, Dorothy, I always said those boys looked decent. Frank turned around and looked at her for a long, long time.""",
   "woman in good coat smiling on snowy street", "I ALWAYS SAID...")
sc("""And Frank said, ma'am, we knocked on your door first. Last night. You looked right at us through the glass and you turned off your light. Mrs. Hadley's face went red as a beet, honey. She turned around and walked back across that street without a word, and she didn't speak to my mother for a year. My mother never said one unkind thing about her. Not once.""",
   "embarrassed woman walking away snow", "WE KNOCKED FIRST")

ch("The box")
sc("""That night, after the house was quiet and warm for the first time in weeks, my mother opened the long flat box. Inside was a winter coat. A real wool coat, deep red, with a fur collar, from the best department store in Pittsburgh. She'd been wearing my father's old work jacket all winter, and Frank had noticed. In the pocket was an envelope with two hundred dollars and a second note.""",
   "red wool coat in gift box", "A REAL WOOL COAT")
sc("""The second note said, for the lady who opened her door. Merry Christmas. Two hundred dollars, sweetheart, in nineteen fifty-eight. That was more than two months of my father's pay. My mother sat at the kitchen table, in her new red coat, holding that note, and she cried until my father finally made it home from the plant at midnight and found her there.""",
   "woman crying at kitchen table red coat", "MORE THAN TWO MONTHS' PAY")

ch("What happened after")
sc("""And it didn't end there, honey. Every Christmas Eve for the next thirty-one years, a card came from Pittsburgh, signed by Frank and whoever was left of the twelve. And every few years, the engines would come down Elm Street again, and Frank would sit at our kitchen table, a little grayer every time, and eat my mother's potato soup. The real kind, thick. He always said it wasn't as good as the thin kind.""",
   "Christmas cards stack old letters", "THIRTY-ONE YEARS OF CARDS")
sc("""When my mother passed, in nineteen eighty-nine, there were thirty-four motorcycles at her funeral. And at the front, in a suit that didn't fit him, was Eddie, the skinny runaway, who was by then a grandfather himself and a deacon in his church in West Virginia. He told the whole room about the night she broke up her chairs.""",
   "motorcycles parked at country church funeral", "THIRTY-FOUR MOTORCYCLES")

ch("Grandma's lesson")
sc("""I'm eighty-two now, sweetheart, and I've thought about that night my whole life. My mother had nine dollars and one pot of soup, and she gave it away to twelve strangers the whole street was afraid of. She didn't do it because she expected anything back. She did it because one boy was shaking in the snow. And everything that came back to her came because of that.""",
   "elderly woman by window snowy evening", "ONE POT OF SOUP")
sc("""Tell me in the comments, honey. Would you have opened that door? Be honest with Grandma. And if you have a story about a stranger's kindness, I want to hear it. There are more of my family's stories in the playlist right there on your screen, and I'll see you in the next one. Good night, sweetheart. Merry Christmas.""",
   "warm lit window in snowy night", "WOULD YOU OPEN THE DOOR?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma74", "Poor Mom Let 12 Freezing Bikers In on Christmas Eve. The NEXT Day...",
     ["Grandma Ruth is a fictional narrator and this is a fictional story, inspired by the kind of Christmas kindness stories families tell.",
      "First aid detail: frostbitten hands should be rewarmed in warm, not hot, water (modern guidance: about 98-102F / 37-39C)."],
     "kindness story", minutes=(13, 14.5), voice="en_US-lessac-high")
