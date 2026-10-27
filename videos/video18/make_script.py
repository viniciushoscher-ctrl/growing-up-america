import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 18 · angle 3 (an everyday theme, rise and fall story) · evening slot · day 6
# The Rise and Fall of the Sears Catalog

sc("""For almost a hundred years, one book sat in nearly every American home. It wasn't the Bible, though some people joked that it was read more often. It was thicker than a phone book, and it could get you almost anything you could imagine. Clothes, tools, toys, furniture, a sewing machine, a shotgun, even an entire house. It was the Sears catalog.""",
   "Sears Roebuck catalog", "THE BOOK IN EVERY HOME")
sc("""If you grew up between the nineteen fifties and the nineteen eighties, you remember it. The fat spring and fall catalogs. And above all, the Christmas Wish Book, which arrived every fall and got worn out by kids circling every toy they wanted. And then, in nineteen ninety-three, it was gone.""",
   "1960s children looking at catalog", "THE WISH BOOK")
sc("""Today, let's tell the whole story. How a railroad station agent in Minnesota built the biggest store in the world, how the catalog changed life in rural America, what it was like to order from it, and how one of the most powerful companies in history let it all slip away.""",
   "Sears Roebuck building Chicago", "THE WHOLE STORY")

ch("A watch and a railroad station")
sc("""The story begins in eighteen eighty-six, in North Redwood, Minnesota. A young railroad station agent named Richard Sears received a shipment of gold-filled pocket watches that a local jeweler had refused to accept. Instead of sending them back, Sears sold them himself, to other station agents up and down the line. He made a quick profit.""",
   "Richard Warren Sears", "1886: A BOX OF WATCHES")
sc("""Sears realized he had found something. He started a mail-order watch business, and soon he needed someone who could repair watches. He put an ad in the paper, and a watchmaker named Alvah Roebuck answered it. By eighteen ninety-three, the company was called Sears, Roebuck and Company, based in Chicago.""",
   "Alvah Curtis Roebuck", "SEARS, ROEBUCK AND COMPANY")
sc("""Richard Sears was a born salesman. He wrote most of the early catalog copy himself, full of bold claims and exciting descriptions. By eighteen ninety-four, the catalog was more than five hundred pages long, selling everything from bicycles to sewing machines to baby carriages. He called it the Cheapest Supply House on Earth.""",
   "1890s Sears catalog pages", "CHEAPEST SUPPLY HOUSE ON EARTH")

ch("Bringing the city to the farm")
sc("""To understand why the catalog mattered, you have to picture rural America in the eighteen nineties. Most Americans still lived on farms or in tiny towns. The nearest store was a general store that might carry a few hundred items, often at high prices. If you wanted something special, you were out of luck.""",
   "1890s general store rural", "THE GENERAL STORE")
sc("""Then, in eighteen ninety-six, the Post Office started Rural Free Delivery. For the first time, mail came right to the farmhouse door. And in nineteen thirteen, Parcel Post began, which meant packages could come too. Suddenly, a farm family in Kansas could buy the same things as a family in Chicago, at the same prices.""",
   "rural free delivery mail wagon", "RURAL FREE DELIVERY")
sc("""The Sears catalog became a window to the wider world. Farm families studied it by lamplight. Children learned to read from it. Immigrants learned English from it, matching the pictures to the words. Many families called it the Wish Book long before Sears officially gave that name to the Christmas catalog.""",
   "farm family reading by lamplight", "A WINDOW TO THE WORLD")
sc("""Not everyone was happy. Small-town shopkeepers hated the catalog, because it took their customers away. In some towns, merchants held bonfires and burned catalogs in the street. Some offered prizes to anyone who brought one in. To avoid embarrassment, Sears began shipping orders in plain brown packages, so neighbors couldn't tell where they came from.""",
   "1900s small town main street shop", "PLAIN BROWN PACKAGES")
sc("""The catalog also had a second life. When the new one arrived, the old one often went out to the outhouse, where its pages served a very practical purpose. People still joke about it today. Some say the glossy color pages were the least popular, for obvious reasons.""",
   "old wooden outhouse farm", "A SECOND LIFE")

ch("Julius Rosenwald and the great machine")
sc("""In eighteen ninety-five, a Chicago clothing businessman named Julius Rosenwald bought into the company. Rosenwald was a brilliant organizer. Orders were pouring in by the thousands every day, and the company could barely keep up. He set out to build a better system.""",
   "Julius Rosenwald", "JULIUS ROSENWALD")
