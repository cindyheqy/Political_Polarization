PEW RESEARCH CENTER
Wave 14 American Trends Panel 
Dates: Jan 12-Feb 8, 2016
Mode: Web and Mail 
Language: English and Spanish
N=4,654

***************************************************************************************************************************

NOTES
   

Questionnaire and topline reflect questions presented in web mode. Mail mode questionnaires available upon request. 


Google+ was removed from analysis in Wave 14 as a social networking site.SNS_C_W14 and SNSNEWSC_W14 were and should be removed from analysiS.
The bases for SNSSOURCE_W14, the SNSACT battery, HASHTAG_W14, and the SNS2A batter should be changed accordingly.
The base for SNSPICTURE_W14 should not be changed as it was reported on in its original form in an earlier report. 


There was an error by the vendor in translating item D for NEWS_PLATFORM to Spanish. The question in the Spanish language survey incorrectly omitted the word “local.” 
This affected the 66 respondents who took the survey in Spanish (4% of the sample after weighting).

NEWS_PLATFORM	And how often do you… [RANDOMIZE]

d.	Watch local television news? 

Translation used:
d.         Ve las noticias por la televisión

Correct translation:
d.         Ve las noticias por un canal local de la televisión


***************************************************************************************************************************
WEIGHTS 

The weighting protocol was changed in Wave 14 to include weighting to targets for Volunteering and Daily Internet Use, and Social Media Usage.

WEIGHT_W14_SOCIALMEDIA is the weight for the combined sample of all web and mail interviews.
Data for all Pew Research Center reports are analyzed using this weight.



***************************************************************************************************************************
SYNTAX

*Syntax for combining local voting questions*.
recode VOTEC_W14 (1=1) (2-5=2) (else=copy) into localvoting.
if F_REG_FINAL=2, localvoting=2.
if F_REG_FINAL=3, localvoting=2.
value labels localvoting 1'Always and registered' 2'Less often or unregistered'.
variable labels localvoting 'Local voting habits'.

*Syntax for creating an index of civic activity*.
count civeng = f_civ_eng_grpsa_rf1 to f_civic_eng_localf_rf1 (1).
if (f_civ_eng_grpsa_rf1 EQ 99) AND
(f_civ_eng_grpsb_rf1 EQ 99) AND
(f_civ_eng_grpsc_rf1 EQ 99) AND
(f_civ_eng_grpsd_rf1 EQ 99) AND
(f_civ_eng_grpse_rf1 EQ 99) AND
(f_civ_eng_grpsf_rf1 EQ 99) AND
(f_civ_eng_grpsg_rf1 EQ 99) AND
(f_civic_eng_locala_rf1 EQ 99) AND
(f_civic_eng_localb_rf1 EQ 99) AND
(f_civic_eng_localc_rf1 EQ 99) AND
(f_civic_eng_locald_rf1 EQ 99) AND
(f_civic_eng_locale_rf1 EQ 99) AND
(f_civic_eng_localf_rf1 EQ 99)
civeng = $SYSMIS.
recode civeng (0=1)(1-2=2)(3-13=3) (else=copy).
value labels civeng 1 'Not active' 2 'Somewhat active' 3 'Highly active'.
variable labels civeng 'Local civic participation'. 

*Syntax to create "Very/somewhat/non loyal" scale*.
compute medialoyal_comb = 2.
if (MEDIALOYAL2_W14 eq 1) and (MEDIALOYAL3_W14 eq 1) medialoyal_comb eq 1.
if (MEDIALOYAL2_W14 eq 2) and (MEDIALOYAL3_W14 eq 2) medialoyal_comb eq 3.
if MEDIALOYAL2_W14 eq 99 medialoyal_comb eq 99.
if MEDIALOYAL3_W14 eq 99 medialoyal_comb eq 99.
value labels labels medialoyal_comb 1 'Very loyal' 2 'Somewhat loyal' 3 'Non-loyal' 99 'Refused either'.
variable labels medialoyal_comb 'Loyalty measure'. 









