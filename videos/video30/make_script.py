import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 30 · angle 3 (an everyday theme, what she trusted vs. what we learned) · evening slot · day 10
# The Truth About the 1960s Kitchen Your Mother Trusted

sc("""Your mother's kitchen in the nineteen sixties was her pride. Gleaming appliances in harvest gold or turquoise. A spice rack. A row of canisters for flour, sugar, coffee and tea. A cabinet full of new products from the supermarket, each one promising to make her life easier, her family healthier and her house cleaner. And she trusted every one of them.""",
   "1960s kitchen housewife modern appliances", "THE KITCHEN SHE TRUSTED")
sc("""Why wouldn't she? The products came from big, respected companies. They were advertised on television by friendly actors in white coats. Doctors endorsed them. Magazines praised them. In the sixties, Americans had enormous faith in science, progress and modern living.""",
   "1960s television advertisement housewife", "ENORMOUS FAITH")
sc("""But some of those things turned out to be very different from what they seemed. And some of the things she was told were old-fashioned turned out to be right all along. So let's open the cupboards of the nineteen sixties kitchen, one by one, and see what we know now.""",
   "1960s kitchen cabinets", "WHAT WE KNOW NOW")

ch("The bug spray")
sc("""Let's start under the sink. In many sixties kitchens, there was a can of bug spray, and it often contained DDT. During the fifties and early sixties, DDT was considered a miracle. It killed mosquitoes, flies and roaches. It was sprayed on crops, in homes, and even from trucks driving through neighborhoods on summer evenings.""",
   "1950s DDT spraying truck neighborhood", "DDT")
sc("""Kids ran behind the fogging trucks, playing in the white cloud. Nobody thought it was dangerous. Then, in nineteen sixty-two, a biologist named Rachel Carson published a book called Silent Spring. She showed that DDT was killing birds and building up in the food chain. The book caused a sensation. In nineteen seventy-two, DDT was banned in the United States for most uses.""",
   "Rachel Carson Silent Spring", "SILENT SPRING")

ch("The cleaning products")
sc("""Also under the sink were the cleaning products. Bleach, ammonia, scouring powder, oven cleaner and furniture polish. Mothers used them all, often in a small kitchen with the windows closed. Some even mixed bleach and ammonia, thinking two cleaners would work better than one. That mixture releases a toxic gas, and it sent many people to the hospital.""",
   "1960s cleaning products under sink", "UNDER THE SINK")
sc("""And the laundry detergent of the sixties was loaded with phosphates. They made clothes whiter, but when the water went down the drain, they fed huge blooms of algae in lakes and rivers. Lake Erie became so polluted that newspapers called it dying. In the early seventies, many states banned or limited phosphates in laundry soap, and the lakes slowly recovered.""",
   "1960s laundry detergent box", "PHOSPHATES")

ch("The sweeteners")
sc("""On the kitchen table, there might have been a little bottle of artificial sweetener. In the sixties, diet sodas became very popular, and many of them were sweetened with a chemical called cyclamate, often mixed with saccharin. Tab, Diet Rite and Fresca. Women trying to stay slim drank them by the case.""",
   "1960s diet soda bottles", "DIET SODA")
sc("""In nineteen sixty-nine, a study found that very high doses of cyclamate caused cancer in rats. The government banned it almost overnight. Companies had to reformulate their diet drinks in a hurry. Later research questioned whether cyclamate was really as dangerous as feared, and it's still allowed in many other countries. But in America, it never came back.""",
   "1960s woman drinking soda kitchen", "BANNED IN 1969")

ch("The red dye")
sc("""In the cupboard, there was food coloring, and many packaged foods contained a dye called Red Dye Number Two. It was in candy, cake mixes, sausages, ice cream and soft drinks. It made maraschino cherries bright red. It was one of the most common food dyes in the country.""",
   "1960s colorful candy cake mix", "RED DYE NUMBER TWO")
sc("""In the seventies, studies raised concerns that Red Dye Number Two might cause cancer. In nineteen seventy-six, the government banned it. The scare was so big that the Mars company took red M and M's out of the bag for almost ten years, even though they had never used that dye. Red M and M's didn't come back until nineteen eighty-seven.""",
   "1970s candy store colorful", "RED M&Ms DISAPPEARED")

ch("The walls")
sc("""Even the kitchen walls held a secret. Many homes built before nineteen fifty, and some built later, were painted with lead-based paint. It was durable, and it came in bright, washable colors that were perfect for a kitchen. When it chipped or peeled, small children sometimes put the flakes in their mouths, because lead tastes slightly sweet.""",
   "1950s kitchen painted walls cabinets", "LEAD PAINT")
sc("""Doctors slowly learned that even small amounts of lead could harm a child's brain and development. In nineteen seventy-eight, lead paint was banned for use in homes. Leaded gasoline was phased out over the next two decades. Since then, the amount of lead in American children's blood has fallen dramatically.""",
   "1970s child painting house", "BANNED IN 1978")

