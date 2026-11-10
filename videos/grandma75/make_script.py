import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 75 · ANGLE TEST: disguise story (rich grandmother poses as a poor woman to test her grandson's bride)
# Model from the 10/11 research: "Billionaire Bank Owner Poses As A Beggar To Test Grandson's Bride" (3.4M) and "Billionaire Mother Disguised As A Nobody" (2.6M).
# Grandma Ruth: born 1944 in Mansfield, Ohio; best friend Evelyn (fictional), owner of a bakery chain.

sc("""Sweetheart, my best friend Evelyn owned forty-two bakeries across Ohio. She was worth more money than this whole town put together. And two weeks before Christmas, I watched her put on a torn coat from the church rummage sale, rub coal dust on her cheeks, and walk into the fanciest restaurant in Columbus looking like a woman who hadn't eaten in three days.""",
   "elderly woman in torn coat at restaurant door", "SHE WAS WORTH MILLIONS")
sc("""She was going to meet the girl her only grandson wanted to marry. And the girl had no idea who she was. Tonight I'm going to tell you exactly what happened at that table, what the bride said when she thought nobody important was listening, and the surprise at the wedding that made three hundred people stand up. Stay with me, honey, because nobody saw that ending coming. Not even me.""",
   "elegant restaurant table Christmas candles", "SHE HAD NO IDEA")

ch("Evelyn")
sc("""Evelyn and I grew up two houses apart on Elm Street. Her family was even poorer than mine. Her father left when she was six, and her mother cleaned houses. In nineteen sixty-one, with eighty dollars and her mother's bread recipe, Evelyn opened a little bakery on Main Street in Mansfield. By the time she was fifty, there were forty-two of them.""",
   "1960s small town bakery storefront", "EIGHTY DOLLARS AND A RECIPE")
sc("""But she never changed, honey. She drove a twelve-year-old Buick. She clipped coupons. She bought her dresses at Sears. And she always said, Ruthie, money shows you who people really are. Most people never find out, because they never have any. I find out every single day. That's what money did to her. It made her suspicious of everybody who smiled at her.""",
   "old Buick car in driveway", "MONEY SHOWS WHO PEOPLE ARE")
sc("""Her only grandson was Michael. His parents died in a car accident when he was nine, and Evelyn raised him herself. He was a good boy, sweetheart, a quiet, gentle boy who became a schoolteacher. And in the fall of two thousand three, he brought home a girl named Brittany, beautiful, blonde, from a wealthy family in Cincinnati. And they were engaged by Thanksgiving.""",
   "young engaged couple autumn", "ENGAGED BY THANKSGIVING")

ch("The plan")
sc("""Michael had never told Brittany about his grandmother's money. Evelyn had asked him not to, since he was a boy. As far as Brittany knew, Michael was a teacher, raised by a grandma who worked at a bakery. And something bothered Evelyn. Brittany had been sweet as pie to Michael's face, but Evelyn had noticed how she looked at his old car and his little apartment.""",
   "young woman looking at old car disappointed", "SOMETHING BOTHERED HER")
sc("""So one night in December, Evelyn sat at my kitchen table and told me her plan. I said, Evelyn, that's crazy. That's a terrible trick to play on a girl. And she said, Ruthie, I'm seventy-nine years old. When I die, that boy gets everything. Forty-two bakeries and every penny. I have to know who he's marrying. And I need you to help me. In a minute I'll tell you what my part was, and why I almost said no.""",
   "two elderly women at kitchen table night", "I HAVE TO KNOW")
sc("""Michael was taking Brittany to dinner at the Fairmont, the fanciest restaurant in Columbus, for her birthday. He'd saved for two months. Evelyn would come in from the street, dressed as a poor old woman, and ask to sit down for a minute because she was cold. She'd pretend she didn't know Michael. And my job was to sit at the next table and watch Brittany's face.""",
   "fancy restaurant dining room Christmas tree", "MY JOB WAS TO WATCH")
sc("""And Michael was in on it, honey. He hated it, but he loved his grandmother, and he agreed. He said, Grandma, you'll see. She's wonderful. You'll feel terrible. And Evelyn said, I hope so, sweetheart. I truly hope so. I've never wanted to be wrong so much in my life.""",
   "young man worried talking to grandmother", "YOU'LL FEEL TERRIBLE")

ch("The restaurant")
sc("""That night, it was sleeting in Columbus. I sat at a little table by the window with a cup of coffee I couldn't drink. At seven fifteen, Michael and Brittany were seated at the next table. She was in a white dress with a fur stole, and she complained about the table, then the bread, then the waiter. Michael just smiled and held her hand.""",
   "woman in white dress complaining to waiter", "SHE COMPLAINED ABOUT EVERYTHING")
sc("""If you're enjoying Grandma's story, tap the like button for me, sweetheart. It helps more people find these stories. At seven thirty, the front door opened, and a cold wind came in, and Evelyn walked in. I almost didn't recognize her myself. Torn brown coat. A scarf over her hair. Old men's boots soaked through. She shuffled right up to their table and put a shaking hand on the back of an empty chair.""",
   "poor elderly woman in torn coat restaurant", "I ALMOST DIDN'T KNOW HER")
sc("""She said, very quietly, excuse me, young people. I'm so sorry. It's very cold outside. Could an old woman sit down for just a minute and get warm? I won't bother you. Michael started to stand up, the way he'd been raised, to pull out the chair. And Brittany put her hand flat on his arm, and pushed him back down into his seat.""",
   "hand pushing man back into chair", "SHE PUSHED HIM DOWN")

ch("What she said")
sc("""Brittany didn't even look at Evelyn's face. She looked at the boots, dripping on the carpet. And she said, loud enough for the next three tables to hear, are you serious? This is a private dinner. Then she waved at the waiter and said, excuse me, can somebody get this woman out of here? She's dripping on everything, and she smells.""",
   "rich young woman pointing angrily", "GET HER OUT OF HERE")
sc("""Evelyn didn't move, honey. She said, just a minute, dear. My feet are frozen. And Brittany laughed. She actually laughed, and she said to Michael, this is why I told you we should've gone to the club. They let anybody in here. Then she turned to Evelyn and said, people like you should be at a shelter, not bothering people at dinner. Don't you have any shame?""",
   "woman laughing cruelly at dinner table", "DON'T YOU HAVE ANY SHAME?")
sc("""I watched Michael's face, sweetheart. I watched it break. And then Brittany did the thing I've never forgotten. She picked up the dinner roll from her bread plate, the one she'd complained about, and she held it out to Evelyn between two fingers, like you'd hold something out to a stray dog, and she said, here. Now go.""",
   "hand holding out bread roll coldly", "HERE. NOW GO.")
sc("""Evelyn took the roll. She said, thank you, dear. God bless you. And she turned and shuffled out the door, back into the sleet. The waiter, a young man named Carlos, ran out after her with his own coat and a bowl of soup in a to-go cup. I saw him through the window, putting his coat around her shoulders. Remember Carlos, honey. He comes back.""",
   "waiter giving coat to old woman in sleet", "REMEMBER THE WAITER")

ch("The car")
sc("""I found Evelyn around the corner, sitting in my car with the heater running, still holding that dinner roll. She wasn't crying. That's what scared me. She just sat there and said, well, Ruthie. Now I know. And then she said, the worst part isn't what she said to me. It's that Michael is going to have to choose. And I raised him to be kind, not to be strong.""",
   "elderly woman sitting in car at night", "NOW I KNOW")
sc("""So far, the plan, the dinner, the dinner roll, and the waiter. Now here's what everybody asks me. What did Michael do? Because he didn't say anything at that table, sweetheart. He just sat there and finished the dinner. He paid. He drove Brittany home. And Evelyn didn't hear a word from him for nine days. Nine days, and the wedding was set for New Year's Eve.""",
   "phone on table silent waiting", "NINE DAYS OF SILENCE")

sc("""Those nine days were the longest of Evelyn's life, honey. She didn't sleep. She called me every night at eleven o'clock. She said, what if I've lost him, Ruthie? What if he's angry at me and not at her? What if he marries her anyway, just to show me? I'd rather lose every bakery I own than lose that boy. And for the first time in sixty years, I heard Evelyn sound afraid.""",
   "elderly woman on phone late at night", "WHAT IF I'VE LOST HIM?")
ch("The wedding")
sc("""Evelyn thought the wedding was off. Then the invitation came. White and gold, three hundred guests, at the biggest church in Cincinnati, paid for by Brittany's father. And on the back, in Michael's handwriting, it said, Grandma, please come. Wear your best dress. Trust me. Evelyn called me and said, Ruthie, I don't understand that boy. And I said, I think you do.""",
   "wedding invitation white and gold", "TRUST ME")
sc("""On New Year's Eve, Evelyn and I sat in the second row. She wore her navy blue church dress from Sears. Brittany's mother looked her up and down and asked if she was with the caterers. The church was full of flowers and candles. Brittany came down the aisle in a dress that cost more than my house. And Michael stood at the front, white as a sheet.""",
   "grand church wedding aisle candles", "WHITE AS A SHEET")
sc("""When the minister asked if anybody had a reason these two should not be married, the church went quiet, the way it always does, for just a second. And Michael said, I do. Three hundred people gasped. Brittany laughed nervously and said, Michael, what are you doing? And Michael turned around, and he looked straight down the aisle, at the back door of the church.""",
   "groom turning to face church crowd", "I DO HAVE A REASON")

ch("The surprise")
sc("""And through the back door came a little old woman in a torn brown coat, a scarf over her hair, and wet men's boots. My heart stopped, honey, because Evelyn was sitting right next to me. It wasn't Evelyn. It was a woman from the shelter on Fourth Street, a real one, named Mrs. Lottie Brown, and she walked slowly up that long aisle, while three hundred people stared.""",
   "poor old woman walking up church aisle", "IT WASN'T EVELYN")
sc("""Michael said, Brittany, two weeks ago, a woman dressed like this asked to sit at our table for one minute, and you called her trash and threw her a roll. This is Mrs. Brown. She's lived on the street for six years. I've been bringing her dinner every night since that night, because somebody should have. Then he said, and the woman at our table was my grandmother.""",
   "groom speaking at altar shocked bride", "IT WAS MY GRANDMOTHER")
sc("""And he pointed right at Evelyn. Everybody turned around. Brittany's mother, the one who'd asked about the caterers, went pale. Michael said, my grandmother owns Evelyn's Bakeries. All forty-two of them. I never told you, because I wanted somebody who loved me with nothing. And now I know you don't. I'm sorry. I can't marry you. Then he walked down the aisle and took Mrs. Brown's arm.""",
   "church guests turning around shocked", "ALL FORTY-TWO OF THEM")

ch("What happened after")
sc("""Brittany screamed, honey. She screamed that it was a trick, and that it wasn't fair, and that she'd have been nice if she had known. And that was the whole point, wasn't it? She would have been nice if she'd known. Her father had to walk her out the side door. The three hundred guests were still standing there, and Evelyn stood up and said, well, the food's paid for. Let's eat.""",
   "bride being led out side door church", "IF SHE HAD KNOWN")
sc("""Michael didn't marry for four more years. And when he did, it was a girl he met volunteering at that same shelter on Fourth Street, a nurse named Ana, whose family came from Mexico with nothing. The first time she met Evelyn, Evelyn wore her torn brown coat on purpose. Ana took one look at her, took off her own scarf, and wrapped it around Evelyn's neck.""",
   "young nurse wrapping scarf around old woman", "SHE TOOK OFF HER SCARF")
sc("""And Carlos, the waiter, the one who ran out in the sleet with his coat? Evelyn found him the week after the dinner. Today, sweetheart, Carlos runs eleven of Evelyn's bakeries. Mrs. Lottie Brown lived the last eight years of her life in a little apartment above the Mansfield bakery, rent free, and she frosted the Christmas cookies every December until she was ninety.""",
   "bakery manager smiling Christmas cookies", "HE RUNS ELEVEN BAKERIES")

ch("Grandma's lesson")
sc("""Evelyn passed in twenty fourteen. At her funeral, Michael told that whole story, and he said, my grandmother taught me that you find out who someone is by how they treat a person who can do nothing for them. I've thought about that every day since, honey. Not how people treat the boss. How they treat the waiter, the cleaning lady, the old woman in wet boots.""",
   "elderly woman portrait in bakery", "HOW THEY TREAT THE WAITER")
sc("""Tell me in the comments, sweetheart. Was Evelyn right to test her, or was it too cruel? Be honest with Grandma. I go back and forth myself. There are more of my family's stories in the playlist right there on your screen, and I'll see you in the next one. Good night, honey.""",
   "warm bakery window Christmas night", "WAS SHE RIGHT?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma75", "Rich Grandma Dressed as a BEGGAR to Test Her Grandson's Bride",
     ["Grandma Ruth is a fictional narrator, and this is a fictional story. Evelyn, Michael, Brittany and the bakeries are invented characters."],
     "disguise test story", minutes=(13, 14.5), voice="en_US-lessac-high")
