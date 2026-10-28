import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 05 · angle 2 (confession: things that are shocking or illegal today) · Billionaires Histories, new format
# I'm 82. What Every 1950s Housewife Had to Do Would Shock You Today
# Grandma Ruth: born 1944 in Mansfield, Ohio; her mother Dorothy was a 1950s housewife. Every law, product and price is real.

sc("""Sweetheart, you know what you asked me at dinner? You asked if your great-grandmother Dorothy had a job. And I laughed. Because she worked harder than anybody I have ever known. Fourteen hours a day, seven days a week, and nobody ever paid her one penny. She was a housewife in the nineteen fifties. And some of the things she had to do, well. You'd call a lawyer today.""",
   "1950s housewife portrait apron kitchen", "SHE NEVER GOT PAID")
sc("""I'm not saying this to complain about the old days. I'm saying it because nobody wrote it down. They wrote down the wars and the presidents. Nobody wrote down what my mother did between six in the morning and ten at night. So I'm going to tell you. Count them with me.""",
   "1950s suburban houses street morning", "NOBODY WROTE IT DOWN")

ch("The day")
sc("""Number one. The day. My mother got up at five-thirty, before anybody. She put the coffee on in the percolator, she made breakfast, she packed three lunch pails, and she ironed my father's shirt for that day, because you ironed every shirt, sweetheart. Every shirt, every sheet, every pillowcase, even the handkerchiefs. Tuesday was ironing day. It took the whole day.""",
   "1950s housewife ironing clothes", "TUESDAY WAS IRONING DAY")
sc("""Monday was wash day. We had a wringer washer in the basement. You filled it with a hose, you ran the clothes through two rollers to squeeze the water out, and if you weren't careful the rollers took your fingers too. Mother had a scar on her hand from it. Then you carried the wet basket up the stairs and hung everything on the line in the yard. Even in January. The sheets froze stiff as boards.""",
   "1950s wringer washing machine basement", "WASH DAY")
sc("""And the whole time, the house had to be perfect by five o'clock. Because at five-thirty, my father came home. And the magazines said, and I'm not making this up, that a good wife should freshen her makeup, put a ribbon in her hair, and have dinner hot on the table when her husband walks through the door. And never, ever complain to him about her day. His day was more important.""",
   "1950s housewife greeting husband door", "DINNER AT FIVE-THIRTY")

ch("The money")
sc("""Number two. The money. My mother had no money of her own. None. Every Friday my father gave her an allowance for the house. Thirty dollars. Out of that came the groceries, the milkman, our shoes, the church plate. If she wanted something for herself, a new pair of stockings, she had to save it from the grocery money a nickel at a time. She kept it in a coffee can behind the flour.""",
   "1950s woman counting money kitchen table", "THE COFFEE CAN")
sc("""And here's the part that shocks people. A married woman in those days couldn't get a credit card in her own name. Not in most places. The bank wanted her husband to sign. She couldn't take out a loan for a car without him. That didn't change until a law in nineteen seventy-four. My mother was fifty-three years old before she had a charge card with her own name on it. She framed the first bill.""",
   "1950s department store charge account counter", "HER OWN NAME")
sc("""And if she had wanted a job? Well. Many schools fired women teachers when they got married. Airlines fired stewardesses when they got married, or turned thirty-two. My mother had wanted to be a teacher her whole life. She gave it up the week she married my father. Nobody asked her if she minded. Nobody thought to.""",
   "1950s airline stewardess uniform", "FIRED FOR GETTING MARRIED")

ch("The doctor")
sc("""Number three. The doctor. When my mother was expecting my brother Danny, the doctor told her to keep smoking, because it would calm her nerves and keep the baby small. Keep the baby small, like that was a good thing. She smoked a pack a day the whole time. Every mother on our street did.""",
   "1950s pregnant woman smoking cigarette", "KEEP SMOKING")
