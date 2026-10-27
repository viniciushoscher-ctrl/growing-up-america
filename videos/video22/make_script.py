import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 22 · angle 1 (a place and a time, one hard day from dawn to night) · morning slot · day 8
# The 1950s Were Harder Than You Remember

sc("""We remember the nineteen fifties as an easy time. And in some ways, it was. But ask the people who actually ran a household back then, and they'll tell you something different. Daily life in the fifties took a lot of hard, physical work. Things we don't even think about today took hours, sweat and patience.""",
   "1950s housewife working kitchen", "HARDER THAN YOU REMEMBER")
sc("""This isn't a sad story. It's a story about how tough and resourceful ordinary people were. The things they did every day, without complaining, would wear most of us out by lunchtime. So let's follow one ordinary family through one ordinary day in nineteen fifty-three, from before sunrise until bedtime.""",
   "1950s family house morning", "ONE ORDINARY DAY")
sc("""As we go, you might start to remember a few things your own parents and grandparents did, that you'd almost forgotten. And you might appreciate them a little more.""",
   "1950s family portrait parents children", "REMEMBER THEM")

ch("5 a.m.: the cold house")
sc("""The day starts early, and in winter, it starts cold. In nineteen fifty, about a third of American homes were still heated with coal. Before anyone else woke up, Dad went down to the basement to shake down the ashes in the furnace and shovel in fresh coal. Until the fire caught, you could see your breath in the bedroom.""",
   "1950s man shoveling coal furnace basement", "SHOVELING COAL")
sc("""Coal was delivered by truck, and poured down a chute into a coal bin in the basement. It left a black dust on everything. The ashes had to be carried out in buckets. And in many farmhouses, there was no furnace at all, just a wood stove in the kitchen that somebody had to keep burning all winter.""",
   "1950s coal delivery truck house", "THE COAL CHUTE")
sc("""In the summer, the problem was the opposite. Air conditioning in homes was rare. Even by nineteen sixty, only about one in eight American homes had it. On hot nights, families slept with the windows open, moved mattresses onto the porch, or lay in front of a box fan with a wet washcloth on their foreheads.""",
   "1950s family porch hot summer night", "NO AIR CONDITIONING")

ch("6 a.m.: one bathroom")
sc("""Then came the morning rush, and most houses had just one bathroom. A family of six had to share it. Dad shaved first, because he had to catch the bus. Then the teenagers, who took forever. Then the little ones. Somebody was always pounding on the door, and somebody was always late.""",
   "1950s family bathroom morning", "ONE BATHROOM, SIX PEOPLE")
sc("""Many older houses had no shower, just a bathtub. Hot water came from a small tank that ran out quickly. So baths were often taken once or twice a week, on Saturday night, and sometimes children shared the bathwater, youngest to oldest. In between, people washed at the sink with a washcloth.""",
   "1950s bathtub old bathroom", "SATURDAY NIGHT BATH")
sc("""And remember, in nineteen fifty, more than a third of American homes still lacked complete plumbing. In the countryside, many families still used an outhouse, even in winter. A chamber pot under the bed saved a cold trip outside at night, and somebody had to empty it every morning.""",
   "1950s rural outhouse winter", "THE OUTHOUSE")

ch("7 a.m.: breakfast from scratch")
sc("""Breakfast was made from scratch. Eggs fried in bacon grease saved from yesterday, in a cast iron pan. Toast made under the broiler, or in a toaster that didn't pop up on its own. Coffee boiled in a percolator. Oatmeal stirred on the stove. There were very few shortcuts, and everything had to be washed by hand afterward.""",
   "1950s mother cooking breakfast stove", "FROM SCRATCH")
sc("""Most kitchens had a refrigerator by then, but many had only a tiny freezer compartment, just big enough for two ice cube trays. It frosted up, and every few weeks it had to be defrosted by hand, with pans of hot water and a butter knife to chip away the ice. Some older families still called it the icebox.""",
   "1950s refrigerator kitchen", "DEFROSTING BY HAND")
sc("""Lunches were packed in paper bags or metal lunch boxes. Sandwiches wrapped in wax paper, because plastic wrap was still new and expensive. A thermos of milk or soup. An apple. Every morning, a mother might make five or six lunches before eight o'clock.""",
   "1950s mother packing lunch boxes", "SIX LUNCHES BEFORE EIGHT")

