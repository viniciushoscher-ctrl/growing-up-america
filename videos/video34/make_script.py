import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 34 · angle 1 (a place and a time, a road trip west, stop by stop) · morning slot · day 12
# Route 66 in 1956: The Great American Road Trip

sc("""It's June of nineteen fifty-six. School just let out. In a driveway on the South Side of Chicago, a father is packing the trunk of a two-tone Chevrolet Bel Air. Suitcases, a cooler, a water bag hanging from the front bumper, and a stack of road maps from the gas station. The kids are already fighting over the window seats. The family is going to California, on Route sixty-six.""",
   "1956 Chevrolet Bel Air family car", "JUNE, 1956")
sc("""Route sixty-six ran almost two thousand four hundred miles, from Chicago to Santa Monica, California. Eight states, three time zones, and some of the most beautiful and empty country in America. John Steinbeck called it the Mother Road. And in the fifties, it was the most famous highway in the world.""",
   "Route 66 highway sign desert", "THE MOTHER ROAD")
sc("""So let's take that trip. Let's ride along with a family in nineteen fifty-six, from the shores of Lake Michigan to the Pacific Ocean. The diners, the motels, the gas stations and the roadside wonders. If you ever took that road, I think you'll feel the hot wind through the window.""",
   "1950s family car road trip highway", "LET'S RIDE ALONG")

ch("The road")
sc("""Route sixty-six was created in nineteen twenty-six, as one of the first federal highways. At first, much of it was gravel and dirt. It wasn't fully paved until nineteen thirty-eight. During the Dust Bowl of the thirties, hundreds of thousands of desperate families from Oklahoma, Texas and Arkansas took it west to California, looking for work.""",
   "1930s Dust Bowl family car migrants", "BUILT IN 1926")
sc("""After the Second World War, Route sixty-six became something new. Not a road of desperation, but a road of adventure. Americans had cars, money and paid vacations for the first time. And the West, with its deserts, canyons and movie stars, was calling. Families took to the road by the millions.""",
   "1950s family car vacation road west", "A ROAD OF ADVENTURE")
sc("""In nineteen forty-six, a songwriter named Bobby Troup wrote a song about the trip. Nat King Cole recorded it, and it became a hit. Get your kicks on Route sixty-six. Everyone knew the words. The song named the towns along the way, and for millions of kids in the back seat, it became a map they could sing.""",
   "1940s jukebox records", "GET YOUR KICKS")
sc("""Planning the trip was half the fun. Weeks before, Dad sent away for free maps and travel guides, or stopped at the auto club office for a TripTik, a little flip-book of maps with the route marked in highlighter. Mom packed sandwiches, a thermos and a coffee can of cookies. And the kids made lists of everything they wanted to see.""",
   "1950s family planning trip map kitchen table", "THE TRIPTIK")

ch("Illinois and Missouri")
sc("""The trip started in Chicago, near the lakefront. The first day took the family south across Illinois, past cornfields, small towns and grain elevators. They stopped at a diner for lunch, maybe a pork tenderloin sandwich bigger than the bun. And the kids started counting license plates from other states.""",
   "1950s Illinois highway cornfields", "ILLINOIS")
sc("""By evening, they crossed the Mississippi River into St. Louis, on the Chain of Rocks Bridge, which had a strange twenty-two degree bend in the middle. Then on into the green hills of the Missouri Ozarks. Along the road, there were billboards for caves, souvenir shops and reptile farms, every few miles.""",
   "Chain of Rocks Bridge Mississippi River", "THE CHAIN OF ROCKS BRIDGE")
sc("""Meramec Caverns in Missouri advertised on barn roofs all along the highway. The owner, Lester Dill, paid farmers to let him paint their barns. He also claimed that the outlaw Jesse James had once hidden in the cave. Families stopped to take the tour, and drove away with a bumper sticker, which Dill is often credited with inventing.""",
   "Meramec Caverns barn advertisement", "MERAMEC CAVERNS")
sc("""Life in the back seat had its own rules. No seat belts, so kids sprawled across the seat, or lay on the floor, or on the shelf under the back window. They played I spy, twenty questions and the alphabet game, finding each letter on signs along the road. They read comic books until they got carsick. And every few miles, someone asked how much longer.""",
   "1950s children back seat car trip", "THE BACK SEAT")

ch("The motels")
sc("""At night, the family looked for a motel. In nineteen fifty-six, there were thousands of small, family-run motels along Route sixty-six. A neon sign out front, with a flashing arrow and the word Vacancy. Little cabins or rooms in a row, with a parking spot right in front of each door. A room might cost five or six dollars a night.""",
   "1950s motel neon sign vacancy", "VACANCY")
