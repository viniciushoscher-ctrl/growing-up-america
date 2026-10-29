import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 10 · angle 1 (one year of her life, her age + the exact year) · Billionaires Histories, new format
# I Was 9 in 1953. This Is What America Was Really Like
# Grandma Ruth: born 1944 in Mansfield, Ohio (9 in 1953); brother Danny born 1947; father Walter at the Westinghouse plant; Elm Street. Every price and event is real.

sc("""Sweetheart, you're nine now, aren't you? Nine. That's a good age. I remember nine very well. It was nineteen fifty-three, in Mansfield, Ohio. A new president, a new queen, a war that finally stopped, and the first television set on our street. And I had a pair of roller skates with a key that I wore on a string around my neck, like a medal.""",
   "1950s children playing sidewalk street", "NINE YEARS OLD")
sc("""Let me take you through the whole year, honey. What we ate, what we watched, what things cost, and what we were afraid of. Because nineteen fifty-three was the year a lot of the America you know got started. And some of it is gone forever.""",
   "1953 small town America main street cars", "1953")

ch("A new president")
sc("""In January, on the twentieth, we watched a new president sworn in. General Eisenhower, the man who won the war in Europe. Ike. My father had served under him, in a way, along with a few million other men, and he stood up in our front room when Ike put his hand on the Bible. My father never stood up for anything on the radio or the television. He stood up for Ike.""",
   "1953 Eisenhower inauguration crowd Capitol", "JANUARY 20, 1953")
sc("""We watched it at the Kowalskis' house, because they had the first television set on the block, a big wooden Admiral with a round-cornered screen the size of a dinner plate. The picture was gray and snowy and rolled up every few minutes, and Mr. Kowalski would get up and bang the side of it. Fifteen people sat on that living room floor.""",
   "1950s family watching early television set living room", "A SCREEN THE SIZE OF A DINNER PLATE")

ch("Lucy has a baby")
sc("""The very night before the inauguration, on a Monday, Lucy had her baby. On I Love Lucy, I mean. Little Ricky was born on the television the same night Lucille Ball had her real baby in the hospital. Forty-four million people watched it, honey. More than watched Ike. The whole country was talking about a baby on a television show.""",
   "1950s I Love Lucy television show", "LITTLE RICKY")
sc("""And you know what's funny? On that show, they weren't even allowed to say the word pregnant. The network wouldn't let them. They had to say expecting. Lucy and Ricky slept in two separate little beds, too, even though they were married in real life. That's how television was in nineteen fifty-three.""",
   "1950s married couple twin beds bedroom", "EXPECTING")

ch("School")
sc("""I was in fourth grade at Bowman Street School. We sat in rows of wooden desks bolted to the floor, with a hole in the corner for an inkwell, and we learned penmanship with the Palmer Method. Ovals and push-pulls, all day, until your wrist ached. If you were left-handed, the teacher made you write with your right. My friend Linda had her left hand tied behind her chair. Can you imagine?""",
   "1950s classroom wooden desks children writing", "THE PALMER METHOD")
sc("""Every morning we said the Pledge of Allegiance and the Lord's Prayer. Then milk, in little glass bottles, two cents each, warm by the time it got to us. The vaccine for polio wasn't ready yet, honey. That came two years later. In fifty-three we were still just afraid, every single summer.""",
   "1950s school children milk bottles classroom", "TWO CENTS FOR MILK")

ch("Games")
sc("""At recess the girls played jacks on the sidewalk and jumped rope, double Dutch, singing the rhymes. Cinderella, dressed in yella, went upstairs to kiss a fella. The boys played marbles for keeps, and if you lost your best shooter, you lost it forever. Danny lost his whole bag of cat's-eyes to a fifth grader in one afternoon and cried all the way home.""",
   "1950s girls jumping rope double dutch sidewalk", "DOUBLE DUTCH")
sc("""After school, it was hopscotch drawn with a piece of chalk, and kick-the-can in the street until supper. There were maybe twenty children on Elm Street, and we all played together, big ones and little ones. No one organized it. No one drove us anywhere. You just walked out your front door and the game was already going.""",
   "1950s children playing kick the can street", "THE GAME WAS ALREADY GOING")

