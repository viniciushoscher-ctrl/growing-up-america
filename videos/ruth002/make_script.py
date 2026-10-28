import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth's Story · Chapter 2 (novela, Season 1) · Billionaires Histories, new format
# My Mother Hid a Letter in the Flour Tin (1944) | Grandma Ruth, Chapter 2
# Canon from chapter 1: Ruth born 8 August 1944; Walter shipped out 2 October 1943; Pearl is Walter and Frank's mother.
# Hook to chapter 3: Dorothy burns a letter signed only "F."

sc("""Last night I told you about the week I was born. The telegram that said my father was missing in France. And Mrs. Pruitt next door, holding me on her knee, counting the months on her fingers. October, November, December. Jack, you asked me what she was counting. Well. Tonight you'll start to understand.""",
   "1940s woman neighbor portrait", "LAST NIGHT")
sc("""Come closer, both of you. Emma, give your brother some of that blanket. This part of the story happened in the fall of nineteen forty-four, when I was a baby in a crib under a window. So I don't remember any of it. Grandma Pearl told me, years later. And some of it I found out for myself, in a way I'll tell you about much, much later.""",
   "1940s baby crib window", "THE FALL OF 1944")

ch("Gossip")
sc("""In a town like Mansfield in those days, sweethearts, news traveled faster than the mail. There was no internet, no phone in your pocket. There was something better. The party line, the church basement, and the beauty parlor on Park Avenue West. And by the end of August, all three of them were talking about Dorothy Miller's baby.""",
   "1940s women beauty parlor talking", "THE BEAUTY PARLOR")
sc("""Mrs. Pruitt never said anything out loud. She was too clever for that. She just asked questions. Isn't it a blessing the baby came so healthy? Didn't Walter ship out in October? My, Frank certainly is a help to her, isn't he? And then she'd smile and sip her coffee, and let the other ladies do the arithmetic.""",
   "1940s women coffee kitchen gossip", "ISN'T IT A BLESSING")
sc("""My mother heard it, of course. You always hear it. At the A and P, two women stopped talking when she came down the aisle with me in the carriage. At church, Reverend Albrecht shook her hand a little too long and said, we are all praying for Walter, Dorothy. All of us. And she said thank you, and held me a little tighter.""",
   "1940s woman grocery store baby carriage", "WE ARE ALL PRAYING")

ch("No news")
sc("""And all that time there was no news about my father. Not one word. Every morning Mother walked to the end of the porch and watched the mailman come up Maple Street. Every morning he shook his head. Missing in action, the telegram had said. In nineteen forty-four, sweethearts, there were tens of thousands of American families waiting on those two words.""",
   "1940s mailman delivering letters street", "EVERY MORNING")
sc("""You see, the fighting in France that summer had been terrible. After D-Day, our boys pushed through the hedgerows of Normandy, field by field. In the last week of July they finally broke through, near a town called Saint-Lô. Thousands of men got separated from their units in that confusion. Some turned up a week later. Some turned up in a German prison camp. And some never turned up at all.""",
   "1944 Normandy soldiers hedgerows", "SAINT-LÔ, JULY 1944")
sc("""Mother kept a map of France on the kitchen wall, torn out of Life magazine. Every night, after the radio news, she put a pin wherever they said the Americans were. Paris. Then the border of Belgium. Then a forest called the Hürtgen, where the fighting went on for months in the freezing rain. She'd stand there with the pins in her mouth, the way she held clothespins, and just look at that map.""",
   "1940s woman kitchen radio news map", "THE MAP ON THE WALL")

ch("Frank")
sc("""Frank kept coming. Every evening after his shift at the steel mill. He fixed the porch step that had been loose since nineteen forty-one. He brought coal for the furnace when the coal man was late. He brought a pound of real butter from a friend, and Grandma Pearl didn't ask which friend, because in those days you didn't ask where the butter came from.""",
   "1940s man fixing porch steps house", "HE FIXED THE PORCH")
