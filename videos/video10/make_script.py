import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 10 · angle 1 (a place and a time: one day in a factory town, hour by hour) · morning slot · day 4
# What Life in a 1950s Factory Town Was Really Like

sc("""Five-thirty in the morning, nineteen fifty-five. It's still dark. In a thousand kitchens across town, a light comes on at the same moment. Coffee is percolating. Lunch pails are being packed. And down by the river, behind a chain-link fence, the smokestacks of the mill are already breathing white into the cold air.""",
   "1950s factory smokestacks morning", "5:30 IN THE MORNING")
sc("""This is a factory town. One big employer, and everything else built around it. The steel mill, the paper mill, the auto plant, the glass works, the textile mill. In the nineteen fifties, millions of Americans lived in towns like this, from Pennsylvania to Michigan to the Carolinas.""",
   "1950s steel mill town houses", "ONE TOWN, ONE EMPLOYER")
sc("""Today we're going to spend one whole day there, from the first whistle in the morning to the last light in the tavern at night. The work, the houses, the families, the union hall and the ball field. This is what life in a nineteen fifties factory town was really like.""",
   "1950s factory workers walking gate", "ONE DAY IN A MILL TOWN")

ch("Before the whistle")
sc("""In the kitchen, mother packs the lunch pail. Two sandwiches, usually bologna or leftover meatloaf on white bread. An apple. A slice of pie wrapped in wax paper. And a thermos of hot coffee, clipped into the curved lid of a black metal pail that her husband has carried for fifteen years.""",
   "1950s wife packing lunch pail kitchen", "THE LUNCH PAIL")
sc("""Father eats standing up, in his work clothes. Heavy boots. Denim or canvas trousers. A flannel shirt, even in summer, because the sparks and the hot metal don't care what season it is. He kisses his wife, rubs the head of the youngest child still asleep at the table, and walks out the door.""",
   "1950s worker leaving house morning", "OUT THE DOOR")
sc("""Most of the men walk to work. The houses were built close to the plant on purpose, decades earlier, often by the company itself. Rows of narrow frame houses on steep streets, with small front porches and backyards just big enough for a clothesline and a vegetable garden.""",
   "1950s company houses row street", "THE COMPANY HOUSES")
sc("""The streets fill with men walking in the same direction, lunch pails swinging, cigarettes glowing in the dark. Fathers, sons, brothers, neighbors. In a lot of families, three generations worked at the same plant. The grandfather on the pension, the father on the floor, and the son just hired on last spring.""",
   "1950s workers walking to mill", "THREE GENERATIONS")

ch("The shift")
sc("""At six forty-five the whistle blows, loud enough to hear all over town. Everybody in town sets their clocks by it. The men line up at the time clock, find their card in the rack, and punch in. One minute late is still late, and the foreman notices.""",
   "1950s factory time clock workers", "THE WHISTLE")
sc("""Inside, the noise is tremendous. Machines pounding. Furnaces roaring. Overhead cranes rumbling along their tracks. In a steel mill, the heat near the open hearth could make a man's face feel like it was on fire. The men talk with hand signals, or shout right into each other's ears.""",
   "1950s steel mill workers furnace", "THE NOISE AND THE HEAT")
sc("""It was hard work, and it could be dangerous work. Most men had a scar, a missing fingertip, or a story about the day a cable snapped. Safety rules existed, but they were looser than today. Hard hats and goggles were becoming common, but earplugs were rare, and many of those men grew hard of hearing by fifty.""",
   "1950s factory worker goggles machine", "A DANGEROUS JOB")
sc("""And yet, the men were proud of what they made. The steel in the new bridges. The glass in the windows of the new suburbs. The cars on every highway in America. When a man drove past a skyscraper or a dam, he could tell his children, our mill made the steel for that.""",
   "1950s steel beams construction bridge", "WE MADE THAT")
sc("""The foreman ran the floor. He was usually an older man who had come up through the ranks, worked every job in the plant, and knew every machine by its sound. He wore a white shirt instead of work clothes, and a different colored hard hat. Some foremen were feared. The good ones were respected for life.""",
   "1950s factory foreman supervising", "THE FOREMAN")
