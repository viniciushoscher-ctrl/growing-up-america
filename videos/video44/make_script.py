import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 44 · angle 2 (a stage of life, a teenage girl's world, room by room) · afternoon slot · day 15
# If You Were a Teenage Girl in 1965, This Was Your Life

sc("""If you were a teenage girl in nineteen sixty-five, you were living in one of the most exciting moments in American history to be young. The Beatles were on the radio. Skirts were getting shorter. Your mother had grown up thinking her only future was marriage, but you were starting to wonder if there might be more. And the whole world seemed to be changing right in front of you.""",
   "1960s teenage girls laughing", "SIXTEEN IN 1965")
sc("""In nineteen sixty-five, there were more teenagers in America than ever before. The oldest baby boomers were turning nineteen. High schools were packed. Teen magazines, record companies, clothing stores and cosmetic brands were all chasing teenage girls and their allowance money. For the first time, they were one of the most powerful groups of shoppers in the country.""",
   "1960s teenage girls shopping", "THE BIGGEST GENERATION")
sc("""So let's spend some time as a teenage girl in nineteen sixty-five. Her bedroom, her clothes, her school, her music, her dates, her dreams and the rules she lived by. If that was you, or your sister, or your mother, I think you'll remember every detail.""",
   "1960s teenage girl portrait", "LET'S GO BACK")

ch("Her bedroom")
sc("""Her bedroom was her kingdom, if she was lucky enough not to share it with a sister. A twin bed with a chenille bedspread. A vanity table with a mirror. A record player and a stack of forty-fives. And on the walls, pictures cut from magazines. Paul McCartney, Herman's Hermits, the Beach Boys and maybe Elvis, if she was a little old-fashioned.""",
   "1960s teenage girl bedroom record player", "HER KINGDOM")
sc("""On her nightstand was a princess phone, if her parents had splurged for a second line, or more likely, she stretched the long cord of the kitchen phone into the hallway closet for privacy. She talked to her best friend for hours, until her father yelled that someone else might need to use the phone.""",
   "1960s teenage girl telephone bed", "THE PRINCESS PHONE")
sc("""And in a drawer, she kept a diary with a tiny lock and key. In it, she wrote about the boy who sat behind her in history class, the fight with her best friend, and her dreams for the future. Many women still have those diaries today, and reading them, they say, is like meeting a stranger they used to know.""",
   "1960s teenage girl writing diary", "THE DIARY WITH A LOCK")
sc("""Her reading came from the drugstore magazine rack. Seventeen magazine was her guide to fashion, dating and growing up. Tiger Beat, which launched in nineteen sixty-five, was full of pinups of teen idols. And she read Nancy Drew mysteries, Gone with the Wind, and maybe a paperback that she kept hidden under the mattress so her mother wouldn't find it.""",
   "1960s teenage girl reading magazine", "SEVENTEEN MAGAZINE")

ch("Her hair and makeup")
sc("""Hair was a serious matter. In the early sixties, the look was big. The bouffant and the beehive, teased high and held in place with clouds of hairspray. Girls slept on giant rollers, sometimes made from orange juice cans, to get their hair smooth and full. Some even ironed their hair on the ironing board to make it straight.""",
   "1960s teenage girl hair curlers", "ORANGE JUICE CANS")
sc("""By nineteen sixty-five, styles were changing. The Beatles and the British Invasion brought new looks from London. Long, straight hair with bangs was in. So was the short, sharp haircut made famous by Vidal Sassoon. Girls with naturally curly hair suffered, and tried everything to straighten it.""",
   "1960s girls long straight hair bangs", "THE LONDON LOOK")
sc("""Makeup was usually a battle with Mom. Many mothers didn't allow it until a certain age, and even then, only a little. Pale pink lipstick. Heavy black eyeliner, if she could get away with it. Fake eyelashes for special occasions. She bought it at the drugstore or the five-and-dime with her babysitting money, and sometimes put it on at school, after leaving the house.""",
   "1960s teenage girl makeup mirror", "A BATTLE WITH MOM")

ch("Her clothes")
sc("""Clothes were changing fast. At school, dress codes still required girls to wear skirts or dresses. No pants allowed, not even in the snow. Skirts had to reach a certain length, and in some schools, girls were made to kneel on the floor, so the teacher could check whether the hem touched the ground.""",
   "1960s high school girls dresses hallway", "KNEEL ON THE FLOOR")
sc("""But fashion was moving the other way. In nineteen sixty-five, the miniskirt arrived from London, made famous by the designer Mary Quant. Hemlines rose higher every season. Parents were horrified. Girls rolled their skirts up at the waistband on the way to school, and rolled them back down before they got home.""",
   "1960s miniskirt fashion girls", "THE MINISKIRT")
sc("""Other must-haves were the shift dress, the A-line skirt, knee socks, penny loafers, Peter Pan collars, and a cardigan sweater with a little sweater clip. Go-go boots were the height of cool. And for the beach, a two-piece bathing suit, if her parents allowed it. Many didn't.""",
   "1960s teenage girls fashion knee socks", "GO-GO BOOTS")
sc("""Many girls sewed their own clothes. Home economics class taught every girl to use a sewing machine, and she bought patterns from Simplicity and McCall's at the fabric store. A teenage girl could make a new dress for a few dollars, and many did, copying the styles they saw in Seventeen magazine.""",
   "1960s girl sewing machine", "SHE SEWED HER OWN")
sc("""And she earned money for all of it. Babysitting was the classic job, paying around fifty cents an hour. Some girls worked at the five-and-dime, the drugstore soda fountain, the movie theater or as a carhop at the drive-in. In summer, they picked fruit, worked at the swimming pool snack bar, or helped at a family business.""",
   "1960s teenage girl babysitting children", "FIFTY CENTS AN HOUR")

ch("Her music")
sc("""Music was everything. In nineteen sixty-five, a teenage girl's radio played the Beatles' Help and Yesterday, the Supremes' Stop! In the Name of Love, the Rolling Stones' Satisfaction, Sonny and Cher's I Got You Babe, and the Byrds' Mr. Tambourine Man. Motown, the British Invasion and folk rock, all at once.""",
   "1960s teenage girls listening records", "HELP! AND SATISFACTION")
sc("""In August of nineteen sixty-five, the Beatles played Shea Stadium in New York, in front of more than fifty-five thousand fans. It was the biggest concert in history up to that time. The screaming was so loud that the band couldn't hear themselves play. Most of the screamers were teenage girls, and many of them still say it was the greatest night of their lives.""",
   "Beatles Shea Stadium 1965", "SHEA STADIUM")
sc("""At home, she watched American Bandstand, Shindig and Hullabaloo, where young dancers in go-go boots danced in cages. She learned the newest dances. The Frug, the Watusi, the Swim, the Jerk and the Monkey. And she practiced in front of the mirror with her best friend until they had it perfect.""",
   "1960s teenagers dancing television show", "THE FRUG AND THE WATUSI")
sc("""And on Friday nights, there were slumber parties. Six girls in pajamas, in sleeping bags on the living room floor. Pizza, potato chips and soda. Prank calls to boys, giggling into the phone. Ouija boards and scary stories after midnight. Hair in rollers and faces covered in cold cream. And almost no sleep at all.""",
   "1960s girls slumber party pajamas", "THE SLUMBER PARTY")

ch("School")
sc("""In school, a teenage girl in nineteen sixty-five took English, history, math and science, along with home economics and typing. Guidance counselors often steered girls toward secretarial courses, nursing or teaching. Few girls were encouraged to become doctors, lawyers or engineers. Some girls listened. Others had other ideas.""",
   "1960s high school girls typing class", "TYPING CLASS")
sc("""Sports options for girls were limited. Many schools had girls' gym class, in one-piece gym suits that everyone hated. There might be a few teams, like volleyball or field hockey, but rarely with real competition. Title Nine, which would open the door to girls' sports, was still seven years away.""",
   "1960s girls gym class uniforms", "THE GYM SUIT")
sc("""So many girls joined other activities. Cheerleading, which was one of the most popular things a girl could do. The pep club, the glee club, the student newspaper and the yearbook. Future Homemakers of America. And everyone wanted to be on the homecoming court. Being crowned homecoming queen was one of the biggest honors in a small town.""",
   "1960s cheerleaders high school football", "HOMECOMING QUEEN")
sc("""And for many girls, the space program was a source of wonder. In nineteen sixty-three, the Soviet Union had sent the first woman into space, Valentina Tereshkova. American girls who dreamed of being astronauts were told that only men could go. It would take until nineteen eighty-three for Sally Ride to become the first American woman in space. Some of the girls of sixty-five cheered her on as grown women.""",
   "1960s girl looking at sky telescope", "DREAMING OF SPACE")

ch("Dating")
sc("""Dating in nineteen sixty-five had a lot of rules. The boy asked the girl, usually by phone, a few days in advance. He came to the door and met her parents. Her father asked where they were going and what time she'd be home. And a girl who called a boy, instead of waiting for him to call her, risked being called forward.""",
   "1960s teenage boy picking up date door", "HE CAME TO THE DOOR")
sc("""A typical date was a movie, a school dance, a football game or a drive-in, followed by a burger and a Coke. In nineteen sixty-five, the movies were The Sound of Music, Doctor Zhivago and the James Bond film Thunderball. And if a couple got serious, they went steady. She wore his class ring on a chain, or his letter jacket.""",
   "1960s teenage couple movie theater", "THE SOUND OF MUSIC")
sc("""For many girls, the big night of the year was the prom. Weeks of planning. A long gown, often homemade or borrowed. Long white gloves. A corsage from her date. A professional photo in front of a paper backdrop. And a dance in the gym, decorated with crepe paper and a theme like Moonlight in Paris or Stairway to the Stars.""",
   "1960s prom couple formal dance", "THE PROM")
sc("""Her parents watched all of this with a mix of pride and worry. Her mother remembered being a teenager during the war, and her father remembered the Depression. They had worked hard to give her a better life, with her own room, her own record player and her own clothes. But they worried about the new music, the short skirts and the long-haired boys. Every generation of parents does.""",
   "1960s parents worried living room", "HER PARENTS WORRIED")

ch("The rules")
sc("""A teenage girl in nineteen sixty-five lived by many rules. Be home by curfew, often ten or eleven. Don't wear too much makeup. Don't go to a boy's house when his parents aren't home. Don't ride in a car with a boy you don't know. And above all, protect your reputation. In a small town, gossip could follow a girl for years.""",
   "1960s mother daughter talking kitchen", "PROTECT YOUR REPUTATION")
sc("""The expectation was clear. Finish high school, maybe go to college or secretarial school, and get married. In nineteen sixty-five, the typical American woman married for the first time at about twenty. Many girls were engaged by the time they graduated high school. And many brides were pregnant with their first child within a year.""",
   "1960s young bride wedding", "MARRIED AT TWENTY")

ch("The changes coming")
sc("""But things were starting to change. In nineteen sixty-three, Betty Friedan's book The Feminine Mystique had asked whether women should want more than a house and a husband. Many mothers read it, and some of them told their daughters to get an education first. The birth control pill had been approved in nineteen sixty, and it would change women's lives enormously.""",
   "1960s woman reading book", "THE FEMININE MYSTIQUE")
sc("""The Civil Rights Act of nineteen sixty-four had made it illegal for most employers to discriminate based on sex. In nineteen sixty-six, the National Organization for Women was founded. College enrollment for women was rising every year. The teenage girls of nineteen sixty-five would graduate into a very different world than the one their mothers had known.""",
   "1960s young women college campus", "A DIFFERENT WORLD")
sc("""And many of them would change it. They became the first women in their families to finish college. They became teachers and nurses, but also doctors, lawyers, scientists, executives, judges and astronauts. Many raised families and had careers. They did things their mothers had only imagined.""",
   "1970s women working professional office", "THEY CHANGED IT")

ch("Looking back")
sc("""If you were a teenage girl in nineteen sixty-five, you're in your late seventies now. Maybe you still have a forty-five of a Beatles song, a faded prom picture, or a diary with a broken lock. Maybe you remember exactly where you were when you first heard Satisfaction on the radio.""",
   "1960s teenage girl snapshot photo", "YOU STILL HAVE IT")
sc("""It was a time of rules and possibilities, of rollers and miniskirts, of the old world and the new. You lived right on the line between them. And in many ways, you were the generation that walked across it.""",
   "1960s teenage girls walking street", "YOU WALKED ACROSS THE LINE")
sc("""So tell us in the comments. How old were you in nineteen sixty-five? What was your favorite song, your favorite outfit and your favorite Beatle? What rule did your parents have that you'll never forget? We read every comment. Next time, we're looking at what Sunday really looked like in nineteen fifties America. Thank you for spending this time with me.""",
   "1960s teenage girls laughing outdoors", "WHO WAS YOUR FAVORITE BEATLE?")

save("video44", "If You Were a Teenage Girl in 1965, This Was Your Life", [
    "The Beatles at Shea Stadium, August 15, 1965, about 55,600 fans: The Beatles official history; New York Mets",
    "1965 hit songs ('Help!', 'Yesterday', 'Stop! In the Name of Love', '(I Can't Get No) Satisfaction', 'I Got You Babe', 'Mr. Tambourine Man'): Billboard",
    "Mary Quant and the miniskirt (mid-1960s): Victoria and Albert Museum",
    "1965 films (The Sound of Music, Doctor Zhivago, Thunderball): American Film Institute",
    "Median age at first marriage for women about 20.6 in 1965: U.S. Census Bureau",
    "Betty Friedan, The Feminine Mystique (1963); FDA approval of the birth control pill (1960): FDA",
    "Civil Rights Act of 1964, Title VII (sex discrimination in employment); National Organization for Women founded 1966: National Archives; NOW",
    "Title IX of the Education Amendments (1972): U.S. Department of Education",
], "angle 2 · a stage of life", minutes=(12, 14.5))