sc("""Many motels had themes to catch a driver's eye. The Wigwam Motels in Arizona and California, where guests slept in concrete teepees. The Blue Swallow in Tucumcari, New Mexico. The Munger Moss in Lebanon, Missouri. A motel with a swimming pool was every kid's dream. After a day in a hot car, nothing was better.""",
   "Wigwam Motel Route 66", "THE WIGWAM MOTEL")
sc("""And motels were changing. In nineteen fifty-two, a man named Kemmons Wilson opened the first Holiday Inn in Memphis, Tennessee, after a frustrating family vacation. He promised clean rooms, a pool, air conditioning and free stays for children. Within a few years, Holiday Inns were popping up everywhere, and the little mom-and-pop motels began to feel the pressure.""",
   "1950s Holiday Inn sign", "HOLIDAY INN")

ch("Oklahoma and Texas")
sc("""On the third day, the family crossed into Oklahoma. More of Route sixty-six ran through Oklahoma than any other state. They passed through Tulsa and Oklahoma City, and small towns with names like Chandler, Stroud and Clinton. The land got flatter, the sky got bigger, and the towns got farther apart.""",
   "1950s Oklahoma highway small town", "OKLAHOMA")
sc("""In the Texas Panhandle, the road ran straight as a ruler for miles. The town of Amarillo was famous for its steak houses. Not far from the highway, a restaurant called the Big Texan would later offer a free seventy-two ounce steak, if you could eat it in an hour. Kids stared at the cowboy hats and the oil wells.""",
   "1950s Texas Panhandle highway flat", "THE TEXAS PANHANDLE")
sc("""Halfway across Texas, at Adrian, a sign marked the exact midpoint of Route sixty-six. Eleven hundred and thirty-nine miles to Chicago, and the same to Los Angeles. Families stopped to take a picture with the Brownie camera, and Mom wrote a postcard to Grandma.""",
   "Route 66 midpoint sign Adrian Texas", "THE MIDPOINT")
sc("""And along the way, there were the diners and cafés. Places like the Midpoint Café, the U-Drop Inn in Shamrock, Texas, with its art deco tower, and countless little truck stops. Truckers knew where the best food was, so families looked for a parking lot full of big rigs. Chicken fried steak, biscuits and gravy, and a slice of homemade pie.""",
   "U-Drop Inn Shamrock Texas", "FOLLOW THE TRUCKERS")

ch("The gas stations")
sc("""Gas stops were frequent, because the big cars of the fifties got only about fifteen miles to the gallon. Gas cost around twenty-three cents a gallon in nineteen fifty-six. An attendant in a uniform and cap ran out to the car, pumped the gas, washed the windshield, checked the oil and the tires, and gave the kids a free road map.""",
   "1950s gas station attendant pumping gas", "23 CENTS A GALLON")
sc("""Every gas company competed for drivers. Phillips sixty-six, Texaco, Conoco, Sinclair with its green dinosaur, and Mobil with its flying red horse. Many gave away free gifts. Glasses, dishes, maps, and later, trading stamps. A clean restroom was a big selling point, and Texaco advertised its registered restrooms.""",
   "1950s Phillips 66 gas station Route 66", "PHILLIPS 66")
sc("""In the desert, gas stations were few and far between. Signs warned, last gas for sixty miles. Cars overheated in the summer heat, so many drivers hung a canvas water bag on the front bumper. As the water seeped through the canvas and evaporated, it stayed cool, and could be poured into the radiator.""",
   "1950s car desert road water bag", "LAST GAS FOR 60 MILES")
sc("""And then there were the Burma-Shave signs. A series of small red signs, spaced along the roadside, each with a few words of a rhyme. You read them one by one as you drove past. Don't lose your head, to gain a minute, you need your head, your brains are in it. Burma-Shave. Kids waited eagerly for the next set, and read them out loud.""",
   "Burma-Shave roadside signs", "BURMA-SHAVE")

ch("New Mexico and Arizona")
sc("""In New Mexico, the landscape changed completely. Red mesas, dry riverbeds, and pueblos that had stood for centuries. Trading posts sold Navajo rugs, turquoise jewelry and Indian pottery. Albuquerque's Central Avenue glowed with neon at night, motel after motel. For a kid from Chicago, it felt like another planet.""",
   "New Mexico mesa desert landscape", "NEW MEXICO")
sc("""In Arizona, the family might take a side trip to the Grand Canyon. They stood at the rim, speechless. They drove through the Petrified Forest and the Painted Desert. And in Holbrook, they slept in a teepee at the Wigwam Motel, and bought rubber tomahawks and moccasins at the souvenir shop.""",
   "Grand Canyon 1950s tourists rim", "THE GRAND CANYON")
sc("""Then came the scariest part of the drive. The Sitgreaves Pass, near Oatman, Arizona, a steep, twisting mountain road with hairpin turns and no guardrails. Some nervous drivers hired local men to drive their cars over the pass for them. Wild burros wandered the road in Oatman, and they still do today.""",
   "Oatman Arizona burros street", "OATMAN")

