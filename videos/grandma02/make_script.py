import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 02 · angle 2 (confession: things that are illegal or dangerous today) · Billionaires Histories, new format
# I'm 82. Things We Did as Kids That Would Get Your Parents ARRESTED Today
# Grandma Ruth is a narrated character: born in 1944 in Mansfield, Ohio. Every product, price and law is real.

sc("""Sit down, sweetheart, and don't tell your mother what I'm about to tell you. Because some of the things we did when I was a girl, well, today somebody would call the police. I'm not joking. Your mother would lose you to the county for half the things my mother did to me before lunch. And we thought it was just a normal Tuesday.""",
   "1950s grandmother telling story armchair", "DON'T TELL YOUR MOTHER")
sc("""I grew up in Mansfield, Ohio, in the nineteen fifties. I was born in forty-four, so by the time I was ten, the whole country was booming, and nobody, and I mean nobody, was worried about safety. We didn't even have the word. Let me count them off for you. You'll see.""",
   "1950s small town main street cars", "NOBODY WAS WORRIED")

ch("The car")
sc("""Number one. The car. Our Chevrolet had no seat belts. Not broken ones. None. They didn't even put them in most cars until nineteen sixty-four, and nobody had to wear them until the eighties. When Father stopped short, Mother's arm shot out across my chest. That was the seat belt. Her arm.""",
   "1950s family car chevrolet interior", "NO SEAT BELTS")
sc("""And the babies. Oh, honey. Babies rode on their mother's lap in the front seat. Or in a little canvas seat that hooked over the back of the bench, so the baby could see out the windshield. My brother Danny rode in one of those. It was made to keep him busy, not safe. Today that would be a crime in all fifty states.""",
   "1950s mother baby car front seat", "THE BABY SEAT")
sc("""In the summer we rode in the back of Uncle Frank's pickup truck. Six of us kids, sitting on the wheel wells, hair flying, all the way out to the county fair on Route thirty. Nobody held on to anything. We sang the whole way. If a policeman passed us, he waved.""",
   "1950s children riding back of pickup truck", "THE BACK OF THE TRUCK")
sc("""And on long trips Father smoked with all the windows rolled up. Mother too. The car would fill up blue, and Danny and I would draw faces in the smoke on the window. When we got carsick, Mother said it was the road.""",
   "1950s man smoking driving car", "WINDOWS UP")

ch("The smoke")
sc("""Which brings me to number two. Cigarettes. Everybody smoked, sweetheart. Everybody. Doctors smoked in the examining room. There were advertisements that said more doctors smoke Camels than any other cigarette. My teacher smoked at her desk during the spelling test. There were ashtrays on the airplane, in the hospital, in the church basement.""",
   "1950s doctor cigarette advertisement", "MORE DOCTORS SMOKE CAMELS")
sc("""And here is the part you won't believe. When I was nine, Father would give me a quarter and send me to Rexall Drugs to buy his Lucky Strikes. A pack cost about twenty-three cents. The man behind the counter knew whose girl I was, and he gave me the pack and two pennies change. Nobody asked a single question.""",
   "1950s drugstore counter cigarettes", "SENT TO BUY CIGARETTES")
sc("""We even had candy cigarettes. Little white sticks of sugar with a red tip, in a box that looked just like the real thing. We held them between our fingers and blew pretend smoke in the cold air. We were practicing, you see. And it worked. Half of my class was smoking by sixteen.""",
   "1950s children candy cigarettes", "CANDY CIGARETTES")

ch("Left alone")
sc("""Number three. They left us alone. All day. In the summer Mother opened the screen door after breakfast and said, go play, and be home when the street lights come on. That was the only rule. Nobody knew where we were for eight hours. No phone, no way to find us. And they didn't worry. They had laundry to do.""",
   "1950s children playing outside summer neighborhood", "HOME WHEN THE LIGHTS COME ON")
sc("""We played in the creek behind the rail yard. We climbed the water tower once, and I will never tell you how high. We played in a house that was being built, walking on the beams with no floor under us. When the workmen saw us, they didn't call anybody. They yelled, get down from there, and went back to their lunch.""",
   "1950s children playing construction site", "THE BEAMS")