sc("""And he held me. That's what Pearl remembered most. Frank would pick me up out of the crib and walk me up and down the front room, singing, Mairzy Doats and Dozy Doats. That silly song that was on every radio that year. And I would stop crying. For him I always stopped crying. Pearl said that was the first thing that frightened her.""",
   "1940s man holding baby singing", "MAIRZY DOATS")
sc("""One night Pearl said to him, very quietly, in the kitchen, Francis, people are talking. And Frank laughed his big laugh and said, Ma, people always talk. Somebody has to look after my brother's family. And Pearl said, your brother's family. Yes. Remember that. And Frank stopped laughing.""",
   "1940s elderly mother son kitchen", "PEOPLE ARE TALKING")

ch("The flour tin")
sc("""Now, every kitchen in America had a set of canisters on the counter in those days. Flour, sugar, coffee, tea, from big to small, in a row. Ours were white enamel with red lids. And since sugar and coffee were rationed, the flour tin was the biggest and the fullest, and the one nobody but my mother ever opened.""",
   "1940s kitchen canisters flour sugar", "FLOUR, SUGAR, COFFEE, TEA")
sc("""In the second week of November, Grandma Pearl decided to bake. It was her birthday, and she wanted a sponge cake, war or no war. She saved up her sugar stamps for a month. And on Saturday morning, while my mother was at the market, Pearl took down the flour tin and dug in the big metal scoop. And the scoop hit something that wasn't flour.""",
   "1940s woman baking flour kitchen", "THE SCOOP HIT SOMETHING")
sc("""It was an envelope, folded in half, pushed all the way down to the bottom and covered with flour. Pearl pulled it out and blew it off. There was no stamp on it. No address. It had never gone through the mail. Somebody had put it into my mother's hand. Or into her mailbox, in the dark.""",
   "1940s old envelope letter", "NO STAMP")
sc("""Pearl told me she stood in that kitchen for a long time with that envelope in her hands. She said she wanted to open it more than she had ever wanted anything. And she said she didn't, because she was a churchgoing woman, and a letter is a letter. So she put it back exactly where it was, and poured the flour back over it, and she made her cake with flour from the neighbor's.""",
   "1940s elderly woman alone kitchen thinking", "A LETTER IS A LETTER")
sc("""But she looked at the handwriting first. Just the front. One word, my mother's name, Dorothy, in pencil, in a big slanting hand. And Pearl knew that handwriting. She had signed every report card that handwriting ever brought home.""",
   "1940s handwriting pencil letter close", "SHE KNEW THAT HANDWRITING")

ch("The election")
sc("""That week was the presidential election. November seventh, nineteen forty-four. President Roosevelt was running for a fourth term, against Governor Dewey of New York. Nobody had ever been president four times. Father was a Roosevelt man, and Mother voted for Roosevelt for him, she said, because he couldn't vote from wherever he was.""",
   "1944 Roosevelt election campaign", "A FOURTH TERM")
sc("""Frank was a Dewey man, of course. Frank was always for whoever my father was against. They had argued about Roosevelt at every Thanksgiving since nineteen thirty-six. And on election night Frank sat in our front room listening to the returns, with his feet up on my father's footstool, smoking my father's brand. And when Roosevelt won, Frank said, well, Walt won't be happy about that. And then nobody said anything, because nobody knew if Walt would ever be anything again.""",
   "1940s family listening radio living room night", "ELECTION NIGHT")

ch("The letter from England")
sc("""And then, eight days before Thanksgiving, it came. Not a telegram this time. A thin blue V-mail letter, with an Army post office address and a little red stamp from the censor. Mother saw it from the porch and ran barefoot down the steps into the street in November. Mrs. Pruitt saw that too.""",
   "1940s V-mail letter army", "V-MAIL")
sc("""It was from a Red Cross nurse at a hospital in England. Your husband, Private Walter J. Miller, is a patient in this hospital. He was found on the twenty-ninth of July with wounds to his leg and his head, and he was without his identification for some time. He is recovering. He asks me to write to say he is thinking of you and the baby every day.""",
   "1940s Red Cross nurse military hospital", "HE IS RECOVERING")
