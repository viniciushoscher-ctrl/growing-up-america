import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 56 · Christmas recipe: homemade cooked eggnog (Google Trends 3/11: christmas treat recipes; eggnog a perennial December search)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, the first time I tasted real homemade eggnog, I was six years old, at Grandma Pearl's farm on Christmas Eve, nineteen fifty. She ladled it out of a big glass punch bowl into little cups, thick and cold and creamy, with nutmeg on top. Mine had no whiskey in it. My father's had plenty. He sang Jingle Bells all the way home in the snow.""",
   "eggnog punch bowl nutmeg cups", "PLENTY OF WHISKEY")
sc("""Today most people only know the carton from the store, which is thin and sweet and tastes like melted ice cream. And when they make it at home, it comes out runny, or it curdles into scrambled eggs. So tonight I'm giving you Grandma Pearl's eggnog, every step, and the five mistakes that ruin it. And stay with me, because the last secret is the one that makes it thick, and it takes nothing but time.""",
   "eggnog carton grocery store", "THIN AND SWEET")

ch("A drink older than America")
sc("""Eggnog is older than the country, honey. In England, rich people drank a hot milk and egg drink with wine or sherry in winter. When it came to the American colonies, people made it with rum, because rum was cheap here, and later with whiskey and brandy. George Washington had his own recipe, and they say it was so strong only the brave would try it.""",
   "colonial Christmas punch bowl", "ONLY THE BRAVE")
sc("""On the farm, Grandma Pearl made it with eggs from her own hens and milk and cream from her own cow, still warm. Nothing in it came from a store except the sugar, the nutmeg and my grandfather's bottle. She made it in the morning and set it in the cold springhouse all day to chill. By evening, it was thick enough to stand a spoon in.""",
   "old farm springhouse winter", "THICK ENOUGH FOR A SPOON")
sc("""In the old days, people made eggnog with raw eggs. Today, we cook it gently into a custard first, so it's safe for everybody, the children and the grandparents and anybody expecting a baby. And honestly, it tastes better cooked. In a minute I'll show you how, and the trick that keeps it from turning into scrambled eggs.""",
   "custard cooking saucepan whisk", "COOK IT GENTLY")

sc("""In our house on Elm Street, eggnog was only for two nights a year, Christmas Eve and New Year's Eve. My mother made it in her big yellow mixing bowl and kept it on the back porch, because the icebox was full of ham. One year the dog got to it first. He spent Christmas Day sleeping under the kitchen table, very happy, and very full.""",
   "dog sleeping under kitchen table", "THE DOG GOT TO IT")

ch("What you need")
sc("""Here's what you need for about six cups. Six egg yolks. Half a cup of sugar. Two cups of whole milk. One cup of heavy cream. A pinch of salt. One teaspoon of vanilla. Half a teaspoon of freshly grated nutmeg, plus more for the top. And a cinnamon stick. If you want it for grown-ups, half a cup to a cup of bourbon, brandy, or dark rum.""",
   "egg yolks milk cream nutmeg", "THE INGREDIENTS")
sc("""And here's mistake number one. Using skim milk or low fat milk. Eggnog is supposed to be rich, honey. It's a once-a-year treat. Thin milk makes thin, watery eggnog that tastes like nothing. Use whole milk and real heavy cream. If you want it a little lighter, use half and half instead of the cream, but never skim.""",
   "whole milk heavy cream bottles", "NEVER SKIM")
sc("""And grate the nutmeg yourself if you can. A whole nutmeg costs about the same as a jar of the ground kind, and it lasts for years. Rub it on a small grater, and the smell fills the whole kitchen. Ground nutmeg from a jar that's been in the cupboard since nineteen ninety tastes like dust. That's mistake number two.""",
   "whole nutmeg grater", "GRATE IT YOURSELF")

ch("The custard")
sc("""Step one. In a bowl, whisk the egg yolks and sugar together for about two minutes, until they turn pale yellow and thick, like a ribbon when you lift the whisk. In a saucepan, warm the milk, the cream, the cinnamon stick, the nutmeg and the salt over medium heat, until it's steaming and little bubbles form around the edge. Don't let it boil.""",
   "whisking egg yolks sugar pale", "PALE YELLOW")
sc("""Step two, and here's mistake number three. Pouring the hot milk into the eggs all at once. The eggs cook instantly into little scrambled lumps. It's called tempering, honey. Pour the hot milk into the eggs very slowly, just a ladle at a time, while you whisk the whole time with your other hand. Warm the eggs up gently, a little at a time.""",
   "ladle hot milk into eggs whisking", "A LADLE AT A TIME")
sc("""If this is helping you, honey, tap the like button for me. It helps Grandma more than you know. When about half the milk is in, pour everything back into the saucepan. Now cook it over medium-low heat, stirring constantly with a wooden spoon or a spatula, scraping the bottom and corners, for about five to eight minutes.""",
   "stirring custard saucepan wooden spoon", "STIR CONSTANTLY")
sc("""Mistake number four is cooking it too hot or too long. It curdles. You want it to reach one hundred sixty to one hundred seventy degrees on a thermometer, no more. Or use the old test. Dip a spoon in, and run your finger across the back. If the line stays clean and doesn't run back together, it's done. Take it off the heat right away.""",
   "finger line custard back of spoon", "THE SPOON TEST")
