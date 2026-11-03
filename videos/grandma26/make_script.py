import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 26 · Christmas tips: cheap simple Christmas table decorations (Google Trends 3/11, rising)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, I've been to a lot of Christmas dinners in eighty-two years. And I can tell you, the most beautiful Christmas table I ever sat at cost less than ten dollars. It was my mother's, in nineteen fifty-two, and it was made of pine branches from the yard, a white bedsheet, and four candles. People who came to our house that night talked about that table for years.""",
   "1950s Christmas dinner table candles", "LESS THAN TEN DOLLARS")
sc("""And last year I went to a house where they had spent three hundred dollars on table decorations, and it looked like a store shelf fell over on it. So tonight I'm giving you nine Christmas table mistakes that make a table look cheap, no matter what you spent. And for every one, the old way to fix it for almost nothing.""",
   "cluttered Christmas table decorations", "LIKE A STORE SHELF FELL OVER")

ch("1. The tall centerpiece")
sc("""Mistake number one. A centerpiece so tall that nobody can see across the table. Big vases, tall branches, towers of ornaments. It looks grand when the table is empty, but the minute people sit down, Aunt Carol is talking to a wall of greenery. A Christmas table is for faces, honey. Not for decorations.""",
   "tall centerpiece dinner table guests", "A WALL OF GREENERY")
sc("""The fix. Keep everything in the middle lower than your chin when you're sitting down. About twelve inches. My mother's rule was, put your elbow on the table and your hand straight up. Nothing taller than your fingertips. Go long instead of tall. A low line of greenery running down the middle of the table, from one end to the other.""",
   "low garland runner dinner table", "LOWER THAN YOUR CHIN")

ch("2. Too many colors")
sc("""Mistake number two. Every color at once. Red plates, green napkins, gold chargers, blue ornaments, silver tinsel, and a plaid tablecloth. It looks busy and cheap, like a dollar store aisle. The tables that look expensive almost always use only two colors, maybe three, and lots of green and white.""",
   "colorful cluttered Christmas table", "LIKE A DOLLAR STORE AISLE")
sc("""Pick two. Red and white. Or green and gold. Or white and silver. Use what you already have in those colors, and put the rest away for another year. My mother's table was white and green, with red only in the candles and a bowl of apples. That's it. Three things red on the whole table, and it looked like a magazine.""",
   "white and green Christmas table candles", "PICK TWO COLORS")

sc("""And if you want a little sparkle, use only one metal. All gold, or all silver. Not both. My mother had six brass candlesticks from Grandma Pearl, and she polished them on the twenty-third of December every year with a rag and a jar of paste. Six gold candlesticks and white candles on a green and white table. People thought we were rich. We were not rich, honey.""",
   "brass candlesticks polished table", "WE WERE NOT RICH")

ch("3. The plastic tablecloth")
sc("""Mistake number three. The shiny plastic tablecloth with printed holly on it. Nothing makes a table look cheaper, faster. It wrinkles, it shines under the lights, and it squeaks when you put a plate down. In the fifties, a plastic tablecloth was for the kitchen and the picnic. Never for Christmas dinner.""",
   "plastic tablecloth printed holly", "IT SQUEAKS")
sc("""The fix costs nothing. A plain white flat bedsheet, ironed, folded under at the ends. That's exactly what my mother used. Nobody can tell it's a sheet once the plates are on. Or a length of plain burlap or cotton from the fabric store for a few dollars. Plain fabric always looks richer than printed plastic. Always.""",
   "white linen tablecloth ironed", "A WHITE BEDSHEET")

ch("4. No real greenery")
sc("""Mistake number four. Plastic garland and fake berries. Real greenery is free, honey, and nothing smells like Christmas the way it does. Go out to the yard, or ask a neighbor with a pine tree, or ask at the Christmas tree lot for the trimmed branches they cut off the bottom. Most lots give them away. Some leave them in a pile by the fence.""",
   "fresh pine branches cut", "REAL GREENERY IS FREE")
sc("""Lay the branches flat down the middle of the table, overlapping like shingles. Tuck in a few sprigs of holly, or rosemary from the store, and some pinecones from the yard. That's your runner. Mist it with water the night before so it stays fresh. And put a towel underneath at the ends, so the sap doesn't touch the tablecloth.""",
   "pine branch table runner pinecones", "OVERLAPPING LIKE SHINGLES")

ch("5. Bright overhead lights")
sc("""Mistake number five. Eating under the big ceiling light. That bright white light from above makes the food look gray, the table look flat, and everybody look ten years older. Your table could be perfect, and the ceiling light will make it look like a cafeteria.""",
   "dining room bright ceiling light", "LIKE A CAFETERIA")
sc("""Turn off the overhead light at dinner, and light the table with candles. Lots of them, low ones, at different heights. Plain white candles in jars, or in glasses from your cupboard, or in hollowed-out apples. Then turn on one small lamp in the corner so nobody trips. Candlelight makes every table look like it cost a fortune. And every face, too.""",
   "candlelit Christmas table glow", "CANDLELIGHT")
