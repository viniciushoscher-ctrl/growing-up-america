import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 67 · everyday recipe: old-fashioned baked macaroni and cheese (Google Trends 3/11: side dishes, Thanksgiving dinner rising)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, in my family, there's one dish that no holiday is allowed to happen without. Not the turkey. Not the ham. Grandma's baked macaroni and cheese. A big, deep dish of tender macaroni in a creamy cheese sauce, with a golden, crunchy top. The grandchildren call the crispy corners the treasure, and they fight over them like pirates.""",
   "baked macaroni cheese golden crust dish", "THE TREASURE")
sc("""But people tell me their mac and cheese comes out grainy and oily, or dry and stiff, or bland as paste. So tonight I'm giving you my mother's baked macaroni and cheese, every step, and the five mistakes that make it grainy. And stay with me, because the last trick is for the top, and it's the reason those corners are worth fighting over.""",
   "grainy oily macaroni cheese", "GRAINY AND OILY")

ch("Thursday macaroni")
sc("""Macaroni and cheese is one of the oldest American dishes, honey. Thomas Jefferson served it at the White House, after he tasted it in Italy and France. But in my house, it was a supper for hard times. A pound of macaroni, a block of cheese, and some milk, and four people ate like kings for about forty cents. My mother made it every Friday during Lent.""",
   "1950s family dinner macaroni", "LIKE KINGS FOR FORTY CENTS")
sc("""Then in the late nineteen thirties, the blue box came along, with the orange powder, and a lot of families stopped making the real kind. My mother would never buy it. She said, Ruth, that's not macaroni and cheese, that's macaroni and a rumor of cheese. In a minute I'll tell you the first mistake, and it's the cheese you buy.""",
   "boxed macaroni cheese 1950s", "A RUMOR OF CHEESE")
sc("""And today, honey, a big dish feeds eight people as a side, or four as a supper, for about twelve dollars. It's the dish people ask you to bring to every potluck, every church supper, and every Thanksgiving. Once you make it right, you'll never be allowed to bring anything else.""",
   "potluck table casserole dishes", "YOU'LL ALWAYS BRING IT")

ch("What you need")
sc("""Here's what you need, honey. One pound of elbow macaroni. Four tablespoons of butter. A quarter cup of flour. Three cups of whole milk. One cup of half and half or evaporated milk. One pound of sharp cheddar cheese, shredded. Four ounces of Gruyere or Monterey Jack, shredded. A teaspoon of dry mustard. A pinch of cayenne and nutmeg. Salt and pepper.""",
   "elbow macaroni cheddar milk butter", "THE INGREDIENTS")
sc("""And for the top, a cup of bread crumbs or crushed butter crackers, two tablespoons of melted butter, and a handful of extra cheddar. Now, mistake number one, the main reason for grainy mac and cheese. Bagged, pre-shredded cheese. It's covered in a powder so it won't clump in the bag, and that powder makes the sauce gritty. Buy a block, and shred it yourself.""",
   "shredding cheddar block grater", "SHRED IT YOURSELF")
sc("""And use sharp cheddar, sweetheart, the sharpest you can find. Mild cheddar melts into nothing and tastes like plain milk. Sharp cheddar has the real cheese flavor. And a second cheese that melts smooth, like Gruyere, Monterey Jack, or even a slice or two of American cheese, which helps keep the sauce silky. My mother used a little Swiss from the deli.""",
   "sharp cheddar gruyere blocks", "SHARP CHEDDAR")

sc("""And let the milk and cheese warm up a little on the counter, honey, about half an hour, before you start. Ice-cold milk poured into a hot pan makes lumps, and cold cheese dropped into hot sauce melts unevenly and gets stringy. Room temperature makes everything melt together smooth and silky. My mother set them out while she put on her apron and found her big wooden spoon.""",
   "milk cheese on counter room temperature", "LET IT WARM UP")

ch("The macaroni")
sc("""Step one. Cook the macaroni in a big pot of well-salted water, but only for about two minutes less than the box says. Mistake number two is cooking it all the way. The macaroni keeps cooking in the oven and soaks up the sauce. If it's fully cooked before it goes in, it comes out soft and mushy, and it drinks up all the sauce, so the whole dish is dry.""",
   "boiling macaroni pot", "TWO MINUTES LESS")
sc("""Drain it, and don't rinse it. The starch on the outside helps the sauce cling. Toss it with a little butter so it doesn't stick together, and set it aside. And salt that water, honey. It should taste like the sea. That's the only chance you get to season the pasta itself. My mother threw in a big handful of salt and said, the macaroni has to taste good too.""",
   "draining macaroni colander", "SALT THE WATER")

ch("The sauce")
sc("""Step two, the cheese sauce. Melt the butter in a big saucepan over medium heat. Whisk in the flour and cook it, stirring, for about two minutes, until it smells a little toasty. Then slowly pour in the milk and the half and half, a little at a time, whisking the whole time so there are no lumps. Bring it to a gentle simmer and let it thicken for about five minutes.""",
   "whisking white sauce saucepan", "WHISK THE WHOLE TIME")
sc("""If this is helping you, honey, tap the like button for me. It helps Grandma more than you know. Now, mistake number three, and this one ruins more mac and cheese than anything. Adding the cheese while the sauce is boiling. Too much heat makes the cheese break apart, so the fat separates into an oily, grainy mess. Take the pot off the heat completely before you add the cheese.""",
   "oily separated cheese sauce", "OFF THE HEAT")