sc("""And if it does start to curdle a little, sweetheart, don't panic. Take it off the heat immediately and pour it into a cold bowl. Then whisk it hard, or blend it for a few seconds. Small lumps will smooth right out. Then pour it through a fine strainer into a clean pitcher or bowl. Always strain it anyway. It catches the cinnamon stick and any little bits of cooked egg.""",
   "straining custard fine sieve", "STRAIN IT")

ch("The secret")
sc("""So far, whole milk and cream, fresh nutmeg, pale yolks, temper the eggs slowly, and cook it gently to one sixty, then strain it. Stir in the vanilla. Now the secret I promised, the one that makes it thick. Mistake number five is drinking it right away, warm. Warm eggnog is thin. Cold eggnog is thick and velvety, the way Grandma Pearl's was.""",
   "pitcher of eggnog cooling", "COLD IS THICK")
sc("""Cover it, and put it in the icebox for at least four hours, and overnight is even better. The custard thickens as it chills, and the flavors of the nutmeg and vanilla come out. That's Grandma Pearl's springhouse. And if you want it extra light and fluffy, whip a half cup of cream to soft peaks right before serving, and fold it in gently.""",
   "eggnog refrigerator overnight", "THE SPRINGHOUSE")

ch("For the grown-ups")
sc("""For the grown-ups, stir in the bourbon, brandy, or rum after it's chilled, a little at a time, and taste it. My father liked bourbon. Grandma Pearl liked a mix of brandy and rum, half and half, and she said it was medicinal. Some people make a big batch with the spirits in it and let it age in the icebox for weeks. That's a little too brave for me, honey.""",
   "bourbon brandy bottles eggnog", "IT'S MEDICINAL")
sc("""And always keep a pitcher without any spirits, for the children and for the drivers. I put a little red ribbon around the handle of the children's pitcher, so nobody mixes them up. Learned that one the hard way in nineteen seventy-three, when my nephew Michael drank two cups of the wrong one and fell asleep under the Christmas tree.""",
   "two pitchers eggnog ribbon", "THE WRONG PITCHER")

sc("""And save those egg whites, honey. Don't throw them away. Put them in a jar in the icebox, and they keep four days. Use them for a batch of divinity, or meringue cookies, or a white cake. Or whip two of them to soft peaks and fold them into the eggnog right before serving, for a frothy, old-fashioned nog. That's how my grandmother's mother made it, back in the eighteen nineties.""",
   "jar of egg whites meringue", "SAVE THE WHITES")

ch("Serving")
sc("""To serve it, pour it into a punch bowl or small glasses, and grate fresh nutmeg over the top. Add a cinnamon stick in each glass for stirring. Or a little dollop of whipped cream. It's rich, sweetheart, so small cups. A big glass of eggnog is like eating a whole pie. Grandma Pearl served it in little glass punch cups no bigger than an egg.""",
   "eggnog glasses cinnamon stick nutmeg", "SMALL CUPS")
sc("""And it's wonderful in other things, too. A splash in your morning coffee. Use it instead of milk for French toast on Christmas morning. Or in a bread pudding, or a pound cake. My granddaughter makes eggnog pancakes on Christmas morning, and the house smells like nutmeg until noon.""",
   "eggnog French toast breakfast", "EGGNOG FRENCH TOAST")
sc("""Homemade eggnog keeps three days in the icebox, in a covered pitcher. Give it a good stir before serving, because it settles. It doesn't freeze well, honey, because it separates when it thaws. So make only what you'll drink in a few days. That's never a problem in my family. The pitcher is always empty by the second day.""",
   "eggnog pitcher refrigerator", "THREE DAYS")

sc("""And if somebody can't have dairy, sweetheart, you can make it with oat milk or almond milk and a can of coconut cream instead of the heavy cream. It's not quite the same, but it's thick and sweet and full of nutmeg. My grandson's wife can't have milk, and I make her a little pitcher every year. She says it tastes like Christmas, and that's the whole point.""",
   "oat milk coconut cream eggnog", "IT TASTES LIKE CHRISTMAS")

ch("Grandma's kitchen")
sc("""So one more time. Whole milk and cream, never skim. Fresh nutmeg. Whisk the yolks and sugar until pale. Temper the eggs slowly with the hot milk. Cook it gently, stirring, to one sixty, and strain it. Chill it overnight. Spirits for the grown-ups, and a ribbon on the children's pitcher. That's Grandma Pearl's eggnog, thick enough to stand a spoon in.""",
   "eggnog punch bowl Christmas party", "THICK ENOUGH FOR A SPOON")
sc("""Tell me in the comments, sweetheart. Do you love eggnog, or can't you stand it? I know families are divided. The whole playlist of Grandma's recipes is right there on your screen, and I'll see you in the next video. Good night, honey. Merry Christmas.""",
   "Christmas evening fireplace drinks", "LOVE IT OR HATE IT?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma56", "Homemade Eggnog EVERYONE's Grandma Made (Why Yours Is RUNNY)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Eggnog history: English posset and colonial American eggnog made with rum, whiskey and brandy.",
      "Food safety: cook egg custard bases to 160 F (USDA Food Safety and Inspection Service).",
      "Recipe as written by Grandma Ruth: 6 egg yolks, 1/2 cup sugar, 2 cups whole milk, 1 cup heavy cream, pinch of salt, 1 tsp vanilla, 1/2 tsp fresh nutmeg, 1 cinnamon stick; cooked to 160 to 170 F, strained, chilled overnight."],
     "christmas recipe", minutes=(10, 14.5), voice="en_US-lessac-high")