ch("The desert and California")
sc("""Next came the Mojave Desert, the hottest and loneliest part of the trip. In summer, temperatures could reach a hundred and fifteen degrees. Most cars had no air conditioning, so families drove at night, with the windows down. Some hung wet towels in the windows. The kids slept in the back seat, sweaty and exhausted.""",
   "Mojave Desert highway 1950s", "THE MOJAVE")
sc("""At last, the road climbed over the Cajon Pass and dropped into the green valleys of Southern California. Orange groves stretched for miles. Palm trees lined the streets. The family passed through San Bernardino, where, as it happened, a pair of brothers named McDonald had a little hamburger stand that would one day change the world.""",
   "1950s California orange groves", "ORANGE GROVES")
sc("""And finally, after six or seven days, they reached Santa Monica, and the end of the road at the Pacific Ocean. The kids ran into the cold water, screaming. Dad stood on the beach and looked out at the ocean, a little amazed that they'd made it. Maybe they went to Disneyland, which had opened the summer before, in nineteen fifty-five.""",
   "Santa Monica pier 1950s beach", "THE PACIFIC")
sc("""The trip home was just as long, and the family was tired, sunburned and happy. They had a shoebox full of postcards, a rubber tomahawk, a jar of desert sand and a hundred stories. Back at school in September, the kids told their classmates about the Grand Canyon and the teepee motel. It was the summer they'd never forget.""",
   "1950s family returning home car luggage", "THE TRIP HOME")

ch("The end of the road")
sc("""But the end was already coming. In nineteen fifty-six, the same year as our trip, President Eisenhower signed the act creating the interstate highway system. Over the next twenty-five years, five different interstates replaced Route sixty-six, piece by piece. The new highways were faster and safer. And they went around the little towns.""",
   "1950s interstate highway construction", "THE INTERSTATE")
sc("""When the interstate bypassed a town, the traffic simply disappeared. Diners, motels and gas stations that had been busy for thirty years went quiet almost overnight. Many closed. Some towns nearly died. In nineteen eighty-four, the last piece of Route sixty-six was bypassed, at Williams, Arizona. In nineteen eighty-five, the road was officially removed from the federal highway system.""",
   "abandoned motel desert highway", "1985: DECOMMISSIONED")
sc("""But people didn't forget it. In the nineties, fans began working to save what was left. Old motels were restored. Neon signs were relit. Historic Route sixty-six signs went up. Today, travelers from all over the world, especially from Europe and Japan, come to drive the old road, looking for the America of nineteen fifty-six.""",
   "Route 66 restored neon motel sign", "THE ROAD LIVES ON")

ch("Why we remember")
sc("""Route sixty-six was more than a highway. It was the great American adventure. The open road, the wide sky, a family together in the car, and a new place around every bend. For a generation of families, that trip west was the vacation of a lifetime.""",
   "1950s family standing by car scenic view", "THE GREAT AMERICAN ADVENTURE")
sc("""If you ever made that trip as a kid, you remember it. The heat. The neon. The teepee motel. The pie at the diner. The first sight of the Pacific. And your father, both hands on the wheel, singing along to the radio. Get your kicks on Route sixty-six.""",
   "1950s father driving car family", "BOTH HANDS ON THE WHEEL")
sc("""So tell us in the comments. Did you ever travel on Route sixty-six? Where did you go, and what do you remember most? And what was the best family road trip of your childhood? We read every comment. Next time, we're looking at what it meant to turn sixteen in nineteen sixty. Thank you for spending this time with me.""",
   "Route 66 sunset desert highway", "DID YOU DRIVE ROUTE 66?")

save("video34", "Route 66 in 1956: The Great American Road Trip", [
    "Route 66 established 1926, about 2,448 miles from Chicago to Santa Monica, fully paved 1938, decommissioned 1985: National Park Service, Route 66 Corridor Preservation Program",
    "John Steinbeck, The Grapes of Wrath (1939), 'the mother road'",
    "'(Get Your Kicks on) Route 66' by Bobby Troup (1946), recorded by the Nat King Cole Trio: Library of Congress",
    "Chain of Rocks Bridge (1929) and its 22-degree bend: Missouri Department of Transportation",
    "Meramec Caverns barn advertising and Lester Dill: Missouri State Historic Preservation Office",
    "First Holiday Inn, Memphis, 1952, Kemmons Wilson: InterContinental Hotels Group history",
    "Route 66 midpoint at Adrian, Texas: Texas Historical Commission",
    "Average U.S. gasoline price about 23 cents a gallon in 1956 (before taxes about 22-23 cents): U.S. Energy Information Administration",
    "Federal-Aid Highway Act of 1956; last segment bypassed at Williams, Arizona, 1984: Federal Highway Administration",
    "Disneyland opened July 17, 1955: The Walt Disney Company",
], "angle 1 · a place and a time", minutes=(12, 14.5))
