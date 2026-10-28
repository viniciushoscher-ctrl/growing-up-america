import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 07 · angle 1 (one year of her life, her age + the exact year) · Billionaires Histories, new format
# I Was 18 in 1962. Here's What America Was Really Like
# Grandma Ruth: born 1944 in Mansfield, Ohio; graduated high school in June 1962; married Tommy Callahan in 1963. Every price and event is real.

sc("""Sweetheart, you're eighteen next spring, aren't you? Your mother told me. Eighteen. Well, let me tell you what eighteen looked like for me. It was nineteen sixty-two. I was finishing high school in Mansfield, Ohio. And that was the year a man flew around the whole world in a tin can, and the year we all went to bed one night in October not sure we'd wake up.""",
   "1960s teenage girl portrait high school", "EIGHTEEN IN 1962")
sc("""I'm going to tell you all of it. What things cost, what we wore, what we were scared of, and what we did on a Saturday night. Because when people talk about the sixties now, they talk about hippies and protests. That came later, honey. In sixty-two we were still wearing white gloves to church.""",
   "1962 American main street cars", "BEFORE THE SIXTIES")

ch("Senior year")
sc("""My senior year, I got up at six. I set my hair the night before on pink sponge rollers and slept on them, which is about as comfortable as sleeping on a bag of walnuts. Then a whole can of Aqua Net to hold it. We wore skirts to school, every day. Girls weren't allowed to wear pants to class. Not even in January, with the snow up to your knees.""",
   "1960s girls hair rollers bedroom", "PINK SPONGE ROLLERS")
sc("""We had a dress code you wouldn't believe. Skirts had to touch the floor when you knelt down, and the vice principal really would make you kneel in the hallway to check. Boys couldn't let their hair touch their collar. A boy in my class got sent home for wearing blue jeans. Blue jeans! That was for working on the farm, not for school.""",
   "1960s high school hallway students lockers", "KNEEL DOWN")
sc("""After school I worked at the Woolworth's downtown, three afternoons a week and all day Saturday, for a dollar an hour. I gave half to my mother for the house, because that's what you did. The other half went into a coffee can on my dresser, and I'll tell you what I was saving for in a minute.""",
   "1960s teenage girl store clerk counter", "A DOLLAR AN HOUR")

ch("John Glenn")
sc("""Now, the twentieth of February, nineteen sixty-two. That morning they rolled a television set into our school auditorium, a big one on a cart, and the whole school sat on the floor and watched. John Glenn, a Marine from New Concord, Ohio, not even two hours from our house, was going up in a rocket called Friendship Seven.""",
   "1962 John Glenn Friendship 7 launch", "FRIENDSHIP 7")
sc("""The Russians had already put a man up the year before, and we were all a little ashamed about that. So when that rocket went up off the pad in Florida, the whole auditorium screamed like it was a football game. He went around the earth three times in less than five hours. Our teacher, Mr. Hoover, cried. A grown man, our chemistry teacher, cried.""",
   "1962 Mercury rocket launch Cape Canaveral", "THREE TIMES AROUND")
sc("""And then there was a problem. A light came on saying the heat shield might be loose. If it came off, he'd burn up coming back down. For a few minutes nobody in the room said a word. Then he splashed down in the ocean and they picked him up, and he was fine. Ohio went crazy. He got a ticker-tape parade in New York with four million people.""",
   "1962 John Glenn parade New York ticker tape", "SPLASHDOWN")

ch("What things cost")
sc("""Let me tell you what things cost, honey, because you'll laugh. Gas was about thirty-one cents a gallon. A loaf of bread was twenty cents. A stamp was four cents, until January of sixty-three, when it went up to five and everybody complained like it was a robbery. A hamburger at the drive-in was fifteen cents.""",
   "1960s gas station attendant pump", "THIRTY-ONE CENTS")
sc("""A brand new Chevrolet was about two thousand five hundred dollars. A nice house was around twelve thousand. My father made about ninety dollars a week at the Westinghouse plant, and we were comfortable. The minimum wage was a dollar fifteen. You could live on one paycheck, a whole family, with a mother at home. I know that sounds like a fairy tale now.""",
   "1962 Chevrolet new car showroom", "ONE PAYCHECK")