ch("8 a.m.: getting to work")
sc("""Getting to work wasn't easy. Many families still had only one car, or none at all. In nineteen fifty, about four in ten households didn't own a car. Fathers took the bus, the streetcar or the train. Some walked miles. Some rode with a neighbor who worked at the same plant.""",
   "1950s men waiting bus stop", "FOUR IN TEN HAD NO CAR")
sc("""And the cars themselves were less reliable. No power steering in most of them. No power brakes. In winter, they wouldn't start, and men pushed them down the street to get them going. Tires went flat often, and every driver knew how to change one. A car with a hundred thousand miles was considered worn out.""",
   "1950s man changing tire car road", "PUSH IT TO START")
sc("""The work week was long, and much of the work was physical. Steel mills, coal mines, factories, farms and construction sites. In nineteen fifty-three, workplace accidents killed around fifteen thousand Americans a year. Many men came home with injuries that never fully healed.""",
   "1950s factory workers heavy work", "PHYSICAL WORK")

ch("9 a.m.: washday")
sc("""Back at home, Monday was washday, and it took the whole day. Many families still used a wringer washer. You filled the tub with a hose or buckets of hot water, added soap, and let it churn. Then you fed each piece of clothing by hand through two rollers to squeeze out the water. Fingers sometimes got caught.""",
   "1950s woman wringer washing machine", "THE WRINGER WASHER")
sc("""Then everything went outside to dry on the clothesline, held with wooden clothespins. In winter, clothes froze stiff on the line, and came inside like boards. If it rained, everything came in fast and was hung on lines in the basement. Electric dryers existed, but in fifty-three, only a small share of homes had one.""",
   "1950s clothesline backyard laundry", "FROZEN ON THE LINE")
sc("""And Tuesday was ironing day. Nearly everything was cotton or wool, and nearly everything wrinkled. Shirts, dresses, sheets, tablecloths and handkerchiefs. Women sprinkled them with water, rolled them up, and ironed for hours with a heavy iron. Many housewives did more than ten hours of laundry and ironing a week.""",
   "1950s woman ironing kitchen", "IRONING DAY")

ch("Noon: the shopping")
sc("""Shopping took time too. The supermarket was growing, but many women still went to several stores. The butcher for meat, the bakery for bread, the corner grocery for milk and canned goods. Many walked or took the bus, carrying heavy bags home. Food was bought more often, because refrigerators were small.""",
   "1950s woman grocery shopping bags", "SEVERAL STORES")
sc("""And money was tight in many homes. Women kept careful budgets in little notebooks, and some kept cash in envelopes labeled for rent, groceries and the electric bill. Meat was expensive, so cheaper cuts were stretched with bread crumbs, rice and potatoes. Nothing was wasted. Leftovers became soup.""",
   "1950s woman budget kitchen table", "ENVELOPES FOR EVERY BILL")

ch("2 p.m.: the telephone")
sc("""In the afternoon, a mother might need to call the doctor. But many families, especially in the country, were on a party line. That meant several households shared the same telephone line. Each house had its own ring pattern. Two shorts and a long, for example. And anyone could pick up and listen in.""",
   "1950s woman telephone wall kitchen", "THE PARTY LINE")
sc("""Long distance calls were expensive, and families saved them for emergencies and holidays. A call across the country could cost several dollars for a few minutes, at a time when a man might earn two dollars an hour. When the phone rang long distance, everyone in the house came running, because it might be bad news.""",
   "1950s family telephone call", "LONG DISTANCE")

ch("3 p.m.: getting sick")
sc("""Getting sick was more dangerous, especially for children. Measles infected millions of American children every year, and killed several hundred of them. Whooping cough, mumps, chickenpox and scarlet fever went through schools in waves. Houses with a contagious child sometimes had a quarantine sign posted on the front door.""",
   "1950s sick child bed mother", "QUARANTINE SIGNS")
sc("""Antibiotics like penicillin were still fairly new, and they were seen as miracle drugs. But many other medicines we take for granted didn't exist yet. Medical care was simpler, and families relied on home remedies. Mustard plasters, castor oil, Vicks VapoRub and chicken soup.""",
   "1950s doctor black bag house call", "MUSTARD PLASTERS")
sc("""And the dentist was something to be feared. Fluoride in drinking water was just beginning to spread in the fifties. Many adults had lost several teeth by middle age, and plenty had dentures by fifty. Drills were slow and loud, and the dentist didn't always use much novocaine.""",
   "1950s dentist office patient", "THE DENTIST")

