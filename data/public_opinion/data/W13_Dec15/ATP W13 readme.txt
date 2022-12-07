PEW RESEARCH CENTER
Wave 13 American Trends Panel 
Dates: Nov 24-Dec 21, 2015
Mode: Web and Mail 
Language: English and Spanish
N=4,787

***************************************************************************************************************************

NOTES


Questionnaire and topline reflect questions presented in web mode. Mail mode questionnaires available upon request. 


The Wave 13 survey featured two questions (DEMNOMOE and REPNOMOE) that asked all panelists who their choice was for the Democratic and Republican nominations for the 2016 presidential 
election and allowed panelists to enter up to three choices. The questions were set up to be randomized in order on the web survey. Quality control measures conducted during the soft 
launch revealed a bug in the software that assigns how blocks of questions are randomized resulting in two programming issues for these questions. 

The soft launch revealed that 10 panelists were not presented one or both of these questions. The result was that 1 panelist did not get both questions, two were presented 
the question about the Republican nomination but not the Democratic nomination while 7 were presented the Democratic nomination but not the Republican. A variable called 
DEMREP_MISSING_W13 was added to the data to flag these 10 cases. 

For the first two days of fielding, mobile web respondents were forced to enter something into all three of the 
textboxes for DEMNOMOE and REPNOMOE, while desktop web respondents were not. As a result, some mobile respondents may have
entered more names than they would have otherwise. The 494 cases that were affected by this are flagged in the dataset
in variable FLAG_W13 with cases separated into three groups noting the levels of risk introduced by the programming error. "Minimal risk"
included 264 respondents that entered "none" or "N/A" or other non-candidate answers and moved to the next question. "Low
risk" included 152 respondents that gave 3 candidates to one party and gave less than 3 candidates to the other party.
"High risk" includes 78 respondents that gave 3 candidates for both parties.


The following variables are recoded based on open-end responses:
DEM1_W13 (DEMNOMOE first choice)
DEM2_W13 (DEMNOMOE second choice)
DEM3_W13 (DEMNOMOE third choice)
REP1_W13 (REPNOMOE first choice)
REP2_W13 (REPNOMOE second choice)
REP3_W13 (REPNOMOE third choice)

***************************************************************************************************************************

WEIGHTS 


WEIGHT_W13 is the weight for the combined sample of all web and mail interviews. 
Data for all Pew Research Center reports are analyzed using this weight.



***************************************************************************************************************************
SYNTAX (if applicable)


