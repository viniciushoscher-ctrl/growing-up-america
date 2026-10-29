import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 13 · angle 3 (a walk through a place that disappeared) · Billionaires Histories, new format
# The Drugstore Soda Fountain, 1957. Here's What It Was Really Like
# Grandma Ruth: born 1944 in Mansfield, Ohio (13 in 1957); best friend Linda Kowalski; brother Danny. The drugstore is a composite; every product, price and date is real.

sc("""Sweetheart, you know that coffee place you like, where they write your name on the cup and it costs seven dollars? Let me tell you about the place I liked when I was thirteen. It was nineteen fifty-seven. It was on the corner of Main Street in Mansfield, Ohio. And for a nickel, a boy in a white paper hat would make you the best thing you ever tasted. Come with me to the soda fountain.""",
   "1950s drugstore soda fountain counter interior", "FOR A NICKEL")
sc("""Every town in America had one, honey. Sometimes three or four. It was inside the drugstore, and it was the center of the whole world if you were a teenager. Today they're almost all gone. So I'm going to walk you through it, from the front door to the back counter, and tell you what everything cost and who was sitting where.""",
   "1950s small town drugstore exterior main street", "THE CENTER OF THE WORLD")

ch("The front door")
sc("""Our drugstore was called Hoffman's, and it had a big glass front with gold letters, and a bell over the door that jingled. The first thing you saw was the magazine rack. Life, Look, the Saturday Evening Post with a Norman Rockwell on the cover. Photoplay and Modern Screen for the movie stars. And the comic books, a whole spinning rack of them, ten cents each.""",
   "1950s drugstore magazine rack comic books", "TEN CENTS EACH")
sc("""Mr. Hoffman didn't mind if you read them standing up, as long as you didn't bend the covers. Danny read every Superman and every Donald Duck in Ohio standing in front of that rack and never bought one. Mr. Hoffman knew. He'd say, Danny Miller, that's the third time you've read that one this week. And Danny would say, I'm studying, Mr. Hoffman.""",
   "1950s boy reading comic book store rack", "I'M STUDYING")
sc("""Next to the door there was a big penny scale. You stood on it, put in a penny, and a card came out with your weight on one side and your fortune on the other. You will meet a tall dark stranger. Linda and I weighed ourselves every single day after school, and every single day she got a better fortune than me. I'm still a little bitter about it.""",
   "vintage penny weight scale fortune drugstore", "YOUR WEIGHT AND FORTUNE")

sc("""And in the summer, there was the sign. A big blue banner over the door with icicles painted on the letters. Air Conditioned. Cool Inside. In nineteen fifty-seven almost nobody had air conditioning at home, sweetheart. So on the hottest days of July, half of Mansfield found a reason to buy aspirin. You'd walk in from the street and the cold hit you like jumping in the lake. People stood by the door just to breathe.""",
   "1950s air conditioned sign store summer", "COOL INSIDE")

ch("The pharmacy")
sc("""In the back was the real drugstore. Mr. Hoffman in a white coat, behind a high counter, with glass jars of colored water in the window and a hundred little drawers. He'd been there since before my mother was born. He mixed some of the medicines himself, with a mortar and pestle. And if you were sick, you didn't call a doctor first. You asked Mr. Hoffman.""",
   "1950s pharmacist white coat counter drugstore", "ASK MR. HOFFMAN")
sc("""He sold everything back there. Aspirin, Vicks, Ipana toothpaste, Brylcreem for the boys, Toni home permanents for the girls, Evening in Paris perfume, film for your Brownie camera. You dropped off the film and came back in a week for your pictures, with white wavy edges. And he knew everybody's business. Every prescription in town. He never said one word to anyone. That was his religion.""",
   "1950s drugstore shelves products cosmetics", "HE KNEW EVERYBODY'S BUSINESS")

ch("The counter")
sc("""But the soda fountain, honey. That was along the whole left wall. A long marble counter, cool to your arms in August, with chrome stools that spun around, covered in red leather. Behind it a big mirror, so you could watch yourself drinking a soda and see the boys come in behind you without turning around. Linda said that mirror was the most important invention in history.""",
   "1950s soda fountain counter stools chrome mirror", "THE MIRROR")
