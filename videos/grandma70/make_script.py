import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 70 · everyday recipe: homemade sloppy joes (Google Trends 3/11: dinner recipes; budget weeknight ground beef)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, in nineteen fifty-eight, the best day of the week at Mansfield Junior High was Wednesday, because Wednesday was sloppy joe day in the cafeteria. The lunch ladies made them in giant pans, and the whole school smelled like onions and sweet tomato. My brother Danny ate three, every Wednesday, and he still says it was the best food he ever had.""",
   "sloppy joe sandwich bun napkin", "SLOPPY JOE DAY")
sc("""But most sloppy joes today come from a can, and they taste like sweet ketchup and nothing else. Or they're greasy, or so runny they soak the bun into mush. So tonight I'm giving you my homemade sloppy joes, a whole family supper in twenty-five minutes, every step, and the five mistakes that make them taste like ketchup. And stay with me, because the last trick is for the bun, and it's the reason they don't fall apart in your hands.""",
   "canned sloppy joe sauce soggy bun", "TASTES LIKE KETCHUP")

ch("The lunch lady's recipe")
sc("""Nobody knows for sure who invented the sloppy joe, honey. Some say a cook named Joe at a cafe in Sioux City, Iowa, in the nineteen thirties, who added tomato sauce to his loose meat sandwiches. Others say it came from Havana. But by the time I was in school, every cafeteria and every church supper in Ohio had them. They were cheap, and children loved them.""",
   "1930s Iowa cafe diner", "A COOK NAMED JOE")
sc("""The lunch lady at our school was Mrs. Dombrowski, a big, kind woman with arms like a blacksmith. In nineteen fifty-nine, my mother asked her for the recipe. Mrs. Dombrowski wrote it down for three hundred students, on the back of a milk carton. My mother spent a whole evening dividing everything by fifty. In a minute I'll tell you Mrs. Dombrowski's two secrets.""",
   "school cafeteria lunch lady 1950s", "FOR THREE HUNDRED STUDENTS")
sc("""And sloppy joes are still one of the cheapest suppers there is, sweetheart. A pound and a half of ground beef feeds six people, with buns, for about twelve dollars. It's ready in twenty-five minutes, it's one pan, and every child at the table will eat it. On a busy weeknight, that's a gift.""",
   "family eating sloppy joes table", "ONE PAN, TWENTY-FIVE MINUTES")

ch("What you need")
sc("""Here's what you need, honey. One and a half pounds of ground beef. One onion, chopped fine. One green bell pepper, chopped fine. Two cloves of garlic. One can of tomato sauce, eight ounces. Half a cup of ketchup. One tablespoon of brown sugar. One tablespoon of Worcestershire sauce. One tablespoon of yellow mustard. One teaspoon of chili powder. Salt and pepper. And six hamburger buns.""",
   "ground beef onion pepper tomato sauce", "THE INGREDIENTS")
sc("""And here's Mrs. Dombrowski's first secret. Mistake number one is using only ketchup. All ketchup makes the sauce too sweet and one-note. Use tomato sauce for the body, a little ketchup for sweetness, and then Worcestershire, mustard and a splash of vinegar to balance it. That tang is what makes it taste like a real supper and not a candy.""",
   "tomato sauce mustard Worcestershire bottles", "NOT ONLY KETCHUP")

sc("""And pick the right meat, honey. Eighty-five percent lean ground beef is just right. Too lean, and it's dry and crumbly. Too fatty, and you'll be spooning out grease all night. You can also use half beef and half ground pork, which makes it sweeter and juicier, or ground turkey with an extra spoon of Worcestershire for a lighter supper. Mrs. Dombrowski used whatever the school district sent her that week.""",
   "ground beef package lean", "THE RIGHT MEAT")

ch("The meat")
sc("""Step one. Brown the ground beef in a big skillet over medium-high heat, breaking it up into small pieces with a wooden spoon. Mistake number two is not browning it well. If you cook it only until it's gray, it tastes boiled. Let it sit and brown until there are crispy brown bits on the bottom of the pan. That's where the flavor comes from.""",
   "browning ground beef skillet", "BROWN IT WELL")
sc("""And break it up small, honey, smaller than you would for tacos. Sloppy joe meat should be fine and loose, so it soaks up the sauce. My mother used a potato masher right in the skillet to break it into tiny pieces. Mrs. Dombrowski used a big metal spatula, chopping straight down like a lumberjack.""",
   "potato masher breaking up beef", "BREAK IT UP SMALL")
sc("""If this is helping you, honey, tap the like button for me. It helps Grandma more than you know. Now, mistake number three. Leaving all the grease in. Tilt the pan, and spoon out most of the fat, leaving about a tablespoon. Too much grease makes the sauce oily and soaks the bun. Then add the onion and green pepper, and cook them with the meat for about five minutes, until they're soft.""",
   "spooning grease out of skillet", "SPOON OUT THE GREASE")

ch("The sauce")
sc("""Step two. Add the garlic and the chili powder, and stir for one minute. Then pour in the tomato sauce, the ketchup, the brown sugar, the Worcestershire and the mustard. Stir it all together, and add a teaspoon of salt and some pepper. And here's Mrs. Dombrowski's second secret. A tablespoon of cider vinegar, or the juice from a jar of pickles.""",
   "adding sauce to beef skillet", "PICKLE JUICE")
sc("""The vinegar wakes everything up, sweetheart. It cuts the sweetness and the richness, so you want another bite. Mrs. Dombrowski used the pickle juice from the giant jars in the cafeteria, because she said it would be a crime to waste it. My mother used it too. And now I always save my pickle juice in the icebox door, just for sloppy joes.""",
   "pickle jar juice spoon", "IT WAKES IT UP")