sc("""At lunchtime, the whistle blows again. The men sit on crates and benches, open their pails, and trade sandwiches and stories. Who's sick. Who's getting married. Which foreman is in a bad mood. And always, always, how the high school team is going to do on Friday night.""",
   "1950s workers lunch break factory", "LUNCH AT THE MILL")

ch("The union")
sc("""In nineteen fifty-five, about one in three American workers outside of agriculture belonged to a union. In factory towns, it was often nearly everybody on the plant floor. The union hall was down the street from the plant, with a flag out front and folding chairs inside.""",
   "1950s union hall meeting workers", "ONE IN THREE")
sc("""The union negotiated the wages, the hours, the vacation and the pension. A contract might bring a raise of a few cents an hour, a week of paid vacation, and health insurance for the family. For a man whose own father had worked twelve-hour days for very little, those contracts felt like a miracle.""",
   "1950s union contract signing", "THE CONTRACT")
sc("""When contracts ran out and talks broke down, there were strikes. The men walked the picket line in shifts, carrying signs, keeping warm around barrels with fires burning inside. Wives brought coffee and sandwiches. Strikes could last weeks or months, and families lived on savings, strike pay and help from neighbors.""",
   "1950s workers picket line strike", "THE PICKET LINE")
sc("""In nineteen fifty-five, the two biggest labor groups in the country, the A F of L and the C I O, merged into one. For the men on the plant floor, it was a sign of how powerful unions had become. Many of them would later say those were the best years for the American working man.""",
   "1950s labor union convention", "1955: THE MERGER")
sc("""Wages in those plants were good for the time. A steelworker or an autoworker might earn around two dollars an hour in the mid-fifties, about twice the minimum wage. With overtime, a man could buy a house, a new car every few years, and a cottage on a lake for summer weekends.""",
   "1950s worker family new car driveway", "TWO DOLLARS AN HOUR")

ch("The town")
sc("""Everything in town depended on the plant. When the plant was busy, the stores on Main Street were busy. The car dealer sold new Chevrolets. The bakery sold birthday cakes. The bank gave out mortgages. When the plant laid men off, the whole town felt it within a week.""",
   "1950s small town main street stores", "WHEN THE PLANT WAS BUSY")
sc("""On every corner, it seemed, there was a church and a tavern. The churches often belonged to the different groups who had come to work at the plant. Polish, Italian, Slovak, Irish, German, Black families who had come up from the South. Each had its own parish, its own festival and its own food.""",
   "1950s ethnic church festival", "A CHURCH ON EVERY CORNER")
sc("""The company was everywhere. It sponsored the Little League team and the bowling league. It built the community swimming pool, the library or the hospital wing. It held a picnic every summer, with games for the children and a hot dog for everybody. Some people loved the company. Some didn't. But nobody could ignore it.""",
   "1950s company picnic families", "THE COMPANY PICNIC")
sc("""Women ran the town while the men were at the plant. They shopped, cooked, cleaned, raised the children, ran the church suppers and the school bake sales. Some worked too, in the stores, the offices or the plant cafeteria. And many women in textile towns worked right on the mill floor, beside the men.""",
   "1950s women shopping town street", "THE WOMEN RAN THE TOWN")
sc("""Children grew up with the sounds of the plant in their ears. The whistle. The trains rolling into the yard at night. The glow of the furnaces on the clouds after dark, which some children thought was the most beautiful thing in the world. They knew that someday, many of them would work there too.""",
   "1950s children playing near factory", "THE GLOW ON THE CLOUDS")
sc("""There was a price for that glow. On some days the air smelled of sulfur, and the soot settled on windowsills and on the laundry hanging outside. Mothers wiped the porch railings every morning. Nobody talked much about pollution in nineteen fifty-five. People said it smelled like money, and they meant it.""",
   "1950s smoke factory town air", "IT SMELLED LIKE MONEY")

ch("After the shift")
sc("""At three o'clock, the whistle blows for the end of the day shift. The gates open and the men pour out, tired and dirty, as the next shift walks in. The plant never stopped. Three shifts, around the clock, every day of the week except a few holidays a year.""",
   "1950s shift change factory gate", "SHIFT CHANGE")
