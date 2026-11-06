import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 43 · Christmas tips: gift wrapping mistakes (Google Trends 3/11: homemade christmas gifts, cheap simple christmas ideas rising)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, my mother could wrap a present so beautifully that you didn't want to open it. Plain brown paper from the butcher, a red ribbon, and a sprig of pine from the yard. That's all. And under our little tree on Elm Street, her presents looked better than the ones from the fancy department store in Cleveland, with their shiny paper and their store bows.""",
   "brown paper gift red ribbon pine", "BETTER THAN THE STORE")
sc("""So tonight I'm giving you seven gift wrapping mistakes that make presents look cheap, and my mother's old tricks to fix every one, most of them free. And stay with me, because the last trick is the one that makes people save the wrapping, and it takes about ten seconds per present.""",
   "beautifully wrapped Christmas presents", "SEVEN WRAPPING MISTAKES")

ch("Mother's wrapping table")
sc("""Every year, the week before Christmas, my mother cleared the kitchen table after supper and turned it into her wrapping station. Scissors, a roll of brown paper, a spool of red ribbon, a jar of paste, and a pile of pine sprigs. I was allowed to hold my finger on the knots. That was the most important job in the house, she said, and I believed her.""",
   "1950s kitchen table wrapping presents", "HOLD THE KNOT")
sc("""She never bought wrapping paper in her life, honey. She saved everything. Brown paper from the butcher, the Sunday funny pages, old maps, even wallpaper samples from the hardware store. And she ironed the ribbon from last year with a warm iron, so it looked brand new. In a minute I'll show you why plain paper looks richer than the fanciest roll at the store.""",
   "ironing ribbon vintage iron", "SHE SAVED EVERYTHING")

ch("1. Too much paper")
sc("""Mistake number one. Using too much paper. People wrap a small box in a huge sheet, and then they fold and fold and tape over all those bunched-up corners, and it looks like a lumpy pillow. Here's the rule. The paper should go around the box with only two inches of overlap, and on the ends, only a little more than half the height of the box.""",
   "lumpy badly wrapped present", "A LUMPY PILLOW")
sc("""So measure it, sweetheart. Roll the box over the paper once, all the way around, add two inches, and cut. Then stand the box on its end. The paper on each side should reach just past the middle. Cut off the extra. With less paper, your corners fold flat and sharp, like a hospital bed. My mother learned that in nurse's training.""",
   "measuring wrapping paper around box", "LIKE A HOSPITAL BED")

ch("2. Tape everywhere")
sc("""Mistake number two. Tape everywhere. Long strips of shiny tape all over the present, on the corners, on the sides, crooked and bubbly. The fix is double-sided tape, or just three little pieces of regular tape, hidden. Fold the edge of the paper under, about half an inch, so it makes a clean, straight line, then tape it underneath where nobody can see.""",
   "too much tape on present", "HIDE THE TAPE")
sc("""And fold that edge under, honey, every time. A raw cut edge always looks a little ragged, even if you cut it straight. A folded edge looks crisp, like a crease in a man's good trousers. Then run your thumbnail along every fold before you tape it. Sharp creases are the whole secret to a present that looks like it came from a shop.""",
   "folding paper edge crisp crease", "RUN YOUR THUMBNAIL")

ch("3. Busy paper, busy bow")
sc("""Mistake number three. Busy paper with a busy bow. Paper covered in Santas and snowmen and candy canes, with a shiny stick-on bow in a different color, and a curly ribbon in another. It's too much. Pick one thing to be the star. If the paper is busy, use a plain ribbon. If the paper is plain, then the ribbon and the trim can shine.""",
   "busy Christmas wrapping paper bow", "PICK ONE STAR")
sc("""And that's why plain paper looks richer, like I promised. Brown kraft paper, white butcher paper, or one solid color. It costs a third of the price of the printed rolls. Then add a nice ribbon, some real greenery, and a handwritten tag, and it looks like something from a fancy shop. The plain paper lets the pretty things stand out.""",
   "kraft paper gifts greenery ribbon", "A THIRD OF THE PRICE")

ch("4. Stick-on bows")
sc("""Mistake number four. Those stick-on plastic bows. They come in a bag of fifty for two dollars, they fall off in the car, and they look exactly like what they are. Here's the fix. Real ribbon, tied around the box both ways, like a cross, with a proper bow on top. Use wired ribbon if you can, because it holds its shape and the loops stand up nice and full.""",
   "stick on plastic bows bag", "THEY FALL OFF")
sc("""If this is helping you, honey, tap the like button for me. It helps Grandma more than you know. Now here's how to tie a bow that lies flat and pretty. Make two loops, like bunny ears, and cross them over, tuck one under, pull it tight. Then pinch the loops and pull them out, so they're the same size. And cut the ends on a slant, or in a V, so they don't fray.""",
   "tying ribbon bow on gift", "CUT A V")
sc("""And a cheap trick for ribbon, honey. Plain cotton string or baker's twine, red and white, costs almost nothing. Wrap it around three or four times and tie a simple knot. Or use strips of fabric torn from an old flannel shirt or a tablecloth. My mother used the leftover red calico from her kitchen curtains for years. People asked her where she bought it.""",
   "red white bakers twine gift", "TORN FABRIC RIBBON")