sc("""In nineteen oh six, Sears opened a giant new complex on Chicago's West Side. It was one of the largest buildings in the world, with conveyor belts, chutes, and a timetable system that tracked every order down to the minute. Henry Ford is said to have visited to study it before building his own assembly line.""",
   "Sears Roebuck West Side Chicago plant", "THE GREAT MACHINE")
sc("""Rosenwald also introduced a famous promise. Satisfaction guaranteed, or your money back. For farm families who had never seen the company and could not touch the products before they bought them, that promise was everything. It built a kind of trust that lasted for generations.""",
   "early 1900s mail order package", "SATISFACTION GUARANTEED")
sc("""Rosenwald became one of the richest men in America, and he gave much of his fortune away. Working with Booker T. Washington, he helped fund the construction of nearly five thousand schools for Black children in the rural South. They were known as Rosenwald Schools, and some of them are still standing today.""",
   "Rosenwald school building", "ROSENWALD SCHOOLS")

ch("A house in a box")
sc("""Perhaps the most amazing thing Sears ever sold was a house. From nineteen oh eight to nineteen forty, Sears sold kit homes through its Modern Homes catalog. You picked a design, sent in your order, and a few weeks later, a railroad boxcar arrived with everything you needed.""",
   "Sears catalog house kit home", "A HOUSE IN A BOX")
sc("""That included about thirty thousand pieces. Precut lumber, numbered so you'd know where each piece went, plus nails, shingles, windows, doors, paint and a seventy-five page instruction book. Prices ranged from a few hundred dollars for a small cottage to a few thousand for a big family home.""",
   "Sears kit home bungalow", "30,000 PIECES")
sc("""Sears sold roughly seventy thousand of these homes across the country. Many families built them with the help of their neighbors, like an old-fashioned barn raising. And many of those houses are still standing and lived in today. Some owners don't even know their house came from a catalog.""",
   "Sears house 1920s neighborhood", "STILL STANDING")

ch("The stores")
sc("""In the nineteen twenties, America started to change. Cars and roads made it easy for people to drive into town. So in nineteen twenty-five, under a leader named General Robert Wood, Sears opened its first retail store, in Chicago. Within a few years, there were hundreds of them.""",
   "1920s Sears department store", "THE FIRST STORE")
sc("""By the nineteen fifties and sixties, the Sears store was a fixture of American life. It anchored the new shopping centers and malls. Families went there for Kenmore washers, Craftsman tools, DieHard batteries and Toughskins jeans. If you bought a refrigerator in the sixties, there was a good chance it came from Sears.""",
   "1960s Sears store shopping center", "KENMORE AND CRAFTSMAN")
sc("""A trip to Sears was a family outing. Dad headed straight for the tool department. Mom looked at appliances and towels. The kids pressed their noses against the toy counter or the candy case, where warm cashews and chocolate were sold by the pound. And everybody met up again at the snack bar for a hot dog.""",
   "1960s family shopping department store", "A FAMILY OUTING")
sc("""And many Sears stores had a catalog desk. You could flip through the catalog in the store, place your order, and come back to pick it up a week later. In the seventies, Sears was the largest retailer in the world. By some estimates, about two out of every three Americans shopped at Sears in a given year.""",
   "1970s department store catalog counter", "THE CATALOG DESK")

ch("The Wish Book")
sc("""For kids, though, the catalog that mattered most was the Christmas Wish Book. Sears published its first Christmas catalog in nineteen thirty-three, during the Depression. By the fifties and sixties, it arrived in the mail every fall, and it was the most exciting thing that came to the house all year.""",
   "1950s children Christmas catalog toys", "IT ARRIVED EVERY FALL")
sc("""Children spent hours with it, lying on the living room floor. Cowboy outfits, dolls, train sets, chemistry sets, Erector sets, bicycles and Barbies. They circled what they wanted, dog-eared the pages, and wrote the item numbers on their letters to Santa. Brothers and sisters fought over who got it first.""",
   "1950s children lying floor catalog", "CIRCLED AND DOG-EARED")
sc("""Parents used the Wish Book too, quietly, after the kids were in bed. They filled out the order form in pen, added the shipping cost, and mailed it in with a check or a money order. A couple of weeks later, a mysterious brown box arrived and disappeared into a closet until Christmas Eve.""",
   "1950s mother writing order form kitchen table", "A MYSTERIOUS BROWN BOX")

ch("Ordering from the catalog")
sc("""If you never ordered from a catalog, here's how it worked. You found what you wanted, wrote down the item number, the size and the color on an order form in the back, and added it all up. Then you mailed it, or later, called it in on the telephone, and waited.""",
   "1950s woman telephone ordering", "THE ORDER FORM")
