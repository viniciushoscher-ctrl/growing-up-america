import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 19 · Christmas tips: gift wrapping, do this and avoid that
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, every Christmas morning I watch my grandchildren rip through forty dollars of wrapping paper in about four minutes. Shiny paper, plastic bows, tape everywhere, and it all goes in a black trash bag before the coffee is ready. And I think of my mother, who wrapped every present we ever got for almost nothing, and they were so pretty that we didn't want to open them.""",
   "Christmas presents under tree wrapped", "FORTY DOLLARS IN FOUR MINUTES")
sc("""So tonight, the seven gift wrapping mistakes that make your presents look cheap, and exactly what to do instead. Most of it costs nothing at all. Some of it you already have in your kitchen drawer. By the end, your presents will be the ones people take pictures of before they open them.""",
   "beautiful wrapped gifts ribbon", "SEVEN MISTAKES")

sc("""In our house, Christmas wrapping was a whole evening. The Sunday before Christmas, my mother cleared the kitchen table after supper, spread out a clean sheet, and brought out the shoebox with the ribbon and the good scissors that nobody else was allowed to touch. Danny and I had to stay in the front room, but we could hear the paper crinkle, and we'd try to guess what was in every box by the sound.""",
   "1950s family kitchen table evening", "THE GOOD SCISSORS")

ch("1. Paper cut too big")
sc("""Mistake number one. Cutting the paper too big. You end up with thick wads of paper folded over and over at the ends, lumpy corners, and so much tape the box looks bandaged. A present with fat ends always looks cheap, no matter how expensive the paper was.""",
   "messy wrapped present tape", "LOOKS BANDAGED")
sc("""Do this instead. Measure. The paper should go around the box with just two inches of overlap, and on the ends it should come up only three quarters of the height of the box. My mother laid the box on the paper, rolled it once around to see, and cut with her good scissors in one long slide. Then she folded the edge of the overlap under, half an inch, so there was no raw cut edge showing. Clean as a store.""",
   "wrapping gift paper scissors table", "TWO INCHES OF OVERLAP")

sc("""And for a box that isn't square, honey, a round tin or an odd shape, don't fight it. Set it in the middle of a big square of paper, gather the paper up around it like a bag, and tie it at the top with ribbon, so it looks like a little sack of candy. My mother wrapped Grandma Pearl's round tins of homemade candy that way every year, and they were the prettiest things under the tree.""",
   "round gift wrapped gathered ribbon top", "LIKE A SACK OF CANDY")

ch("2. Tape everywhere")
sc("""Mistake number two. Tape everywhere you can see it. Long crooked strips across the top, tape on every corner, tape over tape. Tape is the first thing the eye goes to, honey, and it makes even a beautiful paper look rushed.""",
   "scotch tape roll gift wrap", "TAPE OVER TAPE")
sc("""Do this instead. Use double-sided tape, or roll a little piece of regular tape into a loop and hide it under the folded edge. Three small hidden pieces are enough for any box. In nineteen fifty-three, tape was expensive, so my mother used just one or two pieces and a ribbon held the rest. Nobody ever saw a single piece of tape on her presents.""",
   "hands folding gift wrap edge", "HIDE THE TAPE")

sc("""One more trick for crisp edges. After you fold each end, run your thumbnail hard along every fold, all twelve edges of the box. It makes a sharp line, like a pressed shirt collar. My mother called it ironing the present. It takes one minute, and it's the whole difference between homemade and handsome.""",
   "crisp folded edge gift box", "IRONING THE PRESENT")

ch("3. Plastic stick-on bows")
sc("""Mistake number three. The plastic stick-on bow. It's the one thing that says, I wrapped this in the car. They get crushed in the bag, they fall off, and they're all the same in every house in America.""",
   "plastic gift bows pile", "WRAPPED IN THE CAR")
sc("""Do this instead. Real ribbon, tied by hand. Cloth ribbon if you can, or plain red yarn, or kitchen string. Go around the box both ways, crossed underneath, and tie the bow on top. And here's Grandma Pearl's trick. Tuck something into the knot. A sprig of pine. A cinnamon stick. A candy cane. A little bell. It costs pennies, and it looks like a present from a magazine.""",
   "gift tied twine pine sprig cinnamon", "TUCK SOMETHING IN THE KNOT")

sc("""And save your ribbon, sweetheart. When the presents are opened, roll the good ribbons around a piece of cardboard and put them in the shoebox for next year. My mother had red velvet ribbon that went around our presents for eleven Christmases in a row. When it finally got too short, she cut it up and tied the pieces on the tree.""",
   "ribbon rolled spool box", "ELEVEN CHRISTMASES")

ch("4. Too many patterns")
sc("""Mistake number four. Every present in a different loud paper. Santas, snowmen, stripes, glitter, all under the same tree. It looks like a garage sale, honey, and none of the presents stand out because they're all shouting.""",
   "colorful Christmas wrapping paper rolls", "A GARAGE SALE")
