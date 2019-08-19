import re
import alphanum
import washers
import json
from sortedcontainers import SortedDict

sample_a = '''
What a tangle
What a strangling knot to be caught in
To be exiled here
To be stuck in Berlin with Vienna so near
Yet so far from the Emperor's ear
What a strange and impossible sum
To be old while to still be so young
To have sung before speaking a word
To be heard
To be hailed
Then to fail
To be done
To love but to be so naive
To trust and to be so deceived
To mourn, forlorn, to be torn from you
Scorned for another who suffers no grief
To curse God, seeking lightning
And to still be ignored
To hide in this room, now too rich to afford
To hear armies of creditors bang at the door
Always yelling for more
And to have nothing to sell that could help
Except for the Steinway that sits in the corner
For Arthur it all came too easily
To learn the scales in every key
To play the etudes and the suites
The nocturnes and The Fantaisie
To master the sonatas, minuets, and symphonies
To seek the truth fits and starts
To strike the middle F like it's an arrow through the heart
To wing the right hand like a dove (the peaceful flutter of a dove)
And with left a violent shove (some moments will demand a shove)
To needle gently yet relentless with a steady foot upon the pedal
And to clench the iron first inside the velvet glove
To learn to whisper and to scream
(the whisper justifies the scream)
To let each yearning finger breathe
(no, nothing lives unless it breathes)
To burn, to worship, to mislead
To pose a question with a pinky on a key
To flee, to fight, to bleed
To float in air
Nothing solid underneath
To rap those heavy knuckles on the gate to heaven til there's nothing to
Achieve, but—
To go retrieve the length of cable hidden in the cabinet
To metamorphasize the twisted rope unto an alphabet
To lay the lazy C upon the shabby wooden floor to rest
To send the end across the top and bend the C into an S
To curve the tail beneath the S to turn the tangle to a B
To hug the wretched root around the fibers suffocatingly
To wrap again to wrap again to give the coil seven loops
To penetrate the yawning hoop
To tug the loose appendage through
To yank the knot until it's ready for the job it's got to do
To toss the braid above the ceiling beam and to affix the noose
To bid adieu to all of you until there's nothing left to do but
Climb the chair
To cinch the collar
Find the edge
To step into the air

--

Arthur stepped off, yeah he stepped offa the chair
Couldn't weigh a hundred forty pounds
And the rope snapped, yeah, the rope snapped
And then Arthur found himself looking up from the ground
Looking up, looking up, found things looking up
Looking up, looking not so down, no not so down
No knots don't have to stay that way
No, not so tightly wound

What a lovely thing it is to fail
To release those grasping fingernails
Arthur thought the end was near
Then Arthur played for fifty years
And then my father walked down eighth and fiftyseventh street to

Carnegie Hall, yeah it was Carnegie Hall
The show was past sold out for weeks
But they said "if you don't mind, if you don't mind sitting on stage
Sometimes we release a couple seats"
Twenty feet, twenty feet, yeah my dad's twenty three
Twenty feet from the hands on the keys
Yeah, the hands on the keys of a man with the hands that almost didn't exist
That almost didn't exist to see
'''

