import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 36 · everyday/holiday side: green bean casserole from scratch (Google Trends 3/11: green bean recipes, side dishes, Thanksgiving dinner +300%)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, I was there when green bean casserole was born. Well, almost. In nineteen fifty-five, my mother clipped a recipe from the newspaper. Green beans, a can of mushroom soup, and those crispy fried onions on top. She made it for Thanksgiving, my father had three helpings, and it's been on our table every holiday for seventy years.""",
   "green bean casserole fried onions", "I WAS ALMOST THERE")
sc("""But most green bean casserole today is gray and mushy, swimming in salty gray soup, with soggy onions. So tonight I'm giving you how to make it from scratch, the way that tastes like real food. Every step, and the four mistakes that make it mushy. And stay with me, because the last trick is for the onions, and it's the one that makes people ask for the recipe.""",
   "mushy gray casserole dish", "GRAY AND MUSHY")

ch("A recipe from the soup company")
sc("""The original recipe came from a test kitchen at the soup company in Camden, New Jersey, in nineteen fifty-five. A woman named Dorcas Reilly put it together from things every American kitchen had in the pantry. Canned beans, canned soup, and canned onions. It was the age of the can, honey. And she made something people still eat sixty million times every Thanksgiving.""",
   "1950s test kitchen women cooking", "THE AGE OF THE CAN")
sc("""My mother was a little suspicious at first. Grandma Pearl grew her own green beans and canned them herself, and she thought soup from a can was for lazy people. But she ate two plates of it, and then she asked my mother to make it again for Christmas. Grandma Pearl never said she was wrong. She just asked for more.""",
   "grandmother eating holiday dinner", "SHE JUST ASKED FOR MORE")
sc("""In the sixties, I made it the soup-can way for every holiday. Then in nineteen eighty-eight, my daughter-in-law Linda made it from scratch, with fresh beans and her own mushroom sauce, and I tasted it and went quiet. It was like going from a black and white television to color. In a minute I'll show you exactly how she made it.""",
   "family holiday table 1980s", "LIKE GOING TO COLOR")

ch("What you need")
sc("""Here's what you need, honey, for one nine by thirteen dish, about eight servings. One and a half pounds of fresh green beans. Eight ounces of mushrooms, sliced. Half an onion, chopped fine. Two cloves of garlic. Three tablespoons of butter. Three tablespoons of flour. One cup of chicken broth. One cup of milk or half and half. Salt, pepper and a pinch of nutmeg.""",
   "fresh green beans mushrooms butter", "FRESH GREEN BEANS")
sc("""And for the topping. Two big onions, sliced into thin rings. Half a cup of flour. A teaspoon of salt. And oil for frying. Or, if you're short on time, a can of the store-bought crispy onions is fine. Nobody will call the police. But in a few minutes I'll show you why the homemade ones are worth it.""",
   "sliced onion rings flour bowl", "NOBODY WILL CALL THE POLICE")
sc("""You can use frozen green beans, sweetheart. They work fine. Thaw them and pat them dry. But please, not canned beans. Canned green beans are already cooked soft, and by the time they bake in the oven again, they're mush. That's mistake number one, and it's the reason most green bean casserole is gray.""",
   "canned green beans mushy", "NOT CANNED")

ch("The beans")
sc("""Step one. Snap the ends off the fresh beans and cut them in two-inch pieces. Bring a big pot of salted water to a boil, and drop in the beans for only four or five minutes, until they're bright green and just barely tender. Then drain them, and put them right into a big bowl of ice water. Leave them five minutes, and drain them well.""",
   "green beans blanching ice water", "BRIGHT GREEN")
sc("""Why the ice water? It stops the cooking, so the beans stay bright green and keep a little snap. Mistake number two is skipping this, or boiling them too long. Remember, they're going in the oven again for half an hour. If they're soft before they go in, they'll be mush when they come out.""",
   "bowl of ice water green beans", "A LITTLE SNAP")

sc("""And pick good beans at the store, honey. Fresh green beans should be bright and firm, and they should snap clean in half with a little pop when you bend them. If they bend like a rubber band, they're old, and they'll taste like cardboard. Grandma Pearl used to snap one in the store, right there, before she bought a single handful. The grocer hated it.""",
   "snapping fresh green bean", "THE GROCER HATED IT")

ch("The sauce")
sc("""Step two, the mushroom sauce, instead of the can. Melt the butter in a big skillet. Add the mushrooms and leave them alone for three or four minutes until they brown on one side. Don't crowd them and don't stir too soon. Brown mushrooms taste rich and meaty. Gray mushrooms taste like wet paper. Then add the onion and garlic and cook three more minutes.""",
   "browning mushrooms skillet butter", "NOT WET PAPER")
sc("""If this is helping you, honey, tap the like button for me. It helps Grandma more than you know. Now sprinkle the flour over the mushrooms and stir for one minute. Slowly pour in the broth, stirring the whole time, then the milk. Let it bubble gently for five minutes until it's thick like gravy. Add salt, pepper and a little pinch of nutmeg.""",
   "creamy mushroom sauce skillet", "THICK LIKE GRAVY")