ch("5. No tag")
sc("""So far, the right amount of paper, hidden tape and folded edges, one star, and real ribbon instead of stick-on bows. Now mistake number five. A sticker tag, or worse, writing on the paper with a marker. A real tag makes all the difference. Cut them from old Christmas cards, the front picture, with a hole punched in the corner. Tie it on with the ribbon.""",
   "gift tags cut from Christmas cards", "OLD CHRISTMAS CARDS")
sc("""And write it by hand, sweetheart, in your best writing. Not just to and from. Add one little line. For my favorite baker. For the best brother in Ohio. My brother Danny still has every tag I ever wrote him, in a cigar box, sixty years of them. He showed me last Christmas, and I had to go sit in the car for a minute.""",
   "handwritten gift tag cigar box", "SIXTY YEARS OF TAGS")

ch("6. The odd shapes")
sc("""Mistake number six. Trying to wrap odd shapes in paper. A bottle, a ball, a stuffed bear, a frying pan. You end up with a crumpled mess. The fix is a box, or a bag. Put odd things in any old box from the kitchen, a shoebox, a cereal box turned inside out, and wrap the box. Nobody can guess what's inside, and that's half the fun.""",
   "odd shaped gift crumpled paper", "PUT IT IN A BOX")
sc("""And for really big things, like a bicycle, don't wrap it at all. Put a big bow on it and hide it behind a sheet in the corner until Christmas morning. Or wrap a tiny box with a clue inside, and a treasure map to the garage. My father did that for Danny's first bicycle in nineteen fifty-five. Danny cried so hard, he couldn't find the garage.""",
   "bicycle big red bow Christmas", "A TREASURE MAP")

ch("7. The finishing touch")
sc("""And now mistake number seven, the trick I promised. A present with nothing tucked in the bow. It's finished in ten seconds. Slide a little sprig of pine or cedar, a cinnamon stick, a candy cane, a dried orange slice, or a sprig of rosemary under the ribbon, right in the knot. That's the thing people save. They take it off and put it on the windowsill.""",
   "pine sprig cinnamon stick gift bow", "TEN SECONDS")
sc("""My mother tucked a little pinecone in every bow, painted white at the tips, like snow. She'd collect them in October with the grandchildren, and paint them at the kitchen table. Years later, I found a box in her closet with dozens of those little pinecones. People had given them back to her, saying, Dorothy, these are too pretty to throw away.""",
   "white tipped pinecones box", "TOO PRETTY TO THROW AWAY")

sc("""And if you have little ones at home, honey, give them a job like my mother gave me. Let them stamp the plain paper with a cut potato dipped in red paint, stars or trees, before you wrap. Let it dry overnight. It's the prettiest paper in the world, and the grandparents will never throw it away. My granddaughter's potato paper from nineteen ninety-six is still in my cedar chest.""",
   "child potato stamping paper", "POTATO STAMP PAPER")

ch("Saving money")
sc("""And a few last tips for saving money. Buy ribbon and paper the day after Christmas, at half price, for next year. Save the boxes you get. Gift bags can be used ten times, so ask for them back with a smile. Fold the good tissue paper flat and keep it in a drawer. My mother's wrapping cost her about a dollar a year, and it was the prettiest on the street.""",
   "folded tissue paper ribbon drawer", "A DOLLAR A YEAR")
sc("""And set up a wrapping station like she did, honey. Everything in one basket, scissors, tape, ribbon, tags, a pen, and a little bag for scraps. Put on some Christmas music, make a cup of cocoa, and wrap a few every night the week before. Wrapping twenty presents on Christmas Eve at midnight is how presents end up looking like lumpy pillows.""",
   "wrapping basket scissors ribbon cocoa", "A FEW EVERY NIGHT")

ch("Grandma's wrapping")
sc("""So one more time. Cut the paper to fit, with two inches of overlap. Fold the edges under and hide the tape. Run your thumbnail along every crease. Plain paper with pretty ribbon, or busy paper with plain ribbon. Real ribbon, tied both ways. A handwritten tag. Odd shapes in a box. And something tucked in the bow. That's how my mother wrapped Christmas.""",
   "Christmas presents under tree beautiful", "HOW MOTHER WRAPPED")
sc("""Tell me in the comments, sweetheart. Are you a careful wrapper, or a gift bag person? No judging, I promise. The whole playlist of Grandma's Christmas tips is right there on your screen, and I'll see you in the next video. Good night, honey. Merry Christmas.""",
   "Christmas tree presents evening", "WRAPPER OR GIFT BAG?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma43", "7 Gift Wrapping Mistakes That Make Your Presents Look CHEAP",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Thrift-era gift wrapping in mid-century American homes: butcher paper, newspaper, saved and pressed ribbon.",
      "Wrapping method as described by Grandma Ruth: about 2 inches of overlap, edges folded under, tape hidden, ribbon tied both ways."],
     "christmas with tips", minutes=(10, 14.5), voice="en_US-lessac-high")
