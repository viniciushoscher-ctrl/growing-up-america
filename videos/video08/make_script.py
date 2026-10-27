import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 08 · angle 2 (a stage of life: turning 30, as a side-by-side comparison) · afternoon slot · day 3
# 1962 vs 2026: Who Actually Had It Better at 30?

sc("""Imagine two people. Both of them are turning thirty. One turns thirty in nineteen sixty-two. The other turns thirty this year, in twenty twenty-six. They're the same age, maybe even from the same town. But they are living in two completely different Americas.""",
   "1960s young couple portrait", "TWO PEOPLE, BOTH THIRTY")
sc("""The one in nineteen sixty-two was born in nineteen thirty-two, in the depths of the Great Depression. As a child, he heard about the war on the radio. As a young man, he may have served in Korea. And by thirty, he is already a husband, a father and a homeowner.""",
   "1960s young father family home", "BORN IN 1932")
sc("""So let's put them side by side. Home. Work. Money. Marriage. Children. Health. And the things that don't show up in any statistic at all. And then let's try to answer an honest question. Who actually had it better at thirty?""",
   "1960s family suburban house lawn", "WHO HAD IT BETTER?")
sc("""And the thirty-year-old of twenty twenty-six? Born in nineteen ninety-six. A child when the twin towers fell. A teenager in the middle of the great recession. Starting a career just as a pandemic shut the world down. Two very different childhoods, leading to two very different thirtieth birthdays.""",
   "1960s birthday party cake family", "BORN IN 1996")

ch("The house")
sc("""Let's start with the house. In the early sixties, the typical new house sold for around eighteen thousand dollars. A typical family earned around six thousand a year. So a home cost roughly three years of income, and a thirty-year-old with a steady job could usually buy one.""",
   "1960s new suburban house for sale", "THREE YEARS OF INCOME")
sc("""Today, the typical new house sells for around four hundred thousand dollars, and a typical household earns around eighty thousand dollars a year. So a home costs about five years of income, before you even count today's interest rates and insurance. That gap is the single biggest difference between these two lives.""",
   "modern suburban houses construction", "FIVE YEARS OF INCOME")
sc("""In nineteen sixty-two, the average age of a first-time home buyer was in the twenties. Today, it's well into the thirties. Our thirty-year-old in nineteen sixty-two has a mortgage, a lawn and a garage. A great many thirty-year-olds today are still renting, and some are living with their parents.""",
   "1960s young couple new house keys", "A MORTGAGE AT 30")
sc("""But look closer at the two houses. The nineteen sixty-two house was small, often around a thousand or twelve hundred square feet, with one bathroom for the whole family, no air conditioning, and a single-car garage. The typical new house today is about twice that size, with central air and two or three bathrooms.""",
   "1960s small house family living room", "HALF THE SIZE")
sc("""The children in nineteen sixty-two usually shared bedrooms, two or three to a room, sometimes in bunk beds. There was one telephone, one television and one car. The idea that every child would have a room of their own was a luxury, not an expectation. And yet nobody felt poor. Everybody they knew lived the same way.""",
   "1960s children bunk beds bedroom", "SHARED BEDROOMS")
sc("""Getting the mortgage was simpler too. You went to the local bank or savings and loan, sat down with a man who might know your father, and showed him your pay stubs. Many veterans bought with almost no money down, thanks to the GI Bill. A handshake and a signature, and a few weeks later you had the keys.""",
   "1960s bank loan officer couple", "A HANDSHAKE AT THE BANK")

ch("Work and pay")
sc("""In nineteen sixty-two, a thirty-year-old man with a high school diploma could find steady work in a factory, a railroad, a utility company or a store, and expect to stay there for decades. Many jobs came with a pension that would pay him every month for the rest of his life.""",
   "1960s factory workers steady job", "A JOB FOR DECADES")
sc("""Today, the thirty-year-old has probably had five or six jobs already. Many of the factories are gone. Pensions have mostly been replaced by retirement accounts that depend on the stock market. On the other hand, there are careers today that simply didn't exist in nineteen sixty-two, and many of them pay very well.""",
   "1960s office men working desks", "FIVE OR SIX JOBS")
sc("""For women, the difference is enormous. In nineteen sixty-two, a thirty-year-old woman was usually expected to stay home with her children. If she worked, her choices were often limited to teaching, nursing, secretarial work or retail, and she was usually paid much less than a man for the same job. Today, women make up nearly half of the workforce, in every profession.""",
   "1960s women office typists", "TWO DIFFERENT WORLDS FOR WOMEN")
