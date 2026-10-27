import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 27 · angle 3 (an everyday theme, "what happened to") · evening slot · day 9
# What Happened to the Soda Fountain?

sc("""There was a time when every town in America had one. You walked into the drugstore, past the cough syrup and the greeting cards, and there it was. A long marble counter. A row of chrome stools with red leather tops. Shining spigots, glass jars of syrup, and a young man in a white paper hat, ready to make you anything you wanted.""",
   "1950s drugstore soda fountain counter stools", "THE SODA FOUNTAIN")
sc("""At its peak, America had more than a hundred thousand soda fountains. They were where kids went after school, where couples went on dates, and where old men sat every morning with a cup of coffee. Today, only a few hundred remain, most of them in museums, or kept alive by a handful of stubborn owners.""",
   "1950s teenagers soda fountain booth", "MORE THAN 100,000")
sc("""So what happened to the soda fountain? Let's go back to where it started, how it became the heart of American towns, what you could order there, and why it disappeared.""",
   "1950s small town drugstore exterior", "WHAT HAPPENED?")

ch("Medicine in a glass")
sc("""The soda fountain started with medicine. In the early eighteen hundreds, people believed that bubbly mineral water from natural springs was good for their health. Scientists figured out how to make carbonated water artificially, and pharmacists began selling it as a cure for upset stomachs, headaches and nerves.""",
   "19th century pharmacy apothecary", "IT STARTED AS MEDICINE")
sc("""Pharmacists began adding flavors. Lemon, ginger, sarsaparilla, root beer. Then came sweeter syrups like vanilla, strawberry and chocolate. And some of those drinks became world famous. In eighteen eighty-five, a pharmacist in Waco, Texas, created Dr Pepper. In eighteen eighty-six, a pharmacist in Atlanta, John Pemberton, created Coca-Cola.""",
   "John Pemberton Coca-Cola pharmacist", "1886: COCA-COLA")
sc("""Coca-Cola was first sold at Jacobs' Pharmacy in Atlanta, for five cents a glass, from the soda fountain. In eighteen ninety-three, a pharmacist in New Bern, North Carolina, invented a drink he called Brad's Drink. A few years later, he renamed it Pepsi-Cola. Most of America's great soft drinks were born at a soda fountain counter.""",
   "Pepsi Cola New Bern North Carolina", "BORN AT THE COUNTER")
sc("""The fountains themselves became works of art. In the late eighteen hundreds, companies built huge soda fountains of marble, onyx and silver, some as tall as a room, decorated with statues and fancy lamps. They cost thousands of dollars, a fortune at the time. A grand soda fountain was a sign that a town had arrived.""",
   "Victorian marble soda fountain", "WORKS OF ART")

ch("Temperance and the ice cream soda")
sc("""The ice cream soda was born in eighteen seventy-four, in Philadelphia. According to the most popular story, a man named Robert Green was selling soda at a celebration and ran out of cream. So he used vanilla ice cream instead. The crowd loved it. Within a few years, ice cream sodas were the rage all over the country.""",
   "ice cream soda glass", "1874: THE ICE CREAM SODA")
sc("""Then came the sundae. Some towns had laws against selling soda on Sundays, because soda was seen as too indulgent for the Lord's day. So, the story goes, fountain owners served ice cream with syrup on top, and no soda. They called it a Sunday, and later changed the spelling to sundae. Several towns still argue about who invented it.""",
   "ice cream sundae dish", "THE SUNDAY SUNDAE")
sc("""And then, Prohibition. When alcohol was banned in nineteen twenty, the saloons closed. And many of them turned into soda fountains. Some bartenders became soda jerks. The soda fountain became the respectable place to meet friends and socialize. During the twenties, soda fountains boomed.""",
   "1920s soda fountain drugstore interior", "PROHIBITION")
sc("""Even the Great Depression didn't kill the soda fountain. A nickel Coke or a dime sundae was one of the few treats that struggling families could still afford. Some drugstores served cheap lunches to people out of work. And during the Second World War, soda fountains near army bases were packed with young soldiers far from home.""",
   "1930s drugstore soda fountain customers", "THROUGH THE DEPRESSION")

ch("The soda jerk")
sc("""The man behind the counter was called a soda jerk, because of the way he jerked the spigot handle back and forth to pour carbonated water. Being a soda jerk was a great job for a teenage boy. It paid decently, it was fun, and you got to talk to everyone in town, especially the girls.""",
   "1950s soda jerk white hat counter", "THE SODA JERK")
sc("""Soda jerks had their own slang, a fast language shouted to each other across the counter. Adam's ale was a glass of water. Burn one meant a chocolate malted. Eighty-six meant we're out of it. Hold the hail meant no ice. A pair of drawers was two cups of coffee. And a black cow was a root beer float.""",
   "1950s soda fountain counter man", "BURN ONE")