sc("""And when the baby came, sweetheart, they put the mothers to sleep. It was called twilight sleep. They gave you a shot, and you woke up hours later with a baby, and you didn't remember any of it. Fathers weren't allowed in the room. They waited down the hall with a cigar. And then the mother stayed in the hospital for a whole week, flat on her back, and the nurses kept the babies in a nursery behind glass.""",
   "1950s hospital nursery babies window fathers", "TWILIGHT SLEEP")
sc("""And when she was tired, honey, or sad, which happened, the doctor gave her pills. Little yellow pills called Miltown, a tranquilizer. In nineteen fifty-six it was the best-selling drug in America. Then came the diet pills, which were speed. Half the mothers on Elm Street were taking one in the morning and one at night. They called it mother's little helper. Later there was a song about it.""",
   "1950s vintage pill bottles medicine cabinet", "MOTHER'S LITTLE HELPER")

ch("The kitchen")
sc("""Number four. The kitchen. Now, I'll be fair, the kitchen got easier in the fifties. In nineteen fifty-three a company called Swanson came out with the TV dinner. Turkey, cornbread dressing, peas and sweet potatoes, in an aluminum tray, for ninety-eight cents. The first year they sold ten million of them. My father refused to eat one. He said a man deserves a cooked meal. So Mother cooked.""",
   "1950s Swanson TV dinner tray", "NINETY-EIGHT CENTS")
sc("""And the food, sweetheart. You would not believe the food. Everything went into Jell-O. Lime Jell-O with shredded carrots. Lemon Jell-O with tuna fish and olives. A ring of tomato aspic with shrimp inside it, like a little aquarium. Mother made a molded salad for every church supper. It was considered elegant. I would not feed it to a dog today.""",
   "1950s jello salad mold recipe", "TUNA IN THE JELL-O")
sc("""We had no dishwasher. Mother washed every dish, every pot, three times a day, by hand, in the sink, with a bar of soap and a cloth. I dried. Danny was supposed to put them away, and he never did. And the kitchen floor was linoleum, and she waxed it on her knees every Saturday. Every Saturday. My knees hurt just remembering it.""",
   "1950s woman washing dishes kitchen sink", "ON HER KNEES")

ch("The rules")
sc("""Number five. The rules for how a lady looked. My mother never went downtown without a hat and white gloves. Never. Not to the bank, not to the dentist. She wore a girdle every single day of her life, even in August, even to hang the laundry. Rubber girdles, sweetheart, in Ohio in August. And stockings with a seam up the back that had to be perfectly straight.""",
   "1950s women hats white gloves shopping downtown", "HATS AND GLOVES")
sc("""And she could never wear trousers to church, or to town. A woman in pants downtown was talked about. Mother wore pedal pushers in the garden, and if the doorbell rang she ran upstairs and put on a skirt before she opened the door. I'm serious. I watched her do it for the Fuller Brush man.""",
   "1950s woman garden pedal pushers", "THE FULLER BRUSH MAN")

ch("The garden")
sc("""Every August, sweetheart, our kitchen turned into a factory. Canning season. Mother put up two hundred jars of tomatoes, green beans, peaches and pickles, so we'd have vegetables all winter. The big pressure canner rattled on the stove for days, and it was ninety degrees in that kitchen, and she was in a girdle and stockings. If you did it wrong, the jar could poison your family. She never once did it wrong.""",
   "1950s woman canning jars kitchen", "TWO HUNDRED JARS")
sc("""And she made our clothes. My dresses, Danny's shirts, the curtains, the aprons. She bought flour in cotton sacks with flowers printed on them, because the flour companies knew women would sew them into dresses. I wore flour sack dresses to school until I was ten. I thought they were beautiful. They were.""",
   "1950s feed sack dress girl", "FLOUR SACK DRESSES")

ch("The children")
sc("""And the children were all hers. My father never changed a diaper in his life. Not one. When we were bad, she spanked us with a wooden spoon, and the school principal had a paddle, and nobody thought twice. And if she needed to go to the store, she left the baby asleep in the crib and Danny and me in charge. I was seven. It was normal.""",
   "1950s mother children kitchen discipline", "THE WOODEN SPOON")

