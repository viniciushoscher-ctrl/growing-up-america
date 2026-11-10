import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 76 · ANGLE: humiliated grandmother at family Christmas, then the reveal (she owns the house)

sc("""Sweetheart, on Christmas Day of two thousand eleven, my son's new wife sat me at a card table in the laundry room, next to the dryer, and served me a paper plate of leftovers while the rest of the family ate turkey on my own good china in the dining room. She said there just wasn't room for me. What she didn't know was whose name was on that house.""",
   "elderly woman alone at card table laundry room", "THERE'S NO ROOM FOR YOU")
sc("""Tonight I'm going to tell you everything that happened that Christmas, what I heard her say about me through the kitchen door, and the one sentence I said at dessert that made the whole table go silent. Stay with me, honey, because the ending isn't what you'd expect from a sweet old grandma. And I'm still not sorry.""",
   "family Christmas dinner table silent", "ONE SENTENCE AT DESSERT")

ch("The house")
sc("""My husband Harold and I bought that house on Maple Drive in nineteen seventy. Three bedrooms, a big oak tree, and a dining room big enough for twelve. We raised our children there. Harold carved forty-one Christmas turkeys at the head of that table. When he passed in two thousand eight, I was sixty-four and alone in a house full of memories.""",
   "1970s suburban house with oak tree", "FORTY-ONE TURKEYS")
sc("""My son Gary was going through a hard time then. He'd lost his job, and he and his new wife, Tiffany, were behind on their rent. So I did what mothers do. I said, come live with me. There's plenty of room. I gave them the master bedroom, Harold's and mine, and I moved into the little sewing room at the back, because I didn't need much space.""",
   "elderly woman moving into small sewing room", "COME LIVE WITH ME")
sc("""Now, honey, here's the thing nobody told Tiffany. When Harold died, the house didn't go to Gary. It was mine, paid off, every brick. Gary knew. Tiffany didn't. And somewhere in those three years, she started telling people it was their house, and that they were letting me stay. In a minute I'll tell you how I found that out.""",
   "house deed paper on table", "WHOSE HOUSE IS IT?")

ch("Little by little")
sc("""It happened slowly, sweetheart, the way these things always do. First my good china moved to a high shelf I couldn't reach. Then my recipe box went to the garage, because it was clutter. Then my chair at the head of the table, Harold's chair, became Gary's chair. Then my friends from church stopped coming by, because Tiffany always said I was resting.""",
   "china on high kitchen shelf", "LITTLE BY LITTLE")
sc("""Then there were the comments. Mom, you're getting forgetful. Mom, maybe you shouldn't drive. Mom, have you thought about one of those nice places for seniors? And I'd catch Tiffany looking at me across the kitchen, the way you look at a piece of furniture you're planning to get rid of. Gary never said a word. He just looked at his phone.""",
   "woman looking coldly across kitchen", "THOSE NICE PLACES")
sc("""That fall, I found a brochure on the kitchen counter. Sunny Pines Assisted Living. Somebody had circled the price, and written in the margin, in purple pen, Tiffany's purple pen, the words, sell house, pay for this, rest for us. I put it back exactly where I found it, honey. And I didn't say a word. I just started paying attention.""",
   "assisted living brochure on counter", "SELL HOUSE, PAY FOR THIS")

ch("Christmas Day")
sc("""If you're enjoying Grandma's story, tap the like button for me, sweetheart. It helps more people find these stories. On Christmas morning, Tiffany's whole family came. Her parents, her sister, her sister's husband, three children. Fourteen people. And I'd been up since five, making Harold's stuffing, my mother's rolls, and two pies, because I'd made Christmas dinner in that kitchen for forty-one years.""",
   "grandmother cooking Christmas dinner early morning", "UP SINCE FIVE")
sc("""At two o'clock, I carried in the turkey, and I went to sit down, and there wasn't a chair. Fourteen chairs, fourteen place cards in Tiffany's purple pen, and none of them said Ruth. Tiffany smiled at me, a big bright smile, and said, oh, Mom, we're so tight in here. I set you up a little spot in the laundry room. It's cozy. You won't mind, will you?""",
   "place cards on Christmas table", "NONE SAID RUTH")
sc("""Everybody looked at their plates, sweetheart. Her mother looked at me with a little smirk. And my son, my own son, whom I carried and nursed and sat up with through every fever, looked down at his lap and said nothing. So I said, of course not, dear. And I walked into the laundry room, and I sat down at that card table next to the dryer. Remember that card table, honey. You'll see why at the end.""",
   "elderly woman walking away from table sadly", "MY SON SAID NOTHING")

ch("Through the door")
sc("""The laundry room door was right next to the kitchen. And when Tiffany and her sister went in to get the gravy, I heard every word. Her sister said, Tiff, that's kind of harsh. And Tiffany laughed and said, oh, please. She'll be in Sunny Pines by March. Gary's already talking to a realtor. This house is worth three hundred thousand. Next Christmas, we'll have the whole place to ourselves.""",
   "two women whispering in kitchen", "SHE'LL BE GONE BY MARCH")
sc("""I sat there with my paper plate, honey, and I looked at the dryer, and I thought about Harold. I thought about him carrying me over that threshold. Painting the nursery. Hanging the tire swing on the oak tree. I didn't cry. I'm a Mansfield girl. My mother didn't raise a crier. Instead, I got up, and I went to the sewing room, and I made one phone call.""",
   "elderly woman making phone call determined", "ONE PHONE CALL")
