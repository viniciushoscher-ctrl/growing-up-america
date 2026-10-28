import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 04 · angle 1 (one year of her life, her age + the exact year) · Billionaires Histories, new format
# I Was 20 in 1964. Here's What America Was Really Like
# Grandma Ruth: born 1944 in Mansfield, Ohio; married Tommy Callahan in 1963. Every price and event is real.

sc("""Sweetheart, sit here by me. You asked me what year I would go back to, if I could go back to just one. Well, I've thought about it. It's nineteen sixty-four. I was twenty years old. I'd been married for six months. And the whole country felt like it was waking up from a bad dream and dancing at the same time.""",
   "1960s young married couple portrait", "IF I COULD GO BACK")
sc("""You have to understand how that year began. Two months before, in November of sixty-three, President Kennedy was shot in Dallas. I was at the Woolworth's counter when the radio said it, and every person in that store stopped and cried. Grown men. The whole country was in mourning that Christmas. Nobody felt like celebrating anything.""",
   "1963 Kennedy funeral crowd mourning", "NOVEMBER 1963")

ch("Our first home")
sc("""Your grandfather and I lived in a little apartment over a hardware store on North Main Street in Mansfield. Two rooms and a kitchen the size of a closet. The rent was seventy-five dollars a month, and that felt like a fortune. The radiator banged all night, and the man downstairs sold paint, so the whole place smelled like turpentine. I thought it was a palace.""",
   "1960s small apartment kitchen young wife", "SEVENTY-FIVE DOLLARS A MONTH")
sc("""Your grandfather worked at the Westinghouse plant, like my father, on the line that made electric ranges. He made about two dollars and forty cents an hour. I worked at the bank downtown as a teller, until I was expecting, because in those days, sweetheart, a lot of places let you go when you started to show. Nobody thought that was strange. It was just the rule.""",
   "1960s factory workers assembly line appliances", "TWO FORTY AN HOUR")
sc("""We had one car, a nineteen fifty-seven Ford that your grandfather bought used for four hundred dollars. Gas was about thirty cents a gallon. On Sunday afternoons we'd fill it up for three dollars and just drive, out past the farms to Malabar Farm and back, with the windows down and the radio on. That was a date. It didn't cost anything.""",
   "1950s Ford car country road", "SUNDAY DRIVES")

ch("The night the Beatles came")
sc("""And then came the ninth of February. A Sunday. I will never forget it. The Beatles were on The Ed Sullivan Show. We didn't have a television yet, so we went to my parents' house on Elm Street. My brother Danny was sixteen, and he had combed his hair down over his forehead for the occasion. My father thought he looked like a sheepdog.""",
   "1964 Beatles Ed Sullivan Show", "FEBRUARY 9, 1964")
sc("""Seventy-three million people watched that night, honey. Almost half the country. When those four boys started playing I Want to Hold Your Hand, the girls in the studio audience screamed so loud you could barely hear the music. Danny was jumping up and down on the couch. And my father, who never said anything, put down his paper and said, well, they can sing. I'll give them that.""",
   "1964 Beatlemania screaming girls audience", "73 MILLION")
sc("""By April the Beatles had the top five songs in the whole country at the same time. Nobody had ever done that before. Every radio station played them every hour. Your grandfather pretended he didn't like them. Then I caught him singing She Loves You in the shower. Yeah, yeah, yeah. He never lived it down.""",
   "1960s teenagers listening records radio", "THE TOP FIVE")

ch("What things cost")
sc("""Now let me tell you what things cost, because you won't believe me. A loaf of bread was twenty-one cents. A gallon of milk was about a dollar. A first-class stamp was five cents. A movie ticket was a dollar. A brand new house in a nice part of town was about eighteen thousand dollars. And the minimum wage was a dollar twenty-five an hour.""",
   "1960s supermarket prices shopping cart", "TWENTY-ONE CENTS")
sc("""In April Ford came out with a new car called the Mustang. It was so pretty it stopped traffic. The base price was two thousand three hundred and sixty-eight dollars. They sold twenty-two thousand of them on the very first day. Your grandfather stood in front of the dealership window on Park Avenue for twenty minutes like a little boy looking at a bicycle. We couldn't afford it. We couldn't afford it for ten years.""",
   "1964 Ford Mustang new car showroom", "THE MUSTANG")
