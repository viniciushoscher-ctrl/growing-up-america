import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 78 · ANGLE: test story (wealthy grandmother pretends to be broke to see which child takes her in)

sc("""Sweetheart, my neighbor Agnes Whitfield was eighty-one years old and worth about four million dollars, and not one of her three children knew it. So two weeks before Christmas, she called each of them with the same story. She said, I've lost everything. The bank's taking the house. Can I come live with you? And what each of those children said back is the reason I'm telling you this tonight.""",
   "elderly woman on telephone worried", "I'VE LOST EVERYTHING")
sc("""Tonight I'll tell you what the oldest said, what the middle one did, and what the youngest, the one everybody called the failure of the family, showed up with at Agnes's door at two in the morning. Stay with me, honey, because the reading of that will, a year later, was the most talked-about afternoon this town ever had.""",
   "family lawyer office will reading", "THE FAILURE OF THE FAMILY")

ch("Agnes")
sc("""Agnes lived next door to me for thirty-four years. Her husband, Ed, had started a little trucking company in nineteen fifty-six with one truck and a borrowed dollar. By the time he died, he had two hundred trucks. But Ed and Agnes lived like they had one. Same small brick house, same Chevrolet, same Sunday roast. They never told the children how much there was.""",
   "1950s small trucking company one truck", "ONE TRUCK AND A DOLLAR")
sc("""Ed always said, money ruins children who know they're getting it. Let them make their own way. So the three Whitfield children grew up thinking their parents were comfortable, and nothing more. Richard became a lawyer in Chicago. Diane married a dentist and moved to a big house in Columbus. And the youngest, Tommy, became a high school shop teacher, right here in Mansfield.""",
   "three siblings old family photograph", "MAKE THEIR OWN WAY")
sc("""Richard and Diane were the success stories, honey. Agnes had their pictures on the mantel, in silver frames. Graduation, weddings, Christmas in Aspen. Tommy's picture was a school photo stuck in the corner of the mirror. The other two talked about Tommy like he was a disappointment. He never made any money. Married a waitress. Drove a pickup with a door that didn't match. In a minute I'll tell you why that door didn't match.""",
   "silver picture frames on mantel", "THE DISAPPOINTMENT")

ch("The test")
sc("""After Ed died, Agnes started to wonder. Her children called on birthdays and holidays. Richard and Diane sent beautiful gifts. But they never came. Not once in three years. And Agnes said to me, over coffee at my kitchen table, Ruth, I have to decide who gets four million dollars. And I don't know my own children anymore. I know their Christmas cards.""",
   "two elderly women coffee kitchen table", "I KNOW THEIR CHRISTMAS CARDS")
sc("""So she made her plan, and she told only me, because she needed a witness. She'd call each child and tell them that Ed's company had gone under, the bank was foreclosing on the house, and she had nowhere to go. She'd ask each one if she could come live with them. And she'd keep a little notebook of exactly what each one said.""",
   "small notebook and pen on table", "A LITTLE NOTEBOOK")
sc("""I told her it was cruel, sweetheart. I said, Agnes, you'll break their hearts. And she looked at me and said, Ruth, if it breaks their hearts, then I'll know they have hearts. Then I'll tell them the truth and we'll all have a good cry at Christmas. That's all I want. I want to find out they have hearts.""",
   "elderly woman serious face by window", "IF IT BREAKS THEIR HEARTS")

ch("Richard")
sc("""If you're enjoying Grandma's story, tap the like button for me, honey. It helps more people find these stories. She called Richard first, on a Tuesday night. I sat next to her on the couch. Richard listened. There was a long pause. And then he said, Mom, that's terrible. Have you talked to a lawyer? And she said, honey, you're a lawyer. And he said, well, I don't do that kind of law.""",
   "man on phone in city office night", "NOT THAT KIND OF LAW")
sc("""Then she asked him straight out. Richard, can I come stay with you and Pamela? Just until I get on my feet? Another long pause. Then Richard said, Mom, you know our place is small. And Pamela's mother is coming for the holidays. Have you looked into those senior apartments? I could help with the first month. Richard lived in a five-bedroom house in Lake Forest, honey.""",
   "large suburban house Lake Forest", "OUR PLACE IS SMALL")
sc("""Agnes thanked him and hung up. She wrote in her little notebook. Richard. Senior apartment. First month. Then she sat there with that notebook on her lap for a long time. And I didn't say anything, because there wasn't anything to say. She'd been his mother for fifty-six years, and he'd offered her one month's rent.""",
   "notebook on lap elderly hands", "ONE MONTH'S RENT")

ch("Diane")
sc("""She called Diane the next night. Diane cried, honey. Real tears, I could hear them through the phone. She said, oh, Mama, oh no. And for a minute, I thought, here it is. Here's the heart. Then Diane said, Mama, what happened to Daddy's company? Was there anything left? What about the house in Florida? What about the jewelry? Is Grandma's ring still in the safe deposit box?""",
   "woman crying on phone in big kitchen", "WHAT ABOUT THE RING?")
sc("""When Agnes asked if she could come live with her, Diane said, Mama, you know I would in a heartbeat. But Greg has his practice, and the girls have their activities, and we're redoing the guest room. Let me talk to Greg. I'll call you back. Agnes wrote in her notebook. Diane. Asked about the ring. Will call back. Diane never called back, sweetheart. Not that week. Not ever.""",
   "phone sitting silent on table", "SHE NEVER CALLED BACK")

