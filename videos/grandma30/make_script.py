import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 30 · everyday recipe: pinto beans and cornbread (Google Trends 3/11: pinto beans rising in dinner searches)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, in nineteen fifty-four, when the plant cut my father's hours to three days a week, we ate pinto beans and cornbread four nights out of seven. And I'm going to tell you a secret. I didn't know we were poor. I thought it was the best supper in the world. A pot of beans with a ham hock, a skillet of cornbread, and a glass of cold buttermilk.""",
   "pot of pinto beans ham hock", "I DIDN'T KNOW")
sc("""But these days, people tell me their beans never get soft. They cook them for hours and they're still hard in the middle, or they split and turn to mush on the outside while they're hard inside. So tonight I'm giving you Grandma Pearl's pinto beans. Creamy, tender, every single bean, with a rich broth you'll want to drink. Every step, and the four reasons beans stay hard. And stay with me, because reason number three is the one nobody believes until it happens to them.""",
   "hard dry beans spoon", "WHY THEY STAY HARD")

ch("Pearl's bean pot")
sc("""Grandma Pearl kept a brown crock bean pot on the back of her stove for as long as I knew her. During the Depression, a pound of dried pinto beans cost about a nickel, and it fed her family of nine with cornbread. She said, beans and cornbread together are as good as meat. And she was right, honey. The doctors say the same thing today.""",
   "brown crock bean pot stove", "AS GOOD AS MEAT")
sc("""Every Monday, Pearl picked over a pound of beans at the kitchen table, put them to soak in a big bowl, and covered them with a dish towel. On Tuesday morning, they went on the stove with whatever she had. A ham bone from Sunday, a piece of salt pork, or a few slices of bacon. By supper, the whole farmhouse smelled like beans and smoke.""",
   "dried beans soaking bowl", "EVERY MONDAY")
sc("""When I was nine, she let me do the picking. She poured the beans on a white plate, a handful at a time, and I pushed them across with my finger, looking for little stones, broken beans, and the shriveled ones. I found a stone the size of a pea once, and she gave me a penny for it. She said, that's a penny and a tooth you saved.""",
   "picking through dried beans plate", "A PENNY AND A TOOTH")

ch("What you need")
sc("""Here's what you need, honey. One pound of dried pinto beans. One smoked ham hock, or a meaty ham bone, or four slices of thick bacon. One onion, chopped. Three cloves of garlic. One bay leaf. About ten cups of water. And salt and pepper. That's it. If you want them the Texas way, add a teaspoon of cumin and a little chili powder.""",
   "dried pinto beans ham hock onion", "ONE POUND OF BEANS")
sc("""Now, the most important ingredient isn't on the list. It's fresh beans. Dried beans don't last forever, honey. After a year or two on the shelf, they get so dry and hard that they'll never soften, no matter how long you cook them. If that bag has been in your pantry since the last president, throw it out and buy new ones. In a minute I'll show you how to tell fresh beans from old ones at the store.""",
   "old bag of beans pantry", "SINCE THE LAST PRESIDENT")
sc("""How do you tell? Fresh pinto beans are bright, speckled, pink and tan, and they have a little shine. Old beans look faded and dull, sometimes almost gray, and some are wrinkled. Buy them from a busy store that sells a lot of beans, where the bags don't sit around. In the stores near me, the Mexican groceries always have the freshest beans in town.""",
   "fresh speckled pinto beans close up", "BRIGHT AND SPECKLED")

ch("Soaking")
sc("""Step one, the soak. Pick through the beans, rinse them, and put them in a big bowl with enough cold water to cover them by three inches. They'll double in size. Leave them overnight, eight to twelve hours. Soaking makes them cook faster and more evenly, so you don't get the mushy outside and hard middle.""",
   "beans soaking water bowl overnight", "COVER BY THREE INCHES")
sc("""If you forgot to soak them, my mother's quick soak. Put the beans in a pot, cover them with water, bring them to a boil for two minutes, then turn off the heat, put the lid on, and let them sit for one hour. That's almost as good as a whole night. Then drain them, rinse them, and start cooking with fresh water. If this is helping you, honey, tap the like button for me. It helps Grandma more than you know.""",
   "pot of beans boiling stove", "THE QUICK SOAK")
sc("""And here's a little secret for hard water. If your water leaves white spots on the faucet, it's hard, and hard water keeps beans hard too. The minerals toughen the skins. Add a small pinch of baking soda, about an eighth of a teaspoon, to the soaking water. Just a pinch. More than that and the beans taste soapy and turn to mush.""",
   "pinch of baking soda spoon", "JUST A PINCH")

ch("Cooking")
sc("""Step two. Drain the soaked beans and rinse them. In your big heavy pot, cook the onion in a spoon of bacon grease or oil until it's soft, then the garlic for a minute. Add the beans, the ham hock, the bay leaf, and ten cups of fresh water. Bring it up to a boil, then turn it right down to the lowest simmer, just a bubble now and then.""",
   "ham hock beans pot simmering", "THE LOWEST SIMMER")
sc("""This is mistake number two, the one that ruins the most beans. Boiling them hard. A rolling boil bangs the beans around, splits the skins, and turns the outsides to mush before the insides are done. Beans want a lazy simmer. Put the lid on, tilted a little, and leave them alone for two to three hours. Stir every half hour, gently.""",
   "split mushy beans pot", "A LAZY SIMMER")