sc("""We did our shopping at the A and P on Saturday, and I had a budget of fifteen dollars a week for food. Fifteen dollars. That bought meat for every night, a roast on Sunday, eggs, butter, coffee, and a box of Jell-O for dessert. And I clipped every coupon in the Mansfield News Journal, and I saved S and H Green Stamps in little books, to trade for a toaster.""",
   "1960s housewife green stamps grocery", "GREEN STAMPS")

sc("""And at the bank, sweetheart, I saw something every day that would make you angry. A woman could come to my window and deposit her own paycheck. But if she wanted a loan, or a charge account at the department store, she needed her husband to sign. Even if she earned more than he did. Even a widow had trouble. That didn't change until nineteen seventy-four. I'd stamp her papers and keep my mouth shut. Everybody did.""",
   "1960s bank teller window customers", "HER HUSBAND HAD TO SIGN")

ch("The world's fair")
sc("""That summer the World's Fair opened in New York. Everybody wanted to go. It had a giant steel globe, twelve stories high, called the Unisphere, and pavilions from all over the world, and things nobody had ever seen. A telephone where you could see the other person's face. A computer, a real one, the size of a room, that could answer questions.""",
   "1964 New York World's Fair Unisphere", "THE WORLD'S FAIR")
sc("""We drove there in August, your grandfather and me, in that old Ford. It took two days. We slept in the car one night outside Harrisburg. At the General Motors pavilion they had a ride called Futurama that showed you the world of tomorrow, with cities under the ocean and on the moon. We stood in line for two hours. I thought, by the time I'm old, we'll all be living on the moon. Well. Here I am, sweetheart. Still in Ohio.""",
   "1964 World's Fair Futurama General Motors", "THE WORLD OF TOMORROW")
sc("""And Disney had made a boat ride for the Pepsi pavilion, with hundreds of little dolls from every country singing the same song. It's a Small World. I cried on it. I don't know why. I was twenty years old and I'd never seen anything but Ohio, and here were children from the whole world, singing together. It just got me.""",
   "1964 World's Fair It's a Small World pavilion", "IT'S A SMALL WORLD")

ch("The summer of 1964")
sc("""But it wasn't all music and fairs, honey. That summer, on the second of July, President Johnson signed the Civil Rights Act. It made it against the law to keep people out of a restaurant or a hotel or a job because of the color of their skin. You'd be amazed how many people in our town were angry about that. Some of them sat in my own family's church.""",
   "1964 Johnson signing Civil Rights Act", "THE CIVIL RIGHTS ACT")
sc("""And three young men who went to Mississippi that summer to help Black families register to vote disappeared. They were found in August, buried in a dam. Two of them were from New York, one from Mississippi. I remember your grandfather reading that in the paper at breakfast and putting it down and not eating his eggs. He said, that's somebody's son. Three somebodies.""",
   "1964 Freedom Summer civil rights volunteers", "FREEDOM SUMMER")
sc("""And there was a place on the other side of the world called Vietnam, that most of us couldn't find on a map. In August the president said our ships had been attacked in a place called the Gulf of Tonkin, and Congress gave him the power to fight. It was a little story on page four. Nobody on Elm Street thought much about it. Danny was sixteen. He was going to be a mechanic.""",
   "1964 Gulf of Tonkin navy destroyer", "PAGE FOUR")

ch("Home and family")
sc("""Every Saturday morning I had my hair done at the beauty parlor on Park Avenue, a dollar fifty for a wash and set. The beehive was the style that year, piled up high with a whole can of Aqua Net. You slept on a satin pillow and you didn't touch it for a week. And Danny, honey, Danny spent every dollar he had on a nineteen fifty-two Chevy that didn't run. He spent the whole summer under it, in my father's driveway, singing Beach Boys songs. Little Deuce Coupe. Over and over.""",
   "1960s beehive hairdo beauty salon", "A WHOLE CAN OF AQUA NET")
