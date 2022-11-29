PEW RESEARCH CENTER
Wave 31 American Trends Panel 
Dates: January 29-February 13, 2018
Mode: Web
Language: English and Spanish
N=4,656

***************************************************************************************************************************

WEIGHTS 

WEIGHT_W31 is the weight for the sample. 
Data for all Pew Research Center reports are analyzed using this weight.


***************************************************************************************************************************


To protect the privacy of respondents, telephone numbers, county of residence and zip code have been removed from the data file.


***************************************************************************************************************************

Releases from this survey:

April 26, 2018. "The Public, the Political System and American Democracy"
http://www.people-press.org/2018/04/26/the-public-the-political-system-and-american-democracy/

Blog posts from this survey:

March 29, 2018 "Why do people belong to a party? Negative views of opposing party are a major factor" 
http://www.pewresearch.org/fact-tank/2018/03/29/why-do-people-belong-to-a-party-negative-views-of-the-opposing-party-are-a-major-factor/


***************************************************************************************************************************

SYNTAX

ENGAGEMENT MEASURE:
The variable ENGAGEINDEX_W31 was used to assess political engagment among panelists (NOTE: the social media item [CIVIC_ENG_ACTJ_W31] was excluded from this index).

recode CIVIC_ENG_ACTA_W31 (1=2) (2=1) (else=0) into eng_event.
recode CIVIC_ENG_ACTC_W31 (1=2) (2=1) (else=0) into eng_vol.
recode CIVIC_ENG_ACTG_W31(1=2) (2=1) (else=0) into eng_contact.
recode CIVIC_ENG_ACTH_W31 (1=2) (2=1) (else=0) into eng_contribute.
recode CIVIC_ENG_ACTK_W31 (1=2) (2=1) (else=0) into eng_commgov.
recode folgov_w31 (1=1) (2=.67) (3=.33) (4=0) (else=0) into folgov_w31rec.
recode oftvote_w31(1=1) (2=.67) (3=.33) (4=0) (else=0) into oftvote_w31rec.

compute engage_add=eng_event+eng_vol+eng_contact+eng_contribute+eng_commgov+folgov_w31rec+oftvote_w31rec.

VAR lab engage_add_trimod 'engagement and participation additive scale, split into rough terciles'.
val lab engage_add_trimod 1 'low engage-particip' 2 'mid engage-particip' 3 'high engage-particip'.

RENAME VARIABLES (engage_add_trimod=ENGAGEINDEX_W31).


CIVIC KNOWLEDGE INDEX:

compute KNOWLEDGE=0.
if KNOWCIV1_W31=1 KNOWLEDGE = KNOWLEDGE+1.
if KNOWCIV2_W31=2 KNOWLEDGE = KNOWLEDGE+1.
if KNOWCIV3_W31=3 KNOWLEDGE = KNOWLEDGE+1.
if KNOWCIV5_W31=4 KNOWLEDGE = KNOWLEDGE+1.
execute.	

recode KNOWLEDGE (4=1) (2 thru 3=2)(0 thru 1=3).

value label KNOWLEDGE (1) High (2) Medium (3) Low.
variable label KNOWLEDGE “Civic knowledge index”.


