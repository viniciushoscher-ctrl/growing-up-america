import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# Video 38 · angle 2 (a stage of life, thirty at the end of the seventies) · afternoon slot · day 13
# If You Turned 30 in 1979, This Was Your Life
# "Documerica" in the generic queries keeps the photos in the 1970s (EPA DOCUMERICA, 1971-77).

sc("""If you turned thirty in nineteen seventy-nine, you were born in nineteen forty-nine, right at the start of the baby boom. You grew up with Howdy Doody and the polio vaccine. You were a teenager when the Beatles arrived. You came of age in the sixties, with Vietnam, the moon landing and Woodstock. And now, at thirty, you were facing something nobody had warned you about. Being a grown-up in the late seventies.""",
   "Documerica young couple 1970s", "BORN IN 1949")
sc("""There's an old saying from the sixties. Don't trust anyone over thirty. In nineteen seventy-nine, the people who had said it were turning thirty themselves. The first wave of baby boomers was settling down, getting mortgages, raising kids and wondering how they had gotten there so fast.""",
   "Documerica family suburban home", "DON'T TRUST ANYONE OVER THIRTY")
sc("""So what was life really like at thirty in nineteen seventy-nine? The job, the house, the family, the money, and the news. It was a harder time than many people remember. But it was also a time of real freedom and change. Let's go back.""",
   "Documerica city street people", "LET'S GO BACK")
sc("""There were a lot of them. In nineteen seventy-nine, more than three and a half million Americans turned thirty, part of a generation so large that every stage of their lives reshaped the country. When they were babies, the country built maternity wards. When they were children, it built schools. And now that they were thirty, everyone wanted to sell them houses, cars and life insurance.""",
   "Documerica crowd people street", "3.5 MILLION THIRTY-YEAR-OLDS")

ch("The job")
sc("""By thirty, most people in nineteen seventy-nine had been working for about eight to ten years. Many men had served in Vietnam, or had a draft number that never came up. Many had used college deferments and graduated in the early seventies, when good jobs were easier to find. Others had gone straight from high school to the factory.""",
   "Documerica factory worker", "TEN YEARS ON THE JOB")
sc("""But the economy of the late seventies was difficult. Factories in the Northeast and the Midwest were starting to close, as companies moved south or overseas. Steel mills in Ohio and Pennsylvania were laying people off. In nineteen seventy-nine, Chrysler was nearly bankrupt and needed a loan guarantee from the government to survive.""",
   "Documerica steel mill workers Pittsburgh", "THE FACTORIES BEGAN TO CLOSE")
sc("""For women, though, the late seventies were a time of opportunity. By nineteen seventy-nine, about half of all married women worked outside the home, far more than in their mothers' generation. Women were becoming doctors, lawyers, managers and police officers in growing numbers. Many thirty-year-old women were the first in their families to have a real career.""",
   "Documerica woman working office", "HALF OF MARRIED WOMEN WORKED")
sc("""The office of nineteen seventy-nine was full of smoke, typewriters and carbon paper. The IBM Selectric typewriter, with its spinning golf ball, was the height of technology. Copies were made on a Xerox machine. Calculators had just gotten cheap enough for every desk. And if you needed to send a document quickly, you used a telex machine or the mail.""",
   "Documerica office typewriters workers", "THE IBM SELECTRIC")

ch("The money")
sc("""The biggest problem of nineteen seventy-nine was inflation. Prices were rising by more than eleven percent a year. By the next year, it would be over thirteen percent. A paycheck that seemed fine in January felt smaller by December. Families watched the price of groceries, gas and rent climb every month.""",
   "Documerica grocery store shopping", "INFLATION OVER 11%")
sc("""In nineteen seventy-nine, a loaf of bread cost about fifty cents, a gallon of milk about a dollar and seventy-five, and a new car about six thousand dollars. The median family income was around nineteen thousand dollars a year. People felt richer than their parents, but somehow always behind.""",
   "Documerica supermarket checkout", "ALWAYS BEHIND")
sc("""And savings didn't help much. Money in a passbook savings account earned around five percent, while prices rose more than eleven. People learned that holding cash meant losing money. So many bought things instead. A house, a car, a stereo, a color TV. Credit cards, like Visa and MasterCard, became common in the late seventies.""",
   "Documerica bank customers", "CREDIT CARDS")
sc("""Taxes were another frustration. As inflation pushed paychecks higher, people moved into higher tax brackets, even though their money bought no more than before. People called it bracket creep. In nineteen seventy-eight, California voters passed Proposition Thirteen, which slashed property taxes, and a tax revolt spread across the country.""",
   "Documerica people voting polling place", "BRACKET CREEP")

ch("The house")
sc("""Buying a first house at thirty in nineteen seventy-nine was harder than it had been for your parents. The median price of a new home was about sixty-two thousand dollars. And mortgage rates were climbing fast, passing eleven percent by the end of the year. Within two years, they would reach eighteen percent.""",
   "Documerica suburban houses street", "MORTGAGES OVER 11%")