ch("The queen")
sc("""In June, a young woman was crowned queen in England. Queen Elizabeth. She was only twenty-seven. They flew the film across the ocean on airplanes, and it was on American television the same day. My mother cried. She'd never been to England and never would, but she cried anyway, watching that girl in that crown, because she said she looked so alone.""",
   "1953 Queen Elizabeth coronation crowd London", "JUNE 2, 1953")
sc("""For weeks after that, every girl on Elm Street played queen. We made crowns out of the gold foil from Hershey bars and wore our mothers' old curtains for robes. Linda was always the queen. I was always the lady-in-waiting. I didn't mind. Well, I minded a little.""",
   "1950s girls playing dress up crowns backyard", "LINDA WAS ALWAYS THE QUEEN")

ch("Our street")
sc("""Our street had visitors every week. The milkman, early in the morning, rattling the glass bottles. The bread man from the bakery. The Fuller Brush man with his suitcase of brushes, who always gave my mother a free little vegetable brush just for opening the door. And the knife sharpener, who rang a bell and sharpened your scissors on a stone wheel right on the sidewalk for a dime.""",
   "1950s Fuller Brush man door to door salesman", "THE FULLER BRUSH MAN")
sc("""On Sundays we went to church at Trinity Lutheran, all dressed up. I had white gloves and a hat with elastic under the chin, and Danny had a clip-on bow tie he pulled off the minute we got outside. Then Sunday dinner at one o'clock. Pot roast, mashed potatoes, green beans from the garden, and Grandma Pearl's apple pie. Every Sunday, the same. I could cook it with my eyes closed now.""",
   "1950s family Sunday dinner pot roast table", "POT ROAST AT ONE")
sc("""After dinner my father took us for a drive in the Plymouth, out past the farms, and we stopped at the Dairy Queen for a cone. A nickel for a small one. My mother had hers in a cup so it wouldn't drip on her dress. My father always ate his in about three bites and then looked sadly at the empty napkin. That was Sunday, every week, for years.""",
   "1950s family car Dairy Queen ice cream cone", "A NICKEL FOR A CONE")

ch("Summer")
sc("""Summer in nineteen fifty-three was hot. No air conditioning, of course. We slept with the windows open and a wet washcloth on our foreheads, and on the worst nights Father dragged the mattresses out onto the screened porch. You could hear every cricket and every car on Route Thirty. I loved it.""",
   "1950s screened porch summer night", "MATTRESSES ON THE PORCH")
sc("""In the daytime we disappeared. Danny and I would leave after breakfast and come home when the streetlights came on. We rode our bicycles everywhere, no helmets, sometimes two on one bike. We went to the creek and caught crayfish. We drank out of the garden hose. Nobody knew where we were, and nobody worried.""",
   "1950s children riding bicycles summer street", "HOME WHEN THE STREETLIGHTS CAME ON")
sc("""And on Saturday afternoons there was the movie matinee downtown. A quarter got you in, a nickel got you popcorn. A newsreel, a cartoon, a serial that ended with the hero hanging off a cliff, and then the movie. That summer it was Peter Pan, from Walt Disney. I went three times. Danny went to see a movie in three-D, with paper glasses, and screamed when the creature came out of the screen.""",
   "1950s children movie theater 3D glasses audience", "A QUARTER TO GET IN")

ch("The war ends")
sc("""On the twenty-seventh of July, the radio said the fighting in Korea was over. An armistice, they called it. Not a victory, just a stop. Three years of fighting, and more than thirty-six thousand American boys gone. Two of them from Mansfield that I knew of. The older brother of a boy in my class never came home.""",
   "1953 Korean War armistice soldiers", "JULY 27, 1953")
sc("""There were no parades, honey. Not like nineteen forty-five. People were just tired. My father read the paper, folded it, and went out to mow the lawn. He'd been called up for Korea in nineteen fifty and then they didn't need him after all, and I think he felt something about that he never said. He mowed that lawn for two hours.""",
   "1950s man mowing lawn suburban house", "HE MOWED THE LAWN")

ch("What things cost")
sc("""Now, prices. A loaf of bread was about sixteen cents. A gallon of milk, about ninety cents, delivered to the door by the milkman in his white truck. A stamp was three cents. Gas was about twenty-nine cents a gallon. A brand-new Chevrolet was around sixteen hundred dollars. And my father made about seventy-five dollars a week at the Westinghouse plant.""",
   "1950s milkman delivery truck bottles doorstep", "SIXTEEN CENTS")
