import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 04 · angle 1 (a place and a time) · morning slot · day 2
# Lost 70s: Small-Town America in 1974
# Photos: the EPA's DOCUMERICA project (1971-1977) photographed everyday America and is public domain,
# so every query names Documerica to keep the pictures in the right decade.

sc("""It's a Saturday morning in the summer of nineteen seventy-four. The screen door bangs behind you. Somewhere down the street a lawn mower starts, then another. The radio in the kitchen is playing a song you will still know every word of fifty years from now. And the whole town, it seems, has nowhere special to be.""",
   "Documerica small town street 1974", "SUMMER, 1974")
sc("""This is the decade people forget. The fifties get the diners and the poodle skirts. The sixties get the music and the moon. But the seventies were the years most of us actually grew up in, or raised our children in, or went to work in every single day. And small-town America in nineteen seventy-four looked like nowhere else, before or since.""",
   "Documerica main street storefronts", "THE FORGOTTEN DECADE")
sc("""So let's take a walk. Down Main Street, past the gas lines and the five-and-dime. Into the living rooms with the wood paneling and the shag carpet. Out to the ball field on a Friday night. This is small-town America in nineteen seventy-four, the way it really was.""",
   "Documerica town square people", "LOST 70s")

ch("Main Street")
sc("""In nineteen seventy-four, most small towns still had a real downtown. A hardware store where the owner knew what you needed before you did. A drugstore with a lunch counter. A bank with a clock out front that told the time and the temperature. The shopping mall was coming, but in a lot of places it hadn't arrived yet.""",
   "Documerica main street small town", "A REAL DOWNTOWN")
sc("""The cars parked along the curb were enormous. Station wagons with wood paneling down the sides. Big sedans in harvest gold and avocado green, with vinyl tops and bench seats you could fit three people across. A full tank cost more than it used to, and everybody was talking about it.""",
   "Documerica parked cars street", "CARS AS BIG AS BOATS")
sc("""Because that winter had brought the gas lines. After the oil embargo began in October of nineteen seventy-three, the price of gasoline jumped, and in many towns you waited in a line of cars that stretched around the block. Some states let you buy gas only on odd or even days, depending on the last number of your license plate.""",
   "Documerica gas station line 1974", "THE GAS LINES")
sc("""Stations hung flags out front. A green flag meant they had gas. A yellow flag meant it was rationed. A red flag meant they were out. You learned to read those flags from two blocks away. And for the first time, a lot of families started asking whether the next car should be a little smaller.""",
   "Documerica gas station sign", "GREEN, YELLOW, RED")
sc("""The speed limit on the highway dropped to fifty-five miles an hour, to save fuel, and it stayed there for years. Truckers talked to each other on CB radios to warn about speed traps, and before long half the country seemed to have a CB in the car, with a handle like Rubber Duck or Night Owl.""",
   "Documerica highway traffic trucks", "FIFTY-FIVE MILES AN HOUR")
sc("""On the corner there was still a full-service gas station. A bell rang when you drove over the hose, and a young man in a uniform came out to pump your gas, wash your windshield, and check your oil without being asked. If you bought enough gallons, you might even get a free glass or a set of steak knives.""",
   "Documerica gas station attendant", "FULL SERVICE")

ch("The house you lived in")
sc("""Step inside a typical house in nineteen seventy-four and the first thing you'd notice is the color. Orange. Brown. Harvest gold. Avocado green. The refrigerator matched the stove, and the stove matched the countertops, and the whole kitchen looked like an autumn afternoon.""",
   "Documerica family kitchen home", "HARVEST GOLD")
sc("""The living room had wood paneling on the walls and shag carpet on the floor, deep enough to lose a toy in. Some families owned a special rake just for fluffing the shag. There was a console television in a wooden cabinet, and on top of it sat the rabbit ears, which you adjusted with one hand while somebody on the couch shouted, that's it, right there, don't move.""",
   "Documerica living room family television", "THE SHAG CARPET")
