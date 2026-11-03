import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 28 · Christmas recipe: oven-baked Christmas party mix (Google Trends 3/11: Chex, christmas snacks, homemade gifts rising)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, every Christmas Eve in my house, there's a big blue enamel roasting pan on the kitchen counter, full to the top with homemade party mix. Crunchy cereal, nuts, pretzels, all toasted in butter and Worcestershire sauce. By midnight it's empty, and the grandchildren are licking the salt off their fingers. That pan has been on my counter every Christmas Eve since nineteen sixty-one.""",
   "Christmas party mix roasting pan", "SINCE NINETEEN SIXTY-ONE")
sc("""But today, most people make it in the microwave, or they buy the bags at the store, and it comes out greasy, or soggy, or so salty you need a gallon of water. So tonight I'm giving you the old oven way. Every ingredient, every step, and the four mistakes that make party mix soggy. It's the best Christmas snack there is, and the easiest gift you'll ever give.""",
   "soggy snack mix bowl", "NEVER SOGGY")

ch("The recipe on the box")
sc("""This recipe came from the back of a cereal box. In the early nineteen fifties, the company that made Chex cereal started printing a party mix recipe on its boxes, and every mother in America cut it out. My mother taped hers to the inside of the cupboard door, next to the measuring cups. It stayed there until the tape turned brown and the paper fell apart in nineteen seventy.""",
   "1950s cereal box kitchen cupboard", "TAPED TO THE CUPBOARD DOOR")
sc("""In the fifties, it was the snack for company. When the neighbors came over to watch Perry Como's Christmas show on our little black and white television, my mother brought out a bowl of party mix and a bottle of Coca-Cola for each of them. Danny and I sat on the floor with our own little bowl, and we picked out all the nuts first and left the cereal.""",
   "1950s family watching television living room", "WE PICKED OUT THE NUTS")
sc("""I made my first batch as a young bride in nineteen sixty-one, for my husband's office Christmas party. I forgot to stir it, and the bottom burned black. I scraped the top half into a bowl and took it anyway. His boss ate three handfuls and asked who made it. From that day on, I never forgot to stir it again.""",
   "1960s office Christmas party", "I FORGOT TO STIR IT")

ch("What you need")
sc("""Here's what you need, honey, for one big roasting pan. Three cups each of corn Chex, rice Chex and wheat Chex. That's nine cups of cereal. One cup of mixed nuts, or peanuts if you're watching your pennies. One cup of small pretzels. And one cup of bagel chips or plain crackers, broken into bite-sized pieces. Any store brand cereal squares work just as well.""",
   "cereal nuts pretzels bowls", "NINE CUPS OF CEREAL")
sc("""For the butter coating. Six tablespoons of butter. Two tablespoons of Worcestershire sauce. One and a half teaspoons of seasoned salt. Three quarters of a teaspoon of garlic powder. Half a teaspoon of onion powder. That's it. My mother added a pinch of cayenne for my father, and I still do it for my son.""",
   "butter worcestershire sauce spices", "A PINCH OF CAYENNE")

sc("""A word about the nuts, honey. Mixed nuts are best, but they're the most expensive thing in the pan. Plain dry-roasted peanuts are half the price and taste wonderful toasted in butter. My mother used peanuts every year, and only on Christmas Eve did she splurge on a can of cashews. She'd pick them out herself and put them in a little dish just for my father.""",
   "mixed nuts cashews peanuts bowls", "A LITTLE DISH JUST FOR MY FATHER")

ch("Step by step")
sc("""Step one. Heat the oven to two hundred fifty degrees. That's low, sweetheart, and it's supposed to be. Party mix isn't baked, it's dried and toasted slowly. High heat burns the outside before the inside gets crisp. Low heat dries it all the way through, and that's what makes it crunchy for weeks.""",
   "oven dial low temperature", "LOW AND SLOW")
sc("""Step two. Put the cereal, nuts, pretzels and bagel chips in the biggest roasting pan you own. A big pan, so it's spread out, no deeper than two inches. If your pan is small, use two pans. A pile that's too deep steams in the middle, and steamed party mix is soggy party mix.""",
   "cereal mix roasting pan spread", "NO DEEPER THAN TWO INCHES")
sc("""Step three. Melt the butter in a small pot or in the microwave. Stir in the Worcestershire, seasoned salt, garlic powder and onion powder. Now pour it slowly over the mix, a little at a time, while you stir and turn everything gently with a big spoon. Pour, stir, pour, stir. Every piece should get a little shine. Not a soak. A shine.""",
   "pouring butter over snack mix", "A SHINE, NOT A SOAK")
sc("""Step four. Bake for one hour, and stir it every fifteen minutes. Set a timer, honey, because you will forget. When you stir, bring the pieces from the bottom and the corners up to the top. The corners brown fastest. Four stirs in one hour. That's how you get every piece golden and crisp, and no burned bottom like mine in nineteen sixty-one.""",
   "stirring snack mix in oven", "STIR EVERY FIFTEEN MINUTES")
sc("""Step five, and this is the one almost everybody skips. When it comes out of the oven, spread it out on paper towels or brown paper grocery bags, cut open flat on the counter, and let it cool completely, about an hour. The paper soaks up any extra butter, and the mix finishes getting crisp as it cools. If you put it in a tin warm, the steam turns it soft by morning.""",
   "snack mix cooling on paper towels", "COOL IT ON PAPER")

