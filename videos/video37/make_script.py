import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 37 · angle 1 (a place and a time, one Saturday from opening to closing) · morning slot · day 13
# Saturday at the Mall in 1984: The America We Lost
# Capitalised words in the queries keep the image search on Wikimedia Commons (photos before 1990)
# instead of the Prelinger films, which stop in 1969.

sc("""It's a Saturday morning in nineteen eighty-four. You've got twenty dollars from your paper route in your pocket, your hair is feathered just right, and your mom is dropping you and your friends off at the main entrance. She'll pick you up at four, by the fountain. You walk through the glass doors, and there it is. The mall.""",
   "1980s Shopping Mall entrance", "SATURDAY, 1984")
sc("""In the nineteen eighties, the shopping mall was the center of American life, especially for teenagers. It was where you shopped, ate, played video games, saw movies, met friends and maybe met someone special. In those years, America built new malls at a remarkable pace, and by the end of the decade there were thousands of them.""",
   "1980s Shopping Mall interior atrium", "THE CENTER OF AMERICAN LIFE")
sc("""So let's spend a Saturday at the mall in nineteen eighty-four. From opening time to closing time. The stores, the food court, the arcade, the music and the people. If you were there, you might just hear the fountain splashing and smell the Cinnabon.""",
   "1980s Shopping Mall fountain", "FROM OPENING TO CLOSING")
sc("""The mall had been growing for decades. The first fully enclosed mall, Southdale Center in Edina, Minnesota, had opened in nineteen fifty-six. Through the sixties and seventies, malls spread to every suburb in the country. By the eighties, they had pulled the shoppers away from downtown Main Streets almost everywhere. The mall had become the new Main Street.""",
   "Southdale Center Edina Minnesota", "THE NEW MAIN STREET")

ch("Opening time")
sc("""At ten o'clock, the metal gates rolled up on hundreds of storefronts. The mall was clean and quiet. The first people inside were the mall walkers, older men and women in tracksuits and white sneakers, walking laps in the air conditioning. Many malls opened early just for them.""",
   "1980s Shopping Mall corridor stores", "THE MALL WALKERS")
sc("""The malls of the eighties were bright and modern, with skylights, glass elevators, brass railings, potted palm trees and huge fountains. Some had ice skating rinks, carousels or even small amusement parks. Shoppers threw coins into the fountains and made wishes. Some malls collected thousands of dollars a year from them for charity.""",
   "1980s Mall Skylight Atrium Fountain", "THE FOUNTAIN")
sc("""At each end of the mall stood the anchor stores, the big department stores. Sears, J.C. Penney, Montgomery Ward, Macy's or a regional chain like Hudson's, Marshall Field's or Bullock's. Parents shopped there for clothes, appliances and towels. Kids went there to use the restroom and look at the electronics.""",
   "1980s Sears department store Mall", "THE ANCHOR STORES")
sc("""Getting there was half the adventure. Teenagers without a license begged rides from parents or older siblings. In some towns, a city bus stopped right at the mall entrance. Kids rode their bikes for miles and locked them to the rack outside Sears. And once you got your license, driving your friends to the mall on Saturday was the whole point of having a car.""",
   "1980s Mall parking lot cars", "GETTING THERE")

ch("The stores")
sc("""In between were the smaller stores, and for teenagers, they were the real attraction. There was the record store, like Sam Goody or Camelot Music, with racks of vinyl albums and cassette tapes. In nineteen eighty-four, everyone was buying Michael Jackson's Thriller, Prince's Purple Rain, Bruce Springsteen's Born in the U.S.A. and Madonna.""",
   "1980s Record Store cassettes albums", "SAM GOODY")
sc("""There was the bookstore, B. Dalton or Waldenbooks, where kids read comic books and magazines without buying them until a clerk shooed them away. There was Radio Shack, with its batteries, walkie-talkies and the new TRS-80 computer. And there was Spencer Gifts, with its black lights, lava lamps, gag gifts and posters.""",
   "1980s Waldenbooks Bookstore Mall", "WALDENBOOKS AND RADIO SHACK")
sc("""For clothes, teenagers went to The Limited, Chess King, Merry-Go-Round, County Seat and The Gap. The fashion of eighty-four meant parachute pants, Members Only jackets, Swatch watches, jelly bracelets, leg warmers and acid-wash jeans. Girls wore big bangs held up with Aqua Net hairspray. Boys wore Izod shirts with the collar popped up.""",
   "1980s Teenagers Fashion Mall", "MEMBERS ONLY")
sc("""Then there was the shoe store. Nike Air Jordans wouldn't arrive until the following year, but in nineteen eighty-four, kids wanted Nike, Reebok, Converse high-tops and Vans. Girls wanted Keds and jelly shoes. And at the Foot Locker, the clerks wore referee shirts and measured your feet with a metal Brannock device, just like the shoe stores of their parents' day.""",
   "1980s Foot Locker Shoe Store", "THE REFEREE SHIRTS")