ch("The parties")
sc("""Number six. The parties. Now, this part was fun. The Tupperware party. A lady named Brownie Wise came up with it. Instead of selling those plastic bowls in stores, women sold them to each other, at parties in their living rooms. There was coffee and cake, and a game, and you burped the lid to show how it sealed. My mother went to a Tupperware party every month. It was the only night she went out without my father.""",
   "1950s Tupperware party women living room", "BURP THE LID")
sc("""And the Avon lady came to our door. Ding dong, Avon calling. She had a little case full of lipsticks and perfume samples, and she sat at our kitchen table for an hour. My mother bought the same Cotillion cologne every time, for a dollar and a quarter. And for that hour, she wasn't anybody's mother or anybody's wife. She was just a woman picking out a lipstick.""",
   "1950s Avon lady door to door cosmetics", "AVON CALLING")

ch("The law")
sc("""Number seven, and it's the worst one. The law. In those days, sweetheart, if a man hit his wife, most police called it a family matter. They'd come to the door and tell him to cool off, and leave. There was a house on our street where that happened. Everybody knew. Nobody said anything. That's not nostalgia, honey. That's the truth, and I want you to know it.""",
   "1950s police car small town street night", "A FAMILY MATTER")
sc("""And in some states a woman couldn't even sit on a jury. In Mississippi, women weren't allowed on juries until nineteen sixty-eight. And a woman couldn't be a bank officer, a firefighter, or a pilot for the big airlines. Not because it was against the law. Because nobody would hire her. That was just how the world was. Until women changed it.""",
   "1950s courtroom jury men", "NOT ON THE JURY")

ch("The change")
sc("""In nineteen sixty-three a woman named Betty Friedan wrote a book called The Feminine Mystique. It said what all those women were feeling and nobody had words for. That being a perfect wife in a perfect kitchen wasn't enough, for some of them. My mother read it in secret. She hid it under the mattress. I found it there when I was nineteen.""",
   "1960s woman reading book bedroom", "THE BOOK UNDER THE MATTRESS")
sc("""She never said a word to me about it. But that fall, she signed up for a night class at the college. Just one class. Then another. In nineteen sixty-nine, when she was forty-eight years old, my mother finally got her teaching certificate. She taught third grade for twelve years. Mrs. Dorothy Miller. The children adored her.""",
   "1960s teacher classroom children", "MRS. DOROTHY MILLER")

ch("What I think")
sc("""So when people tell you that everything was better back then, sweetheart, you remember your great-grandmother on her knees on that kitchen floor. Some things were better. The neighbors were closer, the families sat down together, and nobody was staring at a phone. But some things were wrong. And the women who lived through it were the bravest people I ever knew.""",
   "1950s women neighbors porch talking", "THE BRAVEST PEOPLE")
sc("""Now tell me, which one surprised you most? And ask your own grandmother which of these she remembers. I bet she has stories of her own. Write them in the comments, I read every one. Come back tomorrow. Goodnight, sweetheart.""",
   "1950s house at night porch light", "GOODNIGHT, SWEETHEART")

for s in S:  # documentary look: four photos per scene and the six rotating camera moves
    s["cuts"], s["moves"] = 4, True

save("grandma05", "I'm 82. What Every 1950s Housewife Had to Do Would Shock You Today",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Equal Credit Opportunity Act, 1974: lenders may no longer refuse credit on the basis of sex or marital status.",
      "Swanson TV dinner introduced 1953 at 98 cents; about 10 million sold in the first year.",
      "Miltown (meprobamate) approved 1955; best-selling prescription drug in the US by 1956-57.",
      "Tupperware home parties built by Brownie Wise from 1951.",
      "'Ding dong, Avon calling' advertising slogan, from 1954.",
      "Betty Friedan, The Feminine Mystique (1963).",
      "Mississippi allowed women on juries in 1968, the last US state to do so."],
     "confession: things that are shocking or illegal today", minutes=(12, 14.5), voice="en_US-lessac-high")
