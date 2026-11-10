import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 91 · ANGLE: humiliated grandma, then the reveal (bride's rich mother treats her like staff; the bride's father knew her)

sc("""Sweetheart, at my grandson's wedding, at a fancy country club in Cincinnati, the bride's mother handed me a tray of dirty champagne glasses and told me to take them to the kitchen. She thought I was the help, because of my plain dress and my old shoes. When I told her I was the groom's grandmother, she laughed and said, oh, that explains it. What she didn't know was who had raised her own husband.""",
   "elderly woman handed tray of glasses at wedding", "TAKE THESE TO THE KITCHEN")
sc("""Tonight I'm going to tell you what that woman said to me all evening, what happened when her husband stood up to give his toast, and the one word he said that made two hundred people turn around in their chairs and look at me. Stay with me, honey, because I've never seen a woman's face change color so many times in one evening.""",
   "wedding reception toast microphone", "ONE WORD")

ch("The wedding")
sc("""My grandson Jake is a good boy, sweetheart. A schoolteacher, like his mother. And in the summer of twenty nineteen, he married a lovely girl named Caroline, whose family had a great deal of money. Her father owned a chain of car dealerships across Ohio and Kentucky, and her mother, Victoria, had planned the wedding for a year. It was at the Riverside Country Club. Four hundred dollars a plate.""",
   "elegant country club wedding reception", "FOUR HUNDRED DOLLARS A PLATE")
sc("""I wore my good navy dress from Penney's, the one I'd worn to Harold's funeral and my granddaughter's graduation. My pearls were the ones Harold gave me for our twenty-fifth anniversary, and they were fake, honey, and we both knew it. My shoes were black flats, because my knees are seventy-five years old. I thought I looked very nice. Victoria didn't agree.""",
   "elderly woman in navy dress and pearls", "MY GOOD NAVY DRESS")
sc("""I'd never met Caroline's father. He'd been traveling all year, and he only flew in the night before the wedding. But I kept hearing his name, Richard Coleman, and something about it tickled the back of my mind. Like a song you can't quite remember. In a minute I'll tell you where I'd heard that name before. It took me forty-five years to put it together.""",
   "elderly woman thinking puzzled", "SOMETHING ABOUT THAT NAME")

ch("Victoria")
sc("""At the cocktail hour, I was standing by a table with a glass of punch, and Victoria came sweeping by in a silver gown, and she shoved a tray of empty glasses right into my hands. She said, these need to go back. And the shrimp is running low. Tell the kitchen. And she walked off before I could say a word. I stood there holding that tray like a fool.""",
   "woman in silver gown handing tray", "THE SHRIMP IS LOW")
sc("""I found her a few minutes later and gave the tray back, very politely. I said, I think there's been a mistake, dear. I'm Ruth. Jake's grandmother. And she looked me up and down, honey, from my flat shoes to my fake pearls, and she laughed. A little tinkly laugh. And she said, oh. Oh, of course. That explains it. And she turned to her friend and rolled her eyes.""",
   "rich woman rolling eyes at elderly woman", "THAT EXPLAINS IT")
sc("""If you're enjoying Grandma's story, tap the like button for me, sweetheart. It helps more people find these stories. It didn't stop there. At dinner, I found my place card, and I was seated at table twenty-two. In the back. By the kitchen door. Next to the photographer's assistant and a cousin nobody had invited. Jake's parents were at table two. I was by the swinging door.""",
   "table by kitchen door at wedding reception", "TABLE TWENTY-TWO")
sc("""And all evening, Victoria made little remarks, loud enough for me to hear when she passed. Some families just don't know how to dress for an occasion. And, I suppose we should be grateful they came at all. And once, to a waiter right next to me, she said, keep the wine away from table twenty-two, they won't know the difference anyway. I just smiled, honey. I'm good at smiling.""",
   "wealthy guests whispering and laughing", "THEY WON'T KNOW THE DIFFERENCE")

sc("""My grandson came back to find me once, honey, and he saw where I was sitting, and his face went red. He said, Grandma, this is wrong. I'm going to say something. And I took his hand and said, Jake, it's your wedding day. Don't you dare spend one minute of it on me. Go dance with your bride. I'm fine right here. And I was, mostly. I'd had worse seats in my life.""",
   "young groom talking to grandmother at table", "GO DANCE WITH YOUR BRIDE")
sc("""The photographer's assistant at my table was a sweet girl named Maria, about twenty, and she'd heard every word Victoria said. She leaned over and said, ma'am, my grandmother cleans houses in Cincinnati. People talk to her like that all the time. And I said, honey, then your grandmother and I would get along fine. We spent the whole dinner talking about our grandchildren. Best company in the room.""",
   "young woman and elderly woman talking at table", "BEST COMPANY IN THE ROOM")
ch("Richard")
sc("""So far, the tray, the laugh, and table twenty-two. Then it was time for the toasts. The best man went first, and then Caroline's father stood up at the head table. A tall, silver-haired man in a beautiful suit. Richard Coleman. He took the microphone and said, I want to thank everybody for coming. And then he stopped, and he looked out over the room, slowly, table by table.""",
   "silver haired man standing with microphone", "HE LOOKED AROUND")
sc("""And his eyes stopped at the back of the room, honey. At table twenty-two. At me. He stood there with that microphone for a long time, and the room went quiet, waiting. Then he said, very softly, into the microphone, I'm sorry. Excuse me, one moment. And he put the microphone down on the table, and he walked off the stage.""",
   "man walking through reception toward back", "HE PUT DOWN THE MICROPHONE")