ch("The margarine")
sc("""In the refrigerator, there was margarine. In the sixties, doctors and advertisers told Americans that butter was bad for the heart, and margarine was the healthy choice. Families switched by the millions. Crisco shortening replaced lard in pie crusts. Margarine went on toast, in cookies, and on every ear of corn.""",
   "1960s margarine butter refrigerator", "MARGARINE")
sc("""But much of that margarine and shortening was made with partially hydrogenated oils, full of what we now call trans fats. Decades later, scientists found that trans fats were actually worse for the heart than butter. In twenty fifteen, the government ordered them removed from the food supply. Grandma's butter, it turned out, wasn't the villain.""",
   "butter dish kitchen table", "TRANS FATS")

ch("The pans")
sc("""On the stove were the new pans. In the sixties, Teflon nonstick cookware became a sensation. Eggs slid right off. No scrubbing. Teflon was made by DuPont, and it seemed like a miracle of modern chemistry. Many women put away their heavy old cast iron skillets and bought a shiny new set.""",
   "1960s frying pan eggs stove", "TEFLON")
sc("""Years later, scientists raised concerns about a chemical called PFOA, which was used in making Teflon. It was found in water supplies near factories and in people's blood. By twenty fifteen, American companies had stopped using it. And many cooks went right back to the cast iron skillet their grandmothers had used all along.""",
   "cast iron skillet stove", "BACK TO CAST IRON")

ch("The MSG scare")
sc("""And here's a scare that went the other way. In the sixties, many kitchens had a shaker of Accent, a flavor enhancer made of monosodium glutamate, or MSG. Mothers sprinkled it on meat, soups and vegetables. Then, in nineteen sixty-eight, a doctor wrote a letter to a medical journal describing symptoms he felt after eating at Chinese restaurants.""",
   "1960s spice shaker kitchen seasoning", "ACCENT")
sc("""The idea spread quickly, and for decades many Americans believed that MSG was dangerous. Restaurants put up signs saying No MSG. But careful studies over many years have mostly failed to find any real harm for most people, and the FDA considers it safe. Glutamate occurs naturally in tomatoes, cheese and mushrooms. Your mother's shaker of Accent was probably fine all along.""",
   "1970s Chinese restaurant American family", "PROBABLY FINE ALL ALONG")

ch("The dishes")
sc("""In the cabinet, there were the good dishes. Many families had Fiesta ware, the brightly colored dinnerware made by the Homer Laughlin China Company in West Virginia. Red, yellow, turquoise, green and cobalt blue. It's still collected today. But the original red-orange glaze contained uranium oxide, which made it mildly radioactive.""",
   "Fiesta ware colorful dishes", "FIESTA WARE")
sc("""For decades, families ate off those plates without knowing. Some Geiger counters still click near them today. Experts say the risk from occasional use is small, but collectors are advised not to eat from the old red pieces. Some older china and pottery also used lead in their glazes, which could leach into acidic foods like tomato sauce and orange juice.""",
   "vintage dinner plates cabinet", "A LITTLE RADIOACTIVE")

ch("The refrigerator door")
sc("""Even the refrigerator had a hidden danger. In the forties and fifties, refrigerators closed with a heavy latch that could only be opened from the outside. When old refrigerators were thrown out in alleys, dumps and backyards, children climbed inside to play hide-and-seek, and couldn't get out. Tragically, many children died this way.""",
   "1950s old refrigerator", "THE LATCH")
sc("""In nineteen fifty-six, Congress passed the Refrigerator Safety Act. It required that new refrigerators could be opened from the inside. That's why refrigerator doors today close with magnets. And for years afterward, parents and teachers warned children never, ever to play in an old refrigerator.""",
   "1960s refrigerator magnetic door kitchen", "MAGNETIC DOORS")

ch("The cigarettes")
sc("""And in many sixties kitchens, there was an ashtray on the table. Roughly four in ten adults smoked. Mothers smoked while cooking, fathers smoked after dinner, and guests smoked over coffee. Children grew up breathing it every day. Pregnant women were often told that a few cigarettes were fine, even relaxing.""",
   "1960s woman smoking kitchen table coffee", "THE ASHTRAY ON THE TABLE")
sc("""In nineteen sixty-four, the Surgeon General's report linked smoking to lung cancer. Warning labels appeared on packs in nineteen sixty-six. Cigarette ads were banned from television in nineteen seventy-one. Over the next decades, millions of parents quit, often because their children begged them to.""",
   "1960s cigarette pack warning", "1964: THE WARNING")

ch("What she got right")
sc("""But here's the other side of the story. A lot of what your mother did in that kitchen turned out to be exactly right. She cooked from scratch. She used fresh vegetables from the garden or the market. She made soup from leftovers, and wasted almost nothing. Today, nutrition experts tell us to do exactly that.""",
   "1960s mother cooking vegetables kitchen", "FROM SCRATCH")