sc("""Do this instead. Pick one plain paper for everything, and change only the ribbon. Brown kraft paper is the cheapest paper there is, and with red ribbon it looks beautiful. White butcher paper with green ribbon. My mother used plain brown paper from the A and P, the kind they wrapped meat in, and tied it with red yarn. The whole tree matched, and people stopped to look.""",
   "brown kraft paper gifts red ribbon", "ONE PAPER, CHANGE THE RIBBON")

sc("""If you want to dress up the plain brown paper, let the children do it. A potato cut in half, carved into a star, dipped in red paint and stamped all over the paper. Or little white fingerprints that look like snow. Danny and I stamped the paper every year, crooked stars everywhere, and Grandma Pearl kept every piece we ever stamped in her cedar chest.""",
   "children stamping paper potato stamp", "POTATO STAMPS")

ch("5. Buying gift bags")
sc("""Mistake number five. Buying a new gift bag for every present. They cost three or four dollars each, sometimes more than the gift inside, and the tissue paper sticks out like a feather duster.""",
   "Christmas gift bags tissue paper", "MORE THAN THE GIFT")
sc("""Do this instead. Wrap in things that are part of the gift. A kitchen towel tied around a jar of jam. A pretty scarf around a book. A cookie tin from the thrift store. A Mason jar with a square of red cloth over the lid. The Japanese have wrapped gifts in cloth for hundreds of years, and my mother did it with flour sack cloth in the war years, because paper was rationed.""",
   "gift wrapped in cloth fabric knot", "THE WRAPPING IS A GIFT")

sc("""And here's a trick for gifts that are hard to hide. A bicycle, a sled, a big box that won't fit under the tree. Don't wrap it at all. Hide it in the garage or at the neighbor's, and tie one end of a long red string to it. Run the string through the house and tie the other end to the child's bedpost on Christmas Eve. In the morning they follow the string. Danny followed one to his first bicycle in nineteen fifty-four, and he talked about it until the day he died.""",
   "red string treasure hunt Christmas morning", "FOLLOW THE STRING")

ch("6. No name, or a sticker")
sc("""Mistake number six. A store-bought sticker that says To and From, or worse, nothing at all, and then nobody knows whose present is whose on Christmas morning.""",
   "gift tag Christmas present", "WHOSE IS THIS?")
sc("""Do this instead. Make tags from last year's Christmas cards. Cut out the pretty picture, punch a hole, write the name on the back, and tie it on with the ribbon. My mother saved every Christmas card in a shoebox for exactly that. And write something on the tag besides the name. A line, a memory. My father wrote a little joke on every one of mine, and I still have some of them.""",
   "old Christmas cards cut tags", "LAST YEAR'S CARDS")

sc("""And for the little ones, a tag with a riddle instead of a name. Who is the only one in this house who sings in the bathtub? Who left their boots in the hall three times this week? My mother did it one year and we laughed so hard my father had to stop the whole morning. Now my grandchildren beg for riddle tags.""",
   "family laughing Christmas morning", "RIDDLE TAGS")

ch("7. Wrapping it all on the 24th")
sc("""Mistake number seven. Wrapping everything on Christmas Eve at midnight, with the bad scissors and the last bit of tape, while everybody else is asleep. That's how presents end up looking cheap. Not from the paper. From being tired.""",
   "late night wrapping presents", "MIDNIGHT ON THE 24TH")
sc("""Do this instead. Wrap as you buy. Keep a wrapping box under the bed with your paper, ribbon, scissors and tags, and every time a present comes home, wrap it that same night. One present takes five minutes. By the twentieth everything is done, and Christmas Eve is for cocoa and carols, the way it should be.""",
   "wrapping supplies box ribbon paper", "WRAP AS YOU BUY")

sc("""And keep the mess under control on Christmas morning, honey. Put one big paper grocery sack by the tree for the wrapping, and one little box for the ribbons and tags worth saving. My father was in charge of the sack. Every time somebody opened a present, he'd hold it out, and we'd throw the paper in like a basketball. Two points for every shot.""",
   "Christmas morning wrapping paper bag", "TWO POINTS")

ch("Grandma's rule")
sc("""So here's the whole lesson, sweetheart. Measure the paper. Hide the tape. Real ribbon, with something tucked in the knot. One paper for the whole tree. Wrap in things that are part of the gift. Tags from old cards. And wrap as you buy. Do that, and the cheapest present under the tree will look like the most expensive one.""",
   "elegant wrapped presents under tree", "THE CHEAPEST LOOKS BEST")
sc("""And tell me in the comments, honey. Are you a paper ripper, or do you open them slowly and save the paper like my mother did? I read every one. Good night, sweetheart. Merry Christmas.""",
   "child opening Christmas present", "RIPPER OR SAVER?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma19", "7 Gift Wrapping Mistakes That Make Your Presents Look CHEAP (AVOID These)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "US paper conservation and rationing on the home front during World War II.",
      "Furoshiki, the traditional Japanese cloth used to wrap gifts."],
     "christmas with tips", minutes=(10, 14.5), voice="en_US-lessac-high")