sc("""And waited. Delivery usually took one to three weeks. There was no tracking number. You just checked the mailbox, or listened for the delivery truck, or waited for the post office to call. When the package finally came, the whole family gathered around to open it.""",
   "1950s mailman delivering package house", "ONE TO THREE WEEKS")
sc("""In a way, it was the online shopping of its day. A huge selection, delivered to your door, with a money-back guarantee. The only difference was that you used a pencil instead of a computer, and you needed a lot more patience.""",
   "1950s family opening package", "THE ONLINE SHOPPING OF ITS DAY")

ch("The fall")
sc("""So what happened? In the seventies and eighties, the world changed again. New discount stores like Kmart and then Walmart offered lower prices. Specialty stores in the mall took away Sears' clothing customers. And the catalog, which had once been a lifeline, was becoming expensive to print and mail.""",
   "1980s discount store shopping", "NEW COMPETITORS")
sc("""In nineteen seventy-three, Sears finished the Sears Tower in Chicago, the tallest building in the world. It was a symbol of power. But by the eighties, the company was losing ground. It tried branching out into insurance with Allstate, stocks with Dean Witter, and real estate with Coldwell Banker. It even launched the Discover card.""",
   "Sears Tower Chicago 1970s", "THE SEARS TOWER")
sc("""The catalog itself was losing money, reportedly more than a hundred million dollars a year by the early nineties. In January of nineteen ninety-three, Sears announced that the big general catalog would end. After ninety-seven years, the book that had sat in almost every American home was gone.""",
   "1990s Sears store exterior", "JANUARY 1993")
sc("""The irony is painful. Just a year later, in nineteen ninety-four, a man named Jeff Bezos started a company that sold books by mail. It was called Amazon. In many ways, Amazon built exactly what the Sears catalog had been, a giant store that delivered almost anything to your door. Sears had the idea a century earlier, and let it go.""",
   "1990s computer home desk", "THE IRONY")

ch("What we remember")
sc("""In the years that followed, Sears kept shrinking. Store after store closed. In two thousand eighteen, the company filed for bankruptcy. Today, only a handful of Sears stores remain in the whole country, a shadow of the giant that once sold everything to everyone.""",
   "empty shopping mall closed store", "A SHADOW OF THE GIANT")
sc("""But the memory of the catalog hasn't faded. Old copies sell to collectors today. People still talk about the toys they circled, the jeans that never wore out, and the tools their fathers bought that are still hanging in the garage. Craftsman tools came with a lifetime guarantee, and some of those wrenches are older than their owners.""",
   "old Craftsman tools garage wall", "STILL IN THE GARAGE")
sc("""The Sears catalog was more than a store. It was a part of American family life. It connected farms to cities, dreams to doorsteps, and children to Christmas. If you grew up with it, you remember the smell of the paper, the weight of it in your hands, and that feeling of turning the page to the toy section.""",
   "1960s family living room reading", "MORE THAN A STORE")
sc("""So tell us in the comments. What was the best thing you ever got from the Sears catalog? Did you circle toys in the Wish Book? Do you still have something from Sears in your house today? We read every comment. Next time, we're taking a walk down Main Street in nineteen fifty-seven. Thank you for spending this time with me.""",
   "1950s Christmas morning children toys", "WHAT DID YOU CIRCLE?")

save("video18", "The Rise and Fall of the Sears Catalog", [
    "Richard Sears and the watch business, North Redwood, Minnesota, 1886; Alvah Roebuck; Sears, Roebuck and Co. 1893: Sears Archives",
    "Rural Free Delivery (1896) and Parcel Post (1913): Smithsonian National Postal Museum",
    "Julius Rosenwald, the 1906 West Side Chicago complex, and nearly 5,000 Rosenwald Schools: National Trust for Historic Preservation; Sears Archives",
    "Sears Modern Homes (1908-1940), about 70,000 sold: Sears Archives",
    "First Sears retail store in 1925 under Robert E. Wood: Sears Archives",
    "First Sears Christmas catalog 1933: Sears Archives",
    "Sears Tower completed 1973: Council on Tall Buildings and Urban Habitat",
    "General catalog ended January 1993 after 97 years: The New York Times, January 26, 1993",
    "Amazon founded 1994: Amazon.com",
    "Sears Holdings Chapter 11 filing, October 2018: U.S. Bankruptcy Court, Southern District of New York",
], "angle 3 · an everyday theme", minutes=(12, 14.5))