sc("""In nineteen sixty-two, one paycheck was usually enough to support the whole family. Today, in most families with children, both parents work. Two incomes are often needed to cover what one income covered back then. That's one of the hardest facts about the comparison, and almost everybody feels it.""",
   "1960s father leaving for work family", "ONE PAYCHECK VS TWO")
sc("""The work week in nineteen sixty-two was forty hours, and when the whistle blew, the work was over. Nobody called you at dinner. Nobody sent you a message at ten o'clock at night. Today's thirty-year-old may earn more in real terms, but for many, the work never really stops. It follows them home in their pocket.""",
   "1960s men leaving factory gate evening", "WHEN THE WHISTLE BLEW")

ch("What things cost")
sc("""Now the everyday prices. In nineteen sixty-two, a gallon of gas cost around thirty cents. A loaf of bread around twenty cents. A new car around twenty-five hundred dollars, which was less than half a year's pay. Today, the average new car costs well over forty thousand dollars, more than half a year's income for a typical household.""",
   "1960s new car dealership showroom", "A CAR FOR HALF A YEAR'S PAY")
sc("""But many things are far cheaper today, measured in hours of work. A television in nineteen sixty-two could cost two or three weeks of pay, and it showed three channels in black and white. Clothing, appliances, a long-distance phone call, a plane ticket. Many of those cost a working family far more back then than they do now.""",
   "1960s family watching television console", "SOME THINGS COST MORE THEN")
sc("""And health care was a different world. In nineteen sixty-two, a visit to the doctor might cost five dollars, and he might come to your house. But there was much less that medicine could do. Medicare didn't exist yet. Many hospitals were small. And plenty of illnesses that are treatable today were simply a matter of luck.""",
   "1960s doctor house call family", "THE DOCTOR CAME TO YOU")
sc("""Life expectancy for a baby born in America in nineteen sixty-two was around seventy years. Today it's close to seventy-nine. Our thirty-year-old in twenty twenty-six can expect to live longer, and to be healthier in old age, than almost anyone in nineteen sixty-two could have imagined.""",
   "1960s hospital nurse patient", "SEVENTY VS SEVENTY-NINE")
sc("""Smoking was everywhere in nineteen sixty-two. More than four out of ten American adults smoked, in offices, on airplanes, in hospitals, even in doctors' waiting rooms. The Surgeon General's famous report on smoking and health didn't come out until January of nineteen sixty-four. Today, only about one adult in nine smokes.""",
   "1960s men smoking office", "FOUR OUT OF TEN SMOKED")

ch("Marriage and children")
sc("""In nineteen sixty-two, the typical man married at around twenty-three, and the typical woman at around twenty. By thirty, most of them had been married for several years and had two or three children, sometimes more. The baby boom was still going strong.""",
   "1960s young family children yard", "MARRIED AT TWENTY")
sc("""Today, the typical age at a first marriage is around thirty for men and twenty-eight or twenty-nine for women. So our thirty-year-old in twenty twenty-six may just be getting married, or may not be married at all. Many are waiting longer to have children, and having fewer of them.""",
   "1960s wedding couple church", "MARRIED AT THIRTY")
sc("""Raising children looked different too. In nineteen sixty-two, kids played outside all day without supervision. Mothers sent them out after breakfast and called them in for supper. Today, children are watched far more closely, driven to every activity, and kept busy with schedules that would have amazed a nineteen sixty-two mother.""",
   "1960s children playing street", "OUTSIDE ALL DAY")
sc("""And the cost of raising them has changed most of all. In nineteen sixty-two, a family with three children could get by on one income, with hand-me-down clothes and a state college costing a few hundred dollars a year in tuition. Today, child care and college tuition are among the biggest worries any young family faces.""",
   "1960s college students campus", "COLLEGE FOR A FEW HUNDRED")
sc("""Most thirty-year-olds in nineteen sixty-two had not gone to college at all. Only about one adult in twelve had a four-year degree. A high school diploma was enough to build a good life. Today, more than a third of adults have a bachelor's degree, and many young people start their thirties still paying off the loans for it.""",
   "1960s high school graduation caps", "ONE IN TWELVE HAD A DEGREE")

ch("Daily life")
sc("""A typical evening in nineteen sixty-two. Dinner at six, with the whole family at the table. The news at six-thirty. A game show or a western at seven. The children in bed by eight-thirty. The parents on the porch or in front of the television, maybe with a neighbor stopping by. And the phone, on the wall, rarely rang after nine.""",
   "1960s family dinner table evening", "AN EVENING IN 1962")