sc("""Behind the counter stood the soda jerk. That's what they called the boy who made the drinks, because he jerked the tap handle back to pour the soda water. Ours was Bobby Shaw, sixteen, with a white jacket, a white paper hat, and a bow tie. He could slide a glass down twenty feet of counter and stop it in front of you without spilling a drop. Every girl in the ninth grade was in love with Bobby Shaw.""",
   "1950s soda jerk white paper hat counter", "BOBBY SHAW")

ch("What we drank")
sc("""Now, the menu. A Coca-Cola from the fountain was a nickel. Bobby made it right there, a squirt of syrup in the glass and then the fizzy soda water from the tap. You could ask for a cherry Coke, or a vanilla Coke, and he'd add a squirt of something else. Or a lime rickey. Or a phosphate, which was soda water with a little acid in it, sour and fizzy, that nobody under eighty has ever heard of.""",
   "1950s soda jerk making drink drugstore fountain", "A NICKEL FOR A COKE")
sc("""A milkshake was twenty or twenty-five cents. Bobby made it in a tall steel cup on a green Hamilton Beach mixer that whined like an airplane. A malted was a milkshake with a spoonful of malted milk powder, and it tasted like heaven. And he'd give you the glass and the steel cup too, with the leftovers in it, so you really got two milkshakes. Two milkshakes for a quarter, sweetheart.""",
   "1950s milkshake mixer steel cup soda fountain", "TWO MILKSHAKES FOR A QUARTER")
sc("""And the banana split, for thirty-five cents, if somebody else was paying. Three scoops, vanilla, chocolate and strawberry, a banana cut the long way, chocolate sauce, pineapple, strawberries, whipped cream, chopped nuts, and a cherry on top of each one. Linda and I split one every Friday. That's why it's called a split, Linda said. She was wrong, but I let her think so.""",
   "1950s banana split ice cream sundae dish", "THE BANANA SPLIT")

sc("""And the ice cream soda, honey. That was the real queen of the fountain. Bobby put a squirt of chocolate syrup in a tall glass, a splash of milk, soda water from the tap, and then two scoops of vanilla ice cream floating on top, with whipped cream. Fifteen cents. You ate it with a long spoon and drank it through a paper straw, and the bubbles went up your nose. My mother had one every Saturday after the grocery shopping. It was the only thing she ever bought just for herself.""",
   "1950s ice cream soda tall glass straw", "THE ONLY THING SHE BOUGHT FOR HERSELF")
sc("""And Grandma Pearl liked a root beer float, which she called a black cow, the way they did when she was a girl. She sat at the end of the counter on Saturday mornings with her pocketbook in her lap and told Bobby Shaw he was too skinny. He'd give her an extra scoop and say, don't tell Mr. Hoffman, Mrs. Miller. She never did.""",
   "1950s woman drugstore lunch counter", "A BLACK COW")

ch("The lunch counter")
sc("""At noon, the counter was full of grownups. Men from the bank and the stores, ladies from shopping, eating lunch on those red stools. A grilled cheese sandwich was about thirty cents. A BLT, forty. A bowl of chili. A slice of pie under a glass dome, with coffee, a quarter. The coffee came in a heavy white cup, and Bobby filled it again without asking until you put your hand over it.""",
   "1950s drugstore lunch counter diners sandwiches", "PIE AND COFFEE, A QUARTER")
sc("""And sweetheart, I have to tell you the hard part too. In a lot of the country, in nineteen fifty-seven, not everybody was allowed to sit at that counter. In the South, Black customers couldn't be served there at all. Three years later, in nineteen sixty, four young college students sat down at a Woolworth's lunch counter in Greensboro, North Carolina, and refused to leave until they were served. They changed the whole country from four stools.""",
   "1960 Greensboro sit-in lunch counter students", "FOUR STOOLS")

ch("The jukebox")
sc("""In the corner was the jukebox, a Wurlitzer, all lit up in red and gold and bubbling tubes. A nickel a song, six for a quarter. That year it was Elvis, All Shook Up and Jailhouse Rock. And Buddy Holly, That'll Be the Day. And Paul Anka, Diana. Danny would put in a nickel for Elvis and play it over and over until Mr. Hoffman came out from the back and pulled the plug.""",
   "1950s Wurlitzer jukebox colorful lights diner", "SIX FOR A QUARTER")
