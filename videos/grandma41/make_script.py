import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 41 · Christmas recipe: rum cake (Google Trends 3/11: christmas cakes recipes, christmas treat recipes rising)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, every family has one Christmas dessert that makes the grown-ups giggle. In ours, it was the rum cake. A golden ring of butter cake, soaked through with a warm butter and rum glaze, and covered in pecans. My Aunt Margaret ate three slices one Christmas Eve in nineteen seventy-four and sang Silent Night in four different keys.""",
   "golden rum cake bundt pecans", "FOUR DIFFERENT KEYS")
sc("""But most rum cakes today come out dry, or the glaze just sits on top in a sticky puddle, or the cake falls apart coming out of the pan. So tonight I'm giving you my rum cake, every step, and the four mistakes that make it dry. And stay with me, because the last secret is about when to pour the glaze, and almost everybody does it wrong.""",
   "dry cracked bundt cake", "DRY OR STICKY")

ch("A cake from the islands")
sc("""Rum cake came to us from the Caribbean, honey, where they've made rich cakes soaked with rum for Christmas for hundreds of years. In the seventies, a quick version became all the rage in America, made with a box of yellow cake mix and a box of pudding mix. Every church cookbook in Ohio had it. Mine had four of them, all slightly different, all claiming to be the original.""",
   "1970s church cookbook pages", "ALL CLAIMING TO BE ORIGINAL")
sc("""I got mine from my friend Joyce, who went on a cruise to Jamaica in nineteen seventy-two and came home with a tan, a straw hat, and this recipe on the back of a cocktail napkin. Joyce told everybody the chef gave it to her. Her husband told me she bribed a waiter with two dollars. I believe her husband.""",
   "1970s cruise ship tourists", "TWO DOLLARS")
sc("""And here's something people don't know. The rum cooks off in the oven, but the glaze doesn't go in the oven, so most of the alcohol stays. This is a grown-up cake, honey. In a minute I'll tell you how to make one the children can eat too, so nobody at the table feels left out.""",
   "glass of rum and cake slice", "A GROWN-UP CAKE")

ch("What you need")
sc("""Here's what you need for the cake. One box of yellow cake mix. One small box of instant vanilla pudding mix, the three and a half ounce size. Four eggs. Half a cup of cold water. Half a cup of vegetable oil. Half a cup of dark rum. And one cup of chopped pecans or walnuts for the bottom of the pan.""",
   "yellow cake mix pudding box eggs", "THE CAKE")
sc("""And for the glaze. One stick of butter. A quarter cup of water. One cup of white sugar. And half a cup of dark rum. That's all. Now, about the rum. Use a dark or gold rum, not white rum. Dark rum has that warm molasses and vanilla flavor. White rum just tastes like alcohol, and that's mistake number one.""",
   "dark rum bottle butter sugar", "DARK RUM, NOT WHITE")

ch("The pan")
sc("""Step one, and this is where most rum cakes are lost before they start. The pan. Use a ten-inch Bundt pan or tube pan. Grease every inch of it with soft butter, with a pastry brush or a paper towel, getting into every little groove. Then dust it with flour, tap out the extra. If you miss one groove, the cake sticks right there and tears in half.""",
   "greasing bundt pan brush butter", "EVERY LITTLE GROOVE")
sc("""Then sprinkle the chopped nuts evenly in the bottom of the pan. When you turn the cake out later, the nuts will be on top, like a crown. Joyce toasted hers first in a dry skillet for five minutes, and that's how I do it too. Toasted pecans taste twice as rich.""",
   "chopped pecans bottom bundt pan", "LIKE A CROWN")

sc("""And if you don't trust your pan, honey, use baking spray with flour in it, the kind made for Bundt pans. And never use a dark, thin, cheap pan if you can help it. Dark pans bake the outside too fast and burn the nuts before the middle is done. A heavy, light-colored pan is worth the money. Mine is from nineteen seventy-one, and it's never stuck once.""",
   "heavy bundt pan light metal", "A HEAVY PAN")

ch("The batter")
sc("""Step two. Heat the oven to three hundred twenty-five degrees. In a big bowl, put the cake mix, the pudding mix, the eggs, the water, the oil and the rum. Beat it with a mixer on low for thirty seconds, then on medium for two minutes. The pudding mix is the secret, honey. It makes the cake dense and moist, almost like a pound cake.""",
   "beating cake batter mixer bowl", "THE PUDDING IS THE SECRET")
sc("""If this is helping you, honey, tap the like button for me. It helps Grandma more than you know. Now pour the batter over the nuts in the pan and smooth the top. Then tap the pan hard on the counter three times. That knocks out the big air bubbles, so you don't get holes in the cake.""",
   "pouring batter bundt pan", "TAP IT THREE TIMES")
sc("""Bake it for about fifty-five minutes to one hour. Mistake number two is overbaking it, which makes it dry, no matter how much glaze you pour on. Start checking at fifty minutes. Stick a long wooden skewer into the thickest part. It should come out with just a few moist crumbs, not wet batter, and not perfectly clean either.""",
   "skewer testing bundt cake", "A FEW MOIST CRUMBS")

