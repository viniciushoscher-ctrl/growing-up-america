import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 19 · angle 1 (a place and a time, a walk door to door) · morning slot · day 7
# Main Street, 1957: A Walk Through the Town We Lost

sc("""It's a Saturday morning in nineteen fifty-seven, and you're standing at the corner of Main Street. The sun is shining on the brick buildings. Cars are parked at an angle along the curb. A bell rings over a shop door. Somebody waves at you from across the street, because in this town, everybody knows everybody.""",
   "1950s main street small town cars", "SATURDAY, 1957")
sc("""In nineteen fifty-seven, almost every town in America had a street like this. It might have been called Main Street, Front Street, Broadway or Market Street. But it was always the heart of the town. It was where you shopped, ate, banked, got your hair cut, saw a movie and caught up on all the news.""",
   "1950s downtown street shops people", "THE HEART OF THE TOWN")
sc("""So let's take a walk. Door by door, block by block, down a typical American Main Street in nineteen fifty-seven. If you grew up in a small town, I think you'll recognize every single place we stop.""",
   "1950s people walking sidewalk storefronts", "LET'S TAKE A WALK")

ch("The drugstore")
sc("""Our first stop is the corner drugstore. Through the glass door, you can smell it before you see it. Medicine, perfume, coffee and fresh-made grilled cheese. On one side, the pharmacist works behind a high counter. On the other side, there's the soda fountain, with a long marble counter and a row of red stools.""",
   "1950s drugstore soda fountain counter", "THE CORNER DRUGSTORE")
sc("""The soda jerk wears a white paper hat. He makes a cherry Coke by pumping syrup into a glass and adding carbonated water. A chocolate malted costs about twenty-five cents. A banana split, maybe thirty-five. Teenagers crowd the booths after school, and old men drink coffee at the counter every morning.""",
   "1950s soda jerk making milkshake", "THE SODA JERK")
sc("""The pharmacist knows everyone in town by name. He knows who has a bad heart and whose baby has a cough. If you call late at night with a sick child, he might open the store just for you. There's a rack of comic books near the door, and a magazine stand with Life, Look and The Saturday Evening Post.""",
   "1950s pharmacist drugstore", "HE KNOWS YOUR NAME")

ch("The five-and-dime")
sc("""Next door is the five-and-dime. Woolworth's, Kresge's, Ben Franklin, or a local store just like them. Wooden floors that creak when you walk. Long counters piled with everything you could need. Thread, buttons, yarn, sewing patterns, kitchen gadgets, school supplies, cheap toys, goldfish and parakeets.""",
   "1950s five and dime store interior counters", "THE FIVE-AND-DIME")
sc("""Kids love the five-and-dime, because it's the one store where their allowance goes a long way. A quarter can buy a bag of candy, a balsa wood airplane, or a little plastic toy. Many of those stores also have a lunch counter, where shoppers stop for a grilled cheese, a slice of pie and a cup of coffee.""",
   "1950s children toys store counter", "WHERE A QUARTER GOES FAR")

ch("The hardware store")
sc("""Across the street is the hardware store, and it's a world of its own. The smell of oil, rope and fresh-cut keys. Nails sold by the pound from wooden bins. Paint mixed by hand. Garden seeds in paper packets. Every tool a man could want, hanging on pegboard walls.""",
   "1950s hardware store interior", "THE HARDWARE STORE")
sc("""The owner can tell you exactly what you need, even if you can only describe it. You bring in the broken part, and he finds you a match. He'll explain how to fix a leaky faucet or sharpen a lawnmower blade. And if you're a little short on cash this week, he'll put it on your account.""",
   "1950s hardware store owner customer", "PUT IT ON MY ACCOUNT")

ch("The department store")
sc("""In the middle of the block is the biggest building on Main Street. The department store. In a bigger town, it might be a J.C. Penney, a Sears or a local family store with the founder's name painted on the side. Inside, there are glass display cases, high ceilings and an elevator with an operator who calls out each floor.""",
   "1950s department store interior shoppers", "THE DEPARTMENT STORE")
sc("""Women shop for dresses, hats, gloves and stockings. Men buy suits, shirts and neckties. Children get measured for new school shoes, and some stores have a machine called a shoe-fitting fluoroscope, which uses X-rays so you can see your toes wiggling inside the shoes. It sounds incredible today, but kids loved it.""",
   "1950s shoe store children fitting", "THE X-RAY SHOE MACHINE")
