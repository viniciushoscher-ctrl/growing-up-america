import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 01 · angle 1 (one year of her life, her age + the exact year) · Billionaires Histories, new format
# I Was 12 in 1956. Here's What Life Was Really Like, Sweetheart
# Grandma Ruth is a narrated character: born in 1944 in Mansfield, Ohio. Every price and event is real.

sc("""Come sit with me, sweetheart. No, bring the blanket, it's cold tonight. You asked me the other day what it was like when I was your age. Well, I was twelve years old in nineteen fifty-six, and I've been thinking about it ever since you asked. So let me tell you. All of it.""",
   "1950s grandmother living room lamp", "COME SIT WITH ME")
sc("""My name was Ruth Ann Miller back then. I lived on a street of white houses in Mansfield, Ohio, with my mother, my father, my little brother Danny, and a dog named Skipper who was afraid of the mailman. Nobody locked their doors on our street. I'm not saying that to sound old. It's just true.""",
   "1950s small town street houses", "MANSFIELD, OHIO")
sc("""Your world is so big, honey. You can see the whole planet on that little phone. My world was about six blocks wide. But I'll tell you a secret. It didn't feel small. It felt like it had everything in it. Let me show you what I mean.""",
   "1950s children walking neighborhood sidewalk", "SIX BLOCKS WIDE")

ch("Mornings")
sc("""My mornings started with the milkman. You've never heard that sound, glass bottles clinking on the porch before the sun was up. Mother left a note in the empty bottle. Two quarts and a pint of cream, please. In winter the cream froze and pushed the little paper cap right up out of the bottle, like a hat.""",
   "1950s milkman delivering milk bottles", "THE MILKMAN")
sc("""Mother was already in the kitchen when I came down. She wore an apron every day of her life. Breakfast was oatmeal or eggs, toast with real butter, and orange juice made from a frozen can. Father read the Mansfield News Journal at the table and drank his coffee black, and you did not talk to him until he folded that paper.""",
   "1950s mother kitchen breakfast family", "BREAKFAST AT SEVEN")
sc("""Then I walked to school. Walked, sweetheart. Nobody drove us. Danny and I went together, and we picked up the Kowalski girls on the corner, and by the time we got to the school there were twenty of us, swinging our lunch pails. Mine was tin, with Roy Rogers on the lid. I loved that lunch pail more than anything I own today.""",
   "1950s children walking to school", "WE WALKED")

ch("School")
sc("""School was strict. We stood every morning and said the Pledge of Allegiance with our hands on our hearts. Two years before, Congress had added the words under God, and some of the older teachers still forgot them. The boys wore their hair short and the girls wore dresses. Always dresses. Even in January, with snow up to your knees.""",
   "1950s classroom children pledge allegiance", "THE PLEDGE")
sc("""My teacher that year was Mrs. Hadley. She had gray hair in a bun and a wooden ruler, and she knew how to use both. We wrote with fountain pens and blotted the ink. If you talked in class, you stood in the corner. If you chewed gum, you wore it on your nose. I only did that once.""",
   "1950s teacher classroom blackboard", "MRS. HADLEY")
sc("""And then there were the drills. A bell would ring, and Mrs. Hadley would say, duck and cover. We crawled under our wooden desks and put our hands over our heads. We were practicing for an atomic bomb, honey. Twelve years old. We didn't really understand it. We just did it, and then we went back to arithmetic.""",
   "duck and cover school drill children desks", "DUCK AND COVER")
sc("""That year we also lined up in the gym for a shot. The polio vaccine. You don't know how afraid our parents were of polio. Every summer, children got sick, and some never walked again. When Doctor Salk's vaccine came, mothers cried in that gym. I remember mine holding my hand so tight it hurt more than the needle.""",
   "1950s children polio vaccine school nurse", "THE POLIO SHOT")

ch("What things cost")
sc("""Now you always ask me about money, so here it is. A bottle of Coca-Cola was a nickel. A comic book was a dime. A loaf of bread was about eighteen cents, and a stamp to mail a letter was three cents. Gasoline was about twenty-two cents a gallon, and a man came out and pumped it for you and washed your windshield too.""",
   "1950s gas station attendant pumping gas", "TWENTY-TWO CENTS A GALLON")
sc("""My father worked at the Westinghouse plant, making electric ranges and appliances. He made about eighty dollars a week, and on that one paycheck we had a house, a car, food on the table, and a week at the lake every August. Mother didn't work outside the house. Hardly any mothers on our street did. That was just how it was.""",
   "1950s factory workers assembly line appliances", "ONE PAYCHECK")