sc("""And keep them covered with liquid the whole time. If the water drops below the top of the beans, add hot water from the kettle, never cold. Cold water shocks them, and Pearl swore it made them tough. I've never tested it, honey, because I've never dared go against Grandma Pearl. Before I go on, the salt, because an old wives' tale has fooled people about it for a hundred years.""",
   "pouring hot water kettle into pot", "NEVER COLD WATER")
sc("""Step three, the salt. When do you add it? Pearl added salt at the start, and so do I, a teaspoon and a half with the water. People will tell you salt keeps beans hard. That's an old wives' tale. Salt in the water actually makes the skins softer and the beans season all the way through. Beans salted only at the end taste flat inside.""",
   "salt spoon pot of beans", "AN OLD WIVES' TALE")
sc("""But what really does keep beans hard is acid. Tomatoes, vinegar, ketchup, molasses, lemon. If you add any of those at the start, your beans can cook all day and never get soft. That's mistake number three. Wait until the beans are completely tender, and then stir in the tomatoes or the vinegar. That's why baked beans take so long. They're full of molasses and tomato from the start.""",
   "can of tomatoes added to pot", "ACID KEEPS THEM HARD")
sc("""How do you know they're done? Scoop out five beans on a spoon, blow on them, and taste all five. Not one. Five. If every one is creamy all the way through, with no chalk in the middle, they're done. If even one is firm, give them another half hour. Then take out the ham hock, pull off the meat, chop it, and put it back in the pot.""",
   "spoonful of tender pinto beans", "TASTE FIVE, NOT ONE")
sc("""Pearl's last trick. Take one cup of beans out, mash them with a fork, and stir them back into the pot. The broth turns thick and creamy and silky. Then simmer with the lid off for fifteen minutes. Taste for salt and pepper. That broth, honey, is what we called pot likker, and we sopped up every drop with the cornbread.""",
   "mashing beans thick broth", "POT LIKKER")

ch("Four reasons they stay hard")
sc("""So the four reasons beans stay hard, sweetheart. One, old beans. Buy fresh. Two, boiling them hard instead of a lazy simmer. Three, acid too early, the tomatoes, vinegar or molasses. Wait until they're soft. And four, hard water. A tiny pinch of baking soda in the soak. Fix those four things and your beans will be creamy every single time. But I'm not done, because coming up is the other half of the supper.""",
   "creamy pinto beans bowl", "FOUR REASONS")

ch("The cornbread")
sc("""And you can't have beans without cornbread. Put two tablespoons of bacon grease in a cast iron skillet and put it in a four hundred twenty-five degree oven to get smoking hot. Meanwhile, stir together one cup of cornmeal, one cup of flour, a tablespoon of baking powder, a teaspoon of salt and a spoon of sugar if you're a Northerner, like me.""",
   "cast iron skillet cornmeal", "IF YOU'RE A NORTHERNER")
sc("""Then one egg and one and a quarter cups of buttermilk, and a quarter cup of melted butter. Stir just until it comes together. Pour the batter into the hot skillet. It should sizzle loud. That sizzle is what makes the crunchy brown crust. Bake for twenty minutes, until it's golden on top. Cut it in wedges right in the skillet.""",
   "cornbread batter sizzling skillet", "IT SHOULD SIZZLE")
sc("""Serve the beans in deep bowls with the cornbread on the side, or crumbled right on top, the way my father ate it. Chopped raw onion on top, and a spoon of chow chow relish if you have it. The leftovers keep five days in the icebox and freeze for three months. And on the third day, mash them up and fry them in bacon grease for refried beans.""",
   "beans and cornbread bowl onion", "MY FATHER'S WAY")

ch("Grandma's kitchen")
sc("""So one more time, honey. Fresh beans, picked over and soaked overnight. A ham hock and an onion. Salt at the start. The lowest simmer, two to three hours, lid tilted, hot water only. No tomatoes or vinegar until they're soft. Taste five beans. Mash a cup for a creamy broth. And a skillet of cornbread with a loud sizzle. That's the supper I grew up on, and I'd still choose it over any steak.""",
   "family supper beans cornbread table", "OVER ANY STEAK")
sc("""Tell me in the comments, sweetheart. Sugar in your cornbread, or no sugar? I know that one starts arguments at every family reunion in America. I read every comment. Every day I'm bringing you another recipe from my kitchen. And if you want another one tonight, the whole playlist of Grandma's recipes is right there on your screen, and I'll see you in the next video. Good night, honey.""",
   "cornbread wedge butter plate", "SUGAR OR NO SUGAR?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma30", "The Pinto Beans EVERYONE's Grandma Made (Why Yours Stay HARD)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Recipe as written by Grandma Ruth: 1 lb dried pinto beans soaked overnight, 1 smoked ham hock, 1 onion, 3 garlic cloves, 1 bay leaf, about 10 cups water, 1 1/2 tsp salt; gentle simmer 2 to 3 hours. Cornbread: 1 cup cornmeal, 1 cup flour, 1 tbsp baking powder, 1 tsp salt, 1 egg, 1 1/4 cups buttermilk, 1/4 cup melted butter; 425 F about 20 minutes in a hot greased skillet.",
      "Bean cooking science: old beans, hard water and acidic ingredients slow softening; salting the cooking water does not keep beans hard."],
     "everyday recipe", minutes=(10, 14.5), voice="en_US-lessac-high")
