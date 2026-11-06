import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save, S

# Grandma Ruth 45 · everyday/holiday recipe: Thanksgiving turkey that isn't dry (Google Trends 3/11: Thanksgiving dinner +300%; Thanksgiving is 26/11)
# Grandma Ruth: born 1944 in Mansfield, Ohio; mother Dorothy, father Walter, brother Danny, Grandma Pearl.

sc("""Sweetheart, I've cooked sixty-one Thanksgiving turkeys. The first one, in nineteen sixty-three, was so dry my father-in-law asked for a glass of water after every bite. He was a polite man, so he drank four glasses and said it was delicious. I cried in the pantry. And I swore I'd never serve a dry turkey again.""",
   "roast turkey Thanksgiving platter", "SIXTY-ONE TURKEYS")
sc("""So tonight I'm giving you my Thanksgiving turkey, juicy and golden, every step, and the five mistakes that make it dry. And stay with me, because the last mistake happens after the turkey comes out of the oven, and almost every family in America makes it, every single year.""",
   "carving juicy turkey breast", "FIVE MISTAKES")

ch("The bird on Elm Street")
sc("""When I was a girl, Grandma Pearl raised her own turkeys on the farm. She'd pick out the best one in October and feed it corn for a month. My brother Danny named it every year, which was a terrible mistake, and every Thanksgiving he refused to eat it. One year he named it Mr. Roosevelt. My father said that was the most Republican dinner he ever ate.""",
   "1940s farm turkeys yard", "MR. ROOSEVELT")
sc("""Back then, people roasted the turkey all morning, at a low oven, until it was falling apart and dry as a bone, and covered it in gravy to hide it. Then in the fifties and sixties the women's magazines started telling us to cook it hotter and faster. My mother didn't trust them. In a minute I'll tell you which one of them was right.""",
   "1950s Thanksgiving dinner family", "WHO WAS RIGHT")

ch("Buying and thawing")
sc("""First, how big a turkey. Plan about a pound and a half per person, so you have leftovers. A twelve to fourteen pound bird feeds eight, with sandwiches the next day. And here's mistake number one, and it starts days before Thanksgiving. Not thawing it all the way. A frozen turkey takes one day in the icebox for every four or five pounds.""",
   "frozen turkey refrigerator thawing", "ONE DAY PER FIVE POUNDS")
sc("""So a fourteen pound turkey needs three full days in the icebox. Put it in on Sunday for Thursday. If the middle is still frozen, the outside overcooks and dries out while you wait for the inside to be done. And never thaw it on the counter, honey. That's how families get sick. If you're late, put it in a sink of cold water, and change the water every half hour.""",
   "turkey in sink cold water", "NEVER ON THE COUNTER")

ch("The dry brine")
sc("""Now my best secret, and it's free. Salt the turkey a day or two ahead. It's called a dry brine. Take out the neck and the bag of giblets. Pat the turkey dry. Then rub it all over with salt, about one tablespoon of kosher salt for every four pounds, mixed with a little pepper and dried thyme. Get some under the skin of the breast, too.""",
   "rubbing salt on raw turkey", "SALT IT AHEAD")
sc("""Then put it on a tray, uncovered, in the icebox for one or two days. The salt goes deep into the meat, and it holds the juices in while it roasts. And the skin dries out in the cold, so it roasts up crispy and golden. Mistake number two is skipping this, or putting the turkey in a bucket of salty water. That makes soggy skin, and a mess in your kitchen.""",
   "uncovered turkey tray refrigerator", "CRISPY SKIN")

sc("""And the timeline, honey, so Thursday isn't a panic. Sunday, the turkey goes in the icebox to thaw. Tuesday, dry brine it. Wednesday, make the pies, the cranberry sauce and the stuffing, ready to bake. Thursday morning, the turkey comes out an hour early and goes in the oven. Write it on a card and stick it on the refrigerator. That card has saved my Thanksgiving for forty years.""",
   "Thanksgiving timeline card refrigerator", "WRITE IT ON A CARD")

ch("Getting ready")
sc("""On Thanksgiving morning, take the turkey out of the icebox an hour before it goes in the oven, so it's not ice cold. Heat the oven to four hundred twenty-five. Don't rinse it, honey. Rinsing a turkey splashes germs all over your sink and does nothing for the taste. Just pat it dry again with paper towels.""",
   "patting turkey dry paper towels", "DON'T RINSE IT")
sc("""Then stuff the inside of the bird, not with stuffing, but with a quartered onion, a lemon, a few cloves of garlic, and some fresh herbs. Sage, thyme and rosemary. They steam inside and perfume the meat. Rub the outside all over with soft butter. Tuck the wing tips under, like the turkey's taking a nap with its hands behind its head.""",
   "onion lemon herbs inside turkey", "TAKING A NAP")
sc("""If this is helping you, honey, tap the like button for me. It helps Grandma more than you know. And here's mistake number three. Cooking the stuffing inside the bird. By the time the stuffing in the middle is hot enough to be safe, the breast is dry as sawdust. Bake your stuffing in a dish on the side. It gets crispy on top, and the turkey cooks faster and more evenly.""",
   "stuffing baking dish crispy top", "STUFFING ON THE SIDE")

