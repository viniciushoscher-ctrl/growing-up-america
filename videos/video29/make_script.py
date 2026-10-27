import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 29 · angle 2 (a stage of life, freshman year to graduation) · afternoon slot · day 10
# If You Started College in 1966, This Was Your Life

sc("""It's a hot day in early September of nineteen sixty-six. Your father pulls the family car up in front of a brick dormitory. In the trunk, there's a suitcase, a typewriter, a clock radio, a reading lamp and a box of sheets your mother ironed. You're eighteen years old. And you're about to become the first person in your family to go to college.""",
   "1960s college campus students dormitory", "SEPTEMBER, 1966")
sc("""Millions of young Americans made that same trip in the sixties. In nineteen sixty, about three and a half million Americans were enrolled in college. By nineteen seventy, it was more than eight million. Colleges were building new dorms, new classrooms and whole new campuses as fast as they could.""",
   "1960s university campus construction", "8 MILLION STUDENTS")
sc("""And if you started college in the fall of sixty-six, you were about to live through four of the most dramatic years in American history. Let's follow a freshman from that first day on campus to graduation in nineteen seventy.""",
   "1960s college students walking campus", "FOUR DRAMATIC YEARS")
sc("""Before you even arrived, there was the acceptance letter. It came in the mail, in a thick envelope if the news was good, and a thin one if it wasn't. Most students applied to only one or two schools, often the state university or a college close to home. And many chose their school simply because a parent, a teacher or an older cousin had gone there.""",
   "1960s teenager reading letter mailbox", "THE THICK ENVELOPE")

ch("Freshman year: the rules")
sc("""College in nineteen sixty-six had a lot of rules, especially for women. Most campuses were still run on a principle called in loco parentis, which meant the college acted in place of your parents. Women's dorms had curfews, often ten or eleven o'clock on weeknights. A housemother at the front desk checked everyone in.""",
   "1960s college women dormitory", "IN LOCO PARENTIS")
sc("""Men were not allowed in women's dorms, except in the lobby, during visiting hours. On some campuses, if a man visited a woman's room on a special open house day, the door had to stay open, and everyone had to keep at least one foot on the floor. Women who came in late could be punished, or even sent home.""",
   "1960s college dormitory lobby students", "ONE FOOT ON THE FLOOR")
sc("""Many schools still had dress codes. Women wore skirts to class and to dinner. Men wore slacks and collared shirts, and sometimes a jacket and tie in the dining hall. At some schools, freshmen even had to wear little caps, called beanies, during their first weeks, so upperclassmen could pick them out.""",
   "1960s college students class dress", "THE FRESHMAN BEANIE")
sc("""Meals were served in a big dining hall, cafeteria style, at set times. Miss dinner and you went hungry, or walked to the snack bar for a grilled cheese. The food was famously bad. Mystery meat, soggy vegetables and Jell-O in every color. Students complained endlessly, and then went back for seconds.""",
   "1960s college dining hall students", "MYSTERY MEAT")

ch("What it cost")
sc("""What did college cost? In nineteen sixty-six, the average yearly tuition at a public four-year college was only a few hundred dollars. Room and board added maybe seven or eight hundred more. A whole year at a state university could cost around twelve hundred dollars. At a private college, it might be twice that.""",
   "1960s college students library", "ABOUT $1,200 A YEAR")
sc("""That sounds incredible today, but the minimum wage in nineteen sixty-six was a dollar twenty-five an hour. Even so, many students paid their own way with a summer job, working in a factory, at a resort or on a road crew. They graduated with little or no debt. Today, the average yearly cost at a public university is many times higher, even after inflation.""",
   "1960s young man summer job factory", "A SUMMER JOB PAID FOR IT")
sc("""And for many, college was paid for by the government. The Higher Education Act of nineteen sixty-five created new grants and student loans for families who couldn't afford college. For the first time, millions of working-class kids, the sons and daughters of factory workers and farmers, could go.""",
   "1960s students graduation families", "THE HIGHER EDUCATION ACT")

ch("Dorm life")
sc("""Dorm rooms were small and simple. Two metal beds, two desks, two dressers and a sink in the corner, if you were lucky. Your roommate was a stranger, picked by the college, and you met for the first time on move-in day. Some roommates became lifelong friends. Others barely lasted a week.""",
   "1960s college dorm room students", "YOUR ROOMMATE")
