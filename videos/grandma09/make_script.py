import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 09 · angle 3 (a walk through a place that disappeared) · Billionaires Histories, new format
# Christmas Downtown, 1955. Here's What It Was Really Like
# Grandma Ruth: born 1944 in Mansfield, Ohio (11 in 1955); brother Danny born 1947; Grandma Pearl. Every product, price and date is real.

sc("""Sweetheart, close your eyes. It's the Saturday after Thanksgiving, nineteen fifty-five. I'm eleven years old. It's snowing just a little, and I'm holding my mother's hand on the corner of Main Street in Mansfield, Ohio. And we're about to walk into a place that doesn't exist anymore. Downtown, at Christmas. Come with me.""",
   "1950s downtown main street Christmas snow shoppers", "CLOSE YOUR EYES")
sc("""You've only ever known the mall, or a box that comes to the door. So you can't know what it was like when the whole town came to the same few blocks, all at once, dressed up in their best, for one month a year. I'll take you store by store. And I'll tell you what everything cost, and what Santa said to me. And why my brother Danny got lost.""",
   "1950s crowded sidewalk downtown shoppers coats hats", "STORE BY STORE")

ch("Getting ready")
sc("""First, you didn't just go downtown, sweetheart. You got ready. My mother put on her good wool coat, her hat with the little feather and her gloves. White gloves in winter, can you imagine. Danny had to wear a tie, and he complained the entire bus ride. I wore my patent leather Mary Janes with white socks, even in the snow. My toes were frozen by noon. I didn't care.""",
   "1950s mother children dressed up coats gloves", "WHITE GLOVES")
sc("""We took the city bus, fifteen cents each, because my father had the car at the plant. The bus was so full of mothers with shopping bags that Danny had to sit on my lap. And when we got off downtown, the first thing you heard was the Salvation Army bell. A man in a uniform, ringing, next to his red kettle. My mother always gave me a dime to drop in.""",
   "1950s Salvation Army bell ringer kettle", "THE RED KETTLE")

ch("The windows")
sc("""Before we went in anywhere, we looked at the windows. Every big department store decorated its front windows for Christmas, and they kept it a secret until the day after Thanksgiving. Then they pulled the curtains. There was a crowd three deep on the sidewalk. Children were lifted up on their fathers' shoulders.""",
   "1950s department store Christmas window display crowd", "THE CURTAINS OPENED")
sc("""And inside those windows, sweetheart, everything moved. Little elves hammering toys. A train going around and around through cotton snow. Reindeer whose heads went up and down. A whole Santa's workshop, with a clock on the wall. I would press my nose on the glass until my mother pulled me away. Grown men stood there just as long as I did.""",
   "1950s animated Christmas window elves toys", "EVERYTHING MOVED")

ch("The parade")
sc("""The day after Thanksgiving there was always a parade, and that was how Santa came to town. The high school band, marching in the cold with their cheeks red. Floats made of chicken wire and paper napkins. The Shriners in their little cars. And at the very end, on a fire truck, with its siren going, Santa Claus himself, waving. And every child on Main Street screamed.""",
   "1950s Christmas parade Santa fire truck main street", "SANTA CAME BY FIRE TRUCK")
sc("""Then, when it got dark, the mayor threw a switch, and every light on Main Street came on at once. Big colored bulbs strung across the street from one side to the other, and a tall tree in the square. The whole crowd said ooh, all together, like one person. Sweetheart, I've seen fireworks since then, and nothing ever looked as good as those lights.""",
   "1950s main street Christmas lights strung night", "THE MAYOR THREW THE SWITCH")

ch("Inside the store")
sc("""Then the revolving door, and that warm air hit you, and that smell. Perfume from the cosmetics counter, roasted nuts and the floor wax. The ceiling was two stories high, with garlands hanging all the way down. And there was music, a lady playing Christmas carols on an organ on the mezzanine. Every year. I thought she lived there.""",
   "1950s department store interior Christmas decorations", "THE REVOLVING DOOR")
sc("""And to go upstairs, you took the elevator. Not a button. There was a lady in a uniform with white gloves, sitting on a little stool inside, and she ran it with a brass handle. She'd call out every floor. Second floor, ladies' coats and hats. Third floor, men's furnishings. Fourth floor, toys and Santa Claus. Every child in town knew the fourth floor.""",
   "1950s elevator operator woman uniform department store", "FOURTH FLOOR, TOYS")
