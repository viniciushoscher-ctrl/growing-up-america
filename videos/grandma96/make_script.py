import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 96 · ANGLE: kindness with family conflict (gives her late mother's house to a homeless family; her children are furious)

sc("""Sweetheart, when my mother died, she left me her little house on Elm Street, the house I grew up in. My children wanted me to sell it. It was worth about ninety thousand dollars. Instead, on Christmas Eve, I handed the keys to a homeless family I had met in a church parking lot three weeks before. My son called me a foolish old woman and didn't speak to me for months.""",
   "small old house on Elm Street in snow", "I GAVE AWAY THE HOUSE")
sc("""Tonight I'm going to tell you how I met that family, what my children said at Christmas dinner, and what that house looked like when my son finally came to see it, three years later. Stay with me, honey, because my son said something on that front porch that I've written in the front of my Bible.""",
   "son standing on porch of small house", "WHAT MY SON SAID")

ch("Mother's house")
sc("""My mother, Dorothy, lived in that little white house on Elm Street for sixty-one years. It's where I learned to walk, where Danny and I fought over the bathroom, where my father hung his hat every night at six o'clock. When she passed in nineteen eighty-nine, the house stood empty for a year, honey, because I couldn't bring myself to do anything with it. I'd go sit in her kitchen sometimes, just to smell it.""",
   "empty old kitchen with sunlight", "SIXTY-ONE YEARS")
sc("""My children were grown by then, with houses and mortgages and children of their own. And they had plans for Grandma's house. Sell it, they said. Ninety thousand dollars. Split it, and it would pay off Mark's car loan, and Susan's credit cards, and maybe start the grandchildren's college funds. They weren't wrong, sweetheart. It made sense. In a minute I'll tell you why I couldn't do it.""",
   "family discussing at kitchen table papers", "IT MADE SENSE")
sc("""Harold left it up to me. He said, Ruthie, it's your mother's house. Whatever you decide, I'll back you. And I prayed about it, honey. I really did. For a whole year, I prayed. And the answer came in the strangest place. In the parking lot of First Methodist, on a Wednesday night in December, at the soup supper.""",
   "church parking lot at night snow", "THE ANSWER CAME")

ch("The family in the car")
sc("""Every Wednesday in winter, our church served a free soup supper in the basement. I ladled the soup. And one night, I noticed a car in the far corner of the parking lot, an old brown station wagon, with fogged-up windows. It was there the next Wednesday too. And the next. And the third Wednesday, I took a bowl of soup out to it in the snow and tapped on the glass.""",
   "old station wagon with fogged windows in lot", "FOGGED-UP WINDOWS")
sc("""Inside were five people, honey. A man named Luis, his wife Rosa, and three children, the littlest about two, all bundled up in blankets in the back. They'd been living in that car for six weeks. Luis had worked at a factory in Toledo that closed. They'd come to Mansfield because a cousin promised him a job, and the job fell through, and the cousin disappeared. And their money ran out.""",
   "family bundled in blankets inside car", "SIX WEEKS IN A CAR")
sc("""If you're enjoying Grandma's story, tap the like button for me, sweetheart. It helps more people find these stories. I asked Rosa where they went when it got really cold. She said, we run the engine for twenty minutes every hour, when we have gas. And we pray. The two-year-old was coughing. That deep, rattly cough. I stood there in the snow holding that soup bowl, and I thought about my mother's empty house, eleven blocks away.""",
   "small child coughing wrapped in blanket", "WHEN WE HAVE GAS")

sc("""That night, I couldn't sleep, honey. I lay awake listening to the wind and thinking about that cough. At two in the morning, I got up, put on my coat, and drove back to the church parking lot with a thermos of hot cocoa and every blanket from our linen closet. The windows were dark. I left it all on the hood of their car, with a note that said, from a friend.""",
   "thermos and blankets on car hood at night", "FROM A FRIEND")
ch("The keys")
sc("""I didn't say anything to them that night. I went home and told Harold, and he said, Ruthie, I've been waiting a year for you to know what to do with that house. I think you know now. So the next morning, I went to Elm Street, and I turned the heat on, and I scrubbed the kitchen. The ladies from church brought sheets and towels and groceries. The men's group fixed the furnace.""",
   "women cleaning old kitchen together", "I TURNED THE HEAT ON")
sc("""On Christmas Eve, I drove to the church parking lot, and I tapped on that fogged-up window, and I handed Rosa a set of keys on my mother's old key ring, with a little brass bell on it. I said, there's a house on Elm Street that's been waiting for a family. It's warm. There's a turkey in the icebox. And it's yours. Rosa looked at those keys and didn't understand.""",
   "elderly hand giving old keys with bell", "IT'S YOURS")
sc("""We drove them there, honey. When Luis walked through that front door, into my mother's warm living room, with a little Christmas tree the church youth group had decorated in the corner, he got down on his knees on my mother's rug. Just went right down. The children ran from room to room screaming, there's a bathtub! There's a bathtub! Rosa held the two-year-old and cried and cried. And Luis's oldest boy, who was nine, came and stood next to me, and took my hand, and said very seriously, ma'am, I'll take good care of it. I promise. And he did, honey. For thirty years.""",
   "man kneeling in warm living room by Christmas tree", "THERE'S A BATHTUB!")

sc("""That first night in the house, Rosa told me later, none of them could sleep either. The children kept getting up to turn the bathroom light on and off, and run the warm water, just to see it work. And at midnight, Luis went out on the front porch in the snow and stood there for an hour, looking at the street. She asked him what he was doing. He said, I'm making sure it's real.""",
   "man standing on porch at midnight snow", "MAKING SURE IT'S REAL")
ch("Christmas dinner")
sc("""So far, the house, the car, the soup, and the keys. The next day was Christmas, and my children came for dinner, and I told them. I thought they'd understand, sweetheart. They didn't. My son Mark set down his fork and said, Mom, you gave Grandma's house to strangers? To people you met in a parking lot? Do you know how much that house is worth?""",
   "son angry at Christmas dinner table", "TO STRANGERS?")
sc("""And then it got worse, honey. Mark said, they'll trash it. They'll sell everything in it. People like that don't take care of things. You're a foolish old woman, and Dad shouldn't have let you. And he got up from the table and took his family home before the pie. Susan didn't yell. But she said, Mom, that was our inheritance too. You should have asked us. And that one hurt more.""",
   "family leaving dinner table angry", "A FOOLISH OLD WOMAN")
sc("""I want to be fair to my children, sweetheart. They weren't greedy people. They were tired people, with bills, who'd been counting on that money. And maybe I should have asked them. I've thought about that a lot. But I knew what they'd say. And I knew a two-year-old was coughing in a car. Sometimes you can't wait for a vote.""",
   "elderly woman alone at kitchen table thinking", "NO TIME FOR A VOTE")

ch("The house")
sc("""I didn't actually give them the house that first day, honey. I rented it to them for one dollar a year. Harold's idea, so it was all legal and proper. And I told Luis, when you get on your feet, we'll talk about the rest. Luis found work in January at a body shop. Rosa started cleaning houses, and then at the hospital. The children went to Lincoln Elementary, where I used to knit mittens.""",
   "man working at auto body shop", "ONE DOLLAR A YEAR")
sc("""And here's what they did with my mother's house, sweetheart. Luis painted the whole outside, white, the way it was when I was a girl. He fixed the porch steps my father always meant to fix. Rosa planted my mother's rose bushes again, red ones, along the front fence. Every spring, they sent me a picture of those roses. And every Christmas, the youngest delivered a plate of Rosa's tamales to my door.""",
   "freshly painted white house with red roses", "MY MOTHER'S ROSES")

sc("""And the neighbors, sweetheart. At first, some of them weren't happy. One man on Elm Street called the city twice to complain about strangers in Dorothy's house. But that first spring, Luis shoveled every walk on the block before dawn after a big snow. Rosa took soup to the old widower next door when he had pneumonia. By summer, that same man who'd complained was teaching Luis's boy to fish.""",
   "man shoveling neighbor's sidewalk at dawn", "THE NEIGHBORS")
ch("Three years later")
sc("""Mark didn't come to that house for three years. He came to my house at Christmas, but things were stiff between us, and we never talked about it. Then, in the third year, his own company laid him off. Twenty-two years, honey, and they let him go two weeks before Thanksgiving. He came to my house white as a sheet and said, Mom, I don't know what to do. We might lose the house.""",
   "middle aged man devastated at mother's door", "WE MIGHT LOSE THE HOUSE")
sc("""Somehow, sweetheart, the whole town knew within a week. And the first person to show up at Mark's door wasn't anybody from his church, or his work, or his neighborhood. It was Luis. With a casserole from Rosa, and a job offer. He'd saved enough to buy the body shop where he worked, and he needed a manager who knew numbers. Mark had been an accountant for twenty-two years.""",
   "man with casserole at door offering job", "IT WAS LUIS")

ch("The porch")
sc("""That Christmas Eve, Mark asked me to drive him to Elm Street. He hadn't seen the house since Grandma died. We pulled up, and he looked at the fresh white paint, and the fixed steps, and the red roses on the fence, buried in snow. And Luis's children ran out on the porch waving. And my son sat in my car and cried like a little boy.""",
   "man crying in car looking at white house", "HE CRIED IN MY CAR")
sc("""Then he walked up onto that porch, and he looked around, and he said the thing I've written in the front of my Bible. He said, Mom, I said they'd trash it. They made it more Grandma's house than it ever was when it was empty. I was the one who was poor. I just had more money. And then he hugged Luis on that porch, and they've been like brothers ever since.""",
   "two men hugging on snowy porch", "I WAS THE POOR ONE")

ch("Grandma's lesson")
sc("""Luis and Rosa bought that house from me for one dollar, honey, the fifth Christmas. I signed the deed at my kitchen table. Today, their oldest son is a nurse, and their daughter teaches second grade, and the little one with the cough is in law school. And Mark still manages that body shop. He says it's the best job he ever had.""",
   "deed signed at kitchen table one dollar", "SOLD FOR ONE DOLLAR")
sc("""Here's what I want you to remember, sweetheart. An empty house isn't an inheritance. A family is. Tell me in the comments, honey, would you have given away that house? Be honest with Grandma. There are more of my family's stories in the playlist right there on your screen, and I'll see you in the next one. Good night. Merry Christmas.""",
   "warm lit house on Elm Street Christmas night", "WOULD YOU HAVE DONE IT?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma96", "I Gave My Mother's House to a Homeless Family. My Son Was FURIOUS",
     ["Grandma Ruth is a fictional narrator, and this is a fictional story. All names are invented."],
     "kindness with family conflict story", minutes=(12, 14.5), voice="en_US-lessac-high")