sc("""I called Walter Simms. Walter had been Harold's lawyer for thirty years, and he lived three streets over. I said, Walter, I'm sorry to call on Christmas. Could you come by at four o'clock for pie? And bring the folder. Walter didn't ask a single question, sweetheart. He just said, Ruth, I've been waiting for this call for a year. I'll be there at four.""",
   "lawyer with folder walking in snow", "BRING THE FOLDER")

ch("Dessert")
sc("""At four o'clock, the doorbell rang. Tiffany opened it, annoyed, and Walter Simms walked right past her into the dining room in his good gray suit, carrying a fat brown folder. He said, merry Christmas, everybody. Where's Ruth? And I came out of that laundry room, honey, carrying two of my pies, and I set them right down on my own table.""",
   "man in gray suit at family dinner", "WHERE'S RUTH?")
sc("""Tiffany said, Mom, who is this? And I said, this is Walter, dear. He's my lawyer. And then I said the sentence I promised you. I said, Tiffany, I heard you in the kitchen. And since you're so worried about room at this table, I thought we'd talk about whose table it is. Fourteen people stopped chewing at the same time. You could've heard a pin drop on that carpet.""",
   "shocked faces around Christmas table", "WHOSE TABLE IS IT?")
sc("""Walter opened the folder and laid the deed right on top of the cranberry sauce. He read it out loud. Property of Ruth Ellen Miller, sole owner, no mortgage, no lien. And then he read the second paper, a letter I'd signed two months before, when I found that brochure. It gave Gary and Tiffany thirty days' notice to find a new place to live.""",
   "legal document on dinner table", "SOLE OWNER")

ch("The fallout")
sc("""Tiffany went white, then red, then white again. She said, you can't do that, you're senile. And Walter smiled and pulled out one more paper, a letter from my doctor, dated that same week, saying I was in excellent health and of perfectly sound mind. Walter said, ma'am, she's sharper than I am. Tiffany's mother picked up her coat and left without a word.""",
   "woman angry red face dinner", "SHARPER THAN I AM")
sc("""And then my son finally looked up from his lap. He said, Mom. Mom, I didn't know she said that. And I said, Gary, you knew about the place cards. You knew about the laundry room. You knew about the realtor. You didn't have to say the words to be part of it. Your father would be ashamed. And that, sweetheart, is when my son started to cry.""",
   "grown son crying at table", "YOUR FATHER WOULD BE ASHAMED")
sc("""So far, the house, the brochure, the laundry room, and the folder. But here's the part nobody believes. I didn't throw my son out to be cruel. I want you to know that. I did it because I loved him, and because I'd watched him disappear for three years, into his phone and his excuses and his wife's plans. And sometimes, honey, love has to slam the door.""",
   "elderly woman looking out window thoughtful", "LOVE SLAMS THE DOOR")

ch("Thirty days")
sc("""Tiffany left Gary in three weeks. Once there was no house to sell, she didn't see much point in staying. She took the car, the television, and my good china, which I never saw again. Gary moved into a little apartment over a hardware store. And for a whole year, my son didn't call me. That was the hardest year of my life, sweetheart. Harder than losing Harold.""",
   "small apartment above hardware store", "A WHOLE YEAR OF SILENCE")
sc("""But something happened in that little apartment. Gary got a job at the hardware store downstairs. Then he became assistant manager. He started going back to church. And the next December, the week before Christmas, my doorbell rang, and there was my son on the porch, in the snow, holding a card table he'd bought at the hardware store.""",
   "man on snowy porch holding card table", "HE BROUGHT A CARD TABLE")

ch("The next Christmas")
sc("""He said, Mom, I want to sit at this table this year. In the laundry room. You sit at the head of the dining room table, where Dad sat. And I'll eat by the dryer and think about what I let happen. I said, Gary, don't be silly. Get in here. And my son put his arms around me on that porch, and he held on like he was five years old.""",
   "mother and son hugging on porch snow", "I WANT TO SIT THERE")
sc("""That Christmas, we set the big table for twelve. My daughter came from Indiana with her kids. My friends from church. Walter Simms and his wife. And the very last place card, in my own handwriting, said Gary, right next to mine. We used paper plates, because Tiffany had my china. Nobody cared. It was the best Christmas dinner in that house since Harold died.""",
   "warm family Christmas dinner paper plates", "THE BEST CHRISTMAS")

ch("What I learned")
sc("""Gary owns that hardware store now, honey. He's married to a wonderful woman named Linda, a schoolteacher who calls me every Sunday. And every Christmas, he sets up that old card table in the laundry room. Not to eat at. He puts the pies on it. He says it reminds him of the day his mother taught him the most important lesson of his life.""",
   "pies on card table Christmas kitchen", "HE KEEPS THE CARD TABLE")
sc("""Here's what I want you to remember, sweetheart. Being kind doesn't mean being a doormat. You can love your children with your whole heart and still say, no, not in my house. Too many grandmothers I know are sitting in the laundry room right now, being polite. Don't you be one of them. You built that table. You get a chair.""",
   "elderly woman at head of table proud", "YOU GET A CHAIR")
sc("""Tell me in the comments, honey. Was I too hard on my son, or did he need it? Be honest with Grandma. And if anyone ever made you feel like a guest in your own home, I want to hear about it. There are more of my family's stories in the playlist right there on your screen, and I'll see you in the next one. Good night, sweetheart.""",
   "warm lit house in snow at night", "WAS I TOO HARD?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma76", "Family Sat Grandma by the DRYER, Unaware She Owned the House",
     ["Grandma Ruth is a fictional narrator, and this is a fictional story. All names are invented."],
     "humiliated grandma story", minutes=(12, 14.5), voice="en_US-lessac-high")