sc("""Here's something you'll find funny. When you paid, the salesgirl didn't open a cash register. She put your money and the sales slip in a little metal tube and stuck it into a pipe in the wall. Whoosh. It shot off across the store, through the ceiling, to an office upstairs. And a minute later, thunk, it came back with your change. Pneumatic tubes. I thought it was magic.""",
   "pneumatic tube system department store cash", "WHOOSH")

ch("The toy floor")
sc("""Oh, the toy floor. Sweetheart, you can't imagine. There was a whole Lionel train layout on a table as big as this room, with mountains and tunnels and a little town with lights in the windows. The boys stood around it like it was church. A Lionel set cost about fifty dollars. That was two weeks of my father's pay. Most boys just looked.""",
   "1950s Lionel toy train display children", "THE LIONEL TRAINS")
sc("""That year, every boy in America wanted one thing. A coonskin cap. Davy Crockett was on Disneyland on television, and the song was on every radio. Davy, Davy Crockett, king of the wild frontier. Stores sold millions of those caps, and the price of raccoon fur went through the roof. Danny wore his to church until the minister asked him to take it off.""",
   "1950s boy coonskin cap Davy Crockett", "KING OF THE WILD FRONTIER")
sc("""For girls, it was dolls. Baby dolls that drank and wet, a bride doll in a white dress. And there was Mr. Potato Head, which back then came with only the parts. You had to use a real potato from your mother's kitchen. Silly Putty in a plastic egg, for a dollar. And a Slinky, walking down the store stairs, over and over, while a salesman made it look easy.""",
   "1950s girls dolls toy department store shelves", "A REAL POTATO")

ch("Santa Claus")
sc("""And then the line for Santa. It went all the way around the toy floor. An hour, sometimes more. Santa sat on a big red throne in a little cottage made of plywood, with fake snow on the roof. A helper in an elf costume took your picture with a flashbulb, pop, and you saw spots for ten minutes.""",
   "1950s department store Santa Claus children line", "THE LINE FOR SANTA")
sc("""When it was my turn, I climbed up and I asked Santa for a Toni doll, the one with the hair you could give a permanent. And for my father to stop working on Saturdays. Santa got quiet. Then he said, I'll see what I can do about the first one, sweetheart. The second one's harder. He smelled like peppermint and cigarettes. Years later I found out he was Mr. Reese from the hardware store.""",
   "1950s girl on Santa lap photograph", "SANTA GOT QUIET")
sc("""And right after Santa, they gave every child a little gift. A candy cane, or a coloring book, or a tiny box with a toy inside. Can you believe it? The store gave you a present just for coming. Danny got a whistle. My mother regretted that whistle for the rest of the day.""",
   "1950s children candy canes Christmas gift", "THE WHISTLE")

ch("Danny gets lost")
sc("""Now, Danny. He was eight that year. While my mother was looking at a pair of gloves for Grandma Pearl, he was right there, and then he wasn't. Just gone. My mother turned white. In those days, there were no cell phones, no cameras. Just a huge store with five floors, two thousand people, and an eight-year-old boy in a coonskin cap.""",
   "1950s crowded department store aisle shoppers", "HE WAS GONE")
sc("""A floorwalker came over, that's what they called the man in the suit who walked the floor and helped the customers. He went to a telephone on the wall, and a minute later, over the whole store, a voice said, will Mrs. Walter Miller please come to the toy department, your son is waiting for you at the trains. Of course he was. Where else would he be.""",
   "1950s department store manager suit telephone", "AT THE TRAINS")
sc("""My mother didn't spank him, which in nineteen fifty-five tells you how scared she was. She just held him so tight his cap fell off. And on the bus home, she held his hand the whole way, and she held mine, and she didn't let go of either of us until we got to Elm Street.""",
   "1950s mother hugging son relief", "SHE HELD HIM TIGHT")

