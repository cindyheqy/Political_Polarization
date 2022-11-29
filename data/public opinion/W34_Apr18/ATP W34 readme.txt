PEW RESEARCH CENTER
Wave 34 American Trends Panel 
Dates: April 23-May 6, 2018
Mode: Web
Sample: Subsample
Language: English and Spanish
N=2,537

***************************************************************************************************************************
NOTES

The following variables are included in the dataset as coded open end responses that have been collapsed into fewer categories. Responses to the first three mentions have been included. 
NOBIOTECH_OE1_W34
NOBIOTECH_OE2_W34
NOBIOTECH_OE3_W34

Respondents who took the science knowledge question in W17 did not receive them in W34. KNOSCT22_W17W34 - KNOSCT_INDEX_W17W34 combines science knowledge variables from both W17 and W34. These variables were used in all Pew Research Center reports from this survey.

KNOSCTINDEX_W17W34 is a variable is the sum of number of correct answers to the science knowledge questions. 
  
***************************************************************************************************************************
WEIGHTS 

WEIGHT_W34 is the weight for the sample. Data for all Pew Research Center reports are analyzed using this weight.


***************************************************************************************************************************
Releases from this survey:

Reports

How highly religious Americans view evolution depends on how they’re asked about it (Feb. 6, 2019)
https://www.pewresearch.org/fact-tank/2019/02/06/how-highly-religious-americans-view-evolution-depends-on-how-theyre-asked-about-it/

Public perspectives on food risks (Nov. 19, 2018)
https://www.pewresearch.org/science/2018/11/19/public-perspectives-on-food-risks/

Most Americans accept genetic engineering of animals that benefits human health, but many oppose other uses (Aug. 16, 2018)
https://www.pewresearch.org/science/2018/08/16/most-americans-accept-genetic-engineering-of-animals-that-benefits-human-health-but-many-oppose-other-uses/

Public views of gene editing for babies depend on how it would be used (July 26, 2018)
https://www.pewresearch.org/science/2018/07/26/public-views-of-gene-editing-for-babies-depend-on-how-it-would-be-used/

FactTank

For Darwin Day, 6 facts about the evolution debate (Feb. 11, 2019)
https://www.pewresearch.org/fact-tank/2019/02/11/darwin-day/

Americans are divided over whether eating organic foods makes for better health (Nov. 26, 2018)
https://www.pewresearch.org/fact-tank/2018/11/26/americans-are-divided-over-whether-eating-organic-foods-makes-for-better-health/

When it comes to food ingredients, health-oriented eaters have a list they avoid (Nov. 21, 2018)
https://www.pewresearch.org/fact-tank/2018/11/21/when-it-comes-to-food-ingredients-health-oriented-eaters-have-a-list-they-avoid/

Americans are narrowly divided over health effects of genetically modified foods (Nov. 19, 2018)
https://www.pewresearch.org/fact-tank/2018/11/19/americans-are-narrowly-divided-over-health-effects-of-genetically-modified-foods/

A majority of Americans support using biotechnology to grow human organs in animals for transplants (Aug. 20, 2018)
https://www.pewresearch.org/fact-tank/2018/08/20/a-majority-of-americans-support-using-biotechnology-to-grow-human-organs-in-animals-for-transplants/

Americans are divided over the use of animals in scientific research (Aug, 16, 2018)
https://www.pewresearch.org/fact-tank/2018/08/16/americans-are-divided-over-the-use-of-animals-in-scientific-research/

More Americans anticipate downsides than upsides from gene editing for babies (July 26, 2018)
https://www.pewresearch.org/fact-tank/2018/07/26/more-americans-anticipate-downsides-than-upsides-from-gene-editing-for-babies/

Americans are closely divided over value of medical treatments, but most agree costs are a big problem (July 9, 2018)
https://www.pewresearch.org/fact-tank/2018/07/09/americans-are-closely-divided-over-value-of-medical-treatments-but-most-agree-costs-are-a-big-problem/

Americans broadly favor government funding for medical and science research (July 3, 2018)
https://www.pewresearch.org/fact-tank/2018/07/03/americans-broadly-favor-government-funding-for-medical-and-science-research/



***************************************************************************************************************************
SYNTAX

F_RELCOM3CAT_FINAL is an index variable that combines frequency of religious attendance, frequency of prayer and importance of religion. 

A person is considered to have a high level of religious commitment if they attend religious services at least weekly, pray at least daily and say religion is very important in their life. People are classified as having low commitment if they say religion is not too or not at all important in their lives and that they seldom or never attend religious services or pray. All others are classified as having medium commitment.

recode RELIMP_FINAL (1=1) (else=0) into highsalience.
recode F_ATTEND_FINAL (1,2=1) (else=0) into highattend.
recode PRAY_FINAL (1,2=1) (else=0) into highprayer.
count high = highsalience highattend highprayer (1).

recode RELIMP_FINAL (3,4=1) (else=0) into lowsalience.
recode F_ATTEND_FINAL (5,6=1) (else=0) into lowattend.
recode PRAY_FINAL (6,7=1) (else=0) into lowprayer.
count low = lowsalience lowattend lowprayer (1).

compute F_RELCOM3CAT_FINAL=2.
if high=3 F_RELCOM3CAT_FINAL =1.
if low=3 F_RELCOM3CAT_FINAL =3.
if RELIMP_FINAL=99 or F_ATTEND_FINAL=99 or PRAY_FINAL=99 F_RELCOM3CAT_FINAL =9.
IF  SYSMIS(RELIMP_FINAL) OR SYSMIS(F_ATTEND_FINAL) OR SYSMIS(PRAY_FINAL) F_RELCOM3CAT_FINAL=$SYSMIS.
val label F_RELCOM3CAT_FINAL 1 'High' 2 'Medium' 3 'Low' 9 'DK/Ref'. 
var label F_RELCOM3CAT_FINAL 'religious commitment – 3 categories'.

formats F_RELCOM3CAT_FINAL (f1.0).


The following syntax can be used to compute the count variable of EAT3 referenced in this FactTank post: https://www.pewresearch.org/fact-tank/2018/11/21/when-it-comes-to-food-ingredients-health-oriented-eaters-have-a-list-they-avoid/

compute EAT3_W34_index=EAT3A_W34 + EAT3B_W34 + EAT3C_W34 + EAT3D_W34 + EAT3E_W34 + EAT3F_W34 + EAT3G_W34 + EAT3H_W34 + EAT3I_W34 + EAT3J_W34.
if (EAT3K_W34=1) EAT3_W34_index=0.
if (EAT3REF_W34=99) EAT3_W34_index=99.

variable labels EAT3_W34_index 'Number of items selected in EAT3 (restrict or limit eating on a regular basis)'.
value labels EAT3_W34_index 99 'Refused all in set'.

formats EAT3_W34_index (f1.0).

execute.
