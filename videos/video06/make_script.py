import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 06 · angle 3 (an everyday theme, as an investigation that follows one paycheck) · evening slot · day 2
# What a Paycheck Really Looked Like in 1962 America

sc("""It's Friday afternoon in nineteen sixty-two. Your husband comes through the front door, hangs his hat on the hook, and puts an envelope on the kitchen table. Or maybe it's your own envelope, from the bank or the store where you work. Either way, everybody in the house knows what Friday means. Payday.""",
   "1960s man coming home family", "FRIDAY, 1962")
sc("""Tonight we're going to follow that one paycheck. Where it came from, how big it was, and exactly where every dollar went. The rent or the mortgage. The groceries. The car. The doctor. The church plate. And the little bit left over at the end, if there was any.""",
   "1960s family kitchen table money", "FOLLOW ONE PAYCHECK")
sc("""Because the numbers from nineteen sixty-two tell a story that might surprise you. Some things cost almost nothing. Some things cost a great deal more than you'd think. And one paycheck, for a lot of American families, was enough to carry the whole household. Let's open the envelope.""",
   "1960s pay envelope money", "OPEN THE ENVELOPE")

ch("How much was in the envelope")
sc("""In nineteen sixty-two, the median family income in America was a little under six thousand dollars a year. That works out to roughly one hundred and fifteen dollars a week, before taxes. In most of those families, it was mostly one paycheck, earned by the father, while the mother ran the house.""",
   "1960s father working office", "ABOUT $115 A WEEK")
sc("""A factory worker with a union job might take home around two and a half dollars an hour. A schoolteacher earned around five thousand dollars a year. A young woman in an office might earn sixty or seventy dollars a week. And the federal minimum wage, for the jobs at the bottom, was one dollar and fifteen cents an hour.""",
   "1960s factory workers assembly", "$1.15 AN HOUR MINIMUM")
sc("""Taxes came out first. Federal income tax, and Social Security, which in nineteen sixty-two took three and one-eighth percent of your pay, up to a limit. Many states took a bit more. What was left went home in the envelope, or more and more often now, as a paper check you took to the bank on Saturday morning.""",
   "1960s bank customers teller", "WHAT CAME OUT FIRST")
sc("""At the bank, you stood in line with your passbook. The teller wrote your deposit in by hand, stamped it, and slid it back across the marble counter. Some of the money went into checking, for the bills. And if you were careful, a few dollars went into savings, where it earned a little interest every quarter.""",
   "1960s bank teller passbook", "THE PASSBOOK")
sc("""For the man of the house, the paycheck said something about who he was. Bringing home enough to support a wife and children on one income was a point of pride in nineteen sixty-two. Men compared notes quietly at the barber shop and the bowling alley, and a raise of five dollars a week was news worth sharing at the dinner table.""",
   "1960s barber shop men talking", "A POINT OF PRIDE")

ch("The roof over your head")
sc("""The biggest bill was the house. In the early sixties, the typical new house sold for around eighteen thousand dollars. With a thirty-year mortgage, often backed by the government for veterans, the monthly payment might be around one hundred dollars, including taxes and insurance.""",
   "1960s suburban house new", "ABOUT $18,000 FOR A HOUSE")
sc("""That meant about a quarter of the paycheck went to the house. The rule of thumb, which every banker repeated, was that a family should never spend more than one week's pay out of every month on housing. In nineteen sixty-two, most families could actually follow it.""",
   "1960s family in front of house", "ONE WEEK'S PAY")
sc("""Renters in the city might pay seventy or eighty dollars a month for an apartment. The landlord often lived in the same building, collected the rent in person on the first of the month, and wrote you a receipt in a little book. Heat and hot water were usually included.""",
   "1960s city apartment building", "RENT DAY")
sc("""Then there were the utilities. The electric bill, the gas bill, the water bill and the telephone, which was rented from the telephone company, not owned. Together, they might run around twenty or twenty-five dollars a month. Long-distance calls were the dangerous part, and every family had a rule about them.""",
   "1960s woman telephone home", "THE TELEPHONE BILL")
sc("""Heating the house was its own expense. Many homes still burned fuel oil, delivered by a truck that filled a tank in the basement. Some older houses still had coal furnaces. And in winter, the rule in a great many homes was simple. If you're cold, put on a sweater, and don't touch that thermostat.""",
   "1960s home furnace basement", "PUT ON A SWEATER")