sc("""And sweetheart, I started babysitting when I was eleven. Eleven years old, alone in a stranger's house with a baby and a toddler, until midnight. Fifty cents an hour. The parents went to the Elks Club and came home smelling of whiskey and drove the babysitter home themselves. Today they'd lose those children. Back then they were good neighbors.""",
   "1950s teenage girl babysitting", "BABYSITTING AT ELEVEN")
sc("""Mothers left babies outside the store in the carriage while they shopped. Just parked them on the sidewalk, in the sunshine, while they went into the A and P. And if you were a kid, you waited in the car. In July. With the windows cracked an inch. For an hour. That was called being good.""",
   "1950s baby carriage outside store sidewalk", "WAIT IN THE CAR")

ch("The fog truck")
sc("""Number four is the one that still gives me chills. Every summer evening a truck came down our street spraying a big white cloud for the mosquitoes. And we ran behind it. All the children did. We ran right into that fog, laughing, spinning, playing hide and seek inside it. It smelled sweet, like kerosene.""",
   "1950s DDT fog truck spraying street", "THE FOG TRUCK")
sc("""It was DDT, honey. They sprayed it on beaches, on children at summer camp, on cows. Mother put it on the shelves to keep the bugs off the flour. Then a woman named Rachel Carson wrote a book in nineteen sixty-two called Silent Spring, and she told everybody what it was doing. It was banned in this country in nineteen seventy-two. We had already breathed it for twenty years.""",
   "1950s DDT spraying children beach", "SILENT SPRING")
sc("""And the paint on my bedroom windowsill, the pretty pink one, that had lead in it. Gasoline had lead in it. Our thermometers had mercury, and when one broke, we rolled the little silver balls around on the kitchen table with our fingers. They were so beautiful. Like magic. Don't you ever touch one.""",
   "1950s child bedroom window", "THE SILVER BALLS")

ch("The shoe store")
sc("""Number five sounds made up, but I promise it's true. At Kobacker's shoe store downtown, they had a machine called a fluoroscope. You put your feet in a slot at the bottom, and you looked through a window on top, and you could see the bones of your toes wiggling inside your new shoes. Green and glowing.""",
   "1950s shoe fitting fluoroscope x-ray machine", "X-RAY SHOES")
sc("""It was an X-ray, sweetheart. A real one, with no lead apron, and no time limit. Danny and I would put our feet in it over and over while Mother tried on gloves. The salesman let us. It was a free show. They had thousands of those machines all over America, and most states didn't ban them until the late fifties.""",
   "1950s children shoe store", "OVER AND OVER")

ch("The toys")
sc("""Number six. The toys. Every boy on our street had a BB gun by the time he was nine. Danny got his Red Ryder for Christmas when he was eight, and he shot out the Pruitts' porch light the same afternoon. Father took the gun away for one week. One week. Then he gave it back and showed him how to aim properly.""",
   "1950s boy red ryder bb gun", "THE RED RYDER")
sc("""We had lawn darts, heavy metal spikes that you threw high up in the air and tried to land in a ring. We had chemistry sets with real chemicals, the kind that could burn a hole in the rug, and some of them had a little bit of uranium in them, for the atomic experiments. And for the Fourth of July, Uncle Frank bought a box of cherry bombs and let us light them ourselves.""",
   "1950s boy chemistry set", "REAL CHEMICALS")
sc("""We roller skated with metal skates that clamped onto your shoes with a key you wore around your neck. No helmets. Nobody had heard of a helmet that wasn't for a football player or a soldier. When you fell, you got a scab. When the scab came off, you fell again.""",
   "1950s children roller skates street", "THE SKATE KEY")

ch("School")
sc("""Number seven. School. The principal at our school kept a wooden paddle in his office, with holes drilled in it so it would swing faster. The boys got paddled for talking back. Nobody's parents complained. Most of the time, the parents said, good, and gave the boy a second one at home.""",
   "1950s school principal office", "THE PADDLE")
sc("""And I'll tell you something else. We had a teacher who told a girl in my class she was too stupid for high school, right in front of everybody. Her name was Betty, and she cried at her desk. Some things about the old days were good. That wasn't one of them. Remember that when people tell you everything was better.""",
   "1950s classroom girl crying desk", "THAT WASN'T GOOD")