sample_b = '''
       riverrun, past Eve and Adam's, from swerve of shore to bend
    of bay, brings us by a commodius vicus of recirculation back to
    Howth Castle and Environs.
        Sir Tristram, violer d'amores, fr'over the short sea, had passen-
    core rearrived from North Armorica on this side the scraggy
    isthmus of Europe Minor to wielderfight his penisolate war: nor
    had topsawyer's rocks by the stream Oconee exaggerated themselse
    to Laurens County's gorgios while they went doublin their mumper
    all the time: nor avoice from afire bellowsed mishe mishe to
    tauftauf thuartpeatrick: not yet, though venissoon after, had a
    kidscad buttended a bland old isaac: not yet, though all's fair in
    vanessy, were sosie sesthers wroth with twone nathandjoe. Rot a
    peck of pa's malt had Jhem or Shen brewed by arclight and rory
    end to the regginbrow was to be seen ringsome on the aquaface.
        The fall (bababadalgharaghtakamminarronnkonnbronntonner-
    ronntuonnthunntrovarrhounawnskawntoohoohoordenenthur-
    nuk!) of a once wallstrait oldparr is retaled early in bed and later
    on life down through all christian minstrelsy. The great fall of the
    offwall entailed at such short notice the pftjschute of Finnegan,
    erse solid man, that the humptyhillhead of humself prumptly sends
    an unquiring one well to the west in quest of his tumptytumtoes:
    and their upturnpikepointandplace is at the knock out in the park
    where oranges have been laid to rust upon the green since dev-
    linsfirst loved livvy. 

        What clashes here of wills gen wonts, oystrygods gaggin fishy-
    gods! Brékkek Kékkek Kékkek Kékkek! Kóax Kóax Kóax! Ualu
    Ualu Ualu! Quaouauh! Where the Baddelaries partisans are still
    out to mathmaster Malachus Micgranes and the Verdons cata-
    pelting the camibalistics out of the Whoyteboyce of Hoodie 
    Head. Assiegates and boomeringstroms. Sod's brood, be me fear!
    Sanglorians, save! Arms apeal with larms, appalling. Killykill-
    killy: a toll, a toll. What chance cuddleys, what cashels aired 
    and ventilated! What bidimetoloves sinduced by what tegotetab-
    solvers! What true feeling for their's hayair with what strawng 
    voice of false jiccup! O here here how hoth sprowled met the
    duskt the father of fornicationists but, (O my shining stars and
    body!) how hath fanespanned most high heaven the skysign of
    soft advertisement! But was iz? Iseut? Ere were sewers? The oaks
    of ald now they lie in peat yet elms leap where askes lay. Phall if
    you but will, rise you must: and none so soon either shall the
    pharce for the nunce come to a setdown secular phoenish.
        Bygmester Finnegan, of the Stuttering Hand, freemen's mau-
    rer, lived in the broadest way immarginable in his rushlit toofar-
    back for messuages before joshuan judges had given us numbers
    or Helviticus committed deuteronomy (one yeastyday he sternely 
    struxk his tete in a tub for to watsch the future of his fates but ere
    he swiftly stook it out again, by the might of moses, the very wat-
    er was eviparated and all the guenneses had met their exodus so
    that ought to show you what a pentschanjeuchy chap he was!)
    and during mighty odd years this man of hod, cement and edi-
    fices in Toper's Thorp piled buildung supra buildung pon the
    banks for the livers by the Soangso. He addle liddle phifie Annie
    ugged the little craythur. Wither hayre in honds tuck up your part
    inher. Oftwhile balbulous, mithre ahead, with goodly trowel in
    grasp and ivoroiled overalls which he habitacularly fondseed, like
    Haroun Childeric Eggeberth he would caligulate by multiplicab-
    les the alltitude and malltitude until he seesaw by neatlight of the
    liquor wheretwin 'twas born, his roundhead staple of other days
    to rise in undress maisonry upstanded (joygrantit!), a waalworth 
    of a skyerscape of most eyeful hoyth entowerly, erigenating from 

    next to nothing and celescalating the himals and all, hierarchitec-
    titiptitoploftical, with a burning bush abob off its baubletop and
    with larrons o'toolers clittering up and tombles a'buckets clotter-
    ing down.
        Of the first was he to bare arms and a name: Wassaily Boos-
    laeugh of Riesengeborg. His crest of huroldry, in vert with
    ancillars, troublant, argent, a hegoak, poursuivant, horrid, horned.
    His scutschum fessed, with archers strung, helio, of the second.
    Hootch is for husbandman handling his hoe. Hohohoho, Mister
    Finn, you're going to be Mister Finnagain! Comeday morm and,
    O, you're vine! Sendday's eve and, ah, you're vinegar! Hahahaha,
    Mister Funn, you're going to be fined again!
        What then agentlike brought about that tragoady thundersday
    this municipal sin business? Our cubehouse still rocks as earwitness 
    to the thunder of his arafatas but we hear also through successive
    ages that shebby choruysh of unkalified muzzlenimiissilehims that
    would blackguardise the whitestone ever hurtleturtled out of
    heaven. Stay us wherefore in our search for tighteousness, O Sus-
    tainer, what time we rise and when we take up to toothmick and
    before we lump down upown our leatherbed and in the night and
    at the fading of the stars! For a nod to the nabir is better than wink
    to the wabsanti. Otherways wesways like that provost scoffing 
    bedoueen the jebel and the jpysian sea. Cropherb the crunch-
    bracken shall decide. Then we'll know if the feast is a flyday. She
    has a gift of seek on site and she allcasually ansars helpers, the
    dreamydeary. Heed! Heed! It may half been a missfired brick, as
    some say, or it mought have been due to a collupsus of his back
    promises, as others looked at it. (There extand by now one thou-
    sand and one stories, all told, of the same). But so sore did abe 
    ite ivvy's holired abbles, (what with the wallhall's horrors of rolls-
    rights, carhacks, stonengens, kisstvanes, tramtrees, fargobawlers,
    autokinotons, hippohobbilies, streetfleets, tournintaxes, mega-
    phoggs, circuses and wardsmoats and basilikerks and aeropagods 
    and the hoyse and the jollybrool and the peeler in the coat and
    the mecklenburk bitch bite at his ear and the merlinburrow bur-
    rocks and his fore old porecourts, the bore the more, and his 

    blightblack workingstacks at twelvepins a dozen and the noobi-
    busses sleighding along Safetyfirst Street and the derryjellybies
    snooping around Tell-No-Tailors' Corner and the fumes and the
    hopes and the strupithump of his ville's indigenous romekeepers,
    homesweepers, domecreepers, thurum and thurum in fancymud
    murumd and all the uproor from all the aufroofs, a roof for may 
    and a reef for hugh butt under his bridge suits tony) wan warn-
    ing Phill filt tippling full. His howd feeled heavy, his hoddit did
    shake. (There was a wall of course in erection) Dimb! He stot-
    tered from the latter. Damb! he was dud. Dumb! Mastabatoom,
    mastabadtomm, when a mon merries his lute is all long. For
    whole the world to see.
        Shize? I should shee! Macool, Macool, orra whyi deed ye diie?
    of a trying thirstay mournin? Sobs they sighdid at Fillagain's
    chrissormiss wake, all the hoolivans of the nation, prostrated in
    their consternation and their duodisimally profusive plethora of
    ululation. There was plumbs and grumes and cheriffs and citherers 
    and raiders and cinemen too. And the all gianed in with the shout-
    most shoviality. Agog and magog and the round of them agrog.
    To the continuation of that celebration until Hanandhunigan's
    extermination! Some in kinkin corass, more, kankan keening.
    Belling him up and filling him down. He's stiff but he's steady is
    Priam Olim! 'Twas he was the dacent gaylabouring youth. Sharpen 
    his pillowscone, tap up his bier! E'erawhere in this whorl would ye
    hear sich a din again? With their deepbrow fundigs and the dusty 
    fidelios. They laid him brawdawn alanglast bed. With a bockalips 
    of finisky fore his feet. And a barrowload of guenesis hoer his head.
    Tee the tootal of the fluid hang the twoddle of the fuddled, O!
        Hurrah, there is but young gleve for the owl globe wheels in
    view which is tautaulogically the same thing. Well, Him a being
    so on the flounder of his bulk like an overgrown babeling, let wee
    peep, see, at Hom, well, see peegee ought he ought, platterplate.
    Hum! From Shopalist to Bailywick or from ashtun to baronoath
    or from Buythebanks to Roundthehead or from the foot of the
    bill to ireglint's eye he calmly extensolies. And all the way (a
    horn!) from fiord to fjell his baywinds' oboboes shall wail him

    rockbound (hoahoahoah!) in swimswamswum and all the livvy-
    long night, the delldale dalppling night, the night of bluerybells,
    her flittaflute in tricky trochees (O carina! O carina!) wake him.
    With her issavan essavans and her patterjackmartins about all
    them inns and ouses. Tilling a teel of a tum, telling a toll of a tea-
    ry turty Taubling. Grace before Glutton. For what we are, gifs 
    a gross if we are, about to believe. So pool the begg and pass the
    kish for crawsake. Omen. So sigh us. Grampupus is fallen down
    but grinny sprids the boord. Whase on the joint of a desh? Fin-
    foefom the Fush. Whase be his baken head? A loaf of Singpan-
    try's Kennedy bread. And whase hitched to the hop in his tayle?
    A glass of Danu U'Dunnell's foamous olde Dobbelin ayle. But,
    lo, as you would quaffoff his fraudstuff and sink teeth through
    that pyth of a flowerwhite bodey behold of him as behemoth for
    he is noewhemoe. Finiche! Only a fadograph of a yestern scene.
    Almost rubicund Salmosalar, ancient fromout the ages of the Ag-
    apemonides, he is smoltenin our mist, woebecanned and packt
    away. So that meal's dead off for summan, schlook, schlice and
    goodridhirring.
        Yet may we not see still the brontoichthyan form outlined a-
    slumbered, even in our own nighttime by the sedge of the trout-
    ling stream that Bronto loved and Brunto has a lean on. Hiccubat 
    edilis. Apud libertinam parvulam. Whatif she be in flags or flitters,
    reekierags or sundyechosies, with a mint of mines or beggar a
    pinnyweight. Arrah, sure, we all love little Anny Ruiny, or, we
    mean to say, lovelittle Anna Rayiny, when unda her brella, mid
    piddle med puddle, she ninnygoes nannygoes nancing by. Yoh!
    Brontolone slaaps, yoh snoores. Upon Benn Heather, in Seeple
    Isout too. The cranic head on him, caster of his reasons, peer yu-
    thner in yondmist. Whooth? His clay feet, swarded in verdigrass,
    stick up starck where he last fellonem, by the mund of the maga-
    zine wall, where our maggy seen all, with her sisterin shawl.
    While over against this belles' alliance beyind Ill Sixty, ollol-
    lowed ill! bagsides of the fort, bom, tarabom, tarabom, lurk the
    ombushes, the site of the lyffing-in-wait of the upjock and hock-
    ums. Hence when the clouds roll by, jamey, a proudseye view is


    enjoyable of our mounding's mass, now Wallinstone national
    museum, with, in some greenish distance, the charmful water-
    loose country and the two quitewhite villagettes who hear show
    of themselves so gigglesomes minxt the follyages, the prettilees!
    Penetrators are permitted into the museomound free. Welsh and
    the Paddy Patkinses, one shelenk! Redismembers invalids of old
    guard find poussepousse pousseypram to sate the sort of their butt.
    For her passkey supply to the janitrix, the mistress Kathe. Tip.
        This the way to the museyroom. Mind your hats goan in!
    Now yiz are in the Willingdone Museyroom. This is a Prooshi-
    ous gunn. This is a ffrinch. Tip. This is the flag of the Prooshi-
    ous, the Cap and Soracer. This is the bullet that byng the flag of
    the Prooshious. This is the ffrinch that fire on the Bull that bang
    the flag of the Prooshious. Saloos the Crossgunn! Up with your
    pike and fork! Tip. (Bullsfoot! Fine!) This is the triplewon hat of
    Lipoleum. Tip. Lipoleumhat. This is the Willingdone on his
    same white harse, the Cokenhape. This is the big Sraughter Wil-
    lingdone, grand and magentic in his goldtin spurs and his ironed
    dux and his quarterbrass woodyshoes and his magnate's gharters 
    and his bangkok's best and goliar's goloshes and his pullupon-
    easyan wartrews. This is his big wide harse. Tip. This is the three
    lipoleum boyne grouching down in the living detch. This is an
    inimyskilling inglis, this is a scotcher grey, this is a davy, stoop-
    ing. This is the bog lipoleum mordering the lipoleum beg. A
    Gallawghurs argaumunt. This is the petty lipoleum boy that
    was nayther bag nor bug. Assaye, assaye! Touchole Fitz Tuo-
    mush. Dirty MacDyke. And Hairy O'Hurry. All of them
    arminus-varminus. This is Delian alps. This is Mont Tivel,
    this is Mont Tipsey, this is the Grand Mons Injun. This is the
    crimealine of the alps hooping to sheltershock the three lipoleums.
    This is the jinnies with their legahorns feinting to read in their
    handmade's book of stralegy while making their war undisides
    the Willingdone. The jinnies is a cooin her hand and the jinnies is
    a ravin her hair and the Willingdone git the band up. This is big
    Willingdone mormorial tallowscoop Wounderworker obscides
    on the flanks of the jinnies. Sexcaliber hrosspower.
'''

def alpha_only(sample):
    pattern = re.compile('[^A-Za-z]+')
    return pattern.sub('', sample)

def frequency(sample):

    letters = alpha_only(sample)

    # encode to washers
    l2n = alphanum.base64_to_data
    n2w = washers.data_to_base4
    washer_numbers = n2w(l2n(letters))

    freq = SortedDict()

    max_width = max(map(lambda x : len(x), washer_numbers))
    for segment in washer_numbers:

        # normalize widths
        width = len(segment)
        for i in range(max_width - width):
            segment.insert(0,0)

        # update frequency
        for washer in segment:
            freq.setdefault(washer, 0)
            freq[washer] += 1

    return freq

def print_frequency(sample):

    freq = frequency(sample)

    # also calculate as ratios of most frequent
    r_freq = SortedDict()
    unit = max(freq.values())
    for key, val in freq.items():
        r_key = str(key)
        r_val = val / unit
        r_freq[r_key] = r_val

    print(json.dumps(freq))
    print(json.dumps(r_freq))
    print()

if __name__ == "__main__":
    print_frequency(sample_a)
    print_frequency(sample_b)