ch("The glaze")
sc("""Step three, the glaze. Start it about ten minutes before the cake comes out. In a small saucepan, melt the butter. Stir in the water and the sugar. Bring it to a boil and let it boil for five minutes, stirring the whole time, until the sugar is completely melted and it's a little thick. Then take it off the heat, and stir in the rum.""",
   "butter glaze saucepan boiling", "BOIL FIVE MINUTES")
sc("""Careful, sweetheart. Always take the pot off the stove before you add the rum, and stand back a little. Rum near a gas flame can catch fire. My friend Joyce singed her eyebrows in nineteen seventy-three, and she had to draw them on with a pencil for the whole New Year's party. She looked surprised until February.""",
   "saucepan off heat stove", "SURPRISED UNTIL FEBRUARY")

ch("The secret")
sc("""And now the secret I promised you, about when to pour the glaze. Most people turn the cake out of the pan first, and then pour the glaze over the top. And the glaze runs right off the outside onto the plate, and the inside of the cake stays dry. That's mistake number three.""",
   "glaze running off cake plate", "IT RUNS RIGHT OFF")
sc("""Here's how Joyce's waiter did it. Take the cake out of the oven, and leave it in the pan. Right away, while it's hot, poke holes all over the bottom with a long skewer, all the way down, every inch or so. Then slowly spoon half of the hot glaze over it, a little at a time, letting it soak in before you add more.""",
   "poking holes in cake skewer", "LEAVE IT IN THE PAN")
sc("""Let it sit in the pan for thirty minutes, soaking. Then put a plate on top, turn it over, and lift the pan off. Poke a few holes in the top, and slowly spoon the rest of the glaze over the top and the sides, brushing it on with a pastry brush. The whole cake drinks it up, all the way through. Not a single dry crumb.""",
   "brushing glaze over bundt cake", "NOT A DRY CRUMB")
sc("""So far, dark rum, every groove greased, pudding in the batter, no overbaking, and the glaze soaked in while it's still in the pan. And here's mistake number four. Cutting it the same day. A rum cake gets better every day for three or four days, as the glaze settles into the cake. Wrap it tight in plastic, and wait at least one night.""",
   "rum cake wrapped plastic", "WAIT ONE NIGHT")

sc("""And if you'd like it even prettier for the table, sweetheart, dust the top with a little powdered sugar right before serving, like fresh snow on the pecans. Or tuck a few sprigs of holly or rosemary around the bottom of the plate, and put a few sugared cranberries in the hole in the middle. It looks like a Christmas wreath you can eat.""",
   "bundt cake powdered sugar holly", "A WREATH YOU CAN EAT")

ch("For the whole family")
sc("""And here's the version for the children, like I promised. Use water or apple juice instead of rum in the cake, and in the glaze, use orange juice and a teaspoon of rum extract, or vanilla. It's not quite the same, but it's moist and sweet and the little ones love it. I make one of each, and I put a red ribbon on the plate of the grown-up one.""",
   "two cakes ribbon plates", "A RED RIBBON")
sc("""It keeps for a week at room temperature, wrapped tight, or longer in the icebox. And it freezes beautifully for three months. Wrap it in plastic, then in foil. It's the perfect cake for mailing to family far away, because it only gets better on the trip. I've mailed one to my son in Arizona every December since nineteen ninety.""",
   "cake wrapped foil mailing box", "IT GETS BETTER")
sc("""Serve it in thin slices, sweetheart, because it's rich. With a spoon of whipped cream, or a scoop of vanilla ice cream, and a cup of strong coffee. Some people warm a slice for a few seconds, so the butter glaze gets soft again. My husband liked his with a slice of sharp cheddar on the side. Ohio men, honey. I don't ask questions.""",
   "rum cake slice whipped cream coffee", "OHIO MEN")

ch("Grandma's kitchen")
sc("""So one more time. Dark rum, not white. Grease every groove. Toasted nuts in the bottom. Pudding mix in the batter, for moistness. Bake at three twenty-five, and don't overbake. Poke holes and soak it with half the glaze while it's still in the pan. Turn it out, glaze the rest. And wait one night before you cut it. That's a rum cake that never dries out.""",
   "glazed rum cake holiday table", "NEVER DRIES OUT")
sc("""Tell me in the comments, sweetheart. What's the dessert in your family that made the grown-ups giggle at Christmas? The whole playlist of Grandma's recipes is right there on your screen, and I'll see you in the next video. Good night, honey. Merry Christmas.""",
   "Christmas dinner dessert evening family", "WHAT MADE THEM GIGGLE?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma41", "Christmas Rum Cake That NEVER Dries Out (Grandma's 1970s Recipe)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Caribbean rum cake traditions and the 1970s American cake-mix-and-pudding rum cake.",
      "Recipe as written by Grandma Ruth: 1 box yellow cake mix, 1 box (3.4 oz) instant vanilla pudding, 4 eggs, 1/2 cup water, 1/2 cup oil, 1/2 cup dark rum, 1 cup chopped pecans; 325 F for 55 to 60 minutes; glaze of 1/2 cup butter, 1/4 cup water, 1 cup sugar boiled 5 minutes plus 1/2 cup dark rum."],
     "christmas recipe", minutes=(10, 14.5), voice="en_US-lessac-high")