sc("""When you pay, the clerk might put your money in a little container and send it zooming along a wire or through a pneumatic tube to the cashier upstairs. A moment later, your change comes zooming back. At Christmastime, the store windows are filled with displays, and Santa sits in a big chair on the toy floor.""",
   "1950s department store Christmas window display", "CHANGE BY TUBE")

ch("The barbershop and the beauty shop")
sc("""Down the street is the barbershop, with its spinning red, white and blue pole. Inside, there are two or three big leather chairs, a row of waiting chairs, and a stack of old magazines. A haircut costs around a dollar. The radio plays a ballgame, and the men argue about politics and fishing.""",
   "1950s barbershop interior barber", "THE BARBERSHOP")
sc("""Little boys get a crew cut or a flattop, sitting on a board laid across the arms of the chair. The barber finishes with a splash of tonic and a dusting of powder on the neck. And for the grown men, there's a hot towel shave with a straight razor, and maybe a shoeshine on the way out.""",
   "1950s boy haircut barbershop", "A FLATTOP")
sc("""A few doors away is the beauty shop, where the women of the town get their hair washed and set. They sit under big hooded dryers, reading magazines and catching up on every bit of news in town. Many people say the beauty shop was the real newspaper of a small town. If it happened, they knew about it there.""",
   "1950s beauty salon women hair dryers", "THE REAL NEWSPAPER")

ch("The bank, the post office and the newspaper")
sc("""On the corner stands the bank, built of stone, with tall columns and a big clock out front. Inside, the floors are marble, and the tellers sit behind brass cages. Children bring in their piggy banks to open a passbook savings account. And the bank president knows every farmer and business owner in the county.""",
   "1950s bank interior tellers", "THE BANK")
sc("""Across the street is the post office, with the American flag flying out front. Inside, there's a wall of little brass mailboxes with tiny glass windows. A stamp costs three cents. Wanted posters hang on the bulletin board. And the postmaster, who's held the job for twenty years, knows everyone's handwriting.""",
   "1950s small town post office", "3-CENT STAMP")
sc("""And there's the newspaper office, with the presses rumbling in the back. The weekly paper reports everything. Who's visiting from out of town. Whose cow won at the county fair. Births, weddings, deaths, and the high school football scores. In a town like this, getting your name in the paper is a very big deal.""",
   "1950s newspaper office printing press", "YOUR NAME IN THE PAPER")

ch("The diner")
sc("""By now, you're hungry. So let's stop at the diner. It might be a shiny steel railroad car diner, or a little café with a counter and a few booths. The cook works the grill where everyone can see him. The waitress calls you honey and refills your coffee before you ask.""",
   "1950s diner interior counter waitress", "THE DINER")
sc("""A hamburger costs about thirty cents. A plate of meatloaf with mashed potatoes and green beans is around seventy-five cents. And there's always pie. Apple, cherry, coconut cream, lemon meringue. Every table has a little jukebox selector, where a nickel buys you one song.""",
   "1950s diner food plate pie", "PIE")
sc("""The diner is where the town really talks. Farmers come in early, before sunrise. Businessmen come for lunch. Teenagers come after the movie. Police officers stop by on their rounds. Everybody's welcome, and almost everybody stops in sooner or later.""",
   "1950s diner customers talking", "EVERYBODY'S WELCOME")

ch("The movie theater")
sc("""Halfway down the block, you can't miss it. The movie theater, with its big marquee full of light bulbs, and black letters announcing what's playing. In nineteen fifty-seven, that might be The Bridge on the River Kwai, An Affair to Remember, or Elvis Presley in Jailhouse Rock.""",
   "1950s movie theater marquee small town", "THE MARQUEE")
sc("""On Saturday afternoon, it's the kids' matinee. For a quarter, children get cartoons, a newsreel, a cowboy serial and a full feature. They throw popcorn, shout at the screen, and cheer for the hero. Parents drop them off at noon and pick them up at four, and everybody's happy.""",
   "1950s children movie theater audience", "THE SATURDAY MATINEE")