sc("""She served smaller portions. A sixties dinner plate was about nine or ten inches wide. Today, many dinner plates are eleven or twelve inches. A soft drink came in a little six-and-a-half-ounce glass bottle. A candy bar was smaller. Families ate snacks less often, and dessert was a treat, not a habit.""",
   "1960s family dinner plate small portions", "SMALLER PLATES")
sc("""She also canned and preserved. Tomatoes, green beans, jams and pickles, put up in glass jars every summer. It was a lot of work, but she knew exactly what was in every jar. Today, home canning has come back into fashion, and many young families are rediscovering the skills that their grandmothers took for granted.""",
   "1960s woman canning jars kitchen", "SHE KNEW WHAT WAS IN EVERY JAR")
sc("""She used cast iron and glass. Pyrex baking dishes and Corning Ware, which went from the freezer to the oven to the table. Those dishes last for generations, and many families still use their mothers' casserole dishes today. Some of those patterns, like Spring Blossom and Butterprint, are now treasured collectibles.""",
   "1960s Corning Ware Pyrex casserole dish", "PYREX AND CORNING WARE")
sc("""And she didn't waste anything. Bacon grease was saved in a can by the stove for frying. Stale bread became bread pudding or stuffing. Chicken bones became broth. Old clothes became dish rags. The idea that you should reduce, reuse and recycle was something she practiced every day, long before anyone made a slogan out of it.""",
   "1960s kitchen stove grease can", "SHE WASTED NOTHING")
sc("""And she sat the whole family down at the table, every night. Researchers today have found that children who eat regular family dinners tend to do better in school, eat healthier, and have fewer problems as teenagers. Your mother didn't need a study to tell her that. She just knew.""",
   "1960s family eating dinner together", "SHE JUST KNEW")

ch("The lesson")
sc("""So what's the lesson of the sixties kitchen? It's not that our mothers were foolish. They trusted the experts, the scientists, the doctors and the companies, just like most people do today. Some of what the experts said turned out to be wrong. And some of what grandma did turned out to be right.""",
   "1960s mother daughter kitchen baking", "THEY TRUSTED THE EXPERTS")
sc("""Maybe in fifty years, people will look back at our kitchens and wonder what we were thinking. The things we trust today might be the stories our grandchildren tell. That's the way it always goes.""",
   "1960s kitchen interior window", "IN FIFTY YEARS")
sc("""But whatever was in those cupboards, what most of us remember about our mothers' kitchens isn't the chemicals. It's the smell of pot roast on Sunday. The sound of the mixer. Licking the beaters. And the feeling of being at home, with someone who loved you, making dinner.""",
   "1960s mother child licking spoon baking", "LICKING THE BEATERS")
sc("""So tell us in the comments. What was in your mother's kitchen that would never be allowed today? And what did she do that you still do now? We read every comment. Next time, we're going to the suburbs of nineteen fifty-eight, and finding out why everyone left the city. Thank you for spending this time with me.""",
   "1960s kitchen family evening", "WHAT WAS IN HER KITCHEN?")

save("video30", "The Truth About the 1960s Kitchen Your Mother Trusted", [
    "Rachel Carson, Silent Spring (1962); EPA ban on most DDT uses, 1972: U.S. Environmental Protection Agency",
    "FDA ban on cyclamates, October 1969: U.S. Food and Drug Administration",
    "FDA ban on FD&C Red No. 2, 1976; red M&M's removed 1976 and returned 1987: FDA; Mars, Incorporated",
    "FDA determination that partially hydrogenated oils are not 'generally recognized as safe', 2015: FDA",
    "PFOA phase-out by U.S. manufacturers by 2015 (EPA PFOA Stewardship Program): EPA",
    "Fiesta red glaze contained uranium oxide (1936-1943 and 1959-1972): Oak Ridge Associated Universities; Homer Laughlin China Company",
    "Phosphate detergent limits in the early 1970s and Lake Erie recovery: EPA Great Lakes program",
    "Lead-based paint banned for residential use in 1978: U.S. Consumer Product Safety Commission; CDC",
    "MSG 'Chinese restaurant syndrome' letter (New England Journal of Medicine, 1968) and FDA safety status: FDA",
    "Refrigerator Safety Act of 1956: U.S. Consumer Product Safety Commission",
    "Surgeon General's report (1964); cigarette warning labels (1966); broadcast cigarette ad ban (1971): CDC",
    "Growth in dinner plate size: Koert van Ittersum and Brian Wansink, Journal of Consumer Research (2012)",
    "Family meals and adolescent outcomes: National Center on Addiction and Substance Abuse at Columbia University",
], "angle 3 · an everyday theme", minutes=(12, 14.5))