ch("Feeding the family")
sc("""Next came the groceries. A family of four might spend around twenty to twenty-five dollars a week at the supermarket. That was nearly a fifth of the paycheck, a much bigger share than families spend today. Food was the second biggest bill in almost every house.""",
   "1960s supermarket shopping cart", "ABOUT $25 A WEEK")
sc("""Here's what that money bought. A loaf of white bread for around twenty cents. A dozen eggs for around thirty cents. A pound of ground beef for around fifty cents. A half-gallon of milk delivered to your door, or bought at the store, for around fifty cents. Coffee came in a can, and nobody had heard of spending a dollar on a single cup.""",
   "1960s grocery store shelves prices", "BREAD FOR 20 CENTS")
sc("""Mothers stretched every dollar. They clipped coupons from the newspaper. They saved trading stamps from the supermarket, licked them into little books, and traded the books for a toaster or a lamp. They bought a whole chicken and made it last three nights. Nothing was ever thrown away.""",
   "1960s housewife cooking kitchen", "STRETCHING EVERY DOLLAR")
sc("""A lot of families also grew part of their own food. A vegetable garden behind the house, tomatoes and beans and squash in the summer, and jars of canned peaches and pickles lined up on basement shelves for the winter. In small towns, some families still kept chickens in the backyard for eggs.""",
   "1960s family vegetable garden backyard", "THE BACKYARD GARDEN")
sc("""The milkman still came to many neighborhoods two or three times a week, leaving glass bottles on the front step in a little metal box. The bread man came too, in some towns, and the egg man from the farm outside town. You paid them weekly, in cash, or they kept a running tab in a little notebook.""",
   "1960s milkman delivery doorstep", "THE MILKMAN'S NOTEBOOK")
sc("""A dinner out was a real treat. A family might go to a diner or a cafeteria once a month, where a hamburger cost around thirty or forty cents. And the new fast-food stands along the highway, with their golden signs, sold a hamburger for fifteen cents, which seemed almost too good to be true.""",
   "1960s family diner restaurant", "DINNER OUT")

ch("The car in the driveway")
sc("""After the house and the food came the car. A brand-new Chevrolet or Ford cost somewhere around two thousand five hundred dollars. Most families bought it on time, with a loan, and paid around sixty or seventy dollars a month for three years. A lot of families bought a good used car instead.""",
   "1960s new car showroom family", "ABOUT $2,500 FOR A NEW CAR")
sc("""Gasoline cost around thirty cents a gallon, and the man at the station pumped it for you. A family car might get twelve or fifteen miles per gallon, and nobody worried much about it. A Sunday drive to see the grandparents might cost a dollar in gas, there and back.""",
   "1960s gas station attendant car", "30 CENTS A GALLON")
sc("""The car was expensive to keep up, though. Tires wore out quickly. The oil was changed every thousand miles. And every few years, the family car needed a new muffler, a new battery, or a whole new transmission, which could eat a month's savings in one afternoon.""",
   "1960s mechanic garage car repair", "THE REPAIR BILL")
sc("""Car insurance was cheaper than today but still a real bill, and many families paid it twice a year. Most people didn't carry much coverage. And plenty of fathers did their own repairs on Saturday mornings, with the hood up in the driveway and a son handing him the wrenches one at a time.""",
   "1960s father son fixing car driveway", "SATURDAY IN THE DRIVEWAY")

ch("Everything else")
sc("""Then came all the smaller things. Clothing, much of it sewn at home or handed down from older brothers and sisters. A visit to the doctor, which might cost five dollars, paid in cash at the front desk. The family dentist. Haircuts. Shoes resoled at the cobbler instead of thrown away.""",
   "1960s mother sewing machine home", "SEWN AT HOME")
sc("""A first-class stamp cost four cents, until it went up to five cents in January of nineteen sixty-three. The newspaper cost a dime. A movie ticket cost well under a dollar. And a family could spend a whole Saturday at the county fair for a few dollars, including the cotton candy.""",
   "1960s family county fair", "A FOUR-CENT STAMP")
sc("""There was the collection plate on Sunday, which many families took seriously, and often a weekly envelope with the family's name on it. There were the insurance payments, to a man who sometimes came right to the door to collect them. And there was the Christmas club at the bank, a dollar or two a week saved all year for presents in December.""",
   "1960s church congregation family", "THE CHRISTMAS CLUB")
