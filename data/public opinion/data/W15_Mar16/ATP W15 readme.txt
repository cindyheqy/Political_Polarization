PEW RESEARCH CENTER
Wave Wave 15  American Trends Panel 
Dates: Mar 2 - Mar 28, 2016
Mode: Web and Mail 
Language: English and Spanish
N=4,726

***************************************************************************************************************************

NOTES


Questionnaire and topline reflect questions presented in web mode. Mail mode questionnaires available upon request. 


Point estimates for all People-Press questions will vary slightly from published reports because
published material was based on analysis conducted on combined W15/16 dataset:

Partisanship and Political Animosity in 2016
http://www.people-press.org/2016/06/22/partisanship-and-political-animosity-in-2016/


The following variables are recoded based on open-end responses:
CHIPcat1_W15
CHIPcat2_W15
CHIPcat3_W15
STRcat1_W15
STRcat2_W15
STRcat3_W15
GENcat1_W15
GENcat2_W15
GENcat3_W15
SC1POScat1_W15
SC1POScat2_W15
SC1POScat3_W15
SC1NEGcat1_W15
SC1NEGcat2_W15
SC1NEGcat3_W15
TECHPOScat1_W15
TECHPOScat2_W15
TECHPOScat3_W15
TECHNEGcat1_W15
TECHNEGcat2_W15
TECHNEGcat3_W15
DEM1_W15 (DEMNOMOE first choice)
DEM2_W15 (DEMNOMOE second choice)
REP1_W15 (REPNOMOE first choice)
REP2_W15 (REPNOMOE second choice)


***************************************************************************************************************************
WEIGHTS 

WEIGHT_FORM_W15 is the weight for the combined sample of all web and mail interviews. 
Data for all Pew Research Center reports are analyzed using this weight.


***************************************************************************************************************************
SYNTAX (if applicable)


*F_RELCOM3CAT_FINAL:
recode F_RELIMP_RF1(1=1) (else=0) into highsalience.
recode F_ATTEND_FINAL (1,2=1) (else=0) into highattend.
recode F_PRAY_RF1 (1,2=1) (else=0) into highprayer.
count high = highsalience highattend highprayer (1).

recode F_RELIMP_RF1 (3,4=1) (else=0) into lowsalience.
recode F_ATTEND_FINAL (5,6=1) (else=0) into lowattend.
recode F_PRAY_RF1 (6,7=1) (else=0) into lowprayer.
count low = lowsalience lowattend lowprayer (1).

compute F_RELCOM3CAT_FINAL=2.
if high=3 F_RELCOM3CAT_FINAL =1.
if low=3 F_RELCOM3CAT_FINAL =3.
if F_RELIMP_RF1=9 or F_ATTEND_FINAL=9 or F_PRAY_RF1=9 F_RELCOM3CAT_FINAL =9.
IF  SYSMIS(F_RELIMP_RF1) OR SYSMIS(F_ATTEND_FINAL) OR SYSMIS(F_PRAY_RF1) F_RELCOM3CAT_FINAL=$SYSMIS.
val label F_RELCOM3CAT_FINAL 1 "High" 2 "Medium" 3 "Low" 9 "DK/Ref". 
var label F_RELCOM3CAT_FINAL “religious commitment – 3 categories”.


*THERMODISTANCE
compute thermodistance = thermob – thermoa.
if thermob=999 or thermoa=999 thermodistance=9.
		
recode thermodistance (-100 thru -75=1) (-74 thru -26=2) (-25 thru 25=3) (26 thru 74=4) (75 thru 100=5) into thermodistanceREC.

variable label thermodistanceREC “Distance between thermometer ratings of the parties”.
value label thermodistanceREC
1 “Much warmer Rep (-100 to -75)”
2 “Warmer Rep (-74 to -26)”
3 “Little difference (-25 to 25)”
4 “Warmer Dem (26 to 74)”
5 “Much warmer Dem (75 to 100)”.


*IDEOPARTYDIFF/IDEOPARTYDIFFREC
compute ideopartydiff = ideodem - ideorep.
if ideodem = 99 or ideorep = 99 ideopartydiff = 99.
recode ideopartydiff (11 thru hi=sysmis).

recode ideopartydiff (-10 thru -1=1) (0=2) (1 thru 4=3) (5 thru 7=4) (8 thru 10=5) (else=sysmis) into ideopartydiffREC.

variable label ideopartydiffREC 'Ideological distance between parties'.
value label ideopartydiffREC
1 “Dem more cons/Rep more lib (-10 to -1)”
2 “No difference between parties (0)”
3 “Dem slightly more lib/Rep slightly more cons (1 to 4)”
4 “Dem more lib/Rep more cons (5 to 7)”
5 “Dem a lot more lib/Rep a lot more cons (8 to 10)”.

*IDEODIFFREP/IDEODIFFREPREC
compute ideodiffrep = ideoself - ideorep.
if ideoself = 99 or ideorep = 99 ideodiffrep = 99.
recode ideodiffrep (11 thru hi=sysmis).

recode ideodiffrep (-10 thru -3=1) (-2 thru 2=2) (3 thru 10=3) (else=sysmis) into ideodiffrepREC.
variable label ideodiffrepREC “Ideological distance between self and Republican Party”.
value label ideodiffrepREC
1 “Self more conservative than Rep Party (-10 to -3)”
2 “No difference between self and Rep Party (-2 to 2)”
3 “Self less conservative than Rep Party (3 to 10)”.

*IDEODIFFDEM/IDEODIFFDEMREC
compute ideodiffdem = ideoself - ideodem.
if ideoself = 99 or ideodem = 99 ideodiffdem = 99.
recode ideodiffdem (11 thru hi=sysmis).

recode ideodiffdem (-10 thru -3=1) (-2 thru 2=2) (3 thru 10=3) (else=sysmis) into ideodiffdemREC.
variable label ideodiffdemREC “Ideological distance between self and Democratic Party”.
value label ideodiffdemREC
1 “Self less liberal than Dem Party (-10 to -3)”
2 “No difference between self and Dem Party (-2 to 2)”
3 “Self more liberal than Dem Party (3 to 10)”