sc("""And here's a thing that came out that year. The TV dinner. Swanson's, in a little aluminum tray with three parts. Turkey, cornbread stuffing, peas and sweet potatoes, for about ninety-eight cents. My mother thought it was a crime. Grandma Pearl said it was the end of civilization. Danny begged for one for a year.""",
   "1950s Swanson TV dinner aluminum tray", "THE END OF CIVILIZATION")
sc("""And the new Chevrolet Corvette came out too, a little white sports car with no roof. Only about three hundred were made that first year. Not one of them ever drove down Elm Street, but every boy in Mansfield had a picture of it torn out of a magazine. Danny had his taped over his bed until he was twelve.""",
   "1953 Chevrolet Corvette white convertible", "THE CORVETTE")

sc("""That fall, my mother let me walk downtown by myself for the first time, nine years old, with a dollar in my coat pocket and a list. A spool of white thread, a card of buttons, and a pound of coffee. I walked those six blocks like I owned the whole city. The lady at the dry goods store called me Miss Miller. I came home ten feet tall.""",
   "1950s girl walking downtown sidewalk shops autumn", "MISS MILLER")

ch("Afraid")
sc("""And we were afraid, honey. Of different things than you. Of polio, every summer. Of the atomic bomb. The Russians had tested a hydrogen bomb that August, and in school we practiced getting under our desks. Of communists. Senator McCarthy was on the radio every week, saying there were communists everywhere. In the government. In Hollywood. Maybe next door.""",
   "1950s school duck and cover drill children desks", "AFRAID")
sc("""Mrs. Pruitt next door said the new family at the end of the street might be communists, because they had a lot of books and didn't go to church. My mother said, Edna, they're Lutherans. They go to the early service. That was the end of that. But that's how it was. Everybody watched everybody.""",
   "1950s neighbors talking over fence suburban", "EVERYBODY WATCHED EVERYBODY")

ch("Christmas")
sc("""And then it was December, and the Kowalskis invited the whole street over to watch the Christmas shows on their television. That winter they even talked about color television, brand new, but nobody we knew would see one for years. We sat on their floor in our pajamas, in black and white, and it was the most wonderful thing in the world.""",
   "1950s family Christmas television living room", "BLACK AND WHITE")
sc("""On Christmas morning there was a big box under our tree, and it was a television. Our own. My father had been saving for two years. A twenty-one-inch Motorola. My mother cried, and Danny ran around the room in circles, and my father just stood there with his coffee and smiled. That was nineteen fifty-three, sweetheart. The year the world came into our living room.""",
   "1950s family new television set Christmas morning", "OUR OWN TELEVISION")

ch("What I learned")
sc("""So that was nine. No phone, no computer, one television for fifteen people. We were afraid of things we couldn't see, and we spent all day outside anyway. I don't want you to think it was perfect, sweetheart. But I'd give a lot for one more summer night on that porch, on a mattress, listening to the crickets.""",
   "1950s summer evening small town houses porch", "ONE MORE SUMMER NIGHT")
sc("""Tell me in the comments. What year were you nine? And what was the first television in your family like? Goodnight, sweetheart. Grandma Ruth will be right here with another story tomorrow.""",
   "1950s vintage television set living room lamp", "WHAT YEAR WERE YOU NINE?")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("grandma10", "I Was 9 in 1953. This Is What America Was Really Like",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Inauguration of Dwight D. Eisenhower, 20 January 1953.",
      "I Love Lucy, 'Lucy Goes to the Hospital', 19 January 1953: about 44 million viewers.",
      "Coronation of Queen Elizabeth II, 2 June 1953.",
      "Korean War Armistice Agreement, 27 July 1953; about 36,500 US deaths in the war.",
      "Swanson TV dinner introduced 1953 at 98 cents.",
      "Chevrolet Corvette introduced 1953; 300 built that model year.",
      "Soviet test of the RDS-6s thermonuclear device, 12 August 1953.",
      "Disney's Peter Pan released February 1953; the 3-D film boom of 1953."],
     "one year of her life", minutes=(12, 14.5), voice="en_US-lessac-high")