sc("""My allowance was twenty-five cents a week, if I dried the dishes and dusted the front room. Twenty-five cents, sweetheart. And I'll tell you, I felt rich. Because a quarter could get you into the Saturday movie, a bag of popcorn, and still leave a penny or two for candy on the way home.""",
   "1950s girl counting coins allowance", "TWENTY-FIVE CENTS")

ch("Saturdays")
sc("""Saturday was the best day of the week. In the morning we watched television, but only if we had finished our chores. We had one set, a big wooden box with a little round screen, black and white. Howdy Doody, Mighty Mouse, The Lone Ranger. And when the shows ended, there was a test pattern with an Indian head on it, and that was that.""",
   "1950s children watching television set", "ONE TELEVISION")
sc("""In the afternoon we went to the matinee at the theater downtown. Two cartoons, a newsreel, a serial that always ended with the hero about to fall off a cliff, and then the main picture. Hundreds of children, no grownups, everybody screaming. The poor usher walked up and down the aisle with his flashlight, and nobody paid him any mind.""",
   "1950s children movie theater matinee audience", "THE SATURDAY MATINEE")
sc("""On the way home we stopped at Woolworth's. Oh, honey, I wish you could have smelled that store. Popcorn, roasted peanuts, perfume and floor wax. Birds in cages at the back. Goldfish in tanks. Long counters of everything a girl could want, and a lunch counter where you sat on a spinning stool and ordered a cherry Coke.""",
   "1950s Woolworth store interior counters", "WOOLWORTH'S")
sc("""And the penny candy. Candy buttons on paper strips. Wax lips. Mary Janes. Bazooka bubble gum with the little comic inside. And candy cigarettes, sweetheart. Little white sticks with red tips, in a box that looked just like the real ones. We'd pretend to smoke them like our fathers did. Nobody thought a thing about it.""",
   "1950s penny candy store jars children", "PENNY CANDY")

ch("The summer of 1956")
sc("""That summer, we lived outside. We left after breakfast and came home when the streetlights came on. Nobody knew where we were, and nobody worried. We rode our bicycles everywhere. Mine was a blue Schwinn I bought with birthday money from Grandma Pearl, and I put playing cards in the spokes so it sounded like a motorcycle.""",
   "1950s children riding bicycles street", "HOME BY THE STREETLIGHTS")
sc("""We played kick the can and red rover until it was too dark to see. We caught lightning bugs in a Mason jar with holes poked in the lid. We drank water straight from the garden hose, warm at first and then cold. And when the ice cream truck came jingling down the street, every door on the block opened at once.""",
   "1950s children playing backyard summer", "LIGHTNING BUGS")
sc("""In August, we drove to Lake Erie. Father packed the trunk of our green Chevrolet so tight he had to sit on it to close it. No seat belts, no air conditioning. Danny and I fought in the back seat the whole way, and Mother said, don't make me turn this car around, at least ten times. She never once turned it around.""",
   "1950s family car road trip station wagon", "DON'T MAKE ME TURN AROUND")
sc("""That same summer, President Eisenhower signed a law to build the interstate highways. Father read about it at the breakfast table and said, Ruthie, someday you'll drive from here to California without a single stoplight. I laughed at him. I didn't believe it. He was right, of course. He usually was, though I'd never have told him so.""",
   "1950s highway construction road building", "THE NEW HIGHWAYS")

ch("The night Elvis came")
sc("""Now, September. I have to tell you about September. On the ninth of September, nineteen fifty-six, Elvis Presley sang on the Ed Sullivan Show. About sixty million Americans watched that night. More than four out of every five televisions in the whole country were tuned to that one show.""",
   "1950s family watching television evening", "SIXTY MILLION WATCHED")
sc("""I begged to stay up. Father said that boy was a bad influence, and he sat in his chair with his arms crossed the whole time. But when Elvis started to sing Hound Dog, I saw his foot tapping. I saw it, sweetheart. I told your grandfather that story at our wedding, and he laughed until he cried.""",
   "1950s teenage girls record player music", "HIS FOOT WAS TAPPING")
sc("""After that, every girl at school wanted a record player. I saved for months and bought my first record at the five and dime. Forty-five rpm, with a big hole in the middle. I played it until it was all scratches. My mother said she'd hear that song in her sleep. I think she secretly liked it too.""",
   "1950s record store teenagers vinyl records", "MY FIRST RECORD")

ch("Home and family")
sc("""Our telephone was black, and it was heavy enough to hurt somebody. It sat on a little table in the hall. And we shared the line with three other families. A party line, they called it. You'd pick it up to call your friend, and Mrs. Duncan from down the street would already be on it, talking about her gallbladder.""",
   "1950s woman talking rotary telephone", "THE PARTY LINE")
