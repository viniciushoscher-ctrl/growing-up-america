import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 18 · everyday recipe test (Vinicius, 2/11/2026): one everyday recipe a day, Grandma Ruth's Kitchen
# The Meatloaf EVERYONE's Grandma Made (Why Yours Comes Out DRY)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, every Wednesday of my childhood was meatloaf night. My father came home from the Westinghouse plant at a quarter to six, and he could smell it from the sidewalk. He'd open the door and say, Dorothy, is that what I think it is? Every single Wednesday, like he was surprised. Thirty years of Wednesdays, and he never once got tired of it.""",
   "meatloaf dinner plate mashed potatoes", "EVERY WEDNESDAY")
sc("""And today, when my grandchildren make meatloaf, it comes out like a brick. Dry, crumbly, gray inside. So tonight I'm giving you my mother's meatloaf, every ingredient and every step, and the four mistakes that make meatloaf dry. It costs less than ten dollars, it feeds six, and the leftovers make the best sandwich in America.""",
   "slice of meatloaf glaze", "LIKE A BRICK")

sc("""In nineteen fifty-two, two pounds of ground beef cost about a dollar ten at the A and P on Park Avenue. My mother bought it on Tuesday, after my father's payday, and every penny of that meatloaf was counted. That's why nothing went to waste, not the stale bread, not the drippings, not a single slice on Thursday. Meatloaf wasn't a fancy dinner, honey. It was a smart one.""",
   "1950s grocery store meat counter", "A DOLLAR TEN")

ch("What you need")
sc("""Here's what you need, honey. Two pounds of ground beef, and not the lean kind. Eighty percent lean, twenty percent fat. The fat is what keeps it juicy. One cup of milk. One cup of crushed saltine crackers, about twenty-four crackers, or three slices of white bread torn up. One onion, chopped very fine. Two eggs. One teaspoon of salt, half a teaspoon of pepper, and a tablespoon of Worcestershire sauce.""",
   "ground beef onion eggs ingredients kitchen", "NOT THE LEAN KIND")
sc("""And for the glaze on top, the part everybody fights over. Half a cup of ketchup, two tablespoons of brown sugar, and one tablespoon of plain yellow mustard. Stir it in a little bowl and set it aside. My mother mixed it in a teacup, always the same chipped blue teacup, and I still use that cup today.""",
   "ketchup brown sugar glaze bowl", "THE CHIPPED BLUE TEACUP")

sc("""One more thing about the beef, sweetheart. Take it out of the icebox about twenty minutes before you start. Ice-cold meat straight from the package is hard to mix gently, so people squeeze it too hard, and that's the beginning of a tough meatloaf. Cool, not cold. And wash your hands with cold water before you mix, so the fat doesn't melt on your fingers.""",
   "raw ground beef bowl kitchen", "COOL, NOT COLD")

ch("The secret")
sc("""Now here's the secret, sweetheart, the one nobody tells you anymore. Before anything else, put the crushed crackers in your big bowl and pour the cup of milk over them. Stir it and let it sit for five minutes, until it's soft and mushy, like oatmeal. That mush holds the juice inside the meat while it bakes. Without it, the juice runs out into the pan and your meatloaf dries out.""",
   "crackers soaking milk bowl", "LIKE OATMEAL")
sc("""Grandma Pearl called it the soak. During the Depression she used stale bread, because nobody threw away stale bread, and she'd say it made the meat go further too. She was right on both counts. Two pounds of beef with the soak feeds six people. Without it, it feeds four, and it's dry.""",
   "stale bread kitchen vintage", "THE SOAK")

sc("""And if you want to know if it's seasoned right before it goes in the oven, do what my mother did. Pinch off a little piece the size of a quarter, flatten it, and fry it in a skillet for a minute. Taste it. Too bland, add a little more salt. Too plain, a little more Worcestershire. It's the only way to know, because you can't fix the salt once it's baked.""",
   "small patty frying skillet", "FRY A LITTLE PIECE")

ch("Step by step")
sc("""Step one. Heat your oven to three hundred and fifty degrees. Chop the onion as fine as you can, almost to mush. Big pieces of onion make the loaf fall apart when you slice it. If your grandchildren don't like onion, grate it on the big holes of a cheese grater. It melts right in and they'll never find it.""",
   "chopping onion cutting board", "GRATE IT")
sc("""Step two. Into the bowl with the soaked crackers, add the eggs, the onion, the salt, the pepper and the Worcestershire, and stir it together. Then add the ground beef on top. And now, honey, use your hands. Mix it gently, with your fingers, just until everything comes together. Not one second longer.""",
   "hands mixing meatloaf bowl", "USE YOUR HANDS")
sc("""Step three. Shape it on a baking sheet lined with foil, not in a loaf pan. Make a loaf about nine inches long and five inches wide, and pat it smooth. In a loaf pan it sits in its own grease and steams. On a sheet, the fat runs off, the sides get a little brown crust, and the glaze caramelizes all around.""",
   "shaping meatloaf baking sheet", "NOT IN A LOAF PAN")
sc("""Step four. Bake it for forty-five minutes. Then take it out, spread the glaze all over the top and the sides with a spoon, and put it back in for about fifteen more minutes, until the glaze is dark and sticky. If you have a meat thermometer, the middle should read one hundred and sixty degrees. That's done, and not a minute more.""",
   "meatloaf glaze baking oven", "ONE HUNDRED SIXTY")