sc("""And here's what was in my coffee can. Seventy-two dollars by May. I was saving for my graduation dress and a pair of real nylon stockings, and if anything was left, a transistor radio. A little one you could carry in your pocket, made in Japan. It cost about twenty dollars. With that radio, I could listen to WHK out of Cleveland under my covers at night.""",
   "1960s transistor radio teenager", "THE COFFEE CAN")

ch("The music")
sc("""Oh, the music. That year everybody was doing the Twist. Chubby Checker's song had come back to number one in January, and every grownup in America was trying it, even my mother, in the kitchen, when she thought nobody was looking. Then there was Ray Charles, I Can't Stop Loving You. And the Four Seasons, Sherry. The boys all tried to sing it high like Frankie Valli. They couldn't.""",
   "1960s teenagers dancing twist party", "THE TWIST")
sc("""Television changed that year too. In July they sent the first live television picture across the Atlantic Ocean, from a satellite called Telstar. We saw France and England live, in our own front room, and my father said, well, now I've seen everything. And in October a young man from Nebraska named Johnny Carson took over The Tonight Show. My parents were never up that late. I was.""",
   "1960s family watching television living room", "TELSTAR")
sc("""On Saturday nights there was a dance at the YMCA, a quarter to get in. A record player, a punch bowl, and a chaperone standing by the wall making sure everyone left room for the Holy Spirit between them. That's what they called it, honey. The Holy Spirit. Six inches. The chaperone had a ruler.""",
   "1960s teenage dance gymnasium chaperone", "ROOM FOR THE HOLY SPIRIT")
sc("""That's where I really got to know your grandfather, Tommy Callahan. He'd taught me to drive two summers before in his father's truck, and now he was twenty and working at the plant. He wore his hair slicked back and smelled like Old Spice. He asked me to dance to a slow song, and he left exactly six inches. I was so disappointed.""",
   "1960s young couple slow dance", "TOMMY CALLAHAN")

ch("Graduation")
sc("""We graduated in June, in the gymnasium, in the heat. Four hundred of us in maroon gowns. My father wore his only suit. My mother wore a hat with a little net veil. And Grandma Pearl sat in the front row and clapped louder than anyone, because she had left school at twelve to work in a laundry. I was the first girl in our family to finish high school.""",
   "1960s high school graduation caps gowns", "JUNE 1962")
sc("""Now, here's something you won't believe. In my class, most of the girls I knew were already engaged, or would be by Christmas. Eighteen, nineteen. That was normal. If a girl wasn't married by twenty-two or twenty-three, the aunts started whispering. Only a few of us went to college, and the counselor told the girls to be a teacher, a nurse or a secretary. Those were the choices.""",
   "1960s young women secretaries typing office", "TEACHER, NURSE OR SECRETARY")
sc("""That summer of sixty-two was a hot one. On Sundays the whole family drove out to Charles Mill Lake with a cooler full of baloney sandwiches and a watermelon. No sunscreen, honey. We rubbed baby oil on our arms to get brown faster, and some girls used a sheet of tinfoil under their chin like a mirror. I peeled like an onion every August. Every single August.""",
   "1960s family lake beach summer picnic", "BABY OIL AND TINFOIL")
sc("""And in August, the radio said Marilyn Monroe had died, in Los Angeles. She was only thirty-six. The girls at the Woolworth's counter talked about nothing else for a week. I had a picture of her from a magazine taped inside my closet door. My mother made me take it down when I was twelve. I put it back up when I was sixteen.""",
   "1962 Marilyn Monroe newspaper headline", "AUGUST 1962")
sc("""That summer two new kinds of stores opened, and nobody in Mansfield paid any attention. In Arkansas a man named Sam Walton opened his first Wal-Mart. And outside Detroit, the Kresge company opened its first Kmart. We all thought downtown would be there forever. It wasn't, honey. But that's another story.""",
   "1960s discount department store shoppers aisles", "SUMMER 1962")

ch("Thirteen days")
sc("""And then came October. On Monday, the twenty-second, President Kennedy came on every channel at seven o'clock at night. We all sat in front of our Motorola. He said the Russians had put nuclear missiles in Cuba, ninety miles from Florida. And that any missile fired from Cuba would be treated as an attack by the Soviet Union on the United States.""",
   "1962 Kennedy television address Cuban missile crisis", "OCTOBER 22, 1962")
