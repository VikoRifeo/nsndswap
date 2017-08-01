#!/usr/bin/env python3
# nsndswap/viko_nsnd.py
# copyright 2017 ViKomprenas, 2-clause BSD license (LICENSE.md)

from nsndswap.util import Track

nsnd = {
    # A Shade of Two
    "criticalErr0r": ["Taureg"],
    "Exploreation": ["Explore", "Upward Movement (Dave Owns)"],
    "Taureg": ["Sburban Jungle", "Beatdown"],
    "HammertimeVsThatBlackDoggo": ["Beatdown", "Doctor", "Sburban Jungle", "Liquid Negrocity", "BeatVale", "Penumbra Phantasm"],
    "Saviour of the Dancing Demon": ["Doctor", "Penumbra Phantasm", "Beatdown", "Sburban Jungle"],
    "Player 2": ["Sburban Jungle", "Beatdown", "Liquid Negrocity", "Doctor", "Dance of Thorns"],
    "Cascadium Dioxide": ["Cascade (Beta)", "Flare", "Doctor", "Penumbra Phantasm", "Black Rose / Green Sun", "Black Hole / Green Sun", "Sburban Jungle"],
    "Unnamed Jungle Club Remix (Extra)": ["Sburban Jungle"],
    "Tales of an Unknown Universe": [],

    # M3l0m4ni4c soundcloud
    "At Shadow's Edge": ["Penumbra Phantasm", "Amen, Brother"],
    "Whirlwind (L8 for D8 Version)": ["Whirlwind", "Patient", "Penumbra Phantasm", "Doctor", "Showtime", "Crystalanthemums", "Crystamanthequins", "Spider's Claw", "Vriska's Theme"],
    "Wishful Thinking": ["Skies of Skaia", "Skaian Summoning", "Theme", "Rex Duodecim Angelus", "Penumbra Phantasm", "Upward Movement (Dave Owns)", "Lotus", "Homestuck Anthem", "Ruins", "Explore", "Skaian Skuffle", "Sburban Jungle", "Cascade (Beta)", "Overture (Canon Edit)", "Even in Death"],
    "\N{Dingbat Circled Sans-Serif Digit Eight}": ["Spider's Claw", "Vriska's Theme", "Rex Duodecim Angelus", "Amen, Brother"],
    "Blacker Than Licorice": ["Three in the Morning", "Liquid Negrocity", "Descend", "Umbral Ultimatum", "Walk-Stab-Walk", "Cascade (Beta)", "The Ballad of Jack Noir", "Lotus", "Non Compos Mentis", "Three's a Crowd", "Calamity", "Explore", "Flight of the White Wolf", "Amen, Brother", "Harlequin"],
    "Whirlwind": ["Showtime", "Doctor", "Patient", "Savior of the Waking World", "Penumbra Phantasm"],
    "Ignition": ["Flare (Cascade Cut)", "MeGaLoVania"],

    # M3l0m4ni4c Sins album
    "Temmie Sleuth": ["Problem Sleuth Title Screen", "Temmie Village"],
    "Midnight Temmie": ["I'm a Member of the Midnight Crew", "Temmie Village"],
    "Infinity Temmie": ["Infinity Mechanism", "Temmie Village"],
    "Lord Temmie": ["English", "Temmie Village"],
    "Temmie Served Cold": ["Eternity, Served Cold", "Temmie Village"],
    "Temmie on My Side": ["Time on My Side", "Temmie Village"],
    "Temmie Dreamers": ["Derse Dreamers", "Temmie Village"],
    "[S] Temmie: Ascend": ["Explore", "Temmie Village"],
    "Temmiesetter": ["Moonsetter", "Temmie Village"],
    "The Lost Temmie": ["The Lost Child", "Temmie Village"],
    "Beatdown (Temmie Style)": ["Beatdown", "Temmie Village"],
    "Temmieawesome": ["Revelawesome", "Temmie Village"],
    "Tems (With Temmies)": ["Ruins (With Strings)", "Temmie Village"],
    "Temmieslammer": ["Sunslammer", "Temmie Village"],
    "Temmie Aggrieves": ["Aggrieve", "Temmie Village"],
    "Endless Temmie": ["Endless Climb", "Temmie Village"],
    "Temmie8reath": ["Spider8reath", "Temmie Village"],
    "BL1ND T3MM13": ["BL1ND JUST1C3 : 1NV3ST1G4T1ON !!", "Temmie Village"],
    "Crystamanthetems": ["Crystamanthequins", "Temmie Village"],
    "Temmiedown": ["Showdown", "Temmie Village"],
    "Cascade of Unfortunate Temmies": ["Cascade (Beta)", "Temmie Village"],
    "Umbral Temmie": ["Umbral Ultimatum", "Temmie Village"],
    "[S] Temmie: Descend": ["Descend", "Temmie Village"],
    "Temmie's Claw": ["Spider's Claw", "Temmie Village"],
    "Atomyk Temmiepyre": ["Atomyk Ebonpyre", "Temmie Village"],
    "Liquid Temmiecity": ["Liquid Negrocity", "Temmie Village"],
    "Savior of the Waking Temmie": ["Savior of the Waking World", "Temmie Village"],
    "ShowTemmie": ["Showtime", "Temmie Village"],
    "Temmie Flares": ["Flare (Cascade Cut)", "Temmie Village"],

    # ViKomprenas soundcloud
    "Dentist (ViKomprenas)": ["Doctor", "Ruins", "Patient", "Savior of the Waking Patient"],
    "Another Elevator": ["Another Jungle", "Sburban Elevator"],
    "Elevator #3": ["Jungle #3", "Sburban Elevator"],
    "Another Paradigm": ["Endless Climb", "Rhapsody in Green", "MeGaLoVania", "The Paradox Paradigm", "Maestro", "Sburban Jungle", "Penumbra Phantasm", "Beatdown", "Look Where We Are", "Crystalanthemums", "Heir of Grief", "Showtime (Piano Refrain)", "Revelawesome", "Three in the Morning", "Ruins", "Jungle #3", "Tock", "Unintentional Touhou", "Courser"],
    "Radiation Sickness": ["Gaster's Theme", "Penumbra Phantasm", "Heartache", "Earthsea Borealis", "the rose rap"],
    "unfinished medley for power464646": ["Carbon Nadsat/Cuestick Genius", "Rhapsody in Green", "Havoc", "Eternity, Served Cold", "Showdown", "Riches to Ruins Movements I & II", "Negastrife", "PPiSHWA", "Carne Vale"],
    "Saiddit Lullaby": ["Colt Blooded", "Look Where We Are"],

    # The Exquisite Corpse
    "Exquisite Corpse": ["Carne Vale", "A Taste for Adventure", "Endless Climb", "RCT Title Screen", "Sburban Jungle", "Courser", "Jungle #3", "MeGaLoVania"],

    # YUM!: The Vore Album
    "A Welcome to the Wonderful World of Vore": [],
    "Can't Keep a Good Man Down": ["A Welcome to the Wonderful World of Vore"],
    "The Cannibal Cafe": ["Dinosaur Comics Theme"],
    "Voreska": ["MeGaLoVania", "Spider's Claw"],
    "Voriginal Content (feat. Mister Pumpkin)": [],
    "Stomach Is An Instrument / Vorejazz": ["A Welcome to the Wonderful World of Vore"],
    "Vorintosh Plus": ["A Welcome to the Wonderful World of Vore", "MACINTOSH PLUS"],
    "the eighth track is about vriska": ["Spider's Claw", "Jungle #3", "Death by Glamour"],
    "Dentist (Vore Cut)": ["Dentist (ViKomprenas)"],
    "this story has about 300 pages of worldbuilding and then someone gets encased in latex and suffocates and it's generally agreed to be a real sexy affair": [],
    "A Farewell to the Wonderful World of Vore": [],
    "[BONUS] The Voreing Experience": [],

    # Sealstuck Volume 1
    "Sealumbra Phantasm": ["Penumbra Phantasm"],
    "sealteamsixgoestotacobellfordinnerexcepteveryonesasealandwecheer": [],
    "Sealburban Jugnle": ["Sburban Jungle"],
    "it's an amusement park! it's a sealival!": ["le canrival"],
    "A seal related undertale pun": ["CORE"],
    "sealsleepytime.wav": [],
    "caseal": ["casin"],
    "Seal Who": ["Doctor Who Theme"],
    "the seal rap": [],
    "Necrosealfoxtasia": ["Necrofantasia"],
    "Pumpkin Party in Seal Hitler's Water Apocalypse": ["Pumpkin Party in Sea Hitler's Water Apocalypse"],
    "Dinoseal Comics": ["Dinosaur Comics Theme"],
    "Sealache": ["Heartache"],
    "Seal Intermission": [],
    "Moonsealer": ["Moonsetter"],
    "Seally Slippery Cave": ["Ice Path"],
    "sealsetter": ["Sunsetter"],
    "eriseals theme": ["Eridan's Theme"],
    "sealwave": [],
    "The Key of Seal": [],
    "just driving my seal to work officer": [],
    "Unintentionally Seal": ["Unintentionally Short"],
    "i put seal noises over an old abandoned project": [],
    "\u30a2\u30b6\u30e9\u30b7 \u8d64\u3061\u3083\u3093 420 / \u30e2\u30c0\u30f3\u6a39\u76ae": ["MACINTOSH PLUS"],
    "This isn't an old song that I bullshitted over, no sir": [],
    "sealsounds.wav": [],
    "Troubled Seas": [],
    "Seal the Deal": [],
    "A Seal Legend - A Seal is 2": ["A Baby Legend"],

    # UNDERTALE Soundtrack
    "Once Upon a Time": [],
    "Start Menu": ["Once Upon a Time"],
    "Your Best Friend": [],
    "Fallen Down": [],
    "Ruins (Undertale)": [],
    "Uwa!! So Temperate♫": [],
    "Anticipation (Undertale)": ["Enemy Approaching"],
    "Unnecessary Tension": [],
    "Enemy Approaching": [],
    "Ghost Fight": [],
    "Determination": [],
    "Home": ["Once Upon a Time"],
    "Home (Music Box)": ["Home"],
    "Heartache": ["Enemy Approaching"],
    "sans.": [],
    "Nyeh Heh Heh!": [],
    "Snowy": [],
    "Uwa!! So Holiday♫": ["Uwa!! So Temperate♫"],
    "Dogbass": ["Ghost Fight"],
    "Mysterious Place": [],
    "Dogsong": ["Enemy Approaching"],
    "Snowdin Town": ["Snowy"],
    "Shop": ["Snowy", "Snowdin Town"],
    "Bonetrousle": ["Nyeh Heh Heh!"],
    "Dating Start!": ["Snowdin Town"],
    "Dating Tense!": ["Undyne"],
    "Dating Fight!": ["Dating Start!"],
    "Premonition (Undertale)": ["You Idiot"],
    "Danger Mystery": [],
    "Undyne": [],
    "Waterfall": ["Ruins (Undertale)"],
    "Run!": ["Undyne"],
    "Quiet Water": ["Ruins (Undertale)"],
    "Memory": ["His Theme"],
    "Bird That Carries You Over a Disproportionately Small Gap": ["Alphys"],
    "Dummy!": ["Ghost Fight"],
    "Pathetic House": ["Ghost Fight"],
    "Spooktune": [],
    "Spookwave": ["Spooktune"],
    "Ghouliday": ["Jingle Bells"],
    "Chill": [],
    "Thundersnail": [],
    "Temmie Village": ["Dogsong"],
    "Tem Shop": ["Temmie Village"],
    "NGAHHH!!": ["Undyne", "Ruins (Undertale)"],
    "Spear of Justice": ["NGAHHH!!"],
    "Ooo": [],
    "Alphys": [],
    "It's Showtime!": [],
    "Metal Crusher": ["Noisemaster's Theme"],
    "Another Medium": ["Waterfall", "Patient"],
    "Uwa!! So HEATS!!♫": ["Uwa!! So Temperate♫"],
    "Stronger Monsters": ["Enemy Approaching"],
    "Hotel": ["Once Upon a Time"],
    "Can You Really Call This A Hotel, I Didn't Receive A Mint On My Pillow Or Anything": ["Hotel"],
    "Confession": ["Snowdin Town"],
    "Live Report": ["It's Showtime!"],
    "Death Report": ["Live Report"],
    "Spider Dance": ["Ghost Fight"],
    "Wrong Enemy ?!": [],
    "Oh! One True Love": [],
    "Oh! Dungeon": ["Oh! One True Love"],
    "It's Raining Somewhere Else": ["sans."],
    "CORE Approach": ["Hotel"],
    "CORE": ["Another Medium"],
    "Last Episode!": ["Metal Crusher"],
    "Oh My...": [],
    "Death by Glamour": ["Another Medium", "Metal Crusher", "It's Showtime!"],
    "For the Fans": ["Oh! One True Love"],
    "Long Elevator": [],
    "Undertale": ["His Theme", "Once Upon a Time"],
    "Song That Might Play When You Fight Sans": ["sans.", "Nyeh Heh Heh!"],
    "The Choice": ["Undertale"],
    "Small Shock": [],
    "Barrier": [],
    "Bergentrückung": ["Once Upon a Time"],
    "ASGORE": ["Bergentrückung", "Heartache", "Determination", "Undyne"],
    "You Idiot": [],
    "Your Best Nightmare": ["You Idiot", "Your Best Friend"],
    "Finale": ["Your Best Friend", "His Theme"],
    "An Ending": ["Ruins (Undertale)"],
    "She's Playing Piano": ["Alphys"],
    "Here We Are": ["Alphys"],
    "Amalgam": ["Enemy Approaching"],
    "Fallen Down (Reprise)": ["Fallen Down", "Once Upon a Time"],
    "Don't Give Up": ["An Ending"],
    "Hopes and Dreams": ["Once Upon a Time", "Your Best Friend", "Snowdin Town"],
    "Burn in Despair!": ["You Idiot"],
    "SAVE the World": ["Once Upon a Time", "Your Best Friend"],
    "His Theme": [],
    "Final Power": ["Hopes and Dreams"],
    "Reunited": ["Once Upon a Time", "Snowdin Town"],
    "Menu (Full)": ["Start Menu"],
    "Respite": ["Ruins (Undertale)"],
    "Bring It In, Guys!": ["Enemy Approaching", "Nyeh Heh Heh!", "sans.", "Snowy", "Snowdin Town", "Undyne", "Ruins (Undertale)", "Death by Glamour", "Another Medium", "Bergentrückung", "Fallen Down", "Once Upon a Time"],
    "Last Goodbye": ["Once Upon a Time"],
    "But the Earth Refused to Die": ["Ruins (Undertale)"],
    "Battle Against a True Hero": ["Ruins (Undertale)", "Alphys"],
    "Power of \"NEO\"": ["Battle Against a True Hero"],
    "MEGALOVANIA": ["Megalovania"],
    "Good Night": ["Once Upon a Time"],

    # UNDERTALE miscellany
    "Empty House": ["Fallen Down"],
    "Meat Factory": [],
    "Happy Town": [],
    "Trouble Dingle": [],
    "Gaster's Theme": [],
    "Grandpa Semi": ["Metal Crusher"],
    "King Description": ["Determination"],
    "Dance of Dog": [],
    "Sigh of Dog": [],
    "Alphys Lab (Unused)": ["Alphys"],
    "Undyne Battle (Unused)": ["Undyne", "Ruins (Undertale)"],
    "Dog Hole": [],
    "Dogtroid": ["Dogsong"],
    "Undertale (Beta)": ["Once Upon a Time"],

    # Misc
    "SPIDER DANCE FROM UNDERTALE BUT NOW ITS SKA I GUESS???": ["Spider Dance"],
    "Sunset (Toby Fox)": ["Sunsetter"],

    # Redditstuck Vol. 1
    "Cogs": [],
    "Hobbyist": [],
    "Spool": [],
    "Crushing Weight": [],
    "Assertion": [],
    "Visions of Grim": [],
    "Colt Blooded": ["Glass Houses"],
    "Incubation": [],
    "What A Hoot": [],
    "Saoshyant": ["Hobbyist"],
    "Alloy": [],
    "Conflict!": [],
    "Sticky Steps": [],
    "Happy Thoughts And Fairy Dust": [],
    "Effervescence": [],
    "Malediction": [],
    "Solid Water Whispers": [],
    "Divine Intervention": [],
    "Thank You Based Prince": [],
    "Look Where We Are": [],
    "Hyperion": [],

    # Redditstuck Vol. 2
    "Prelude For A Leading Lady": [],
    "Land of Glaciers and Magma": [],
    "Inflection": [],
    "Halcyon": ["My Favorite Things"],
    "Symmet": ["Symmet [Midi]"],
    "Symmet [Midi]": [],
    "In The Sorcerer's Tower": [],
    "Siphon": [],
    "Calmshit": [],
    "The Dremaer And The Dream": [],
    "Lewd Lunacy": [],
    "Slippery Slope": ["Sticky Steps"],
    "Gnade": [],
    "Calm Before Storm": [],
    "Glass Houses": [],
    "To Cross The Void": [],
    "Frieden": [],
    "Where Are We Now": ["Look Where We Are"],
    "(I Can't Get No) Smooth Pencils": [],
    "Pizza Bagels": [],
    "The Fake-Out": [],
    "Maelstrom": [],

    # Hypertonic Dreams
    "Palfrey Motive": [],
    "Vitriolium": [],
    "Redox Redux": [],
    "All Saints to Arms": [],
    "Blueshift": [],
    "Den of Sin": [],
    "Duck Muffler": [],
    "Paperthin": ["Jingle Bell Rock"],
    "Reprieve": [],
    "Notes From The Left Field": [],
    "Hard Pill to Swallow": [],
    "Sad Mountain Dew Music": ["Sticky Steps"],
    "Tryptophantasm": [],
    "High Upon Hinterland": [],
    "Untruly Yours": [],
    "Burnout Flounce": [],
    "Ex Nihilo": [],

    # ndividedbyzero soundcloud
    "Retconjuration": ["Wind chime foley", "Homestuck Anthem"],
    "Juju Breaker": ["Purple Bard", "Sburban Jungle", "Black Rose / Green Sun", "Explore", "English", "Eternity, Served Cold"],

    # Remastered Remixes Vol. 1
    # i can't believe i've done this
    # homestuck-related remixes only
    # titles are from when they were on meems's soundcloud
    "Old Secret Cover (Remastered Remix)": ["Old Secret"],
    "Endless": ["Endless Climb"],
    "Doctor (Remastered Remix)": ["Doctor"],
    "Dissension (Remastered Remix)": ["Dissension"],
    "Chorale For Jaspers (Remastered Remix)": ["Chorale for Jaspers"],
    "Carefree": ["Carefree Action"],
    "Black (Remastered Remix)": ["Black"],
    "Beatdown (Remastered Remix)": ["Beatdown (Strider Style)"],
    "Atomic Ebonpyre": ["Atomyk Ebonpyre"],  # sic
    "Aggrieve (Remastered Remix)": ["Aggrieve"],
    "Upward Movement (Remastered Remix)": ["Upward Movement"],
    "Skies Of Skaia (Remastered Remix)": ["Skies of Skaia"],
    "Showtime Piano Refrain (Remastered Remix)": ["Showtime (Piano Refrain)"],
    "Showtime Original Mix (Remastered Remix)": ["Showtime"],
    "Sburban Jungle Remix": ["Sburban Jungle"],
    "Sburban Countdown (Remastered Remix)": ["Sburban Countdown"],
    "Revelawexome": ["Revelawesome"],  # sic
    "Pony Chorale (Remastered Remix)": ["Pony Chorale"],
    "Harlequin (Remastered Remix)": ["Harlequin"],
    "Guardian (Remastered Remix)": ["Guardian"],
    "Gardner": ["Gardener"],  # sic
    "Explore (Remastered Remix)": ["Explore"],
    "Carne Vale Remastered Remix": ["Carne Vale"],
    "Eternity Served Cold Covered Remixed Remastered": ["Eternity, Served Cold"],
    "Nuclear Remastered Remix": ["Nuclear"],
    "Cascade Remixed Remastered": ["Cascade"],
    "Terezi Owns Remastered Remix": ["Terezi Owns"],
    "Savior Of The Waking World (Remastered Remix)": ["Savior of the Waking World"],
    "Lotus (Remastered Remix)": ["Lotus"],
    "Heir Conditioning Remastered Remix": ["Heir Conditioning"],
    "Kall And Kontakt Remastered Remix Remastered Reimagined": ["CONFERANCE CALL ~~LAST CONTACT~~"],
    "Rex Duodecim Angelus Remastered Remix": ["Rex Duodecim Angelus"],
    "Bearburban Jungle": ["Sburban Jungle"],
    "Megalovania Orchestral Remix": ["MeGaLoVania"],  # does this count as homestuck????
    "MegalovAAAAAAAAAAAAAAAnia": ["MeGaLoVania"],  # what about this
    "Bearlovania": ["MeGaLoVania"],  # or this

    # cosmicTerrorist soundcloud
    "Mannequin (cosmicTerrorist)": ["Mannequin"],
    "Solid Griscosity": ["Liquid Negrocity"],
    "Sunset (cosmicTerrorist)": ["Sunset (Toby Fox)"],
    "Last Breath of the Heir": ["Showtime (Piano Refrain)", "Doctor", "Penumbra Phantasm", "Harlequin", "Liquid Negrocity"],
    "Doctor Percocets": ["Doctor", "Mask Off", "Penumbra Phantasm"],
    "Patient (Full Mix)": ["Patient"],
    "Omnipotential Bark": ["Walk-Stab-Walk", "Sburban Jungle", "Atomic Bonsai", "Umbral Ultimatum", "Penumbra Phantasm", "Cascade", "Liquid Negrocity", "Dissension"],
    "Savior of the Hard Rock World": ["Savior of the Waking World"],
    "Waking Up": ["Penumbra Phantasm", "Doctor", "Get Up"],
    "8 BIT Liquid Negrocity": ["Liquid Negrocity"],
    "Breath Of Air": ["Doctor", "Penumbra Phantasm"],
    "Climbing for Eternity": ["Endless Climb"],
    "The Legend of the Sovereign Slayer": ["Liquid Negrocity", "The Ballad of Jack Noir"],
    "Strider Squadron": ["Upward Movement", "Beatdown", "Atomyk Ebonpyre", "Candles and Clockwork", "Unite Synchronization", "Sburban Jungle"],
    "It's Showtime (Homestuck Version)": ["Showtime", "It's Showtime"],
    "Doctor Lotus": ["Doctor", "Lotus"],

    # Phase
    "Epoch": ["Beatdown"], # combined
    "Advanced Medical Action": ["Doctor"],
    "StarLight": [],
    "Edge Of Oblivion": ["At The Price of Oblivion"],
    "Strife In Sea Hitlers Palace": ["PPiSHWA"], # sic
    "Awaken": ["MeGaLoVania", "Sburban Jungle", "Showtime"],
    "DeadTone": ["Dead Beat"],
    # Skipping Creatrix (duplicated w/ 9)
    "Final Fight": ["Doctor", "Even in Death", "Showtime", "MeGaLoVania", "PPiSHWA", "Beatdown"],
}


def parse():
    return [Track(x, y) for x, y in nsnd.items() if y is not NotImplementedError]