sc("""Mother cooked everything from scratch. Pot roast on Sunday, meatloaf on Wednesday, fish on Friday. Jell-O salad with little pieces of fruit stuck in it, for company. Nothing was ever thrown away. Leftover roast became hash, stale bread became pudding, and bacon grease lived in a coffee can next to the stove, for frying.""",
   "1950s housewife cooking kitchen stove", "NOTHING WAS WASTED")
sc("""Every night at six o'clock, we sat down to supper together. All four of us, no exceptions. You didn't leave the table until you were excused. You ate what was on your plate, or you sat there looking at it. I sat with a plate of liver and onions until eight thirty once. I still won't eat liver, honey. Not for anybody.""",
   "1950s family dinner table eating together", "SUPPER AT SIX")
sc("""And on Sundays, we put on our best clothes and went to church. White gloves, a little hat, shoes that pinched. Then dinner at Grandma Pearl's, with the good china and the whole family around one long table, uncles arguing about the Cleveland Indians and aunts trading recipes in the kitchen.""",
   "1950s family Sunday dinner grandmother", "SUNDAYS AT GRANDMA'S")

ch("Fall and the election")
sc("""In November there was an election, and Eisenhower won again. Ike, everybody called him. Father wore an I Like Ike button on his coat for weeks. At school we held our own pretend vote with paper ballots in a shoebox. Ike won there too, by a lot. I voted for him because I liked his smile. That's how twelve-year-olds vote.""",
   "1950s election campaign Eisenhower rally", "I LIKE IKE")
sc("""Thanksgiving was at our house that year. Mother got up at five in the morning to put the turkey in. Twenty-two pounds. We had mashed potatoes, sweet potatoes with little marshmallows on top, green beans and three kinds of pie. Then the men fell asleep in front of the football game, and the women did every single dish by hand.""",
   "1950s Thanksgiving dinner family turkey", "TWENTY-TWO POUNDS")
sc("""And Christmas. Oh, sweetheart. The Sears catalog came in the fall, the one we called the Wish Book, and Danny and I circled everything in it. I wanted a doll with real hair that year. On Christmas morning she was under the tree, and I named her Margaret. I still have her. She's in the cedar chest upstairs. I'll show you tomorrow.""",
   "1950s children Christmas morning tree presents", "THE WISH BOOK")

ch("What I miss")
sc("""Now, I don't want you to think it was all perfect. It wasn't. Not everybody was welcome on every street, or at every lunch counter, the way I was. Women couldn't do half the things you'll do. And we didn't know half of what we know now about cigarettes or bombs. Some things got better, honey, and they needed to.""",
   "1950s city street people downtown crowd", "IT WASN'T PERFECT")
sc("""But you asked me what I miss. I miss the sound of the screen door. I miss knowing every family on the street by name. I miss being bored on a summer afternoon, lying in the grass and looking at the clouds with nothing to do and nowhere to be. I don't think children get to be bored anymore. I think that's a loss.""",
   "1950s children lying grass summer", "WHAT I MISS")
sc("""Most of all, I miss my mother's kitchen on a Saturday night, with the radio on and the smell of something baking, and my father laughing at something on the television, and Danny asleep on the rug with Skipper. I didn't know it then, sweetheart. I didn't know those were the good old days. Nobody ever does, while they're living them.""",
   "1950s family evening home radio", "THE GOOD OLD DAYS")
sc("""Now, it's late, and your mother will have my hide. But come back tomorrow, and I'll tell you about the first time I drove a car, and the boy who taught me. Your grandfather. Goodnight, sweetheart. And if you liked hearing about the old days, stay close. Grandma has a lot more stories to tell.""",
   "1950s house at night porch light", "GOODNIGHT, SWEETHEART")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("grandma01", "I'm 82. Here's What Growing Up in 1956 America Was Really Like",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Elvis Presley on The Ed Sullivan Show, 9 September 1956: about 60 million viewers, 82.6% of the TV audience (Nielsen).",
      "Federal-Aid Highway Act signed by Eisenhower, 29 June 1956.",
      "US prices 1956: first-class stamp 3 cents (1932-1958), gasoline about 22 cents a gallon, bread about 18 cents a loaf.",
      "'Under God' added to the Pledge of Allegiance, 14 June 1954.",
      "Salk polio vaccine licensed April 1955; school vaccination campaigns 1955-1957.",
      "Eisenhower re-elected 6 November 1956.",
      "Westinghouse electric range plant, Mansfield, Ohio."],
     "one year of her life (her age + the exact year)", minutes=(12, 14.5), voice="en_US-lessac-high")