sc("""And there was the toy store, KB Toys or Kay-Bee, packed with He-Man figures, Transformers, which arrived that very year, Care Bears, Strawberry Shortcake and Rubik's Cubes. And everyone was looking for a Cabbage Patch Kid. The year before, at Christmas of nineteen eighty-three, parents had literally fought in stores to get one.""",
   "Toys R Us store 1980s", "CABBAGE PATCH KIDS", modern=True)
sc("""And there was the electronics store, where crowds gathered around the newest gadgets. The Sony Walkman, which let you carry your music anywhere. Boom boxes the size of suitcases. Atari and ColecoVision game consoles. And at the very end of January nineteen eighty-four, Apple introduced the Macintosh computer, with a famous television ad during the Super Bowl.""",
   "1980s Electronics Store televisions", "THE NEWEST GADGETS")

ch("The arcade")
sc("""For many kids, the best part of the mall was the arcade. Aladdin's Castle, Tilt, or Time Out. Dark rooms full of flashing lights and electronic sounds, where every game cost a quarter. The change machine on the wall turned your dollar bills into a stack of quarters, and they disappeared fast.""",
   "1980s Video Arcade games", "A QUARTER A GAME")
sc("""The games of nineteen eighty-four were legends. Pac-Man, Ms. Pac-Man, Donkey Kong, Galaga, Centipede, Frogger and Dragon's Lair. The best players drew a crowd. They put their initials on the high score screen. And a kid who could play Galaga for an hour on one quarter was famous at school on Monday.""",
   "Pac-Man Arcade cabinet", "PAC-MAN", modern=True)
sc("""Parents left younger kids at the arcade while they shopped. Older kids hung out there for hours. It was loud, dark and a little bit rough around the edges, and that was exactly why teenagers loved it.""",
   "1980s Arcade teenagers playing", "LOUD AND DARK")
sc("""Next door, there might be a photo booth. Four pictures for a dollar, printed in a strip a few minutes later. Friends crammed into the tiny booth, made silly faces, and split the strip. Many people still have those little strips tucked into old yearbooks and shoeboxes, the only photos they have of that afternoon.""",
   "1980s Photo Booth strip friends", "FOUR PICTURES FOR A DOLLAR")

ch("The food court")
sc("""By noon, everyone was hungry, and everyone headed to the food court. The food court was a new idea in the seventies and eighties. A big open area full of tables, surrounded by counters selling every kind of fast food. Pizza, tacos, Chinese food, hot dogs and hamburgers, all in one place.""",
   "1980s Food Court Mall", "THE FOOD COURT")
sc("""There was Orange Julius, with its frothy orange drink. Hot Dog on a Stick, where the employees wore those famous striped uniforms and tall hats. Sbarro for pizza. Chick-fil-A, which started in a mall in Atlanta. And the Great American Cookie Company, with giant cookies, and the smell of fresh pretzels drifting through the whole mall.""",
   "Orange Julius stand Mall", "ORANGE JULIUS")
sc("""Teenagers sat at the food court for hours, nursing one soda. They gossiped, flirted, made plans, and watched everyone go by. For a generation of kids, the food court was what the soda fountain had been to their parents. The place where everyone met.""",
   "1980s Teenagers Food Court table", "WHERE EVERYONE MET")
sc("""And the sweet smells were everywhere. Cinnabon opened its first store in a mall near Seattle in nineteen eighty-five, and the smell of its cinnamon rolls would soon fill malls across the country. There were candy stores selling jelly beans by the pound, made famous by President Reagan, who kept a jar of them on his desk.""",
   "1980s Candy Store jelly beans", "JELLY BEANS")

ch("Hanging out")
sc("""Hanging out at the mall was a national pastime. Parents felt it was safe. It was indoors, there were security guards, and nothing bad was supposed to happen at the mall. So kids were dropped off for whole afternoons. They walked laps, window shopped, and went nowhere in particular.""",
   "1980s Teenagers walking Mall", "HANGING OUT")
sc("""Kids called them mall rats. They had no money to spend, but they knew every store, every clerk and every bench. They knew which store had the cutest employees and which security guard would kick you out for sitting on the fountain. The mall was their neighborhood.""",
   "1980s Teenagers sitting bench Mall", "MALL RATS")
sc("""Teenagers had their first jobs at the mall too. Scooping ice cream, folding sweaters at the Gap, selling shoes at Foot Locker or working the counter at Hot Dog on a Stick. A sixteen-year-old in nineteen eighty-four earned the minimum wage of three thirty-five an hour. And you got an employee discount.""",
   "1980s Shoe Store Mall employee", "$3.35 AN HOUR")
sc("""And the mall had its own soundtrack. Soft music played from speakers in the ceiling, easy-listening versions of popular songs. Each store played its own music too, so walking down the corridor meant hearing a dozen songs at once. The splash of the fountain. The beep of the cash registers. The squeak of sneakers on the shiny tile floor.""",
   "1980s Mall interior shoppers", "THE SOUNDTRACK")

