import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 92 · ANGLE: kindness story (a child's letter to Santa delivered to the wrong house; Grandma answers it)

sc("""Sweetheart, in December of nineteen ninety-one, the mailman put a letter in my box by mistake. It was addressed in crayon, to Santa Claus, North Pole, and it had no stamp. The little girl who wrote it didn't ask for a doll or a bike. She asked Santa for a winter coat for her mother, and for her daddy to stop being sad. I've never thrown that letter away. And I answered it.""",
   "child's crayon letter to Santa in mailbox", "DEAR SANTA")
sc("""Tonight I'm going to tell you what that letter said, how I found the little girl who wrote it, and what she sent me in the mail twenty-eight years later, in a box with no return address. Stay with me, honey, because her father's part of this story is the one that still makes grown men cry when I tell it at church.""",
   "small box wrapped in brown paper on porch", "A BOX WITH NO ADDRESS")

ch("The letter")
sc("""It was a Tuesday, the tenth of December. I was bringing in the mail, bills and Christmas cards, and there it was, a folded piece of school notebook paper, tucked in with the rest. On the outside, in red crayon, it said, To Santa Clos, North Pole. Somebody had dropped it in a mailbox with no stamp, and the post office had just sort of passed it along until it landed on me.""",
   "folded notebook paper red crayon envelope", "TO SANTA CLOS")
sc("""I opened it, honey. I know I shouldn't have. It said, Dear Santa. My name is Emily. I am seven. I have been good. I don't need any toys this year. Please bring my mom a winter coat because hers has a hole and she is cold at the bus stop. And please make my daddy not sad anymore. He lost his job at the plant and he sits in the dark. Love, Emily. P.S. We don't have a chimney, so use the door.""",
   "child's handwritten letter crayon close up", "USE THE DOOR")
sc("""I sat right down on my porch step in the cold and read it three times. We don't have a chimney, so use the door. Harold came home and found me there, with my cheeks wet. He read it, and he didn't say anything. He just went inside and came back with his coat on and said, all right, Ruthie. How are we going to find her? In a minute I'll tell you the clue that found her.""",
   "elderly couple reading letter on porch", "HOW DO WE FIND HER?")

ch("Finding Emily")
sc("""There was no last name, sweetheart, and no address. Just Emily, seven, and a daddy who'd lost his job at the plant. But in nineteen ninety-one, only one plant in Mansfield had laid people off that fall. The big appliance plant on Fifth Street had let go of four hundred men in October. Harold had friends there. So Harold started asking around at the union hall.""",
   "union hall men talking 1990s", "FOUR HUNDRED MEN")
sc("""And the second clue was in the letter itself, honey. On the back, Emily had drawn a picture. A little house, a mom, a dad, and a girl, all in crayon. And next to the house, she'd drawn a tall tower with a big round top, colored silver. I knew that tower. It was the water tower on the north end of town, by the trailer park on Leppo Road.""",
   "child's crayon drawing house and water tower", "THE WATER TOWER")
sc("""If you're enjoying Grandma's story, tap the like button for me, sweetheart. It helps more people find these stories. Two days later, a man at the union hall told Harold about a fellow named Dale Pruett, who'd been laid off in October and lived in the trailer park on Leppo Road with his wife, Karen, and their little girl. And their little girl's name was Emily.""",
   "trailer park in winter small town", "DALE PRUETT")

sc("""Harold drove out there the next afternoon, just to look, honey. He parked by the water tower and watched. And he saw a woman come out of a little blue trailer at the end of the row in a thin brown coat with a tear at the elbow, and walk to the bus stop in the wind. She stood there with her arms wrapped around herself for twenty minutes. Harold came home and said, Ruthie, it's her. And that coat has a hole in it.""",
   "woman in torn coat at bus stop wind", "THAT COAT HAS A HOLE")
ch("The plan")
sc("""Now, here's the thing, honey. Dale was a proud man. Harold knew men like him, men who'd worked since they were sixteen and never asked anybody for anything. If two strangers showed up at his door with charity, he'd slam it in our faces. Harold said, Ruthie, a man who sits in the dark doesn't want pity. He wants to be needed. And that's when Harold got his idea.""",
   "proud man sitting alone in dark room", "HE WANTS TO BE NEEDED")
sc("""Harold had a friend, George Hill, who owned a small heating and plumbing business, and George was always complaining he couldn't find good men who'd show up on time. So Harold went to George and said, I know a man. Worked at the appliance plant eighteen years. Never missed a day. George said, send him over. And Harold said, no, George. You go to him. And you tell him you heard he was the best.""",
   "two older men talking in workshop", "TELL HIM HE'S THE BEST")
sc("""And then there was the coat. I went to Lazarus in Columbus and bought the warmest winter coat I could find, a long red wool one with a hood, in the size I guessed from the drawing. Which was a silly way to guess a size, sweetheart. And I bought a little doll for Emily, too, because she was seven, and I didn't care what she'd said. Every seven-year-old needs a doll.""",
   "red wool winter coat in gift box", "A LONG RED COAT")

sc("""And I bought groceries too, honey. A ham, potatoes, a bag of oranges, a box of chocolates, and a tin of my own molasses cookies. Harold said, Ruth, Santa doesn't bring ham. And I said, this Santa does. We packed it all in a big box, and Harold wrapped it in brown paper, and on top he wrote, in big block letters so it wouldn't look like my handwriting, For the Pruett family. From the North Pole.""",
   "box of groceries wrapped in brown paper", "THIS SANTA BRINGS HAM")
ch("Christmas Eve")
sc("""So far, the letter, the water tower, and the union hall. On Christmas Eve, at nine o'clock at night, Harold and I drove out to Leppo Road. The trailer was dark except for one little lamp. We didn't knock. We left the two boxes on the step, wrapped in brown paper. On top was a letter, and I'd written it on my best stationery, with a fountain pen, in my most careful handwriting.""",
   "gift boxes on trailer step at night snow", "WE DIDN'T KNOCK")
sc("""It said, Dear Emily. I got your letter. You're right, you don't have a chimney, so I used the door. Here is a coat for your mother, so she won't be cold at the bus stop. And a little something for you, because good girls who don't ask for anything for themselves are my very favorite kind. Your daddy's sadness is a harder thing to fix. But I'm working on it. Love, Santa.""",
   "handwritten letter fountain pen stationery", "I USED THE DOOR")
sc("""Then we rang the doorbell and ran, honey. Harold was fifty, with a bad knee, and I was forty-seven, and we ran down that gravel lane in the dark like a couple of teenagers and ducked behind our own car. And we watched the door open, and a little girl in pajamas look down at those boxes. And we heard her scream, Mommy! Daddy! He came! He used the door!""",
   "little girl in pajamas at door with presents", "HE USED THE DOOR")

ch("The job")
sc("""Two days after Christmas, George Hill drove out to Leppo Road. He knocked on the door and said to Dale, I hear you were the best man on the line at the plant. I need a man like that. Can you start Monday? Dale stood in that doorway, honey, and George said he didn't say anything for a whole minute. Then he shook George's hand so hard George's fingers hurt for a week.""",
   "two men shaking hands at trailer door", "CAN YOU START MONDAY?")
sc("""Dale never knew it was Harold, sweetheart. George never told him. He thought George Hill had just heard about him somewhere. He worked for George for twenty-two years and became his partner. And when George retired, Dale bought the whole business. Pruett and Hill Heating. You'll still see their trucks all over Mansfield today. Every one of them has a little red star on the door.""",
   "heating company van with red star on door", "PRUETT AND HILL")

sc("""And every Christmas after that, honey, a card came to the trailer, and later to the little house the Pruetts bought on Wood Street, signed Santa. Every year until Emily was twelve, in my careful fountain pen handwriting. One year I sent her a book. One year, ice skates. And when she was twelve, I sent her a last letter, telling her she was old enough now to be Santa for somebody else.""",
   "Christmas card signed Santa fountain pen", "BE SANTA FOR SOMEBODY ELSE")
ch("Twenty-eight years later")
sc("""Harold passed in two thousand eight, and he never knew how the story ended. In December of two thousand nineteen, a box came in the mail with no return address. Inside, honey, was the letter I'd written as Santa. On my stationery, in my handwriting, yellowed and soft, folded so many times it was coming apart at the creases. And a new letter, typed.""",
   "old yellowed letter in box with new letter", "MY OWN LETTER CAME BACK")
sc("""It said, Dear Mrs. Miller. My name is Emily Pruett Walsh. I'm thirty-five. My dad died last month, and in his tool box, we found this letter from Santa that I'd lost when I was ten. He'd kept it for twenty-five years. And folded inside it was a note in his handwriting. It said, Ask Ruth Miller on Maple Drive. Her stationery. Her husband got me the job. I knew. I always knew.""",
   "note in man's handwriting found in toolbox", "I ALWAYS KNEW")
sc("""Dale had figured it out, sweetheart. Years and years ago. He'd seen my handwriting on a church potluck sign-up sheet and recognized it. And he never said one word to us, because he knew Harold had wanted it that way. He let Harold give him his dignity, and he gave Harold the dignity of never having to be thanked. Two proud men, honey. Neither one ever said a thing.""",
   "church potluck sign up sheet handwriting", "NEITHER ONE SAID A THING")

ch("Emily")
sc("""Emily came to see me that Christmas Eve. She's a teacher now, a second-grade teacher, in Columbus. And she told me that every December, she has her second-graders write letters to Santa. And then she reads every one. And every year, there's one like hers, a child who asks for a coat for their mother, or for their daddy to stop being sad. And she answers that one. Using the door.""",
   "teacher reading children's letters at desk", "SHE ANSWERS THEM")
sc("""She brought me a present, too. A framed picture. It was her crayon drawing from nineteen ninety-one, the house and the water tower, that she'd found in Dale's toolbox along with everything else. And she'd added something with a new red crayon, very carefully. A little old couple, running down a gravel lane, holding hands. It's on my kitchen wall, right next to the refrigerator.""",
   "framed child's crayon drawing on kitchen wall", "RUNNING DOWN THE LANE")
sc("""Here's what I want you to remember, honey. Sometimes the best way to help somebody is to make sure they never have to say thank you. Give the coat, and ring the bell, and run. Tell me in the comments, sweetheart, did you ever get a gift from Santa you could never explain? There are more of my family's stories in the playlist right there on your screen, and I'll see you in the next one. Merry Christmas.""",
   "doorstep with gift at night snow porch light", "RING THE BELL AND RUN")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma92", "A Letter to SANTA Came to My House by Mistake. So I Answered It",
     ["Grandma Ruth is a fictional narrator, and this is a fictional story. All names are invented."],
     "kindness story (secret gift)", minutes=(12, 14.5), voice="en_US-lessac-high")