sc("""But please, no scented candles on the dinner table. Cinnamon and vanilla candles fight with the smell of the turkey and the rolls. Your nose gets confused, and the food tastes like a gift shop. Save the scented candles for the bathroom and the front hall. Plain, unscented white candles on the table.""",
   "unscented white pillar candles", "NO SCENTED CANDLES")

sc("""And put a small vase of greenery or a jar candle in the bathroom too, sweetheart. That's the one room every guest visits alone, and they notice. A clean towel folded nice, a sprig of pine in a glass, one candle. My mother said you can tell everything about a house from the guest towel. She was a little dramatic. But she wasn't wrong.""",
   "guest bathroom candle towel pine", "THE GUEST TOWEL")

ch("6. Paper napkins")
sc("""Mistake number six. Paper napkins with Santa on them. I understand, honey, nobody wants to iron. But a real cloth napkin, even a cheap one, changes the whole table. You can buy plain white cotton napkins in a pack for a few dollars and use them every Christmas for twenty years.""",
   "cloth napkins folded table setting", "A REAL CLOTH NAPKIN")
sc("""And here's my mother's trick for making them look special. Tie each one with a piece of red yarn or kitchen twine, and tuck in a little sprig of pine or rosemary. Or a single candy cane. Lay it right on the plate. It takes ten minutes for the whole table, and it looks like you hired somebody.""",
   "napkin tied twine rosemary sprig", "LIKE YOU HIRED SOMEBODY")

ch("7. Crowded table")
sc("""Mistake number seven. Too much stuff. Decorations, serving dishes, salt and pepper, butter, gravy, three kinds of rolls, and no room for anyone's elbows. A crowded table looks cluttered, and cluttered looks cheap. In my mother's house, the serving dishes stayed on the sideboard, and my father carved at the head of the table.""",
   "crowded holiday dinner table dishes", "NO ROOM FOR ELBOWS")
sc("""So clear the decorations to one low line down the middle. Put the big serving dishes on the counter or a side table and let people serve themselves. Leave only the bread, the gravy, and the butter on the table. Give each person at least two feet of space. A table with breathing room looks generous.""",
   "elegant uncluttered dinner table", "ROOM TO BREATHE")

ch("8. Nothing personal")
sc("""Mistake number eight. A table with nothing personal on it. You can buy a beautiful table setting in any store, and it will look like any store. What makes a table yours is one small thing that tells people they belong there. In our house, it was name cards.""",
   "place card handwritten name table", "SOMETHING PERSONAL")
sc("""My mother wrote each person's name on a little card in her round handwriting, and propped it on a walnut or tucked it in a pinecone. Or write each name on a paper tag and tie it to an ornament, and let people take the ornament home. My grandchildren still have the little glass balls with their names in gold paint from when they were small.""",
   "ornament name tag place setting", "THEY TAKE IT HOME")

ch("9. Forgetting the smell")
sc("""And mistake number nine, the one nobody thinks about. A Christmas table should smell like Christmas before anybody sits down. My mother's trick cost almost nothing. She pushed whole cloves into oranges, in rows or in little stars, and set them in a bowl in the middle of the table. They're called pomanders, and people have made them for hundreds of years.""",
   "oranges studded with cloves pomander", "ORANGES WITH CLOVES")
sc("""Make them with the children a few days before. An orange, a small jar of whole cloves, and a toothpick to start the holes. They smell wonderful, they look like little Christmas ornaments, and when the warm room heats them up, the whole table smells like orange and spice. A bag of oranges and a jar of cloves, five dollars, and the best centerpiece in America.""",
   "children making clove oranges table", "FIVE DOLLARS")

sc("""And one more piece of advice, the most practical one. Set the table the night before. On Christmas Eve, after the children are in bed, lay the cloth, the branches, the candles, the plates and the napkins. Then on Christmas Day, when the kitchen is a storm and the turkey is late, the table is already done and waiting. My mother never once set a table in a hurry.""",
   "table set night before candles dark", "SET IT THE NIGHT BEFORE")

ch("Grandma's ten-dollar table")
sc("""So here is my ten-dollar Christmas table, honey. A white sheet, ironed. Pine branches from the yard down the middle, low. A few pinecones and clove oranges. Plain white candles in jars and glasses. Cloth napkins tied with red yarn and a sprig of green. A name on every plate. Two colors. Overhead light off. That's all. It will look like a magazine.""",
   "simple elegant Christmas table pine candles", "THE TEN-DOLLAR TABLE")
sc("""Tell me in the comments, sweetheart. What did your family's Christmas table look like when you were little? Did you have the good china, or paper plates? I read every comment. Good night, honey. Merry Christmas.""",
   "vintage family Christmas dinner", "WHAT DID YOUR TABLE LOOK LIKE?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma26", "9 Christmas Table Mistakes That Make It Look CHEAP (Fix Them for $10)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Pomanders: oranges studded with whole cloves, a centuries-old European custom.",
      "Christmas tree lots commonly give away trimmed lower branches."],
     "christmas with tips", minutes=(10, 14.5), voice="en_US-lessac-high")