sc("""Taste it, honey. This is mistake number three. An unseasoned sauce. Green beans soak up salt, so the sauce should taste a little too salty on its own. A splash of soy sauce or Worcestershire gives it a deep flavor, the way the canned soup tried to. Linda's secret was a spoon of sour cream stirred in at the end. Don't tell her I told you.""",
   "tasting sauce spoon kitchen", "DON'T TELL LINDA")

ch("The onions")
sc("""So far, fresh beans, a quick boil, ice water, browned mushrooms, and a well-seasoned sauce. Now the onion trick I promised. Toss the thin onion rings in a bag with the flour and salt, and shake them until they're coated. Shake off the extra flour. Heat about half an inch of oil in a heavy skillet to medium-high.""",
   "onion rings shaking flour bag", "SHAKE THEM")
sc("""Fry the onions in small batches, two or three minutes, stirring, until they're deep golden brown. Lift them out onto paper towels and sprinkle with a little salt. They get crispier as they cool. And they taste so good you'll have to guard them. My grandchildren eat a third of them off the paper towels before they ever reach the casserole.""",
   "frying onion rings golden skillet", "GUARD THEM")
sc("""And here's the real secret, the one people ask about. Mistake number four is putting all the onions on at the start. They get soggy under the oven heat. Mix half of the onions into the beans and sauce, so you get onion flavor in every bite. Save the other half and put them on top only for the last five minutes. That's how they stay crispy.""",
   "crispy onions on casserole top", "THE LAST FIVE MINUTES")

sc("""If frying makes you nervous, sweetheart, bake the onions instead. Toss the floured rings with a few spoons of oil, spread them on a baking sheet in one layer, and bake them at four hundred twenty-five for about twenty minutes, turning them halfway, until they're golden. Not quite as crisp as fried, but close, and no splatter on your stove the day before company comes.""",
   "baked onion rings sheet pan", "NO SPLATTER")

ch("Putting it together")
sc("""Step four. Heat the oven to three hundred fifty. Stir the beans into the mushroom sauce with half the onions, and spread it in a buttered nine by thirteen dish. Bake for twenty-five minutes, until it's bubbling at the edges. Then pile the rest of the crispy onions on top, and bake five more minutes. Let it rest five minutes before serving.""",
   "green bean casserole baking dish oven", "BUBBLING AT THE EDGES")
sc("""And you can make it ahead, which is a blessing on a holiday when the oven is full. Make the beans and sauce the day before, mix them, put them in the dish, cover it, and keep it in the icebox. Fry the onions the day before too, and keep them in a paper bag on the counter, not in the icebox, or they go soft. Add ten minutes to the baking time.""",
   "casserole dish covered refrigerator", "MAKE IT AHEAD")

ch("Not just for holidays")
sc("""And don't save it only for Thanksgiving, sweetheart. Green bean casserole is a wonderful weeknight side dish with a pork chop or a roast chicken. Make half the recipe in an eight by eight dish. Add some shredded chicken or ham, and it's a whole supper in one dish. Linda calls that her lazy Tuesday casserole.""",
   "weeknight dinner pork chop green beans", "LAZY TUESDAY CASSEROLE")
sc("""And if you do want the quick version with the can, honey, I won't judge you. Here's how to make it taste better. Use fresh or frozen beans, not canned. Brown some fresh mushrooms in butter and stir them into the soup. Add a splash of soy sauce and some black pepper. And save half the onions for the end. It's ninety percent as good, in half the time.""",
   "can of soup green beans quick", "NINETY PERCENT AS GOOD")
sc("""Leftovers keep three or four days in the icebox. Warm them in the oven, not the microwave, so the beans don't go mushy. And put fresh crispy onions on top when you warm it, if you have any left. You won't. Nobody ever has onions left, honey.""",
   "leftover casserole reheating oven", "YOU WON'T")

ch("Grandma's kitchen")
sc("""So one more time. Fresh or frozen beans, never canned. Boil four minutes, then ice water. Brown the mushrooms in butter for a real sauce, and season it well. Fry your own onions. Half in the casserole, half on top for only the last five minutes. That's green bean casserole the way it should taste, bright green, creamy, and crispy on top.""",
   "green bean casserole holiday table", "BRIGHT, CREAMY, CRISPY")
sc("""Tell me in the comments, sweetheart. Green bean casserole at your holiday table, yes or no? I know some families fight about it. The whole playlist of Grandma's recipes is right there on your screen, and I'll see you in the next video. Good night, honey.""",
   "Thanksgiving dinner family table", "YES OR NO?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma36", "Green Bean Casserole EVERYONE Makes WRONG (Why Yours Is MUSHY)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Green bean casserole created in 1955 by Dorcas Reilly in the Campbell Soup Company test kitchen in Camden, New Jersey.",
      "Recipe as written by Grandma Ruth: 1 1/2 lb fresh green beans blanched 4 to 5 minutes; 8 oz mushrooms, 1/2 onion, 2 garlic cloves, 3 tbsp butter, 3 tbsp flour, 1 cup broth, 1 cup milk, nutmeg; 2 onions fried in flour; 350 F for 25 minutes plus 5 with onions on top."],
     "everyday recipe", minutes=(10, 14.5), voice="en_US-lessac-high")