ch("5 p.m.: dinner")
sc("""By late afternoon, dinner had to be ready when Dad walked in the door. Everything was cooked on the stove or in the oven. No microwave, no dishwasher, very few frozen meals. A pot roast took three hours. Potatoes had to be peeled by hand. Pies were made with homemade crust.""",
   "1950s mother cooking dinner kitchen", "A THREE-HOUR POT ROAST")
sc("""After dinner came the dishes. In nineteen fifty-three, only a tiny fraction of homes had a dishwasher. So the dishes were washed in the sink, by hand. Kids took turns washing and drying, and argued about whose turn it was. A big family dinner could mean an hour at the sink.""",
   "1950s children washing dishes sink", "WHOSE TURN IS IT?")

ch("7 p.m.: the evening")
sc("""In the evening, many families gathered around the television. But in fifty-three, that television was small, with a round-cornered black and white screen, maybe two or three channels, and a picture that rolled and flickered. Someone had to get up and adjust the rabbit-ear antenna, or climb on the roof to turn the big one.""",
   "1950s family watching small television", "ADJUST THE ANTENNA")
sc("""Television tubes burned out, and you had to take them to the drugstore to test them on a tube-testing machine. Radios did the same. Repairmen made house calls. And many families didn't have a TV at all yet. They listened to the radio, read, sewed, played cards or just sat on the porch.""",
   "1950s drugstore tube tester", "THE TUBE TESTER")
sc("""Mothers often kept working after dinner. Mending socks with a darning egg. Letting out hems as the children grew. Sewing a new dress from a pattern. Making a Halloween costume. Many women sewed most of their family's clothes, and their hands were never still.""",
   "1950s woman sewing machine evening", "NEVER STILL")

ch("10 p.m.: what it took")
sc("""And then, finally, bed. Many children shared a bed with a brother or sister. Houses were small, often under a thousand square feet, with two or three bedrooms for a family of five or six. The quiet of the night was broken by a train whistle, a dog barking, or a baby crying in the next room.""",
   "1950s children sharing bedroom", "SHARING A BED")
sc("""Add it all up, and it was a lot. Studies from the time found that full-time housewives worked around fifty hours a week on housework alone. Men worked long, hard shifts, often with overtime on Saturdays. Children had chores before and after school. Almost nobody had what we would call free time.""",
   "1950s family working together yard", "50 HOURS A WEEK")
sc("""So why do people remember the fifties as easy? Partly because, compared with the Depression and the war that came before, it really was easier. People had steady jobs, enough food and hope for the future. For people who had lived through hunger and fear, a cold house and a wringer washer felt like a good life.""",
   "1950s family smiling living room", "EASIER THAN BEFORE")
sc("""And partly because the hard work brought people together. Families worked side by side. Neighbors helped each other. Children learned to be useful. When people remember the fifties fondly, they're not remembering the coal furnace. They're remembering the people who stood next to them while they did the work.""",
   "1950s neighbors helping each other", "SIDE BY SIDE")
sc("""If your parents or grandparents lived through those years, now you know a little more about what their days were really like. They were tough, and they rarely complained. Next time you push a button and the laundry is done, you might think of them.""",
   "1950s mother father portrait", "THEY RARELY COMPLAINED")
sc("""So tell us in the comments. What was the hardest chore you remember from your childhood? Did your family have a coal furnace, a wringer washer or a party line? We read every comment. Next, we're looking at what it cost to buy your first house in nineteen fifty-six. Thank you for spending this time with me.""",
   "1950s small town house evening", "WHAT WAS YOUR HARDEST CHORE?")

save("video22", "The 1950s Were Harder Than You Remember", [
    "Home heating fuel 1950 (coal about 35% of homes): U.S. Census Bureau, Historical Census of Housing Tables, House Heating Fuel",
    "Homes lacking complete plumbing in 1950 (about 35%): U.S. Census Bureau, Historical Census of Housing Tables",
    "Room air conditioning in about 12% of U.S. homes by 1960: U.S. Census Bureau",
    "About 41% of households had no car in 1950: U.S. Department of Transportation; Census of Housing",
    "Work-related deaths around 15,000 a year in the early 1950s: National Safety Council, Accident Facts",
    "Measles: about 3-4 million infections and 400-500 deaths a year before the 1963 vaccine: CDC",
    "Community water fluoridation began in Grand Rapids, Michigan in 1945: CDC",
    "Housework time studies (about 50 hours a week): Joann Vanek, Scientific American (1974)",
    "Average size of new single-family homes about 1,000 square feet in 1950: National Association of Home Builders",
], "angle 1 · a place and a time", minutes=(12, 14.5))
