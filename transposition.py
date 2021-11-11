import itertools
import sys
import ngram_score as ns

def strip(text):
    return text.replace(",", "").replace("  ", "").replace(".", "").replace("\n", "").upper()

def factors(number):
    l = []
    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            l.append(i)
    return l


def convert_text(texts, order):
    main_text = ""
    for tex in texts:
        ntex = ""
        for n in range(len(order)):
            ntex += tex[order[n]-1]
        print(ntex)
        main_text += ntex
    return main_text

#quads = ns.ngram_score("english_quadgrams.txt")
#quints = ns.ngram_score("english_quintgrams.txt")

text = """
JNOCT HLTOB OIWHE LEWNV SROAA ETMHU UGTAU ASOYO TIBNB TDINN AFHIL STALN TEUAT EEYHA DMOEE TOHVV AIOOR ESWTO INDAA TAATI GIRKH OETAS ICAYN NGECA AURHC EIEDM TBLCK IEHWT NFPSA RBEST HELET NEHME IOUIS OOUTN ENTOE AARNY ENNBE OFGID NRCNE EPOMF TEOYE ODPGP OALCG AAHYS CNSAN ETNAN ELOTH ROASY UNEUI TAEIA ACUEE TFPRE ATFLA ALMID IADEE ETEWC URNUL HCMII ETISA ONNSA TSGON ERIRW RMFHU SHMGE EIGUL TROEL SITEC HTTIT ETSAT ISAWT IAAUC NYRCO RTGIL KSDFL HTEDI ETHYC REINE AHWRT MAENO HTYTE NSNEE HMICE EDORN HNISN AWSET OTECS GCRTN NCSTT EIENE SISWT OHTUL CANEC MTSIA AIIEH CRUCS SNOGS ESEAT VRLAH INOEO NHMAI DIHAE FCGTF EEASA EWAFU SUCSN AEAOW MLONH WEMSE LEXEH ETVNP IDAYT NMHWO LTFNO TNRWO BNAIF TDINC UTNEL TKKTA TNEEI RTAAA IEUWR TLEON ETTRT ADADE IICSD NRYTT NIIGE SATVH URPSD MROIO OIEIH NTHTU DTOUE EMELT EABIA GOECI UTNFO WMEOO DWSOA RATOF ROHTE ARDCE YAORB FIRBE HGALV ERASA HSIUL GNTIW ETRNE RGEHI FRETS SCKOM TBONU LFDIA HHSEF DHCEE YRGIT GAAEH VETAO ENYTS IEIEG ETDNT HTICI OMIHE NNBNF EIAIT OANEE OIHDI EAORN TLHGO EDSFO LGAIK IIHBI LIEAB HLROT STOTH IWEGE TOOWC AGAHR ANHRH IEIAU VIIEC EALII RDSOE HTTSO YELIS EETER MCNLN CKURT EEDHH ITDSL SONTI SSONH MIEES UIHWM IFUOH ORHNO YDETO OERON DEWGU RIAPO ELNOT TICCG EVFIU RLNCN SAAET WDCIR UAEUN DLENS IATRE NMNEH VOEOH PMIWS TPTES CMNTY EEIHL IXCWA ODEHE DPSEU AEERI UERNN AENUE TTCTU TDSCN TFVNC EMSWW ODXUO TTTKO TFMES LIIDE MNSDI TNAVT LODHT NMLOO GWTAL BHYII EHRCN DIDDO VTAHD ANACN CSAAL OUIHT OKHEO NSGDT SOSWH UPTSR EOUNG NWSHV ITEEY UITHV ALYNR THWTH TANCS DAEIG TBNZL IBTOS WTETR COROT MITEC ORAND ITDAM KOLEA NTDNA ERWRU WRSOA YSAAD EWGTE NVDTS UTYEF NTTMN ALOKE HHKOT AEAHE GUTAT EYNTI BETRL ABTDT SIEUP OGAEE IEPLS HBPEN OEITL CIEOR NFLAT SEIET LAGMN SNILA TETNW SBNWI LTILT ODIST THDCN RTTUU IIWRN TEGTO SWLIC ONGNH NYAOG SOBAL AOCGN HYRAT UTHOO IAEGD ALRHI RAIEO TETAO EAETJ RWSYL YUAIT EALFT LWTAA HRAVN ROHRS EVGEC OBICA ITRDO NIAES EHAEN GNTEE ERAUE EHOEL YTEOA OAIET ILBNI OADRI GTEYA ELNNI GDALN KNADT LETEW EENTE THPOY FCEER HOUOE EEOFT TUAAD MONIL ISTSH AAGNA ALUEI XUUNA HETDT VAKHI AGAON TNEND HEEOT PIAER RTERS TRNTR ETTCN EITPU KRSYE RIREE DEILH RISEO NTNEY GLDTL FSIAD OSFOH HIETI EAHRF YEIIE ETTFS AHTES SFSLR NEACO GHBTO RSEET EHINN NTUSW DHEEO HRIRS NDHTK LHACR ENHHL ANIYI RAS
""".replace(",", "").replace(" ", "").replace(".", "").replace("\n", "").upper()


text = strip(text)
print(text)
print("Brute force of transposition cypher")
print(f"Length of text: {len(text)}")
len_factors = factors(len(text))
print("Factors of length: ", *len_factors)
factor = int(input("Enter the row length: "))
if factor not in len_factors:
    raise Exception("Number not a factor")

try:
    texts = []
    for i in range(int(len(text) / factor)):
        print(text[(factor*i):(factor*i)+factor])
        texts.append(text[(factor*i):(factor*i)+factor])
    done = False
    if "--bf" in sys.argv:
        lowest = 0
        best_text = ""
        perms = [x for x in range(1, factor+1)]
        for perm in list(itertools.permutations(perms)):
            main_text = convert_text(texts, perm)
            print(main_text)
            #print(quads.score(main_text))
            #print(quints.score(main_text))
            if input("Again?") == "y":
                break
            continue
            score = quads.score(main_text) + quints.score(main_text)
            if score < lowest:
                print("new best:", main_text)
                best_text = main_text
        print(best_text)


    while not done:
        order = [int(x) for x in input("Enter order: \"5,3,2\"").split(",")]
        if len(order) != factor:
            print("Enter a list of the length of the factor")
            continue
        main_text = convert_text(texts, order)

        done = input("Done?") == "Y"
except Exception as e:
    raise e
