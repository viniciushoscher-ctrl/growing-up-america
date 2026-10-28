import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 03 · angle 3 (a walk through a place that disappeared: Woolworth's) · Billionaires Histories, new format
# I Worked at Woolworth's in 1960. Here's What It Was Really Like Inside
# Grandma Ruth is a narrated character: born in 1944 in Mansfield, Ohio. Every price and date is real.

sc("""Sweetheart, you go to the mall, or you push a button on your phone and a box shows up on the porch. When I was sixteen, there was one store on Main Street that had everything in the world inside it. And I worked there. Let me walk you through the front door of the F. W. Woolworth Company, Mansfield, Ohio, nineteen sixty.""",
   "1950s Woolworth store front main street", "WOOLWORTH'S, 1960")
sc("""People called it the five and dime. When Mister Woolworth started it, back in eighteen seventy-nine, everything in the store cost five cents or ten cents. By my time, prices had gone up a little, but the name stuck. There were thousands of them across America. And now there's not a single one left. Not one. So come on. I'll show you what you missed.""",
   "vintage five and dime store interior", "THE FIVE AND DIME")

ch("The front door")
sc("""First, the sign. Big red letters, gold trim, right across the top of the building. The doors were heavy wood and glass, and they had a brass push plate that was worn down smooth from a million hands. When you opened them, a smell came out. I can still smell it. Popcorn, floor wax, perfume, and roasting nuts, all at once.""",
   "1950s department store entrance doors", "THAT SMELL")
sc("""The floor was wooden boards, oiled every week, and it creaked in the same places every day. You could tell who was coming down the aisle by the creak. The ceiling was pressed tin, way up high, with ceiling fans going round and round. No air conditioning in our store until nineteen sixty-two. In the summer the fans just moved the hot air from one side to the other.""",
   "vintage store interior wooden floor ceiling fans", "THE CREAKING FLOOR")

ch("My first job")
sc("""I got the job the summer I turned sixteen. Mrs. Lambert, the floor manager, looked at my hands, looked at my shoes, and asked me to count out change for a dollar and thirty-seven cents. I did it right, and she said, you start Saturday. I was paid seventy-five cents an hour. Thirty hours a week. That was twenty-two dollars and fifty cents, and I felt like a millionaire.""",
   "1950s teenage girl working store counter", "SEVENTY-FIVE CENTS AN HOUR")
sc("""We wore a uniform. A blue smock with a white collar and my name on a little pin. Ruth. No makeup that was too bright, no gum, no sitting down. Ever. If there were no customers, you dusted. If there was no dust, Mrs. Lambert found some.""",
   "1950s shop girls uniform store", "NO SITTING DOWN")

ch("The counters")
sc("""Now, the store wasn't shelves like today, sweetheart. It was counters. Long wooden counters with glass on top, divided into little sections, and a girl behind each one. You didn't grab things yourself. You pointed, and the girl handed it to you. Thread, buttons, ribbon, hairpins, all in little bins with the price on a card.""",
   "1950s five and dime counters merchandise", "THE COUNTERS")
sc("""The notions counter was the busiest. A spool of thread was ten cents. A card of buttons, fifteen. A package of needles, five. Every woman on our street sewed her own clothes, and her children's clothes, and Woolworth's was where she came for everything but the cloth.""",
   "1950s sewing notions thread buttons", "TEN CENTS A SPOOL")
sc("""Then there was the cosmetics counter, and that's where I wanted to work. Tangee lipstick, the orange one that turned pink on your lips. Evening in Paris perfume, in a cobalt blue bottle, for about a dollar. Pond's cold cream. Little compacts with a mirror inside. The teenage girls stood there for an hour after school, trying on everything and buying nothing. I know. I was one of them.""",
   "vintage cosmetics counter lipstick perfume", "EVENING IN PARIS")
sc("""The toy counter at Christmas was a madhouse. Slinkies. Hula hoops, which had come out two years before and every child in America wanted one. Paper dolls, jacks, marbles, cap guns, yo-yos. The kids pressed their noses on the glass until it was all smudged, and I had to wipe it twenty times a day.""",
   "1950s toy store christmas children", "NOSES ON THE GLASS")

sc("""Right by the front door was the candy counter, and it was the most dangerous place in the store for a sixteen-year-old girl on her feet all day. Chocolate creams, peanut clusters, orange slices, all piled up behind glass and sold by weight. A quarter pound of chocolate stars for twenty cents. The girl weighed it on a little silver scale and poured it into a paper bag with a scoop.""",
   "vintage candy counter scale scoop", "SOLD BY THE POUND")
sc("""And the nut machine. A big glass case with a heat lamp inside, and cashews and Spanish peanuts turning slowly under the light. That's what made the whole store smell so good. They put it by the door on purpose, sweetheart. Mister Woolworth was no fool. You walked in for a spool of thread, and you walked out with a bag of hot cashews.""",
   "vintage roasted nuts display store", "HOT CASHEWS")

ch("The pets")
sc("""And in the back, sweetheart, we had pets. Yes. Real ones. A whole corner with goldfish in glass tanks, ten cents a fish. Parakeets in cages, singing all day long. And baby turtles, little green turtles the size of a quarter, in a plastic bowl with a plastic palm tree. Every child in Mansfield had one of those turtles at some point.""",
   "vintage pet department goldfish parakeets", "TEN CENTS A FISH")
sc("""The turtles were later banned, by the way. In nineteen seventy-five. They carried salmonella, and children put them in their mouths, because of course they did. Danny had one named Ike. It lived for eleven years, longer than his marriage. Don't repeat that.""",
   "baby turtle pet bowl", "A TURTLE NAMED IKE")

ch("The lunch counter")
sc("""But the heart of the store, honey, was the lunch counter. It ran all along one side. Red stools that spun, chrome trim, a long Formica counter, and a mirror behind it so you could watch yourself eat. There were pies under glass domes, and a big soda machine, and a grill that never turned off.""",
   "1950s Woolworth lunch counter stools", "THE LUNCH COUNTER")
sc("""A grilled cheese was twenty-five cents. A hot dog was twenty. A cup of coffee was a dime, and the waitress kept filling it for nothing. The ladies from the courthouse came in at noon, every day, the same stools, and ordered the same thing. Tuna on white toast and a cherry Coke.""",
   "1950s diner food grilled cheese coffee", "A DIME FOR COFFEE")
sc("""And here's my favorite thing in the whole store. Above the counter hung a row of balloons. Inside each balloon was a little piece of paper with a price. When you ordered a banana split, you got to pop a balloon. Inside it said one cent, or nineteen cents, or the full thirty-nine. Every child in the store would gather around and scream when somebody got the penny.""",
   "1950s banana split ice cream sundae", "POP A BALLOON")
sc("""I'll tell you a secret. Mrs. Lambert knew which balloon had the penny. And when a little boy came in alone, with his hands full of nickels and his face dirty, she would point at the right one. She never said a word about it. She just pointed.""",
   "1950s boy eating ice cream counter", "SHE JUST POINTED")

ch("Greensboro")
sc("""Now I have to tell you something that's not so sweet, because you should know. That same year, nineteen sixty, on the first of February, four young Black college students sat down at the Woolworth's lunch counter in Greensboro, North Carolina. And they asked for a cup of coffee. And they were refused. Because in the South, that counter was for white people only.""",
   "1960 Greensboro sit-in Woolworth lunch counter", "GREENSBORO, 1960")
sc("""They didn't leave. They came back the next day, with more students. And the next. Within weeks there were sit-ins at lunch counters in dozens of cities. People poured ketchup on their heads. They burned them with cigarettes. They sat there anyway. By July, that Greensboro counter was serving everybody.""",
   "1960 civil rights sit-in students", "THEY SAT THERE ANYWAY")
sc("""In Mansfield, our counter served anybody who had a quarter. But I'll be honest with you. When we heard about Greensboro on the radio in the stockroom, some of the girls said those students were troublemakers. I didn't say anything. I wish I had. Part of that counter is in the Smithsonian today. Someday you go see it, and you think about how brave they were.""",
   "Smithsonian Woolworth lunch counter museum", "I WISH I HAD")

ch("Saturdays")
sc("""On Saturdays the whole town came downtown. Farmers in from the county with their wives, boys in letter jackets, mothers with three kids and a list. The store was so packed you couldn't turn around. The register rang all day, that big brass National cash register, with the little numbers that popped up in the window. Ching.""",
   "1950s busy main street saturday shoppers", "SATURDAY DOWNTOWN")
sc("""There was a photo booth by the door. Four pictures for a quarter. You pulled the curtain, and you made faces, and two minutes later a wet strip of photos came out of a slot. Your grandfather and I took four pictures in that booth on our second date. I still have them. They're in the shoebox in my closet, if you want to see.""",
   "vintage photo booth strip couple", "FOUR FOR A QUARTER")
sc("""And there was the record counter. Forty-fives were about sixty-nine cents. The boys would ask me to put on a record so they could listen before they bought it, and they'd listen to the whole thing, and then not buy it. Every Saturday. Elvis, the Everly Brothers, Chubby Checker doing the Twist. I knew every word to every song that year.""",
   "1960s teenagers record store 45 records", "SIXTY-NINE CENTS")

sc("""Christmas was the hardest. We stayed open until nine at night, and the line at my register went all the way back to the hardware. People bought tinsel, glass ornaments from Germany, strings of big colored bulbs, and those little ceramic angels with the gold wings. I wrapped presents in red paper until my fingers bled. And on Christmas Eve, Mrs. Lambert gave every girl a box of chocolates and a silver dollar.""",
   "1950s christmas ornaments store display", "A SILVER DOLLAR")

ch("The end")
sc("""I worked at Woolworth's for two summers and one Christmas. Then I went on to other things. But the store stayed. For years. Every time I went downtown, I went in, just to smell it and sit at the counter. Mrs. Lambert retired in nineteen seventy-one. The waitress, Marge, was there until the end.""",
   "1970s main street downtown stores", "TWO SUMMERS AND ONE CHRISTMAS")
sc("""And then the malls came, honey. And then the big stores out by the highway, with the giant parking lots. Main Street got quieter every year. Our Woolworth's closed in the nineteen-eighties. I don't remember the exact day. Nobody does. That's how these places go. Nobody throws a funeral. One day you drive by and it's a cell phone store.""",
   "empty downtown storefront closed", "NOBODY THREW A FUNERAL")
sc("""In July of nineteen ninety-seven the company closed the last of its Woolworth's stores in America. Four hundred stores, all at once. It was on the news for about one minute. A hundred and eighteen years. Gone. The company is still around under another name, selling sneakers. But the five and dime is gone forever.""",
   "1990s closed store going out of business", "1879 TO 1997")

ch("What I miss")
sc("""You know what I miss most? It's not the prices, although a grilled cheese for a quarter would be nice. It's that everybody went to the same place. The banker's wife and the farmer's wife stood at the same counter, buying the same thread. You saw your whole town there. You can't buy that with a button on your phone.""",
   "1950s women shopping together store", "THE WHOLE TOWN")
sc("""So the next time you're in one of those big stores, sweetheart, I want you to imagine a red stool that spins, and a balloon over your head with a penny inside. And a lady named Mrs. Lambert who knows which one to point at. That was Woolworth's.""",
   "vintage soda fountain red stools chrome", "THAT WAS WOOLWORTH'S")
sc("""Now tell me, did your grandparents have a five and dime in their town? What was it called? Tell me in the comments, I'd love to know. And come back tomorrow, because Grandma has a lot more stories. Goodnight, sweetheart.""",
   "1950s house at night porch light", "GOODNIGHT, SWEETHEART")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("grandma03", "I Worked at Woolworth's in 1960. Here's What It Was Really Like Inside",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "F. W. Woolworth opened his first five-cent store in 1879; the last ~400 US Woolworth's closed in July 1997 (company later renamed Foot Locker).",
      "Greensboro sit-in began 1 February 1960; the Greensboro counter was desegregated 25 July 1960. A section is at the Smithsonian's National Museum of American History.",
      "Woolworth's banana split balloon promotion (1-39 cents), 1950s-60s.",
      "Hula hoop introduced by Wham-O, 1958.",
      "FDA ban on sale of turtles under 4 inches, 1975.",
      "Evening in Paris (Bourjois) and Tangee lipstick, popular US cosmetics of the 1940s-60s."],
     "a walk through a place that disappeared (Woolworth's)", minutes=(12, 14.5), voice="en_US-lessac-high")