sc("""Now, mistake number four. Not simmering it long enough. Bring it to a bubble, then turn it down low and let it simmer, uncovered, for about ten to fifteen minutes, stirring now and then. The sauce thickens, the flavors blend, and the meat soaks it all up. Taste it, and add more salt, sugar or vinegar until it tastes just right to you.""",
   "simmering sloppy joe mixture", "LET IT SIMMER")
sc("""It should be thick enough to mound on a spoon, not runny like soup. If it's too runny, keep simmering. If it gets too thick, add a splash of water. And here's a test. Drag a spoon across the bottom of the pan. If the sauce slowly fills in the path, it's right. If it rushes back like a river, it needs more time.""",
   "thick sauce spoon mounding", "THICK, NOT RUNNY")

ch("The bun")
sc("""So far, not only ketchup, brown the meat well, break it up small, spoon off the grease, a splash of pickle juice, and simmer it thick. Now the trick I promised, the bun. Mistake number five is a cold, soft, plain bun. The sauce soaks right in, and the bottom bun turns to mush and falls apart in your hands before you're halfway done.""",
   "soggy bun falling apart", "THE BUN")
sc("""Here's how. Butter the cut sides of the buns, and toast them in a hot skillet, butter side down, for about a minute, until they're golden and crisp. The toasted, buttered surface keeps the sauce from soaking in. And a toasted bun tastes ten times better. Mrs. Dombrowski toasted three hundred buns every Wednesday on a giant griddle. She said nobody deserves a soggy bun.""",
   "toasting buttered buns skillet", "NOBODY DESERVES A SOGGY BUN")
sc("""Then pile the meat on the bottom bun, generously. Top it with a slice of cheddar cheese if you like, which melts right into it, and a few dill pickle slices. Put the top on, and serve it with a fork on the side and plenty of napkins. They're called sloppy for a reason, honey. Nobody ever ate one without dripping on their shirt.""",
   "sloppy joe cheese pickles bun", "PLENTY OF NAPKINS")

sc("""And for a party or a crowd, sweetheart, make them in a slow cooker. Brown the meat and vegetables on the stove first, then put everything in the slow cooker on low for three or four hours. Set out a basket of toasted buns, cheese and pickles, and let everybody build their own. It's the easiest food there is for a ball game, a birthday, or a funeral lunch at the church.""",
   "slow cooker sloppy joes party buns", "FOR A CROWD")

ch("Serving")
sc("""Serve them the cafeteria way, sweetheart. With potato chips, a pickle spear, and a little cup of coleslaw on the side. Or with french fries or tater tots. The children will think it's the best supper in the world. And the grown-ups will too, if they're honest. My husband asked for sloppy joes on his seventieth birthday instead of steak.""",
   "sloppy joe chips coleslaw plate", "THE CAFETERIA WAY")
sc("""And here's a supper for when you're out of buns. Spoon the sloppy joe mixture over a baked potato, with cheese on top. Or over buttered egg noodles. Or put it in a baking dish, cover it with refrigerated biscuits, and bake it twenty minutes for a sloppy joe pie. My granddaughter calls that one sloppy joe casserole, and her children eat two helpings.""",
   "sloppy joe over baked potato", "NO BUNS NEEDED")

ch("Keeping")
sc("""The sloppy joe mixture keeps four days in the icebox, and it freezes beautifully for three months. Make a double batch, and freeze half in a container or a zipper bag laid flat. Thaw it overnight, warm it in a pan, and supper is ready in ten minutes. I always have a bag in my freezer for the nights the grandchildren show up hungry and unannounced.""",
   "frozen sloppy joe bags freezer", "FOR UNANNOUNCED GRANDCHILDREN")

sc("""And one more old trick, honey. If you're feeding picky children, chop the onion and green pepper very, very fine, almost into mush, or grate them on a box grater. They melt right into the sauce, and nobody knows they're eating vegetables. My mother hid a whole carrot in Danny's sloppy joes for ten years. He found out at his own wedding, and he was outraged.""",
   "grated carrot onion box grater", "HIDDEN VEGETABLES")

ch("Grandma's kitchen")
sc("""So one more time. Tomato sauce, a little ketchup, Worcestershire and mustard, not only ketchup. Brown the meat well and break it up small. Spoon off the grease. Onion and green pepper. A splash of pickle juice. Simmer it until it's thick. And butter and toast the buns. That's Mrs. Dombrowski's sloppy joes, and Danny still says they're the best food in the world.""",
   "sloppy joes family supper table", "THE BEST FOOD EVER")
sc("""Tell me in the comments, sweetheart. What was the best day in your school cafeteria? Pizza day, sloppy joe day, or something else? The whole playlist of Grandma's recipes is right there on your screen, and I'll see you in the next video. Good night, honey.""",
   "1950s school cafeteria lunch trays", "THE BEST CAFETERIA DAY?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma70", "Sloppy Joes EVERYONE's Grandma Made (Why Yours Taste Like KETCHUP)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "The sloppy joe, an American loose-meat sandwich in tomato sauce; one origin story credits a cook named Joe in Sioux City, Iowa, in the 1930s.",
      "Recipe as written by Grandma Ruth: 1 1/2 lb ground beef, 1 onion, 1 green pepper, 2 garlic cloves, 8 oz tomato sauce, 1/2 cup ketchup, 1 tbsp brown sugar, 1 tbsp Worcestershire, 1 tbsp mustard, 1 tsp chili powder, 1 tbsp cider vinegar or pickle juice; simmered 10 to 15 minutes; buttered toasted buns."],
     "everyday recipe", minutes=(10, 14.5), voice="en_US-lessac-high")