sc("""Inside, the theater is grand, with velvet curtains, a balcony, and painted ceilings. An usher in a uniform shows you to your seat with a flashlight. Popcorn costs a dime. For many small towns, the theater is the most beautiful building in town, and the place where first dates and first kisses happen.""",
   "1950s movie theater interior balcony", "THE MOST BEAUTIFUL BUILDING")

ch("Saturday night")
sc("""As the sun goes down, Main Street fills up. Saturday night is the big night of the week. Farm families come into town to shop, visit and see a movie. Stores stay open late. People stroll up and down the sidewalk, stopping to talk with friends and neighbors they haven't seen all week.""",
   "1950s main street night lights people", "SATURDAY NIGHT")
sc("""Teenagers cruise the street in their cars, around and around, radios playing. Old men sit on a bench outside the hardware store, watching the world go by. Kids beg for one more ice cream cone. In many towns, there's a band concert in the park, or a dance at the American Legion hall.""",
   "1950s teenagers cars main street night", "AROUND AND AROUND")

ch("What happened")
sc("""So what happened to that Main Street? In the years after nineteen fifty-seven, America changed in ways that slowly emptied it. The interstate highways, which started in nineteen fifty-six, made it easy to drive past small towns, or to drive out to a bigger one.""",
   "1950s interstate highway construction", "THE INTERSTATE")
sc("""Shopping centers and malls grew up on the edge of town, with free parking and everything under one roof. The first fully enclosed mall in America, Southdale Center in Minnesota, had opened just a year earlier, in nineteen fifty-six. Over the next thirty years, thousands of malls followed.""",
   "Southdale Center 1956 mall", "SOUTHDALE, 1956")
sc("""Then came the big discount stores. Kmart in nineteen sixty-two. Walmart, the same year. They offered lower prices than any small shop could match. One by one, the drugstore, the hardware store, the five-and-dime and the department store closed. In many towns, the movie theater went dark too.""",
   "1960s discount store parking lot", "1962: KMART AND WALMART")
sc("""By the nineteen eighties, many Main Streets were half empty. Boarded-up windows. For Lease signs. The bank building turned into a law office, or nothing at all. In nineteen eighty, the National Trust for Historic Preservation started the Main Street program, to try to bring those downtowns back to life.""",
   "1980s empty small town main street", "FOR LEASE")

ch("The town we lost")
sc("""Some of them have come back. Today, many small towns have restored their old Main Streets, with coffee shops, bakeries and antique stores in the old buildings. But something is different. The pharmacist who knew your name, the barber who'd cut your hair since you were three, and the Saturday nights when the whole town came out are mostly memories now.""",
   "small town main street brick buildings", "SOME HAVE COME BACK")
sc("""What we lost wasn't just stores. It was a way of living. A place where you couldn't walk a block without saying hello to someone. Where business was done on a handshake. Where you were part of a town, not just a customer. For many people, that's what they miss the most.""",
   "1950s neighbors talking sidewalk", "A WAY OF LIVING")
sc("""If you grew up on a Main Street like this, you carry it with you. The bell over the door. The squeak of the stool at the soda fountain. The light of the marquee. The smell of the hardware store. It's still there, every time you close your eyes.""",
   "1950s main street evening", "THE BELL OVER THE DOOR")
sc("""So tell us in the comments. What was the name of your town, and what was the name of its Main Street? What store do you miss the most? We read every comment. Next, we're looking at what it was like to become a mother in nineteen fifty-five. Thank you for spending this time with me.""",
   "1950s small town street sunset", "WHAT WAS YOUR TOWN?")

save("video19", "Main Street, 1957: A Walk Through the Town We Lost", [
    "Shoe-fitting fluoroscopes in U.S. shoe stores (about 10,000 in use in the early 1950s): Oak Ridge Associated Universities, Health Physics Historical Instrumentation Museum",
    "First-class postage 3 cents (1932-1958): U.S. Postal Service",
    "1957 films (The Bridge on the River Kwai, An Affair to Remember, Jailhouse Rock): American Film Institute catalog",
    "Federal-Aid Highway Act of 1956: Federal Highway Administration",
    "Southdale Center, Edina, Minnesota, opened October 1956 as the first fully enclosed mall: Minnesota Historical Society",
    "First Kmart and first Walmart, both 1962: company histories",
    "National Trust for Historic Preservation Main Street program, 1980: Main Street America",
], "angle 1 · a place and a time", minutes=(12, 14.5))