sc("""In the evenings we listened to the radio, because we still didn't have a TV of our own. Your grandfather would read the sports page and I'd sew. I made almost all my own clothes. A Simplicity pattern cost thirty-five cents, and a yard of cotton was about fifty cents. I made a blue dress that summer that I wore to every wedding for five years.""",
   "1960s young woman sewing machine home", "A SIMPLICITY PATTERN")
sc("""On Sundays we went to dinner at my mother's. Pot roast, mashed potatoes, green beans from the garden and a pie. Every single Sunday. My father carved, my mother served, and Danny ate like a horse. There was a new empty chair at that table that year. My grandmother, Pearl, had passed away the October before. Nobody sat in her chair. Not for a long time.""",
   "1960s family sunday dinner table", "THE EMPTY CHAIR")
sc("""And in September, sweetheart, I found out I was expecting. Your Aunt Susan. I told your grandfather in the car, in the parking lot of the A and P, because I couldn't wait until we got home. He was so happy he drove into the shopping cart corral. We had to pay for two carts. He didn't care.""",
   "1960s young couple happy car", "THE SHOPPING CARTS")

ch("Fall and the election")
sc("""That fall was the election. Johnson against Senator Goldwater from Arizona. The commercials were frightening. There was one with a little girl picking petals off a daisy, and then a countdown, and an atomic bomb. They only showed it once, but everybody talked about it for weeks. Johnson won by a landslide. Forty-four states.""",
   "1964 presidential election Johnson campaign", "THE DAISY")
sc("""And the Surgeon General had said in January that cigarettes caused cancer. It was on the front page of every newspaper. And you know what? Everybody kept smoking. Your grandfather smoked Pall Malls until nineteen seventy-five. In nineteen sixty-four, honey, you could still smoke in the hospital waiting room while your wife had a baby.""",
   "1960s man smoking cigarette newspaper", "THE SURGEON GENERAL")
sc("""Christmas that year, your grandfather surprised me. He'd been working double shifts in secret for two months. On Christmas morning there was a television in the corner of our little apartment, a Zenith, black and white, nineteen inches. Two hundred dollars. Bonanza on Sunday nights. I think I cried more over that television than I did at our wedding.""",
   "1960s vintage television christmas living room", "THE ZENITH")

ch("What I miss")
sc("""So that was nineteen sixty-four, sweetheart. It wasn't perfect. Nothing ever is. There was a war starting that would break my family's heart, and there were people fighting for rights they should have had all along. But we didn't know what was coming. We were young, we were in love, and the Beatles were on the radio.""",
   "1960s young couple dancing", "WE DIDN'T KNOW")
sc("""What I miss most is how little we needed. Two rooms, one car, fifteen dollars a week for food, and a radio. And we thought we were rich. Because we had each other, and Sunday dinner, and a whole future out there that looked like the World's Fair. That feeling. That's what I'd go back for.""",
   "1960s couple porch evening", "HOW LITTLE WE NEEDED")
sc("""Now, what year would you go back to, if you could? And if your grandparents were young in sixty-four, ask them where they were the night the Beatles came on. Tell me in the comments. And come back tomorrow, sweetheart. Grandma has a lot more stories. Goodnight.""",
   "1960s house at night porch light", "GOODNIGHT, SWEETHEART")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("grandma04", "I Was 20 in 1964. Here's What America Was Really Like",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "The Beatles on The Ed Sullivan Show, 9 February 1964: about 73 million viewers (Nielsen).",
      "Billboard Hot 100, 4 April 1964: the Beatles held the top five positions.",
      "Ford Mustang introduced 17 April 1964, base price $2,368; about 22,000 orders on the first day.",
      "1964-65 New York World's Fair opened 22 April 1964 (Unisphere, GM Futurama, 'it's a small world').",
      "Civil Rights Act signed 2 July 1964. Chaney, Goodman and Schwerner found 4 August 1964.",
      "Gulf of Tonkin Resolution, 7 August 1964. Surgeon General's report on smoking, 11 January 1964.",
      "US prices 1964: stamp 5 cents, federal minimum wage $1.25, gasoline about 30 cents a gallon."],
     "one year of her life (her age + the exact year)", minutes=(12, 14.5), voice="en_US-lessac-high")