sc("""I want you to understand what that meant to us. We had grown up with the duck and cover drills. Since I was in third grade, the teacher would yell drop, and we'd crawl under our wooden desks and put our hands over our necks. As if a desk would stop an atomic bomb. But we believed it. We were children.""",
   "1950s duck and cover school drill", "DUCK AND COVER")
sc("""At school the next day, nobody could think about chemistry. The teachers had us practice the drill again, all of us lined up in the basement hallway, sitting against the wall with our heads between our knees. A girl named Carol started crying and couldn't stop. And the principal came on the loudspeaker and asked us to pray. In a public school. Nobody thought twice about it then.""",
   "1960s school students civil defense drill hallway", "THE BASEMENT HALLWAY")
sc("""That week, people in Mansfield bought out the grocery stores. Canned soup, bottled water, flashlight batteries. A man two streets over had a bomb shelter in his backyard, and everybody suddenly wanted to be his friend. My father didn't say much, as usual. He just filled the bathtub with water every night before bed. Every night. That frightened me more than the television.""",
   "1960s fallout shelter family backyard", "HE FILLED THE BATHTUB")
sc("""At the Woolworth's, nobody bought anything but candles. Tommy came by the counter on Thursday and said, Ruthie, if this is the end of the world, I don't want to go without asking you something. And I said, Tommy Callahan, don't you dare ask me anything at a Woolworth's lunch counter. So he didn't. Not then.""",
   "1960s lunch counter young man woman", "DON'T YOU DARE")
sc("""On Sunday, the twenty-eighth, it was on the radio that Khrushchev had agreed to take the missiles out. The church bells rang, I remember. My mother cried into her dish towel. And my father drained the bathtub. Thirteen days, honey. For thirteen days the whole world held its breath, and I was eighteen and thought I'd never get to be nineteen.""",
   "1962 newspaper headline Soviet missiles Cuba", "THE 28TH OF OCTOBER")

ch("Christmas")
sc("""That Christmas felt different. Everyone held on a little tighter. We went to church on Christmas Eve, and the place was so full people stood in the back. My brother Danny, who was fifteen, sang in the choir and his voice cracked on O Holy Night, and nobody laughed, not even me.""",
   "1960s church Christmas Eve candlelight", "CHRISTMAS EVE 1962")
sc("""And on Christmas night, Tommy came over for pie. And on our front porch, under the light, in the cold, with my father pretending not to watch from the window, he asked me. Not at a lunch counter. He had a ring that cost him four weeks' pay, and I said yes before he finished the question.""",
   "1960s couple front porch winter night", "UNDER THE PORCH LIGHT")

ch("What I learned")
sc("""So that was eighteen. No phone in my pocket. No computer. A transistor radio and a coffee can. We were scared of the bomb, and we did the Twist anyway. We thought the world could end on a Tuesday, and we went to work on Wednesday. I'm not telling you it was better, honey. Some of it was terrible. But we knew how to keep going.""",
   "1960s small town street evening", "WE KEPT GOING")
sc("""Now, tell me in the comments, if you were there. Where were you during those thirteen days in October? And what did your father do? I'd love to know if he filled the bathtub too. Goodnight, sweetheart. Grandma Ruth will be right here with another story tomorrow.""",
   "1960s family home living room lamp", "WHERE WERE YOU?")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("grandma07", "I Was 18 in 1962. Here's What America Was Really Like",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "John Glenn's Friendship 7 orbital flight, 20 February 1962; New York ticker-tape parade, 1 March 1962.",
      "Cuban Missile Crisis, 16-28 October 1962; President Kennedy's televised address, 22 October 1962.",
      "First Wal-Mart opened in Rogers, Arkansas, 2 July 1962; first Kmart in Garden City, Michigan, 1962.",
      "US first-class stamp rose from 4 to 5 cents on 7 January 1963.",
      "Federal minimum wage $1.15 an hour from September 1961.",
      "'The Twist' by Chubby Checker returned to number one on the Billboard Hot 100 in January 1962.",
      "Death of Marilyn Monroe, 4-5 August 1962; Telstar 1 relayed the first live transatlantic television, July 1962.",
      "Johnny Carson became host of The Tonight Show on 1 October 1962.",
      "Duck and Cover, US Federal Civil Defense Administration film, 1951."],
     "one year of her life", minutes=(12, 14.5), voice="en_US-lessac-high")