sc("""Good soda jerks were showmen. They tossed scoops of ice cream in the air and caught them in the glass. They slid sodas down the counter. They knew every regular customer's order by heart. Many famous people worked as soda jerks when they were young, and many said it taught them how to talk to anybody.""",
   "1950s soda jerk making sundae", "SHOWMEN")

ch("What you could order")
sc("""So what could you order? The menu was long. A cherry Coke, made fresh with a squirt of cherry syrup. A lime rickey. A chocolate egg cream, which had neither eggs nor cream, just milk, chocolate syrup and seltzer. A root beer float, or a Coke float with vanilla ice cream.""",
   "1950s soda fountain menu board", "THE MENU")
sc("""There were milkshakes, made in a tall metal cup on a green Hamilton Beach mixer, and served with the extra in the cup on the side. There were malteds, made with malted milk powder. And there was the banana split, three scoops with chocolate, strawberry and pineapple sauce, whipped cream, nuts and a cherry on top.""",
   "1950s milkshake mixer metal cup", "THE MALTED")
sc("""Many soda fountains also served lunch. Grilled cheese, tuna salad sandwiches, egg salad, chicken noodle soup and hot dogs. In the fifties, a sandwich and a Coke might cost about forty cents. Women shopping downtown stopped in for a light lunch. Businessmen sat at the counter with a newspaper.""",
   "1950s lunch counter sandwich soda", "LUNCH AT THE COUNTER")
sc("""The prices were small. In nineteen fifty, a Coke at the fountain was usually a nickel, as it had been for more than fifty years. An ice cream soda was around fifteen to twenty cents. A sundae, twenty-five. A banana split, thirty-five cents. With a quarter, a kid could have a very good afternoon.""",
   "1950s children soda fountain counter", "A NICKEL COKE")
sc("""And the fountain had its own special sounds. The hiss of the carbonated water. The whir of the mixer. The clink of the long spoon against a tall glass. The pop of a straw being pulled out of a paper wrapper, and then the wrapper being blown across the counter at your little brother.""",
   "1950s milkshake glass straw counter", "THE SOUNDS")

ch("The heart of the town")
sc("""By the nineteen forties and fifties, the soda fountain was the heart of American towns. After school, it filled with teenagers. They crowded the booths, played the jukebox, flirted, gossiped and did homework. Many first dates happened there, over two straws in one milkshake.""",
   "1950s teenagers soda fountain booth jukebox", "TWO STRAWS")
sc("""In the morning, the counter belonged to the regulars. Farmers, shop owners, retired men and the town's police officer. They drank coffee, read the paper and settled the problems of the world. In many towns, important business deals were made over a cup of coffee at the drugstore counter.""",
   "1950s men drinking coffee counter morning", "THE REGULARS")
sc("""The soda fountain was also a place where kids learned to be grown-ups. They ordered on their own, paid with their own money, and minded their manners, because the pharmacist knew their parents. And if they misbehaved, word got home before they did.""",
   "1950s boy ordering soda counter", "WORD GOT HOME")
sc("""Some soda fountains were famous far beyond their towns. Schwab's Pharmacy in Hollywood was said to be where movie stars were discovered. Walgreens built its early reputation on its fountains, and is often credited with popularizing the malted milkshake in the nineteen twenties. For millions of Americans, Walgreens meant a milkshake before it meant a prescription.""",
   "1920s Walgreens drugstore", "SCHWAB'S AND WALGREENS")

ch("A place of struggle")
sc("""But not every American was welcome at the soda fountain. In much of the South, lunch counters were segregated by law, and Black customers were refused service. On February first, nineteen sixty, four Black college students sat down at the Woolworth's lunch counter in Greensboro, North Carolina, and asked for coffee.""",
   "Greensboro sit-in Woolworth lunch counter 1960", "GREENSBORO, 1960")
sc("""They were refused, but they stayed in their seats until the store closed. The next day, they came back with more students. Within weeks, sit-ins had spread to dozens of cities. By that summer, the Greensboro Woolworth's lunch counter was integrated. Part of that counter is now in the Smithsonian in Washington.""",
   "Greensboro Woolworth counter Smithsonian", "THE SIT-INS")

ch("The decline")
sc("""So what happened? Part of the answer is the bottle and the can. In the forties and fifties, soft drinks in bottles became cheap and easy to buy at the grocery store. By the sixties, cans were common too. Families bought six-packs and kept them in the refrigerator at home. There was no need to go out for a Coke.""",
   "1950s soda bottles six pack grocery store", "THE SIX-PACK")