sc("""He walked all the way through that ballroom, between the tables, past the cake and the dance floor and two hundred people in their best clothes, to the very back. To table twenty-two. And he stood in front of me, and he looked at my face, and his own face crumpled up like a little boy's. And then he said one word. He said, Mama Ruth?""",
   "man kneeling by elderly woman at wedding table", "MAMA RUTH?")

ch("Ricky")
sc("""And then I knew him, sweetheart. Forty-five years fell away in a second. Ricky Coleman. A skinny, freckled boy from the house behind ours on Maple Drive, whose father drank and whose mother worked nights at the hospital. From the time he was seven until he was fourteen, Ricky ate supper at my kitchen table almost every night. My children called him their other brother.""",
   "1970s freckled boy at kitchen table supper", "RICKY COLEMAN")
sc("""When he was cold, I gave him Mark's old coats. When he got a bad report card, I sat with him at the kitchen table and did fractions until ten at night. When his father came home drunk and loud, Ricky would climb the back fence in his pajamas and sleep on our couch. Harold taught him to throw a football and change a tire. And he called me Mama Ruth.""",
   "boy climbing backyard fence at night", "HE CLIMBED THE FENCE")
sc("""When he was fourteen, his mother finally left his father and moved them to Kentucky, and I lost track of him, honey. I wrote twice. The letters came back. I never knew what became of Ricky Coleman. And now here he was, on his knees by table twenty-two, at his own daughter's wedding, holding my hands and crying in front of two hundred people.""",
   "returned letters stamped return to sender", "THE LETTERS CAME BACK")

sc("""Ricky told me later what happened after Kentucky. His mother got sick when he was seventeen, and he quit school to sell cars, washing them in the lot for tips. He was good at it, because, he said, he'd learned from me how to talk to anybody like they mattered. By thirty, he owned his first dealership. By fifty, he had nineteen. And he never stopped looking for me.""",
   "young man washing cars at dealership lot", "HE NEVER STOPPED LOOKING")
ch("The toast")
sc("""He stood up, and he took my hand, and he walked me all the way back through that ballroom to the head table. Every head turned. Then he picked up the microphone again and he said, I'm sorry, everybody. I need to tell you who this is. And I saw Victoria's face at the head table, honey. It was white as the tablecloth.""",
   "man leading elderly woman through ballroom", "EVERY HEAD TURNED")
sc("""Richard said, when I was a boy, my father was a drunk, and our house was not a safe place. And there was a woman who lived behind us, who fed me supper every night for seven years. Who taught me fractions, and bought me my first suit for the eighth grade dance. Every good thing I am, I learned at her kitchen table. I've looked for her for thirty years. And she's here. She's my daughter's new grandmother.""",
   "man giving emotional speech at wedding", "EVERY GOOD THING I AM")
sc("""And then he said, Mama Ruth, I named my first dealership after you. It's the Ruth Avenue Ford in Lexington. I never knew if you'd see it. The whole room stood up, sweetheart. Two hundred people, on their feet, clapping. My grandson Jake was crying. Caroline was crying. And Victoria was sitting there with her mouth open, holding her champagne glass in midair.""",
   "wedding guests standing applauding", "THE WHOLE ROOM STOOD")

ch("Victoria's face")
sc("""And then Richard turned to his wife. He said, Victoria, where was Mama Ruth seated tonight? And Victoria said, very quietly, I didn't know. And Richard said, table twenty-two, by the kitchen door? A waiter told me. And a guest at that table told me what you said about the wine. Victoria didn't say anything at all. I've never seen anyone wish so hard to disappear into a chair.""",
   "embarrassed woman at head table", "WHERE WAS SHE SEATED?")
sc("""Richard had a waiter bring another chair, and he put me at the head table, right between him and the bride. And here's the part I love, honey. My new granddaughter, Caroline, leaned over and whispered, Grandma Ruth, I'm so sorry about my mother. And will you teach me the fractions? I laughed so hard I spilled my punch on Richard's beautiful suit. He didn't mind one bit.""",
   "bride and elderly woman laughing at head table", "TEACH ME THE FRACTIONS")

ch("After")
sc("""Victoria apologized to me the next morning at the brunch, sweetheart. Stiffly, but she did it. And I'll give her credit. Every Christmas since, a card comes in her handwriting, and the second year, there was a pair of real pearls inside. I wear them to church. But the best thing that came out of that wedding was Ricky. Richard. He comes to my house every Christmas Eve now, and he climbs over my back fence. On purpose.""",
   "man climbing over backyard fence laughing", "OVER THE FENCE ON PURPOSE")
sc("""Here's what I want you to remember, honey. You never know who's sitting at table twenty-two. The plain old woman in the cheap dress might be the reason the man at the head table turned out good. Treat everybody at the party like they're the guest of honor. Because to somebody in that room, they are.""",
   "elderly woman smiling at wedding table", "TABLE TWENTY-TWO")
sc("""Tell me in the comments, sweetheart. Was there a neighbor or a teacher who fed you, or helped raise you, when things were hard at home? I'd love to hear about them. There are more of my family's stories in the playlist right there on your screen, and I'll see you in the next one. Good night, honey.""",
   "warm kitchen table evening supper", "WHO FED YOU?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma91", "Bride's Mother Treated Grandma Like the HELP, Unaware Who She Was",
     ["Grandma Ruth is a fictional narrator, and this is a fictional story. All names are invented."],
     "humiliated grandma story", minutes=(12, 14.5), voice="en_US-lessac-high")