ch("Tommy")
sc("""She almost didn't call Tommy. She said, Ruth, he doesn't have room. He's got three kids in a two-bedroom house. It isn't fair to ask him. But I said, Agnes, you asked the other two. So on Thursday night, she called Tommy. And she told him the same story. The company, the bank, the house. And she hadn't even gotten to the question when he cut her off.""",
   "small house at night lights on", "HE CUT HER OFF")
sc("""He said, Mom, are you safe right now? Are you warm? Is there food in the house? She said, yes, honey, I'm fine. And he said, okay. Don't do anything. Don't sign anything. I'm coming. And he hung up. Agnes looked at me and said, coming? It's ten o'clock at night. I said, Agnes, I think your son is getting in his truck.""",
   "man grabbing keys and coat at night", "I'M COMING")
sc("""At two o'clock in the morning, there were headlights in Agnes's driveway. I saw them from my bedroom window. It was Tommy's old pickup, the one with the door that didn't match. And in the back, under a tarp in the snow, was a twin mattress, a box of groceries, a space heater, and a set of tools. He'd driven over from the other side of town with everything he thought his mother might need.""",
   "old pickup truck in snowy driveway night", "TWO IN THE MORNING")

ch("The door")
sc("""Agnes opened the door in her robe. And Tommy, her disappointment, the shop teacher with the mismatched door, said, Mom, Carla and I talked. The kids are going to double up. You're getting Katie's room. It's got the best light. We'll get your things tomorrow. And if the bank wants this house, they can have it. You've got us. You've always got us.""",
   "son at door hugging mother in robe", "YOU'VE ALWAYS GOT US")
sc("""Agnes asked him, honey, what about money? Tommy laughed. He said, Mom, we don't have any. We never have. We'll figure it out. We always do. And then he told her about the door. The pickup's passenger door was green because he'd bought it at a junkyard after a drunk driver hit him. He'd been driving it two years, because new doors cost money, and his kids needed braces.""",
   "pickup truck green mismatched door", "WHY THE DOOR WAS GREEN")
sc("""Agnes broke down right there in the hallway, honey. She told him everything. The test, the notebook, the four million dollars. And Tommy stood there, and his face went from confused, to hurt, to something I've never forgotten. He said, Mom, you didn't have to test me. You just had to ask me to Christmas dinner. And then he went outside and sat in his truck for a long time.""",
   "man sitting alone in truck at night snow", "YOU JUST HAD TO ASK")

ch("Christmas")
sc("""So far, the lawyer, the ring, and the truck at two in the morning. Agnes spent that Christmas at Tommy's little house, in Katie's room with the best light, eating Carla's ham on a folding chair. She told me it was the happiest Christmas she'd had since Ed died. Richard sent a fruit basket. Diane sent a card that asked if there was news about the ring.""",
   "small cozy house Christmas dinner folding chairs", "A FRUIT BASKET")
sc("""Agnes never told Richard and Diane the truth, honey. Not that Christmas, not ever. She said, Ruth, they had their chance to show me who they were. I'm not going to give them a second one with the answers already written on the board. She paid off Tommy's house that January, and told him it was from a little savings account Ed had left. She bought the kids braces. She bought him a new door.""",
   "new truck door being installed", "A NEW DOOR")

ch("The will")
sc("""Agnes passed the next December, peacefully, in her sleep, in the room with the best light. And in January, all three children sat in a lawyer's office for the reading of the will. Richard flew in from Chicago in a long black coat. Diane came in a fur. Tommy came in his work boots. I was there too, honey, because Agnes had asked me to be.""",
   "three siblings in lawyer office", "THE READING OF THE WILL")
sc("""The lawyer read it slowly. To my son Richard, I leave one month's rent at a senior apartment of his choosing, so he'll know what it feels like. To my daughter Diane, I leave my mother's ring, since that's what she asked about. To my son Thomas, who came at two in the morning, I leave everything else. And then he said the number. Four million, one hundred thousand dollars.""",
   "lawyer reading will papers", "WHO CAME AT TWO IN THE MORNING")
sc("""Diane screamed. Richard said he'd contest it, and then he saw the little notebook, which the lawyer pulled out of the folder, with every phone call written down in Agnes's handwriting and my signature as witness at the bottom of each page. He didn't contest it, honey. And Tommy? Tommy just sat there with his hands on his knees and cried, because all he wanted was his mother back.""",
   "notebook with handwritten notes and signature", "THE NOTEBOOK")

ch("What Tommy did")
sc("""Tommy still teaches shop at the high school, sweetheart. He didn't quit. He still drives a pickup. But every Christmas Eve, he takes the families of every one of his students who's struggling, and he quietly pays their heating bills through the winter. He calls it the two a.m. fund. Nobody knows it's him. Nobody but me, and now you.""",
   "shop teacher in classroom with students", "THE TWO A.M. FUND")
sc("""Here's what I want you to remember, honey. You never know who your real riches are until you need them. Agnes had a mantel full of silver frames and one school photo stuck in the mirror, and she had it exactly backwards. Call the one who'd come at two in the morning. And if you're the one who would, God bless you. Don't ever stop.""",
   "school photo tucked in mirror frame", "THE ONE WHO COMES")
sc("""Tell me in the comments, sweetheart. Was Agnes right to test her children, or was it wrong? And who in your family would come at two in the morning? There are more of my family's stories in the playlist right there on your screen, and I'll see you in the next one. Good night, honey.""",
   "pickup headlights in snowy night", "WHO WOULD COME FOR YOU?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma78", "Rich Grandma Told Her 3 Kids She Was BROKE to See Who'd Take Her In",
     ["Grandma Ruth is a fictional narrator, and this is a fictional story. All names are invented."],
     "disguise test story", minutes=(12, 14.5), voice="en_US-lessac-high")