sc("""Then add the cheese one handful at a time, stirring after each one until it melts smooth, before adding the next. Save about a cup of cheddar for the top. Stir in the dry mustard, the cayenne, a pinch of nutmeg, salt and pepper. The mustard and cayenne don't make it spicy, honey. They make it taste cheesier. That's my mother's secret.""",
   "melting cheese into sauce handful", "ONE HANDFUL AT A TIME")
sc("""And mistake number four. Not enough sauce. The sauce should look like too much when you mix it with the macaroni, soupy and loose. The macaroni drinks it up in the oven. If it looks just right before baking, it'll be dry and stiff after. Taste the sauce, too. It should taste a little too salty and too cheesy on its own.""",
   "saucy macaroni before baking", "MORE THAN LOOKS RIGHT")

ch("Assembling")
sc("""So far, cheese from the block, sharp cheddar, macaroni undercooked by two minutes, cheese added off the heat, a handful at a time, and plenty of sauce. Now stir the macaroni into the sauce, and pour it into a buttered nine by thirteen dish. Heat the oven to three hundred seventy-five. Spread it out evenly, all the way to the corners.""",
   "pouring macaroni into baking dish", "TO THE CORNERS")

ch("The top")
sc("""And now the trick I promised, for the top. Mistake number five is a plain top, or only cheese, which turns greasy. Mix the bread crumbs or crushed butter crackers with the melted butter and the cup of saved cheddar. Sprinkle it all over the top, right to the edges. The butter makes it crisp and golden, and the cheese melts into a lacy crust. Those are the treasure corners.""",
   "bread crumbs cheese topping casserole", "THE TREASURE CORNERS")
sc("""Bake it for about twenty-five to thirty minutes, until it's bubbling at the edges and golden brown on top. If you want it even crispier, turn on the broiler for the last two minutes, and watch it every second. Then let it rest for ten minutes before serving. Hot mac and cheese straight out of the oven is runny. Ten minutes later, it's creamy and holds together.""",
   "golden bubbling mac and cheese oven", "REST TEN MINUTES")

sc("""And serve it the old way, sweetheart. Cut it into big squares with a spatula, so everybody gets a piece of the crunchy top. Put it next to a ham or a turkey, or serve it all by itself for supper with a plate of sliced tomatoes and some green beans. On Fridays in Lent, that was our whole supper, and nobody ever went to bed hungry.""",
   "square of mac and cheese spatula", "NOBODY WENT HUNGRY")

ch("Making it your own")
sc("""You can change it a hundred ways, sweetheart. Stir in crumbled bacon or diced ham. Add a little chopped green chile. Use smoked Gouda for a smoky flavor. Or put a layer of sliced tomatoes on top before the crumbs, the way they do in the South. My granddaughter adds roasted broccoli, so she can tell herself it's healthy.""",
   "mac and cheese bacon tomatoes", "SO IT'S HEALTHY")
sc("""And you can make it ahead, honey, which is a blessing on Thanksgiving. Make it the day before, but don't add the crumb topping. Cover it and keep it in the icebox. The next day, add a splash of milk over the top, because it'll be thick, then the crumbs, and bake it about forty-five minutes. It keeps four days, and it freezes for two months, without the topping.""",
   "covered casserole refrigerator ahead", "MAKE IT AHEAD")
sc("""And to reheat it, add a splash of milk and warm it in the oven, covered with foil, at three fifty for about twenty minutes. The microwave makes it oily. And here's a treat. Cold leftover mac and cheese, cut into squares, dipped in egg and bread crumbs, and fried in a little butter. My husband called it macaroni toast, and he ate it every Saturday morning.""",
   "fried mac and cheese squares skillet", "MACARONI TOAST")

ch("Grandma's kitchen")
sc("""So one more time. Shred your own cheese, sharp cheddar and something smooth. Undercook the macaroni by two minutes, and salt the water. A smooth white sauce. Take it off the heat, and add the cheese a handful at a time. Mustard and cayenne. Plenty of sauce, more than looks right. A buttery crumb and cheese top. Bake until golden, and rest ten minutes. That's my mother's mac and cheese, never grainy.""",
   "mac and cheese holiday table family", "NEVER GRAINY")
sc("""Tell me in the comments, sweetheart. Are you a crunchy corner person, or a creamy middle person? In my family, it's a war. The whole playlist of Grandma's recipes is right there on your screen, and I'll see you in the next video. Good night, honey.""",
   "warm kitchen evening casserole", "CORNER OR MIDDLE?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma67", "Baked Mac and Cheese EVERYONE's Grandma Made (Why Yours Is GRAINY)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Macaroni and cheese in early American cooking, including Thomas Jefferson's interest in macaroni; boxed macaroni and cheese introduced in 1937.",
      "Recipe as written by Grandma Ruth: 1 lb elbow macaroni, 4 tbsp butter, 1/4 cup flour, 3 cups whole milk, 1 cup half and half, 1 lb sharp cheddar, 4 oz Gruyere or Jack, dry mustard, cayenne, nutmeg; crumb topping with butter and cheddar; 375 F for 25 to 30 minutes."],
     "everyday recipe", minutes=(10, 14.5), voice="en_US-lessac-high")
