PEW RESEARCH CENTER
Wave 40 American Trends Panel 
Dates: November 27-December 10, 2018
Mode: Web 

Sample: Full panel
Language: English and Spanish
N=10,618

***************************************************************************************************************************
NOTES

The following variables were created through thematic coding done by researchers on responses to open-ended survey items. For instances in which responses touched 
on more than one of the themes highlighted in the coding scheme, respondents were assigned multiple codes in the order in which each theme was mentioned in their
response. The coded variables below represent the first, second, and third mentions of themes from the coding scheme within individual item responses (as applicable).

PROBSOPEN1a_W40_OE1
PROBSOPEN1a_W40_OE2
PROBSOPEN1a_W40_OE3
PROBSOPEN1a_REFUSED_W40
PROBSOPEN1b_W40_OE1
PROBSOPEN1b_W40_OE2
PROBSOPEN1b_W40_OE3
PROBSOPEN1b_REFUSED_W40
SOLVE2_W40_OE1
SOLVE2_W40_OE2
SOLVE2_W40_OE3
SOLVE2_W40_REFUSED
INSTCONF2_W40_OE1
INSTCONF2_W40_OE2
INSTCONF2_W40_OE3
INSTCONF2_W40_REFUSED
TRUSTCURE2_W40_OE1
TRUSTCURE2_W40_OE2
TRUSTCURE2_W40_OE3
TRUSTCURE2_W40_REFUSED
AVOID2_W40_OE1
AVOID2_W40_OE2
AVOID2_W40_OE3
AVOID2_W40_REFUSED
AVOID4_W40_OE1
AVOID4_W40_OE2
AVOID4_W40_OE3
AVOID4_W40_REFUSED
PERSCONF2_W40_OE1
PERSCONF2_W40_OE2
PERSCONF2_W40_OE3
PERSCONF2_W40_REFUSED
TRUSTCURE4_W40_OE1
TRUSTCURE4_W40_OE2
TRUSTCURE4_W40_OE3
TRUSTCURE4_W40_REFUSED
QB1EXP_W40_OE1
QB1EXP_W40_OE2
QB1EXP_W40_OE3
QB1EXP_W40_REFUSED

***************************************************************************************************************************
WEIGHTS 


WEIGHT_W40 is the weight for the sample. Data for all Pew Research Center reports are analyzed using this weight.


***************************************************************************************************************************
Releases from this survey:

July 22, 2019. "Key findings about Americans’ declining trust in government and each other"
https://www.pewresearch.org/fact-tank/2019/07/22/key-findings-about-americans-declining-trust-in-government-and-each-other/

July 22, 2019. "Trust and Distrust in America"
https://www.people-press.org/2019/07/22/trust-and-distrust-in-america/

August 6, 2019. "Young Americans are less trusting of other people – and key institutions – than their elders"
https://www.pewresearch.org/fact-tank/2019/08/06/young-americans-are-less-trusting-of-other-people-and-key-institutions-than-their-elders/

September 19, 2019. "Americans’ perceptions about unethical behavior shape how they think about people in powerful roles"
https://www.pewresearch.org/fact-tank/2019/09/19/americans-perceptions-about-unethical-behavior-shape-how-they-think-about-people-in-powerful-roles/

September 19, 2019. "Why Americans Don’t Fully Trust Many Who Hold Positions of Power and Responsibility"
https://www.people-press.org/2019/09/19/why-americans-dont-fully-trust-many-who-hold-positions-of-power-and-responsibility/

March 5, 2020. "Most Americans rely on their own research to make big decisions, and that often means online searches"
https://www.pewresearch.org/fact-tank/2020/03/05/most-americans-rely-on-their-own-research-to-make-big-decisions-and-that-often-means-online-searches/

March 11, 2020. "About one-in-four Americans say they’ve had fewer advantages in life than others their age"
https://www.pewresearch.org/fact-tank/2020/03/11/about-one-in-four-americans-say-theyve-had-fewer-advantages-in-life-than-others-their-age/

***************************************************************************************************************************
SYNTAX

The syntax below can be used to create the variable 'trustindex', which was used for published analysis of this wave's data.

recode soctrust2_w40 (1=1) (2=0) (99=9) into trust.
recode gsstrust2_w40 (2=1) (1=0) (99=9)  into fair.
recode gsstrust3_w40 (1=1) (2=0) (99=9) into help.

missing values trust fair help (9).

compute index_temp= trust + fair + help.
if (trust=9 or fair=9 or help=9) index_temp=9.

recode index_temp (0,1=1) (2=2) (3=3) (9=9) into trustindex.

VALUE LABELS trustindex 1 'Low' 2 'Middle' 3 'High' 9 'DK/Ref'.
VARIABLE LABELS trustindex "Index measuring trust in others as indicated by responses to items SOCTRUST2, GSSTRUST2, and GSSTRUST3".