ch("The doctor")
sc("""Number eight. The medicine. When Mother felt tired, the doctor gave her diet pills. They were amphetamines, honey, the same thing they'd arrest you for today. Half the mothers on our street took them, with their coffee, and cleaned the whole house by nine in the morning. They called them pep pills, like it was a vitamin.""",
   "1950s housewife pills medicine bottle", "PEP PILLS")
sc("""When I had a cough, Mother gave me a spoonful of syrup that had codeine in it, from the drugstore, no prescription. When I had a toothache, they rubbed whiskey on my gums. And when Danny couldn't sleep as a baby, Grandma Pearl put a drop of paregoric in his bottle. That was opium. In a baby bottle. And she was a churchgoing woman.""",
   "1950s vintage medicine bottles", "A DROP IN THE BOTTLE")

ch("Growing up")
sc("""Number nine. The rules for teenagers. In Ohio, when I turned eighteen in nineteen sixty-two, I could walk into a bar and buy a beer. It was a weak one, called three point two beer, but it was legal. And nobody checked anything. Some of the boys in my class had been buying it since fifteen, with a pencil mustache.""",
   "1960s teenagers diner soda fountain", "THREE POINT TWO")
sc("""People hitchhiked, sweetheart. Nice girls, too. You stood on the side of Route forty-two with your thumb out, and a farmer in a truck stopped, and you climbed in. I did it twice. Once to get home from Lake Erie when our ride left without us. I'm not proud of it. But I'd be lying if I said I was scared.""",
   "1950s hitchhiker roadside thumb", "THUMBS OUT")
sc("""And there was no drinking and driving law worth anything. The men drank three beers at the Legion and drove home. Our neighbor kept a bottle in his glove box and called it his road map. Of course people died. Too many. It took mothers marching in the nineteen-eighties to change that. Good for them.""",
   "1950s bar men drinking beer", "THE ROAD MAP")

ch("Why we lived")
sc("""So you're asking, Grandma, how did you live through all that? Well, honey, some of us didn't. I want to be honest with you. I knew a boy who died in the creek. I knew a girl who went through a windshield. We don't tell those stories at the reunion. That's the price we paid for all that freedom.""",
   "1950s memorial church small town", "SOME OF US DIDN'T")
sc("""But I'll tell you what we had. We had nerve. We fixed our own bikes. We settled our own fights. We knew every family on six blocks, and they knew us, and if I did something wrong on Elm Street, Mother heard about it before I got home on Maple. Nobody was watching us, and everybody was watching us. I don't know how else to say it.""",
   "1950s neighbors talking over fence", "EVERYBODY WAS WATCHING")
sc("""I'm glad you have seat belts, sweetheart. I'm glad nobody gives you pep pills. I really am. But sometimes I wish you could run behind a truck in the summer, without the poison, just once, and feel what it was like to be that free. Nobody knew where we were. And we were fine. Mostly.""",
   "1950s children running summer evening", "THAT FREE")
sc("""Now, which one surprised you most? Tell me, and tell me which ones your friends' grandparents did too. I bet there are some I forgot. And come back tomorrow, because I'll tell you about the store where I had my first job, the one with the lunch counter that isn't there anymore. Goodnight, sweetheart.""",
   "1950s house at night porch light", "GOODNIGHT, SWEETHEART")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("grandma02", "I'm 82. Things We Did as Kids That Would Get Your Parents ARRESTED Today",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Seat belts: front lap belts standard on US cars from 1964 (1965 model year); first state seat-belt law, New York 1984.",
      "'More doctors smoke Camels' campaign, R.J. Reynolds, 1946-1952.",
      "Rachel Carson, Silent Spring (1962); EPA cancellation of DDT, 1972.",
      "Shoe-fitting fluoroscopes: about 10,000 in US stores by the early 1950s; banned by most states by the late 1950s.",
      "Ohio allowed 18-20 year olds to buy 3.2 beer until 1988.",
      "Paregoric (camphorated tincture of opium) sold for infants in the mid-20th century.",
      "Mothers Against Drunk Driving founded 1980."],
     "confession: things that are illegal or dangerous today", minutes=(12, 14.5), voice="en_US-lessac-high")