sc("""Many of the men stopped at the tavern on the corner on the way home. One beer, sometimes two. A shot and a beer, if it had been a hard day. The bartender knew everybody's order. A ball game was on the radio, or on the small television above the bar, and the arguments about it never ended.""",
   "1950s men tavern bar beer", "ONE BEER ON THE WAY HOME")
sc("""At home, dinner was on the table at five-thirty. Meat and potatoes, almost always. Pierogi on Friday in Polish homes, spaghetti on Sunday in Italian ones. The whole family sat down together, and the father got the biggest piece, because he had worked the hardest. Nobody argued about that.""",
   "1950s family dinner table working class", "DINNER AT 5:30")
sc("""After dinner, the men sat on the porch or worked in the garden. On summer evenings, the neighbors talked across the fences, and the children played in the street until dark. In the fall, the men went hunting on weekends. In the winter, there was the bowling league, the lodge, and church bingo.""",
   "1950s neighbors porch evening street", "THE PORCH IN THE EVENING")
sc("""The men on the night shift slept during the day, in bedrooms with heavy curtains, while the rest of the town went on outside. Their children learned to play quietly in the afternoons. Their wives learned to cook breakfast at three in the afternoon and dinner at midnight. In a factory town, every family lived on the plant's clock.""",
   "1950s woman cooking kitchen night", "THE NIGHT SHIFT FAMILY")

ch("Friday nights")
sc("""Friday was payday and game day. The paychecks came out at the end of the shift, and that evening the stores stayed open late. Then the whole town went to the high school football stadium, which was often named after a company founder, and sat in the bleachers under the lights.""",
   "1950s high school football crowd", "PAYDAY AND GAME DAY")
sc("""In mill towns, high school football was almost a religion. The players were the sons of the men in the bleachers. Many of them would be working beside their fathers within a year. And for a lot of those boys, Friday nights under the lights would be the best memory of their lives.""",
   "1950s high school football players", "ALMOST A RELIGION")
sc("""After the game, the teenagers went to the drive-in or the diner. The parents went home, or to the social club for a dance. And late at night, the whistle blew for the shift change again, and a new crew of men walked through the gate, as the town slept.""",
   "1950s teenagers diner night", "THE NIGHT SHIFT")
sc("""The men who did those jobs were not famous. Nobody wrote songs about them, at least not then. But in nineteen fifty-five, America produced more steel, more cars and more goods than any country on earth. And it happened because of towns like this one, and the men and women who woke up at five-thirty every morning.""",
   "1950s workers group portrait factory", "NOT FAMOUS, BUT ESSENTIAL")

ch("What happened to it")
sc("""For many of those towns, the good years didn't last. Starting in the late nineteen sixties and seventies, plants closed or moved away. Foreign competition, new technology and changing companies emptied out mills all over the country. The whistles went quiet. And the towns built around them had to find a way to survive.""",
   "1950s empty factory building", "WHEN THE WHISTLE STOPPED")
sc("""But if you grew up in a town like that, you remember it. The sound of the whistle. The smell of the mill when the wind changed. Your father's lunch pail on the kitchen counter. The pride in his voice when he said what his plant made. Those towns built America. And the people in them knew it.""",
   "1950s father daughter porch portrait", "THOSE TOWNS BUILT AMERICA")
sc("""So tell us in the comments. Did your father or grandfather work at a mill or a plant? What did they make? We read every comment, and we'd love to hear their stories. Next, we're going to a wedding in nineteen sixty-five. Thank you for spending this time with me.""",
   "1950s factory town sunset river", "WHAT DID YOUR FATHER MAKE?")

save("video10", "What Life in a 1950s Factory Town Was Really Like", [
    "Union membership about one third of nonagricultural workers in the mid-1950s: Bureau of Labor Statistics, Handbook of Labor Statistics; Monthly Labor Review",
    "AFL-CIO merger, December 5, 1955: AFL-CIO history",
    "Deindustrialization of manufacturing towns from the late 1960s: Bureau of Labor Statistics manufacturing employment series",
    "Film footage: Prelinger Archives (public domain) via the Internet Archive",
], "angle 1 · a place and a time", minutes=(12, 14.5))