sc("""A typical evening in twenty twenty-six. Dinner, if everybody's home at the same time. Then every member of the family on a different screen, in a different room, watching something different. More choices than anyone in nineteen sixty-two could imagine. But often, a lot less together.""",
   "1960s family living room together", "MORE CHOICES, LESS TOGETHER")
sc("""In nineteen sixty-two, our thirty-year-old knew his neighbors by name. He belonged to a church, a union local, a bowling league, or a lodge like the Elks or the Rotary. Membership in clubs and community groups was at an all-time high. That kind of belonging is much harder to find today.""",
   "1960s men bowling league", "THE BOWLING LEAGUE")
sc("""Shopping was a trip into town, with a list. If a store didn't have what you needed, you ordered it from the catalog and waited two weeks. Today's thirty-year-old can have almost anything delivered to the door the next day. That's a kind of convenience no one in nineteen sixty-two could have dreamed of.""",
   "1960s woman shopping department store", "WAIT TWO WEEKS")
sc("""Vacations were simpler too. A week at the lake, or a road trip in the station wagon to see the Grand Canyon or the grandparents. Flying was a luxury for the wealthy, and people dressed up to board an airplane. Today a young couple can fly across the country for less than a week's pay, in jeans.""",
   "1960s family road trip station wagon", "DRESSED UP TO FLY")
sc("""And yet the nineteen sixty-two world had real fears of its own. That autumn, during the Cuban Missile Crisis, families listened to the radio and wondered if the world would end. Schoolchildren practiced hiding under their desks. Every generation of thirty-year-olds has its own reasons to lie awake at night.""",
   "1960s family listening radio news", "OCTOBER 1962")

ch("Who had it better?")
sc("""So what's the verdict? In nineteen sixty-two, the big things were easier. A house, a car and a family were within reach for a young couple with ordinary jobs and one income. Communities were tight. The future felt like it was going to be better than the past.""",
   "1960s happy family new car", "THE BIG THINGS WERE EASIER")
sc("""In twenty twenty-six, the small things are easier and life lasts longer. Medicine is better. Food is more varied. Travel is cheaper. Women and minorities have choices that were closed to them in nineteen sixty-two. But the big things, the house and the security, are much harder to reach.""",
   "1960s airport travelers airplane", "THE SMALL THINGS ARE EASIER")
sc("""And some things simply can't be compared. A nineteen sixty-two thirty-year-old who was Black, in much of the country, could not eat at certain lunch counters, vote freely, or buy a house in certain neighborhoods. For millions of Americans, the good old days were not good at all. That's part of the honest answer too.""",
   "1960s civil rights march", "NOT GOOD FOR EVERYONE")
sc("""Maybe the honest answer is this. The thirty-year-old of nineteen sixty-two had less, but was more sure of it. The thirty-year-old of today has more, but is less sure of all of it. And if you were thirty in the sixties or seventies yourself, you probably have your own opinion.""",
   "1960s older couple porch", "LESS, BUT MORE SURE")
sc("""So tell us in the comments. How old were you when you bought your first house, and what did it cost? And who do you think had it better? We read every comment. And stay with us, because next we'll learn the money-saving tricks that every grandmother used in nineteen fifty-five. Thank you for spending this time with me.""",
   "1960s suburban street houses evening", "WHO HAD IT BETTER?")

save("video08", "1962 vs 2026: Who Actually Had It Better at 30?", [
    "Median family income 1962 (about $5,956): U.S. Census Bureau, Current Population Reports P60",
    "Median sales price of new houses (about $18,000 in 1963; about $400,000 in 2024-2025): U.S. Census Bureau, New Residential Sales",
    "Median household income about $80,000 (2023): U.S. Census Bureau, Income in the United States 2023",
    "Median age at first marriage (1960s: about 22.8 men, 20.3 women; recent: about 30 men, 28 women): U.S. Census Bureau, Historical Marital Status Tables MS-2",
    "Life expectancy at birth about 70 (1962) and about 78-79 (recent): CDC National Center for Health Statistics",
    "Average new-vehicle transaction price above $40,000 (2024-2025): Kelley Blue Book / Cox Automotive",
    "Medicare created July 30, 1965: Social Security Amendments of 1965",
    "Adult smoking about 42% (1965) and about 11% (2022); Surgeon General's report January 11, 1964: CDC",
    "Adults 25+ with a bachelor's degree: 7.7% (1960), about 38% (2022): U.S. Census Bureau, Educational Attainment tables",
], "angle 2 · a stage of life", minutes=(12, 14.5))