sc("""Many young couples needed both incomes to qualify for a mortgage. Some bought old houses in the city and fixed them up themselves, a trend that came to be called gentrification. Others bought condos or townhouses, which were new in many places. And many simply kept renting, and waited.""",
   "Documerica young couple painting house", "BOTH INCOMES")
sc("""Inside the house, the style was pure late seventies. Earth tones everywhere. Brown, orange, gold and green. Shag carpet. Wood paneling. Macrame plant hangers. A waterbed, if you were adventurous. A stereo system with big speakers and an eight-track or cassette deck. And a new microwave oven, which many families bought around that time.""",
   "Documerica living room 1970s interior", "EARTH TONES")
sc("""And the kitchen had changed too. Avocado and harvest gold appliances. A Mr. Coffee machine on the counter, which Joe DiMaggio advertised on television. A Crock-Pot, the slow cooker that let working parents start dinner in the morning and come home to a hot meal. And a fondue pot, from a wedding gift, used maybe twice.""",
   "Documerica kitchen family cooking", "MR. COFFEE AND THE CROCK-POT")

ch("The family")
sc("""By thirty, many people in nineteen seventy-nine were married with young children. But families were changing. Couples were marrying a little later and having fewer children than their parents. The average family had about two kids, compared with three or four in the fifties.""",
   "Documerica young family children", "FEWER CHILDREN")
sc("""Divorce was also much more common than in their parents' generation. In the late seventies and early eighties, the divorce rate in America reached its highest point ever. Many thirty-year-olds had already been married and divorced once. Single parents, stepfamilies and joint custody became part of everyday life.""",
   "Documerica woman child home", "DIVORCE PEAKED")
sc("""Raising kids in nineteen seventy-nine meant Sesame Street, which was ten years old, and Mister Rogers. It meant Star Wars toys, which every child wanted after the movie came out in nineteen seventy-seven. And it meant less worry than parents feel today. Kids still played outside, rode bikes all day, and came home when it got dark.""",
   "Documerica children playing street", "STAR WARS TOYS")
sc("""And childcare was a new worry. With both parents working, many young families needed help. Day care centers were opening across the country. Some families relied on grandparents, neighbors or a babysitter down the street. Latchkey kids came home to empty houses after school. It was a big change from the way the thirty-year-olds of nineteen seventy-nine had grown up.""",
   "Documerica day care children", "DAY CARE")

ch("Gas lines again")
sc("""Then, in the spring and summer of nineteen seventy-nine, the gas lines came back. A revolution in Iran cut oil supplies, and panic set in. Lines at gas stations stretched for blocks. Some stations ran out completely. In many states, you could only buy gas on odd or even days, depending on the last digit of your license plate.""",
   "Documerica gas station line cars", "THE GAS LINES")
sc("""People waited for hours, sometimes before dawn, just to fill up. Tempers flared. Gas prices passed a dollar a gallon in many places for the first time. Americans started buying smaller cars, especially from Japan. Hondas, Toyotas and Datsuns were suddenly everywhere. Detroit was caught off guard.""",
   "Documerica small cars traffic", "SMALL CARS FROM JAPAN")
sc("""The family car of a thirty-year-old in nineteen seventy-nine might be a Ford Pinto, a Chevy Chevette, an AMC Gremlin, or a Volkswagen Rabbit. If you had kids, maybe a station wagon with wood paneling. Many of those cars were not well made, and rust was a constant problem. But gas mileage was now the number one question at every car lot.""",
   "Documerica car dealership lot", "THE PINTO AND THE CHEVETTE")
sc("""In July of nineteen seventy-nine, President Jimmy Carter gave a famous speech on television about what he called a crisis of confidence. He said Americans were losing faith in the future. The press called it the malaise speech. Many thirty-year-olds felt exactly what he was describing, even if they didn't like hearing it.""",
   "Jimmy Carter 1979 speech", "A CRISIS OF CONFIDENCE")

ch("The news")
sc("""Nineteen seventy-nine was full of unsettling news. In March, there was a partial meltdown at the Three Mile Island nuclear plant near Harrisburg, Pennsylvania. Thousands of families with young children left the area. That same month, a movie about a nuclear accident called The China Syndrome was playing in theaters. The timing was eerie.""",
   "Three Mile Island nuclear plant", "THREE MILE ISLAND")
sc("""In July, the American space station Skylab fell out of orbit and broke up over the Indian Ocean and Western Australia. For weeks, people joked about where it would land. And in November, Iranian students took more than fifty Americans hostage at the U.S. embassy in Tehran. They would be held for four hundred and forty-four days.""",
   "Skylab space station", "SKYLAB FALLS")
sc("""Every night, the news counted the days of the hostage crisis. Yellow ribbons appeared on trees across the country. People felt frustrated and helpless. It was a hard way to end a decade, and many people who turned thirty that year remember it clearly.""",
   "Yellow ribbon tree", "THE YELLOW RIBBONS")