sc("""How do you know it's done? Take out one piece of the corn cereal, let it cool for a minute on the counter, and bite it. It should snap clean and taste toasty, with no chew at all. If it bends or feels a little tough, give the whole pan another ten minutes and check again. Humid days take longer. My kitchen in July and my kitchen in December are two different ovens.""",
   "testing crunchy cereal piece", "IT SHOULD SNAP")

ch("Four mistakes that make it soggy")
sc("""So the four mistakes, sweetheart. Mistake one, the microwave. Yes, it's on the box now, and yes, it's faster. But the microwave cooks it unevenly, some pieces chewy, some burned. The oven at two-fifty is the only way to get every piece crunchy. Mistake two, too much butter. More butter doesn't make it better. It makes it greasy, and greasy goes soft.""",
   "microwave bowl snack mix", "NOT THE MICROWAVE")
sc("""Mistake three, a pan that's too crowded. Spread it thin, use two pans if you have to. And mistake four, storing it warm, or in a container that isn't airtight. Cool it all the way, then into tins or jars with tight lids. Done right, it stays crunchy for two weeks. In my house it never lasts two weeks, but it could.""",
   "airtight jars snack mix", "COOL IT ALL THE WAY")

sc("""And if a batch does go soft in the tin, don't throw it away, sweetheart. Spread it on a baking sheet and put it back in a two hundred fifty degree oven for fifteen minutes. Let it cool flat on paper again, and it comes right back to crunchy. I've rescued more than one batch the morning of a party that way, and nobody ever knew.""",
   "snack mix baking sheet oven", "NOBODY EVER KNEW")

ch("Make it a Christmas mix")
sc("""Now, for Christmas, here's what I do to make it festive. After it's completely cool, I stir in a cup of red and green candy-coated chocolates and a handful of mini marshmallows. Sweet and salty together. Never add the chocolate while it's warm, or you'll have a melted brown mess. The grandchildren call this one Grandma's Christmas crunch.""",
   "Christmas snack mix red green candies", "GRANDMA'S CHRISTMAS CRUNCH")
sc("""Or make a sweet version for people who don't like salty. Instead of the Worcestershire and garlic, melt the butter with a quarter cup of brown sugar and a teaspoon of cinnamon, and bake it the same way. Then when it's cool, drizzle melted white chocolate over it and toss in dried cranberries. It tastes like Christmas morning.""",
   "cinnamon sugar snack mix cranberries", "LIKE CHRISTMAS MORNING")

ch("The best homemade gift")
sc("""And this is why I love party mix, honey. One batch costs about ten dollars and fills six quart jars. Put it in a clear jar with a red ribbon around the lid, or in a cellophane bag with a little tag. It doesn't break in the mail like cookies, it doesn't melt like candy, and men love it. Every man in my family gets a jar of party mix at Christmas, and not one of them has ever complained.""",
   "snack mix gift jars ribbon", "MEN LOVE IT")
sc("""I make mine the second week of December, three big batches in one afternoon, one after the other. The whole house smells like toasted butter and Worcestershire. Then I fill the jars on the kitchen table, write the tags, and give them to the mailman, the paper boy, my doctor's nurses, and every one of my neighbors on the street.""",
   "kitchen table gift jars tags", "THREE BATCHES IN ONE AFTERNOON")
sc("""And for the children, give them a bowl and let them each make their own mix from little bowls of everything. Cereal, pretzels, nuts, candies, marshmallows. They scoop what they like into a bag and tie it with a ribbon. Then they give it to their teacher. My great-granddaughter made eleven bags last year and gave one to the man who drives her school bus.""",
   "children making snack mix bags", "THE MAN WHO DRIVES THE BUS")

ch("Grandma's kitchen")
sc("""So one more time. Nine cups of cereal and three cups of nuts, pretzels and chips. Six tablespoons of butter with Worcestershire, seasoned salt, garlic and onion. Pour it slowly, just a shine. Two hundred fifty degrees for one hour, stirring every fifteen minutes. Cool it flat on paper, then into tight jars. That's the party mix that's been on my counter every Christmas Eve for sixty-five years.""",
   "homemade party mix bowl Christmas", "SIXTY-FIVE YEARS")
sc("""Tell me in the comments, sweetheart. What do you pick out first, the nuts, the pretzels, or the little rye chips? Everybody has a favorite piece, and everybody leaves something at the bottom of the bowl. Every day I'm bringing you another Christmas recipe from my kitchen. Good night, honey. Merry Christmas.""",
   "bowl of snack mix hands", "WHAT DO YOU PICK OUT FIRST?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma28", "The Christmas Party Mix EVERYONE's Grandma Made (Why Yours Goes SOGGY)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Chex Party Mix recipe first printed on Chex cereal boxes in the early 1950s (Ralston Purina).",
      "Recipe as written by Grandma Ruth: 9 cups cereal squares, 1 cup mixed nuts, 1 cup pretzels, 1 cup bagel chips; 6 tbsp butter, 2 tbsp Worcestershire, 1 1/2 tsp seasoned salt, 3/4 tsp garlic powder, 1/2 tsp onion powder; 250 F for 1 hour, stirring every 15 minutes."],
     "christmas recipe", minutes=(10, 14.5), voice="en_US-lessac-high")