sc("""There was one telephone on each floor, a pay phone in the hallway. When it rang, whoever was closest answered and shouted down the hall. Long distance calls home were expensive, so students called once a week, usually on Sunday night, when rates were cheaper. Parents waited by the phone.""",
   "1960s student pay phone hallway", "ONE PHONE PER FLOOR")
sc("""Most of the communication was by letter. Students wrote home every week, often asking for money. Parents sent back letters with a check, a few dollars in cash, or a care package of homemade cookies. Getting mail was the highlight of the day. An empty mailbox could ruin a whole afternoon.""",
   "1960s student reading letter mailbox", "LETTERS HOME")
sc("""And there was laundry. For many young men, college was the first time they had ever washed their own clothes. Some mailed their laundry home in a special canvas case, and their mothers mailed it back clean and folded, sometimes with cookies tucked inside. Others just let it pile up until it couldn't be ignored.""",
   "1960s laundry bag student", "MAILING THE LAUNDRY HOME")

ch("Classes")
sc("""Classes were big. Freshman lectures might have several hundred students in a huge hall, with a professor at the front and a microphone. Students took notes by hand, in spiral notebooks. Papers were typed on a manual or electric typewriter, with carbon paper for a copy. A typing mistake meant correction fluid, or starting the page over.""",
   "1960s college lecture hall students", "THE LECTURE HALL")
sc("""The library was the center of the academic world. No internet, no computers. Students searched the card catalog, a huge wooden cabinet full of little drawers, and then hunted for books in the stacks. Research for a term paper could take weeks. During finals, the library stayed open late, and every chair was full.""",
   "1960s library card catalog student", "THE CARD CATALOG")
sc("""Calculations were done with a slide rule, a ruler with a sliding middle piece. Engineering students carried them in a leather case on their belts. Electronic calculators wouldn't be affordable until the seventies. Computers existed, but they filled entire rooms, and students fed them programs on stacks of punched cards.""",
   "1960s student slide rule", "THE SLIDE RULE")
sc("""Grades mattered more than ever. A bad semester could mean losing a scholarship, or, for young men, losing a draft deferment. Students pulled all-nighters fueled by black coffee and No-Doz tablets. During exam week, the dorms went quiet. And when grades were posted on a bulletin board in the hallway, crowds gathered to look for their student numbers.""",
   "1960s students studying late night", "THE ALL-NIGHTER")

ch("Social life")
sc("""Social life revolved around the weekend. Fraternities and sororities were at the height of their popularity. Rush week came every fall. There were mixers, where boys from one dorm met girls from another, with a band or a record player and punch in a bowl. Homecoming was a huge event, with a parade, floats and a football game.""",
   "1960s college homecoming parade float", "HOMECOMING")
sc("""On Saturday afternoons, the whole campus went to the football game. Students wore their school colors, cheered with the band, and carried pennants. In winter, it was basketball. Afterward, there were parties, dances and late-night trips to the diner for burgers and fries.""",
   "1960s college football game crowd", "SATURDAY AFTERNOON")
sc("""And there was the music. In nineteen sixty-six and sixty-seven, college students listened to the Beatles' Revolver and Sgt. Pepper's, Bob Dylan, Simon and Garfunkel, the Beach Boys' Pet Sounds, and the Doors. Every dorm room had a record player. And late at night, students listened to new FM radio stations that played whole album sides.""",
   "1960s college students record player dorm", "SGT. PEPPER'S")
sc("""Dating had its own rituals. A man asked a woman out days in advance, by phone or in person. He picked her up at the dorm lobby, signed her out with the housemother, and had her back before curfew. If they got serious, he gave her his fraternity pin, which was called getting pinned. It was the step before engagement, and many couples married right after graduation.""",
   "1960s college couple dating campus", "GETTING PINNED")

ch("The draft")
sc("""For young men in college in the late sixties, there was one thing always in the back of their minds. The draft. The war in Vietnam was growing. In nineteen sixty-six, the United States had about three hundred eighty thousand troops there, and the number kept rising. Every month, thousands of young men were drafted.""",
   "1960s young men draft board", "THE DRAFT")
sc("""College students could get a student deferment, called a two-S, which postponed the draft while they were in school. But they had to stay enrolled and keep their grades up. Some men stayed in school, or went on to graduate school, partly to avoid being sent to Vietnam. Flunking out could mean a ticket to the jungle.""",
   "1960s college student studying desk", "THE 2-S DEFERMENT")