sc("""Thinking of you and the baby. You see, Mother had written to him about me in the spring, when she knew. So he knew there would be a baby. He just didn't know when. He was lying in a hospital bed in England with a bandage around his head, and he didn't know what day his daughter was born. Not yet.""",
   "1940s wounded soldier hospital bed letter", "HE DIDN'T KNOW WHEN")
sc("""Mother read that letter out loud on the porch, and then she read it again, and then she sat down on the top step and laughed and cried at the same time. Pearl came out and held her. And the ladies came out of every house on Maple Street, and somebody started singing, and for one afternoon, sweethearts, everybody forgot to count.""",
   "1940s women hugging porch celebration", "EVERYBODY FORGOT TO COUNT")

ch("Thanksgiving")
sc("""Thanksgiving that year was the happiest Grandma Pearl could remember since before the Depression. Turkey was hard to get, so we had a chicken. There was no sugar for pumpkin pie, so Mother made it with corn syrup and molasses. Frank brought a bottle of wine. The Pruitts came. And at the table, Pearl said grace, and she thanked God for bringing her son back from the dead.""",
   "1940s family thanksgiving dinner table", "THANKSGIVING, 1944")
sc("""Frank raised his glass and said, to Walt. Everybody said, to Walt. And Pearl watched Frank drink his wine. She said he drank the whole glass without stopping. And then he excused himself and went out on the back porch in the cold, without his coat, and stood there in the dark for a long time.""",
   "1940s man alone back porch night winter", "TO WALT")

ch("The stove")
sc("""That night, after everyone had gone, Pearl couldn't sleep. Old people never can, sweethearts, you'll see. Around two in the morning she came downstairs for a glass of milk. And the kitchen light was off, but the kitchen wasn't dark. There was an orange glow coming from the stove.""",
   "1940s kitchen night dark stove", "TWO IN THE MORNING")
sc("""Our stove was a big old coal and gas range, the kind with a little iron door on the side for the fire. And my mother was kneeling in front of that little door in her nightgown. She had the flour tin open on the floor beside her. And she was feeding a piece of paper into the fire, slowly, one corner at a time.""",
   "1940s old coal kitchen stove fire", "THE LITTLE IRON DOOR")
sc("""Pearl didn't say a word. She stood in the doorway in the dark. And just before the last piece of paper went into the fire, Mother held it up to the light, to read it one more time. And Pearl saw the bottom of the page. There was no name. No love, no yours truly. Just one letter, written big, in pencil.""",
   "1940s letter burning fire close", "ONE LETTER")
sc("""F.""",
   "1940s fire embers stove glow", "F.")

ch("Next time")
sc("""Now, Emma, don't you look at me like that. I know what you're thinking. I'm only telling you what Grandma Pearl saw, with her own eyes, in nineteen forty-four. What it means, well. That took me forty years to find out. And you'll have to be patient too.""",
   "1940s old family photographs album", "BE PATIENT")
sc("""Tomorrow I'll tell you about the spring of nineteen forty-five, and the night the whole town rang its bells. And the soldier who came home early, with something to say about my father. Goodnight, sweethearts. Grandma Ruth will be right here tomorrow night.""",
   "1940s house at night porch light", "CHAPTER 3: THE BELLS")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("ruth002", "My Mother Hid a Letter in the Flour Tin (1944) | Grandma Ruth, Chapter 2",
     ["Grandma Ruth's Story is a work of fiction told by a narrated character. The history around it is real.",
      "Operation Cobra and the breakout near Saint-Lô, 25-31 July 1944.",
      "Battle of Hürtgen Forest, September 1944 - February 1945.",
      "US presidential election, 7 November 1944: Franklin D. Roosevelt re-elected for a fourth term over Thomas E. Dewey.",
      "V-mail (Victory Mail), microfilmed wartime letters, 1942-1945.",
      "'Mairzy Doats', a number-one hit in the US in 1944.",
      "WWII sugar rationing in the US, 1942-1947."],
     "novela chapter 2", minutes=(12, 14.5), voice="en_US-lessac-high")