ch("Roasting")
sc("""Set the turkey on a rack in a roasting pan, breast up. Put a cup of broth, a chopped onion and a carrot in the bottom of the pan, for the gravy. Roast it at four twenty-five for thirty minutes to get the skin golden. Then turn the oven down to three twenty-five, and keep roasting. That's the answer, honey. Hot to start, then lower. My mother and the magazines were both half right.""",
   "turkey roasting pan oven rack", "HOT, THEN LOWER")
sc("""A fourteen pound turkey takes about three to three and a half hours in all. But don't trust the clock, and don't trust that little red popper that comes stuck in the turkey. It pops when the breast is already overcooked. Mistake number four is going by time instead of temperature. Buy a meat thermometer. It costs about ten dollars, and it's the best ten dollars you'll spend all year.""",
   "meat thermometer turkey thigh", "TRUST THE THERMOMETER")
sc("""Put the thermometer in the thickest part of the breast, not touching the bone. Take the turkey out when the breast reads one hundred sixty degrees, and the thickest part of the thigh reads about one seventy-five. It keeps cooking while it rests, and the breast will climb up to a safe one sixty-five. If the skin gets too dark before that, lay a piece of foil loosely over the breast.""",
   "checking turkey temperature foil", "ONE HUNDRED SIXTY")
sc("""And don't open the oven every fifteen minutes to baste, sweetheart. Every time you open the door, the oven loses heat, and the turkey takes longer and dries out more. With the dry brine and the butter, you don't need to baste at all. Peek through the window. Pearl used to say, a watched turkey never browns.""",
   "oven window roasting turkey", "A WATCHED TURKEY")

ch("The last mistake")
sc("""So far, thaw it all the way, dry brine it, stuffing on the side, hot then lower, and go by the thermometer. Now the last mistake, the one I told you every family makes. Carving it the minute it comes out of the oven. When you cut a hot turkey, all the juices run out onto the cutting board, and the meat on the plate is dry.""",
   "juices running cutting board", "CARVING TOO SOON")
sc("""Let it rest for at least thirty minutes, honey, and up to an hour for a big bird. Cover it loosely with foil and a clean dish towel. It stays hot for an hour, I promise. While it rests, the juices settle back into the meat. And this is the perfect time to make the gravy, warm the rolls, and put the side dishes in the oven.""",
   "turkey resting under foil", "REST THIRTY MINUTES")

ch("The gravy")
sc("""For the gravy, pour the drippings from the pan into a big measuring cup and let the fat rise to the top. Spoon off four tablespoons of the fat into a saucepan, and whisk in four tablespoons of flour. Cook it two minutes. Then slowly whisk in four cups of the drippings and broth. Simmer it until it's thick, and taste it for salt and pepper.""",
   "whisking turkey gravy saucepan", "FOUR AND FOUR")
sc("""And scrape the roasting pan, sweetheart. Put it on the stove, pour in a little broth, and scrape up all the brown bits stuck to the bottom with a wooden spoon. Pour that into the gravy. That's where the real flavor lives. My mother said a gravy without the pan scrapings is just brown paste.""",
   "scraping roasting pan brown bits", "THE PAN SCRAPINGS")

ch("Carving")
sc("""To carve, take off the whole legs first, cutting through the joint. Then cut the whole breast off the bone in one piece, on each side, and slice it across the grain, about a half inch thick. That way every slice has a little skin on it. It's much easier than slicing it on the bird, and nobody ends up with a shredded mess.""",
   "carving turkey breast slices", "THE WHOLE BREAST")
sc("""And the leftovers, honey. Pull all the meat off the bones the same night, and put it in the icebox in containers, with a little gravy or broth so it stays moist. It keeps four days, or freezes for three months. And make soup from the bones on Friday. Pearl said the bones were the best part of the turkey, and she was right.""",
   "turkey sandwich leftovers containers", "SOUP ON FRIDAY")

ch("Grandma's turkey")
sc("""So one more time. Thaw it in the icebox, a day for every five pounds. Dry brine it with salt a day or two ahead, uncovered. Herbs inside, butter outside, stuffing on the side. Four twenty-five, then three twenty-five. A thermometer, and out at one sixty in the breast. Rest it thirty minutes before you carve. That's how I've made fifty-nine juicy turkeys in a row.""",
   "golden roast turkey table family", "FIFTY-NINE IN A ROW")
sc("""Tell me in the comments, sweetheart. Who cooks the turkey in your family? And has anybody ever had a turkey disaster? I'd love to hear it. The whole playlist of Grandma's recipes is right there on your screen, and I'll see you in the next video. Good night, honey.""",
   "Thanksgiving family table evening", "ANY TURKEY DISASTERS?")

for s in S:
    s["cuts"], s["moves"] = 4, True

save("grandma45", "Thanksgiving Turkey EVERYONE Makes WRONG (Why Yours Is DRY)",
     ["Grandma Ruth is a narrated character built from real memories and records of the era.",
      "Food safety: thaw turkey in the refrigerator about 24 hours per 4 to 5 pounds; poultry safe at 165 F; do not rinse raw poultry (USDA Food Safety and Inspection Service).",
      "Method as written by Grandma Ruth: dry brine about 1 tbsp kosher salt per 4 lb for 1 to 2 days; 425 F for 30 minutes then 325 F; out at 160 F in the breast; rest 30 minutes."],
     "everyday recipe", minutes=(10, 14.5), voice="en_US-lessac-high")