sc("""There were three networks, maybe four channels if you counted public television, and when the stations signed off late at night, the national anthem played and then the screen turned to snow. If you missed a show, you missed it. There was no way to watch it later. You simply waited for the reruns in the summer.""",
   "Documerica family watching television", "THREE CHANNELS")
sc("""The telephone hung on the kitchen wall, with a cord long enough to stretch into the pantry for a private conversation. There was one line for the whole family. If your sister was on it, you waited. And if you wanted to call the next town over, that was long distance, and you kept it short, because your father would see it on the bill.""",
   "Documerica woman telephone kitchen", "ONE LINE FOR THE FAMILY")
sc("""Dinner was at six o'clock, at the kitchen table, and everybody was expected to be there. Meatloaf. Tuna casserole. Hamburger Helper, which had arrived a few years earlier and promised a whole meal from one pound of beef. And on special nights, a frozen TV dinner in an aluminum tray, eaten in front of the television.""",
   "Documerica family dinner table", "DINNER AT SIX")
sc("""In the garage there was a second refrigerator, a workbench with coffee cans full of nails and screws, and a lawn mower your father worked on every spring. The garage door didn't open by itself. You got out of the car, lifted the handle, and pushed it up by hand, even in the rain.""",
   "Documerica suburban garage house", "THE GARAGE")

ch("Growing up in 1974")
sc("""For a kid in nineteen seventy-four, summer meant freedom. You left after breakfast on a bicycle with a banana seat and high handlebars, and you didn't come back until the streetlights came on. Nobody had any idea where you were. Nobody seemed to worry about it either.""",
   "Documerica children bicycles street", "BACK BY THE STREETLIGHTS")
sc("""You drank from the garden hose. You played kickball in the street and moved out of the way when a car came. You rode in the back of a pickup truck to the lake, with the wind in your hair, and nobody thought twice. In the back seat of the station wagon, seat belts were stuffed down between the cushions, mostly forgotten.""",
   "Documerica children swimming lake", "THE GARDEN HOSE")
sc("""On Saturday mornings there were cartoons, and nothing else mattered until noon. In the afternoon there might be a matinee at the movie house downtown, where a ticket and a box of candy cost less than a dollar or two. And in the summer of nineteen seventy-five, a movie about a shark kept a whole generation out of the water.""",
   "Documerica movie theater small town", "THE SATURDAY MATINEE")
sc("""School meant a long ride on a yellow bus, a lunch box with your favorite television show on the side, and a thermos that never quite kept the soup warm. The teacher wrote on a chalkboard. Tests were printed on a mimeograph machine, and the pages came out purple and damp, smelling of ink. Every kid in America remembers that smell.""",
   "Documerica school bus children", "THE MIMEOGRAPH")
sc("""Teenagers cruised Main Street on Friday and Saturday nights, up one side and down the other, again and again, radios turned up. The drive-in at the edge of town was still open in the summer. And the local pizza place, with its red checked tablecloths and its jukebox, was where you went after the game.""",
   "Documerica teenagers cars town night", "CRUISING MAIN STREET")

ch("Work and money")
sc("""For the grown-ups, nineteen seventy-four was a hard year for money. Prices were rising faster than anybody could remember. The newspapers called it inflation, and by the end of the year it was running above ten percent. A trip to the grocery store cost noticeably more in December than it had in January.""",
   "Documerica grocery store shopping", "PRICES WENT UP")
sc("""In nineteen seventy-four, the federal minimum wage rose to two dollars an hour. A gallon of gas that had cost around thirty-nine cents the year before now cost over fifty cents in many places. A first-class stamp cost ten cents. People clipped coupons, planted vegetable gardens, and turned the thermostat down and put on a sweater.""",
   "Documerica vegetable garden family", "TWO DOLLARS AN HOUR")
sc("""Mothers who had stayed home in the fifties and sixties were going back to work, in banks and stores and offices and hospitals. Some needed the second paycheck. Some simply wanted to. Either way, the kitchen table conversations were changing, and so were the families sitting around them.""",
   "Documerica woman working office", "THE SECOND PAYCHECK")