sc("""Another part of the answer is the car and the drive-in. In the fifties and sixties, teenagers had cars, and they wanted to go where they could park and eat. Drive-in restaurants and then fast food chains like McDonald's, which began franchising in nineteen fifty-five, offered burgers, fries and shakes quickly and cheaply.""",
   "1950s drive-in restaurant carhop", "THE DRIVE-IN")
sc("""Then the drugstores themselves changed. Big chain pharmacies like Walgreens, Rexall and Eckerd grew larger, and they found that the space taken by a soda fountain could earn more money selling cosmetics, greeting cards and other merchandise. The fountains took a lot of labor, and the profit was small.""",
   "1960s chain drugstore interior", "THE CHAIN DRUGSTORE")
sc("""And finally, downtown itself was emptying. As shopping moved to the malls on the edge of town, the old drugstores on Main Street lost their customers. One by one, through the sixties and seventies, the fountains were torn out. Marble counters were broken up. Stools were sold for scrap.""",
   "1970s empty downtown main street", "TORN OUT")
sc("""By the nineteen seventies, the soda fountain was largely gone. Some survived in dime stores and department stores into the eighties. Woolworth's kept its lunch counters until the very end of the company, in nineteen ninety-seven. But for most Americans, the soda fountain had become a memory.""",
   "1970s Woolworth lunch counter", "A MEMORY")

ch("The survivors")
sc("""But not all of them are gone. Across America, a few hundred old-fashioned soda fountains still operate. Some have been running for more than a hundred years. Places like the Lexington Candy Shop in New York City, which opened in nineteen twenty-five, and old family drugstores in small towns across the Midwest and South.""",
   "Lexington Candy Shop New York", "STILL OPERATING")
sc("""Many of them are run by families who have owned them for generations. They still use the original marble counters and the old syrup pumps. They still make cherry Cokes by hand. And on a summer afternoon, you'll find grandparents bringing their grandchildren, to show them what a real malted tastes like.""",
   "old fashioned soda fountain counter today", "A REAL MALTED")
sc("""And the soda fountain lives on in other ways. Every milkshake, every root beer float, every banana split you've ever eaten came from that counter. So did Coca-Cola, Pepsi and Dr Pepper. The soda fountain may be mostly gone, but its menu is still everywhere.""",
   "root beer float glass", "ITS MENU IS EVERYWHERE")

ch("What we lost")
sc("""What we lost wasn't really the soda. It was the place. A counter where strangers sat side by side. A soda jerk who knew your name. A booth where you shared a milkshake with your first love. A place where the whole town, young and old, came together over something sweet.""",
   "1950s soda fountain customers counter", "IT WAS THE PLACE")
sc("""If you grew up with a soda fountain, you remember the sound of the spinning stool, the hum of the mixer, the clink of the long spoon on the glass. And you remember exactly what you always ordered. That's how much it meant.""",
   "1950s soda fountain stools chrome", "WHAT YOU ALWAYS ORDERED")
sc("""So tell us in the comments. What was the name of your drugstore, and what did you always order at the soda fountain? Did you ever work behind the counter? We read every comment. Next time, we're going back to life on an American farm in nineteen fifty-five. Thank you for spending this time with me.""",
   "1950s drugstore soda fountain", "WHAT DID YOU ORDER?")

save("video27", "What Happened to the Soda Fountain?", [
    "Over 100,000 soda fountains in the U.S. at their peak (1920s-1950s): Anne Cooper Funderburg, Sundae Best: A History of Soda Fountains (2002)",
    "Dr Pepper created 1885 in Waco, Texas; Coca-Cola created 1886 by John Pemberton, first sold at Jacobs' Pharmacy: Dr Pepper Museum; The Coca-Cola Company",
    "Pepsi-Cola, originally 'Brad's Drink' (1893), Caleb Bradham, New Bern, North Carolina: PepsiCo",
    "Robert M. Green and the ice cream soda, Philadelphia, 1874: Funderburg, Sundae Best",
    "Soda jerk slang: H. T. Webster and others; American Speech journal (1936)",
    "Coca-Cola price of five cents from 1886 to 1959: The Coca-Cola Company; Daniel Levy and Andrew Young, 'The Real Thing' (2004)",
    "Greensboro sit-in, February 1, 1960; counter section at the Smithsonian National Museum of American History",
    "McDonald's franchising began April 1955 (Ray Kroc, Des Plaines, Illinois): McDonald's Corporation",
    "Woolworth's U.S. five-and-dime stores closed in 1997: The New York Times",
    "Lexington Candy Shop, New York City, opened 1925",
], "angle 3 · an everyday theme", minutes=(12, 14.5))