sc("""And there was credit, though not as much as today. Department stores gave charge accounts to good customers. A few people carried a new kind of card from a company called Diners Club. But most families still paid cash, and if they couldn't afford something, they waited until they could.""",
   "1960s department store shoppers", "PAY CASH OR WAIT")
sc("""Some families bought big things on the installment plan. A new refrigerator, a washing machine, or a console television might be paid off at a few dollars a month for two years. A payment book came with it, a little booklet of coupons, one torn out and mailed in with a check every month until the last one was gone.""",
   "1960s appliance store refrigerator", "THE PAYMENT BOOK")
sc("""And what about vacations? For many families, the summer vacation was a week at a lake cabin, a trip to see relatives, or a long drive to a national park, with the whole family packed into the station wagon. Motels cost around eight or ten dollars a night. Mother packed sandwiches so nobody had to pay for lunch on the road.""",
   "1960s family station wagon vacation", "THE SUMMER VACATION")

ch("The envelope system")
sc("""So how did families keep it all straight? In a lot of houses, the answer was the envelope system. On payday, the mother sat at the kitchen table and divided the cash into envelopes. One for the house. One for groceries. One for the car. One for church. One for the doctor. One for savings, if there was anything left.""",
   "1960s woman kitchen table bills", "THE ENVELOPE SYSTEM")
sc("""When the grocery envelope was empty, the grocery shopping was done until next Friday. That was the whole budget, right there in a shoebox or a kitchen drawer. No spreadsheets. No apps. Just a pencil, a stack of envelopes, and a woman who knew exactly where every dollar went.""",
   "1960s housewife budget notebook", "WHEN IT'S GONE, IT'S GONE")
sc("""Many fathers handed the whole envelope to their wives and received a small allowance back, for lunch, gas and the barber. It sounds strange now. But in nineteen sixty-two, in a great many American homes, the person who actually managed the money was the mother.""",
   "1960s husband wife kitchen", "MOTHER KEPT THE BOOKS")

ch("Who had it better?")
sc("""Was it easier back then? In some ways, yes. One paycheck could buy a house, a car, and three meals a day for a family of four or five. Housing took about a quarter of the pay. A young couple with a high school education could often afford a home of their own before thirty.""",
   "1960s young family new home", "ONE PAYCHECK WAS ENOUGH")
sc("""In other ways, no. Families had far less. One car. One television. One bathroom, for six people. Clothes were mended until they fell apart. A long-distance call was an event. And many Americans, especially in the rural South, in the cities and in minority neighborhoods, never got anywhere near that median paycheck at all.""",
   "1960s family small house porch", "BUT THEY HAD LESS")
sc("""What's certain is this. People knew the value of a dollar, because they could see it, hold it, and count it out on the kitchen table every Friday. That habit stayed with that generation for the rest of their lives. If your parents or grandparents saved string and rubber bands, now you know why.""",
   "1960s grandparents home portrait", "THE VALUE OF A DOLLAR")
sc("""So tell us in the comments. What did your father or mother earn in the sixties, and what did your family's house cost? We read every one. And stay with us for more. Next time, we'll take you to the main streets of small-town America, in full color. Thank you for spending this time with me.""",
   "1960s small town main street evening", "WHAT DID YOUR HOUSE COST?")

save("video06", "What a Paycheck Really Looked Like in 1962 America", [
    "Median family income 1962 (about $5,956): U.S. Census Bureau, Current Population Reports P60",
    "Federal minimum wage $1.15/hour (Sept 1961 - Sept 1963): U.S. Department of Labor",
    "Social Security (OASDI) employee tax rate 3.125% in 1962: Social Security Administration, tax rate history",
    "Median sales price of new houses, about $18,000 in 1963: U.S. Census Bureau, New Residential Sales",
    "Average retail food prices (bread, eggs, ground beef, milk) early 1960s: Bureau of Labor Statistics, Average Price Data",
    "First-class postage 4 cents, raised to 5 cents January 7, 1963: U.S. Postal Service, rates history",
    "Average gasoline price about 30-31 cents per gallon in 1962: U.S. Energy Information Administration",
], "angle 3 · an everyday theme", minutes=(12, 14.5))