sc("""In December of nineteen sixty-nine, the government held the first draft lottery since World War Two. Every birthday was drawn, one by one, on live television. Young men gathered in dorm lounges to watch. If your birthday came up with a low number, you were likely to be drafted. If it was high, you were probably safe. It was one of the most tense nights of their lives.""",
   "1969 draft lottery television", "THE DRAFT LOTTERY")

ch("Change on campus")
sc("""By nineteen sixty-seven and sixty-eight, campuses were changing fast. Students protested the war, marched for civil rights, and demanded a voice in how their colleges were run. Teach-ins, rallies and sit-ins became common. Some students joined the protests. Many more simply watched, studied and worried.""",
   "1960s college students protest rally", "THE PROTESTS")
sc("""Styles changed too. Freshmen who arrived in sixty-six with crew cuts and pleated skirts looked very different by seventy. Hair got longer. Skirts got shorter, then much longer. Jeans and sandals replaced slacks and loafers. And one by one, the old rules about curfews and dress codes disappeared.""",
   "1960s college students long hair campus", "STYLES CHANGED")
sc("""Nineteen sixty-eight was the hardest year. In April, Martin Luther King Junior was killed. In June, Robert Kennedy was killed. Students who had grown up believing in a bright future suddenly saw a country in turmoil. Many say that year changed them more than any class they ever took.""",
   "1960s students candlelight vigil", "1968")
sc("""In July of nineteen sixty-nine, many students were home for the summer when Apollo eleven landed on the moon. They watched it on the family television, with their parents and little brothers and sisters. After everything that had happened, it was a moment of pure pride. For one night, the whole country seemed to be cheering together.""",
   "1969 family watching moon landing television", "JULY 1969")

ch("Graduation")
sc("""And then, in the spring of nineteen seventy, the class that started in sixty-six graduated. They had arrived in a world of beanies and curfews and left in a world that had been turned upside down. That May, the shootings at Kent State in Ohio shook campuses across the country. Some schools canceled classes and even graduation ceremonies.""",
   "1970 college graduation caps gowns", "THE CLASS OF 1970")
sc("""But most of them walked across the stage, shook the president's hand, and took their diploma, while their parents cried in the audience. For many, they were the first in their family ever to graduate from college. It was the proudest day of their parents' lives.""",
   "1970 graduation family photo", "THE PROUDEST DAY")
sc("""The class of nineteen seventy went on to become teachers, engineers, lawyers, nurses, business owners and soldiers. They raised families, built careers and lived through everything that came next. But many say those four years, from sixty-six to seventy, shaped who they were for the rest of their lives.""",
   "1970s young professionals office", "SHAPED FOR LIFE")

ch("Then and now")
sc("""Today, college looks very different. No curfews. No beanies. Computers in every pocket. But it costs far more, and many students graduate with tens of thousands of dollars in debt. In nineteen sixty-six, a young person could pay for college with a summer job. That's almost impossible today.""",
   "1960s campus students walking autumn", "THEN AND NOW")
sc("""If you started college in the late sixties, you remember it. The typewriter in your dorm room. The pay phone in the hall. The letters from home with a five-dollar bill inside. The roommate you'll never forget. And the feeling that the whole world was changing, and you were right in the middle of it.""",
   "1960s college dorm typewriter", "YOU WERE RIGHT IN THE MIDDLE")
sc("""So tell us in the comments. Where did you go to college, and what year did you start? What was your dorm like, and what do you remember most? We read every comment. Next time, we're looking at the truth about the nineteen sixties kitchen your mother trusted. Thank you for spending this time with me.""",
   "1960s university campus sunset", "WHERE DID YOU GO TO COLLEGE?")

save("video29", "If You Started College in 1966, This Was Your Life", [
    "Total fall college enrollment about 3.6 million in 1960 and 8.6 million in 1970: National Center for Education Statistics, Digest of Education Statistics",
    "Average tuition, fees, room and board at public four-year institutions about $1,000-$1,300 in the mid-1960s: NCES Digest of Education Statistics",
    "Federal minimum wage $1.25 an hour (1963-1967): U.S. Department of Labor",
    "Higher Education Act of 1965: U.S. Department of Education",
    "U.S. troops in Vietnam about 385,000 at the end of 1966: National Archives; U.S. Department of Defense",
    "Selective Service 2-S student deferment and the December 1, 1969 draft lottery: Selective Service System",
    "Assassinations of Martin Luther King Jr. (April 4, 1968) and Robert F. Kennedy (June 6, 1968): National Archives",
    "Kent State shootings, May 4, 1970: Kent State University; National Archives",
], "angle 2 · a stage of life", minutes=(12, 14.5))