sc("""In the evenings, when school was out, the booths in the back were full of teenagers. Letter jackets and ponytails and saddle shoes. That's where you found out who was going steady, who had broken up, who was going to the sock hop on Saturday. It was our telephone and our newspaper and our television all in one, honey. And it all happened over a nickel Coke.""",
   "1950s teenagers booth diner letter jacket ponytail", "GOING STEADY")
sc("""And that's where I had my first date. Well, sort of. A boy named Gary Lutz from my class asked me if I wanted a Coke after school, and he paid. A whole nickel. We sat at the counter and didn't say one word to each other for ten minutes, staring at ourselves in the mirror. Then he said, well, see you, and left. Linda said it counted. I'm not sure it did.""",
   "1950s teenage boy girl soda fountain shy", "DID IT COUNT?")

sc("""In the fall of nineteen fifty-eight, Bobby Shaw joined the Army. On his last day, he made every girl in the store a free cherry Coke, and Mr. Hoffman pretended not to see. Linda cried into hers. Then a new soda jerk came, a boy named Ronnie with big ears, and within a month every girl in the ninth grade was in love with Ronnie. That's how it was, sweetheart. The stool never stayed empty for long.""",
   "1950s young man soldier uniform portrait", "THE NEW SODA JERK")

ch("The rules")
sc("""There were rules, sweetheart. No feet on the stools. No chewing gum stuck under the counter, though everybody did. Boys took their caps off. If you were loud, Mr. Hoffman would look at you over his glasses from the back, and that was enough. And if you didn't have the nickel, Bobby would give you a glass of water with a cherry in it, and call it a Shirley Temple, so you didn't feel poor.""",
   "1950s soda fountain cherry glass water counter", "A GLASS OF WATER WITH A CHERRY")

ch("Where it went")
sc("""So what happened to it? Little by little, it went away. In nineteen fifty-five a man named Ray Kroc opened a McDonald's in Illinois, fifteen-cent hamburgers, and soon there were drive-ins and burger stands out by the highways. Then the big chain drugstores came, and they didn't want a soda fountain. Too much work, too little money. They pulled the counters out and put in more shelves.""",
   "1950s McDonald's restaurant original golden arches", "FIFTEEN-CENT HAMBURGERS")
sc("""Hoffman's closed in nineteen seventy-one, when Mr. Hoffman retired. They took out the marble counter and the stools and the mirror and sold them at an auction. I heard a man from Columbus bought the mirror for his basement. Somewhere in Ohio, there's a mirror that has watched every girl in Mansfield fall in love with Bobby Shaw. I hope it's somewhere nice.""",
   "empty old drugstore building closed storefront", "THE MIRROR WENT TO COLUMBUS")
sc("""There are still a few soda fountains left in America, sweetheart. Old ones, kept by people who love them. If you ever see one, go in. Sit on the stool and spin around once. Order a cherry Coke from the fountain and watch them make it. And look in the mirror. You might see me there, thirteen years old, waiting for Bobby Shaw to slide me a glass.""",
   "vintage soda fountain still operating today", "SPIN AROUND ONCE")
sc("""Now tell me in the comments. What was the name of the drugstore in your town, and what did you order? I'll bet somebody out there remembers phosphates. Goodnight, sweetheart. Grandma Ruth will be right here with another story tomorrow.""",
   "1950s drugstore neon sign night street", "WHAT DID YOU ORDER?")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("grandma13", "The Drugstore Soda Fountain, 1957. Here's What It Was Really Like",
     ["Grandma Ruth is a narrated character built from real memories and records of the era. Hoffman's drugstore is a composite.",
      "Greensboro sit-ins at the Woolworth's lunch counter, beginning 1 February 1960.",
      "Ray Kroc's first McDonald's franchise, Des Plaines, Illinois, 15 April 1955; hamburgers 15 cents.",
      "Wurlitzer jukeboxes; 1957 hits including Elvis Presley's 'All Shook Up' and Buddy Holly's 'That'll Be the Day'.",
      "Hamilton Beach drink mixers, used in US soda fountains from the 1910s.",
      "US soda fountains peaked in the 1940s-50s and declined with chain drugstores and fast food."],
     "a walk through a place that disappeared", minutes=(12, 14.5), voice="en_US-lessac-high")
