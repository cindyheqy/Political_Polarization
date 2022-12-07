PEW RESEARCH CENTER
Wave W24 American Trends Panel 
Dates: January 9-January 23, 2017
Mode: Web
Language: English and Spanish
N=4,248

***************************************************************************************************************************
NOTES


In the final sample, 7.3% of panelists (N=309) were presented REL3 without a slider. These respondents are not included in the analysis.
Analysis for REL3 should be based only on those (N=3,939) who received the slider, defined as variable REL3_TYPE_W24=2.


The following coded variables are included at the end of the dataset. Syntax is provided below. 
ON7RECTOTA_W24
ON7RECTOTB_W24
ON7RECTOTC_W24
ON7RECTOTD_W24
ON7RECTOTE_W24
ON7RECTOTH_W24
ON7RECTOTI_W24
ON7RECTOTREF_W24


***************************************************************************************************************************
WEIGHTS 


WEIGHT_W24 is the weight for the sample. 
Data for all Pew Research Center reports are analyzed using this weight.




***************************************************************************************************************************
SYNTAX

*/Create ON7RECTOT_W24 by combining ON7 responses with ON7REC responses

COMPUTE ON7RECTOTA_W24=$SYSMIS.
COMPUTE ON7RECTOTB_W24=$SYSMIS.
COMPUTE ON7RECTOTC_W24=$SYSMIS.
COMPUTE ON7RECTOTD_W24=$SYSMIS.
COMPUTE ON7RECTOTE_W24=$SYSMIS.
COMPUTE ON7RECTOTH_W24=$SYSMIS.
COMPUTE ON7RECTOTI_W24=$SYSMIS.
COMPUTE ON7RECTOTREF_W24=$SYSMIS.
IF (ON7_YES_W24=1 AND ON7_A_W24=1) OR (ON7REC_A_W24=1) ON7RECTOTA_W24=1.
IF (ON7_YES_W24=1 AND ON7_B_W24=1) OR (ON7REC_B_W24=1) ON7RECTOTB_W24=1.
IF (ON7_YES_W24=1 AND ON7_C_W24=1) OR (ON7REC_C_W24=1) ON7RECTOTC_W24=1.
IF (ON7_YES_W24=1 AND ON7_D_W24=1) OR (ON7REC_D_W24=1) ON7RECTOTD_W24=1.
IF (ON7_YES_W24=1 AND ON7_E_W24=1) OR (ON7REC_E_W24=1) ON7RECTOTE_W24=1.
IF (ON7_YES_W24=1 AND ON7_H_W24=1) OR (ON7REC_H_W24=1) ON7RECTOTH_W24=1.
IF (ON7REC_I_W24=1) ON7RECTOTI_W24=1.
IF (ON7RECREF_W24=99) ON7RECTOTREF_W24=1.
EXECUTE.


VALUE LABELS ON7RECTOTA_W24
1 Being called offensive names.
VALUE LABELS ON7RECTOTB_W24
1 Being physically threatened.
VALUE LABELS ON7RECTOTC_W24
1 Being harassed for a sustained period.
VALUE LABELS ON7RECTOTD_W24
1 Being stalked.
VALUE LABELS ON7RECTOTE_W24
1 Having someone try to purposefully embarrass you.
VALUE LABELS ON7RECTOTH_W24
1 Being sexually harassed. 
VALUE LABELS ON7RECTOTI_W24
1 None of these. 
VALUE LABELS ON7RECTOTREF_W24
1 Refused all items in set. 
fre ON7RECTOTA_W24 ON7RECTOTB_W24 ON7RECTOTC_W24 ON7RECTOTD_W24 ON7RECTOTE_W24 ON7RECTOTH_W24 ON7RECTOTI_W24 ON7RECTOTREF_W24.

VARIABLE LABELS ON7RECTOTA_W24 Being called offensive names (ON7 and ON7REC Combined).
VARIABLE LABELS ON7RECTOTB_W24 Being physically threatened (ON7 and ON7REC Combined).
VARIABLE LABELS ON7RECTOTC_W24 Being harassed for a sustained period (ON7 and ON7REC Combined).
VARIABLE LABELS ON7RECTOTD_W24 Being stalked (ON7 and ON7REC Combined).
VARIABLE LABELS ON7RECTOTE_W24 Having someone try to purposefully embarrass you (ON7 and ON7REC Combined).
VARIABLE LABELS ON7RECTOTH_W24 Being sexually harassed (ON7 and ON7REC Combined).
VARIABLE LABELS ON7RECTOTI_W24 None of these (ON7REC).
VARIABLE LABELS ON7RECTOTH_W24 Refused all at ON7REC (ON7REC).