ch("Lunch at the tea room")
sc("""But first, lunch. On the top floor, there was a tea room. White tablecloths, real silver, waitresses in black dresses with little white aprons. Ladies came downtown just to eat there. My mother ordered the chicken salad on a lettuce leaf, sixty-five cents. Danny and I had grilled cheese and a chocolate soda. It was the fanciest place I had ever been.""",
   "1950s department store tea room women lunch", "THE TEA ROOM")
sc("""And a lady came around to the tables modeling dresses, from the store, while you ate. She'd stop at your table and turn around, slowly, and tell you the price and which floor. My mother said that was how they got you. You'd finish your chicken salad and go straight down to the second floor with your pocketbook open.""",
   "1950s fashion model women dresses 1955", "THAT'S HOW THEY GOT YOU")

ch("My own shopping")
sc("""After lunch, my mother gave me one dollar of my own, to buy presents, and let me go into the Woolworth's by myself while she waited outside. A whole dollar. I walked up and down those wooden floors for half an hour, adding it up in my head. A handkerchief for my father, ten cents. A comb for Danny, five cents. That left eighty-five cents for my mother.""",
   "1950s Woolworth five and dime counter girl shopping", "ONE WHOLE DOLLAR")
sc("""And for my mother I bought a little blue bottle of Evening in Paris perfume. Every girl bought her mother Evening in Paris, it was the five-and-dime perfume. The lady at the counter wrapped it in tissue paper for free and tied it with a ribbon. My mother wore it to church every Sunday for a year, until the bottle was empty, and she kept the empty bottle on her dresser until she died.""",
   "1950s perfume counter woman gift wrapping", "EVENING IN PARIS")

ch("How we paid")
sc("""Now, how did we pay for Christmas? Not with a credit card, sweetheart. Most people didn't have one. My mother had been putting money in a Christmas Club at the bank since January. A dollar a week, and in November they gave you a check for fifty dollars. That was our whole Christmas. For four people, and something for Grandma Pearl.""",
   "1950s bank teller woman savings book", "THE CHRISTMAS CLUB")
sc("""For the big things, there was layaway. You picked out the toy in October, paid a little every week, and the store kept it in the back for you, with your name on a tag. And then my mother had her books of S and H Green Stamps. You got stamps at the grocery store, licked them into little books, and traded the books for a toaster. Our toaster cost my mother eight books of stamps.""",
   "1950s S&H Green Stamps books redemption", "GREEN STAMPS")

ch("Where it went")
sc("""We went downtown every Christmas for years. Then, little by little, it changed. Malls started opening out by the highways, with free parking and a roof over everything. The first big indoor mall opened in Minnesota in nineteen fifty-six. People liked not having to fight the snow. And one by one, the big stores downtown closed.""",
   "1950s shopping mall interior shoppers fountain", "THE MALLS")
sc("""Now, when I drive down Main Street, sweetheart, some of those buildings are still there. Some are offices. Some are empty, with paper over the windows. And I stand on the corner where I held my mother's hand, and I can still hear that bell. Whoosh, thunk, fourth floor, toys and Santa Claus.""",
   "empty downtown storefronts old buildings main street", "THE CORNER")
sc("""Tell me in the comments. What was the department store in your town called? Did you ride the elevator with the lady with the white gloves? I'd love to know. Goodnight, sweetheart. Grandma Ruth will be right here with another story tomorrow.""",
   "1950s downtown Christmas lights night street", "WHAT WAS YOURS CALLED?")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("grandma09", "Christmas Downtown, 1955. Here's What It Was Really Like",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Davy Crockett, King of the Wild Frontier, aired on ABC's Disneyland, December 1954 - February 1955; the coonskin cap craze of 1955.",
      "Mr. Potato Head, Hasbro, 1952: originally sold as parts for a real potato.",
      "Lamson pneumatic tube cash systems, used in department stores from the 1880s.",
      "Southdale Center, Edina, Minnesota, the first fully enclosed shopping mall in the US, opened October 1956.",
      "S&H Green Stamps trading stamps, Sperry & Hutchinson, from 1896.",
      "Evening in Paris perfume by Bourjois, a best-selling five-and-dime fragrance of the 1940s-50s.",
      "Christmas Club savings accounts, offered by US banks from the early 1900s."],
     "a walk through a place that disappeared", minutes=(12, 14.5), voice="en_US-lessac-high")