ch("The afternoon")
sc("""In the afternoon, there was a movie. Many malls had a movie theater with two to six screens. In the summer of nineteen eighty-four, it might have been Ghostbusters, Indiana Jones and the Temple of Doom, Gremlins or The Karate Kid. Tickets cost about three dollars and fifty cents.""",
   "1980s Movie Theater Mall marquee", "GHOSTBUSTERS")
sc("""Families came in the afternoon too. Mothers with strollers. Fathers looking at power tools at Sears. Grandparents resting on the benches. Little kids riding the coin-operated horses and rocket ships. On weekends, there might be a car show in the center court, a craft fair, or a school choir singing.""",
   "1980s Family shopping Mall stroller", "THE WHOLE FAMILY")
sc("""And at Christmas, the mall was magical. Giant decorations hung from the ceiling. Santa sat on a throne in the center court, and the line to see him stretched for an hour. Shoppers carried armloads of bags. And the sound of carols mixed with the splashing of the fountain.""",
   "Santa Claus children Christmas 1980s Mall", "CHRISTMAS AT THE MALL")

ch("Closing time")
sc("""By four o'clock, your feet hurt, your money was gone, and your mom was waiting by the fountain. You had a bag from the record store with one cassette in it, a Swatch you'd been saving for, and a story about who you saw at the food court. It had been a great day.""",
   "1980s Mall teenagers shopping bags", "YOUR MONEY WAS GONE")
sc("""At nine o'clock, the stores closed. The gates rolled down. The lights dimmed. The cleaning crews came out with their floor polishers. And in the empty parking lot, the last cars pulled away under the tall orange lights. Tomorrow, it would all start again.""",
   "1980s Mall parking lot night", "THE GATES ROLLED DOWN")

ch("What happened")
sc("""So what happened to the mall? In the nineties and two thousands, things began to change. Big-box stores like Walmart and Target offered lower prices. Outlet malls and strip centers grew. Then came online shopping. Amazon, founded in nineteen ninety-four, made it possible to buy almost anything without leaving home.""",
   "1990s Big Box store", "ONLINE SHOPPING", modern=True)
sc("""The anchor stores began to close. Sears, J.C. Penney and Macy's shut hundreds of locations. When an anchor closed, the smaller stores lost their customers too. Many malls fell into decline. Today, hundreds of American malls are dead or dying, with empty storefronts, dry fountains and silent food courts.""",
   "closed Shopping Mall empty", "DEAD MALLS", modern=True)
sc("""Some malls have been torn down and replaced with apartments, offices or outdoor shopping centers. Some have become churches, schools or medical centers. Photographers travel the country taking pictures of abandoned malls, and people watch videos of them online, feeling a strange nostalgia for a place that once felt so ordinary.""",
   "abandoned Shopping Mall interior", "A STRANGE NOSTALGIA", modern=True)

ch("The America we lost")
sc("""What did we lose? Not just stores. We lost a place where the whole community gathered, under one roof, on a Saturday afternoon. Teenagers, parents, grandparents and toddlers, all in the same place at the same time. Today, we mostly shop alone, on our phones.""",
   "1980s Shopping Mall crowd people", "UNDER ONE ROOF")
sc("""If you were a teenager in nineteen eighty-four, you remember. The Orange Julius. The arcade. The record store. The fountain full of pennies. Your friends, your feathered hair and your Walkman. The mall was your world, and for a few years, it was everybody's.""",
   "Teenagers Shopping Mall 1980s", "IT WAS YOUR WORLD", modern=True)
sc("""So tell us in the comments. What was the name of your mall? What was your favorite store, and what did you always eat at the food court? Did you have a job at the mall? We read every comment. Next time, we're looking at what it meant to turn thirty in nineteen seventy-nine. Thank you for spending this time with me.""",
   "1980s Shopping Mall sign", "WHAT WAS YOUR MALL?")

save("video37", "Saturday at the Mall in 1984: The America We Lost", [
    "Growth in the number of U.S. shopping centers in the 1980s: International Council of Shopping Centers",
    "1984 best-selling albums (Thriller, Purple Rain, Born in the U.S.A.): Billboard; RIAA",
    "Transformers toy line launched in the U.S. in 1984: Hasbro",
    "Cabbage Patch Kids Christmas 1983 shortages: The New York Times; The Strong National Museum of Play",
    "Chick-fil-A's first restaurant in a mall, Greenbriar Mall, Atlanta, 1967: Chick-fil-A",
    "Federal minimum wage $3.35 an hour (1981-1990): U.S. Department of Labor",
    "Average U.S. movie ticket about $3.36 in 1984: National Association of Theatre Owners",
    "Amazon founded in 1994: Amazon.com",
], "angle 1 · a place and a time", minutes=(12, 14.5))