ch("The fun")
sc("""But life at thirty in nineteen seventy-nine wasn't all bad news. There was disco. Saturday Night Fever had come out in nineteen seventy-seven, and by seventy-nine, disco was everywhere. Couples went out on Saturday night to dance under a mirror ball. Donna Summer, the Bee Gees, Gloria Gaynor and Chic were on every radio.""",
   "Documerica disco dancing", "DISCO")
sc("""But in July of nineteen seventy-nine, a radio DJ in Chicago held Disco Demolition Night at Comiskey Park, blowing up a crate of disco records between games of a baseball doubleheader. The crowd stormed the field, and the second game was forfeited. It was a sign that the disco era was ending. Rock, new wave and country were coming back.""",
   "Comiskey Park Chicago", "DISCO DEMOLITION NIGHT")
sc("""At home, thirty-year-olds watched Mork and Mindy, Taxi, M*A*S*H, Dallas and Saturday Night Live. In September, a new cable channel called ESPN went on the air, showing sports around the clock. Video cassette recorders were just appearing, expensive, but amazing. For the first time, you could record a show and watch it later.""",
   "Documerica family watching television", "ESPN AND THE VCR")
sc("""And there was fitness. The jogging craze of the late seventies was in full swing. James Fixx's Complete Book of Running was a best seller. Thirty-year-olds bought Nike running shoes and headbands, and ran through their neighborhoods every morning. Racquetball clubs and health spas opened everywhere.""",
   "Documerica people jogging park", "THE JOGGING CRAZE")
sc("""Weekends meant cookouts, softball leagues, bowling and trips to the lake. Many thirty-year-olds had grown up camping with their parents, and now took their own kids. Others went to rock concerts, the same bands they had loved at eighteen, now playing in big arenas. Fleetwood Mac, the Eagles, Led Zeppelin, Billy Joel and Bruce Springsteen.""",
   "Documerica family camping lake", "WEEKENDS")

ch("Thirty")
sc("""Turning thirty in nineteen seventy-nine meant looking back on a remarkable life so far. You had seen more change in thirty years than your grandparents had seen in a lifetime. Television, rock and roll, the civil rights movement, Vietnam, the moon landing, Watergate. And you were only halfway through.""",
   "Documerica adult portrait", "HALFWAY THROUGH")
sc("""It also meant looking ahead. The eighties were coming. Within a few years, inflation would fall, the economy would boom, and many of those thirty-year-olds would buy homes, build careers and raise families. They would become the parents of a new generation, and eventually, the grandparents of another.""",
   "Documerica family home yard", "LOOKING AHEAD")
sc("""If you turned thirty in nineteen seventy-nine, you're in your late seventies now. Think back to that year. The gas line. The disco. The first VCR. The little kids at home, the mortgage you weren't sure you could afford. You made it through. And you probably did a lot better than you thought you would.""",
   "Documerica couple sunset", "YOU MADE IT THROUGH")
sc("""So tell us in the comments. How old were you in nineteen seventy-nine, and what do you remember most? Did you wait in a gas line? Did you go to a disco? We read every comment. Next time, we're asking what happened to the door-to-door salesman. Thank you for spending this time with me.""",
   "Documerica sunset city skyline", "HOW OLD WERE YOU IN 1979?")

save("video38", "If You Turned 30 in 1979, This Was Your Life", [
    "CPI inflation 11.3% in 1979 and 13.5% in 1980: Bureau of Labor Statistics",
    "Chrysler Corporation Loan Guarantee Act of 1979: U.S. Treasury",
    "Married women's labor force participation about 49% in 1979: Bureau of Labor Statistics",
    "Median family income about $19,600 in 1979: U.S. Census Bureau",
    "Median price of a new home about $62,900 in 1979: U.S. Census Bureau, New Residential Sales",
    "30-year mortgage rates passed 11% in late 1979 and peaked above 18% in 1981: Freddie Mac Primary Mortgage Market Survey",
    "U.S. divorce rate peaked around 1979-1981: CDC National Center for Health Statistics",
    "1979 oil crisis and odd-even gas rationing: U.S. Energy Information Administration; Federal Reserve History",
    "President Carter's 'crisis of confidence' speech, July 15, 1979: Miller Center, University of Virginia",
    "Three Mile Island accident, March 28, 1979: U.S. Nuclear Regulatory Commission",
    "Skylab reentry, July 11, 1979: NASA",
    "Iran hostage crisis, November 4, 1979 to January 20, 1981 (444 days): National Archives",
    "Disco Demolition Night, Comiskey Park, July 12, 1979: Chicago History Museum",
    "ESPN launched September 7, 1979: ESPN",
    "Photos: EPA DOCUMERICA project (1971-1977), U.S. National Archives, public domain",
], "angle 2 · a stage of life", minutes=(12, 14.5))