sc("""Step five, and don't skip this one. Let it rest on the counter for ten minutes before you slice it. If you cut it straight from the oven, it crumbles and the juice runs all over the board. Ten minutes, and it slices clean like bread. That's when my mother mashed the potatoes, so everything was ready at the same time.""",
   "meatloaf resting kitchen counter", "TEN MINUTES")

sc("""And here's a little trick for a meatloaf that looks pretty on the table. Before it goes in the oven, press a long shallow groove down the middle of the top with the side of your hand. The glaze sits in that groove like a little river and doesn't all run off the sides. My mother did it with the edge of a spoon, and her meatloaf always looked like the picture in the Betty Crocker book.""",
   "meatloaf glaze top close up", "A LITTLE RIVER")

ch("Four mistakes that make it dry")
sc("""Now the four mistakes, sweetheart. Mistake one. Using lean beef. Ninety percent lean is fine for a lot of things, but not meatloaf. It comes out dry no matter what you do. If you want it lighter, mix half beef and half ground pork, the way the Hungarian ladies at our church did. Never all lean beef.""",
   "ground beef package meat counter", "NEVER ALL LEAN")
sc("""Mistake two. Mixing it too much. When you squeeze and knead it like bread dough, the meat gets tight and tough, like a hockey puck. Mix gently, only until you can't see streaks of egg. My mother said treat it like you're tucking a baby in, not like you're punching your brother.""",
   "mixing ground meat bowl", "NOT LIKE BREAD DOUGH")
sc("""Mistake three. Skipping the soak. Dry crumbs straight from the box pull the juice out of the meat instead of holding it in. Always soak them in milk first. And mistake four. Overbaking it. People leave it in for an hour and a half to be safe, and they bake every drop of juice out. Use a thermometer, take it out at one sixty, and let it rest.""",
   "meat thermometer meatloaf", "TAKE IT OUT AT 160")

ch("What goes with it")
sc("""In our house, meatloaf always came with mashed potatoes and green beans, and nothing else would do. Here's my mother's trick for the potatoes. Warm the milk and the butter in a little pan before you add them, so the potatoes stay fluffy instead of turning gluey. And save the drippings from the meatloaf pan for a little gravy, if there are any.""",
   "mashed potatoes green beans dinner", "WARM THE MILK")

sc("""And here's how to change it up, once you've got the plain one down. Put a few strips of bacon over the top instead of the glaze, the way Grandma Pearl did on Sundays. Or hide a row of hard-boiled eggs down the middle before you shape it, so every slice has a little circle of egg. Or add a cup of shredded cheddar to the mix. My grandson calls that one the cheeseburger loaf.""",
   "bacon wrapped meatloaf baking", "THE CHEESEBURGER LOAF")

ch("Leftovers")
sc("""And the best part of meatloaf is Thursday. Cold meatloaf, sliced thin, on white bread with ketchup and a leaf of lettuce. My father took that sandwich to the plant every Thursday, wrapped in wax paper, in his black lunch pail. Or fry a thick slice in a skillet with a little butter until it's crispy on both sides, and put a fried egg on top. That's breakfast fit for a king.""",
   "meatloaf sandwich lunch", "THURSDAY IS BETTER")
sc("""It keeps four days in the icebox, wrapped tight. And it freezes beautifully. Slice it first, put wax paper between the slices, and freeze them in a bag. Then you can take out one slice at a time for a quick supper. When I lived alone after my husband passed, that was how I ate my mother's meatloaf, one slice at a time.""",
   "frozen food bag freezer kitchen", "ONE SLICE AT A TIME")

ch("Grandma's kitchen")
sc("""So here it is one more time, honey. Eighty-twenty beef. Soak the crackers in milk. Fine onion. Mix gently with your hands. Shape it on a sheet, not a loaf pan. Forty-five minutes, glaze, fifteen more. Take it out at one sixty, and let it rest ten minutes. That's my mother's Wednesday meatloaf, and it has never once come out dry.""",
   "family dinner table meatloaf", "NEVER DRY")
sc("""Now tell me in the comments, sweetheart. What did your family eat every week, without fail? Meatloaf, pot roast, tuna casserole? Every day I'm bringing you one recipe from my kitchen, the way my mother and Grandma Pearl made it, and I read every comment for the next one. Good night, honey.""",
   "vintage kitchen evening warm light", "WHAT DID YOUR FAMILY EAT?")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("grandma18", "The Meatloaf EVERYONE's Grandma Made (Why Yours Comes Out DRY)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "USDA: ground beef is safe at an internal temperature of 160 F.",
      "Recipe as written by Grandma Ruth: 2 lb 80/20 ground beef, 1 cup milk, 1 cup crushed saltines, 1 onion, 2 eggs, 1 tsp salt, 1/2 tsp pepper, 1 tbsp Worcestershire; glaze 1/2 cup ketchup, 2 tbsp brown sugar, 1 tbsp yellow mustard; 350 F for 45 min, glaze, about 15 min more to 160 F; rest 10 min."],
     "everyday recipe", minutes=(10, 14.5), voice="en_US-lessac-high")