sc("""Still, a lot of small towns were built around one big employer. A mill, a mine, a plant, or a railroad yard. The whistle blew at the change of shift, and half the town seemed to be on the road at once. A man with a high school diploma could still find steady work there, with a union card and a pension at the end of it.""",
   "Documerica factory workers mill", "THE SHIFT WHISTLE")
sc("""And on the farms around those towns, families still worked the land the way their parents had, only with bigger tractors. The county fair in August was the high point of the year. Blue ribbons for the best pie, the best steer, the best quilt. A Ferris wheel lit up against the dark fields.""",
   "Documerica farm family tractor", "THE COUNTY FAIR")

ch("Friday nights and Sunday mornings")
sc("""On Friday night in the fall, the whole town went to the high school football game. The bleachers were full. The band played under the lights. You could smell popcorn and cold air and somebody's cigarette, and afterward everybody drove slowly down Main Street honking their horns if the home team won.""",
   "Documerica high school football game", "FRIDAY NIGHT LIGHTS")
sc("""Sunday morning was church, in your good clothes, followed by a big dinner in the middle of the day. Most stores were closed. The streets were quiet. In the afternoon, families went for a drive with no place in particular to go, just to look at the fields and the houses and be together in the car.""",
   "Documerica church congregation small town", "SUNDAY DINNER")
sc("""In the summer there were parades on the Fourth of July, with fire trucks and marching bands and kids on decorated bicycles, and by nineteen seventy-four, everyone was already talking about the Bicentennial, two years away. Red, white and blue was painted on fire hydrants, mailboxes and park benches all over the country.""",
   "Documerica Fourth of July parade", "COUNTING DOWN TO 1976")
sc("""And when the weather turned cold, the whole town seemed to move indoors. The bowling alley filled up with league nights. The church basement hosted potluck suppers, every casserole labeled with a strip of masking tape so it would find its way home. And the high school gym became the center of the world on basketball nights.""",
   "Documerica bowling alley people", "LEAGUE NIGHT")
sc("""In August of nineteen seventy-four, the whole country gathered around those same television sets to watch a president resign. Whatever people thought of it, they watched it together, in living rooms and diners and barber shops, at the same moment. That was the last decade when a whole nation still did that.""",
   "Documerica people watching television together", "AUGUST 1974")

ch("Why we miss it")
sc("""Was it a perfect time? No. There were gas lines, layoffs, and worries about money that kept parents awake at night. But there was also a kind of slowness that's gone now. A town where you knew the mailman's name. A phone that rang on the wall. A whole summer that felt like it would never end.""",
   "Documerica small town evening street", "NOT PERFECT, BUT OURS")
sc("""If you grew up in a small town in the seventies, you carry that town with you. The sound of the screen door. The smell of the shag carpet after it was vacuumed. Your mother calling your name down the street at dusk. It's still there, whenever you close your eyes.""",
   "Documerica children playing yard sunset", "YOU CARRY IT WITH YOU")
sc("""So tell us, in the comments. What town did you grow up in, and what year? We read every single one. And if this brought back memories, stay a while, because next we're going back to nineteen fifty-nine, to the very first job you ever had. Thank you for spending this time with me.""",
   "Documerica small town main street dusk", "WHAT TOWN DID YOU GROW UP IN?")

save("video04", "Lost 70s: Small-Town America in 1974", [
    "1973-74 oil embargo, odd-even gasoline rationing and gas station flag system: U.S. Department of Energy / Federal Energy Office records; contemporary press (1973-74)",
    "U.S. inflation above 10% in 1974: Bureau of Labor Statistics, CPI-U annual data",
    "President Nixon's resignation, televised August 8, 1974: National Archives",
    "Photographs: DOCUMERICA project, U.S. Environmental Protection Agency (1971-1977), public domain, via Wikimedia Commons / National Archives",
], "angle 1 · a place and a time", minutes=(12, 14.5))
