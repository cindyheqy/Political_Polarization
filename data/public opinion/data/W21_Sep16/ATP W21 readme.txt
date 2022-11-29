PEW RESEARCH CENTER
Wave 21 American Trends Panel 
Dates: September 27-October 10, 2016
Mode: Web
Language: English and Spanish
N=4,132

***************************************************************************************************************************

NOTES

There was a programming error for question PRIMARYPAST. There were 35 (out of 3615) cases that should have been asked the question but were not. Affected cases are coded as 
98 Not asked. 


There was a programming error for question FIRSTPRIM. There were 49 (out of 74) cases that should have been asked the question but were not. Affected cases are coded as 
98 Not asked. 


There was a programming error for question FIRSTGELECTb. There were 102 (out of 157) cases that should have been asked the question but were not. Affected cases are coded as 
98 Not asked. 


There was a programming error for question PTYPRIMARYPAST. The answer choices were not randomized when they were supposed to have been. 



The following coded variables are included at the end of the dataset. Syntax is provided below. 
VOTEGENHORSE_W21
VOTEGENHORSEGP_W21
VOTEGENHORSE2_W21
VOTEGENHORSE2GP_W21
CONTESTEDSENATE_W21
STRAIGHTTICKET_W21



***************************************************************************************************************************

WEIGHTS 


WEIGHT_W21 is the weight for the sample. 
Data for all Pew Research Center reports are analyzed using this weight.


***************************************************************************************************************************

SYNTAX (if applicable)


Please create VOTEGENHORSE as follows and include variable in dataset:
do if F_REG_FINAL=1.
compute VOTEGENHORSE=0.
if VOTEGENA_W21=1 or VOTEGENB_W21=1 VOTEGENHORSE=1.
if VOTEGENA_W21=2 or VOTEGENB_W21=2 VOTEGENHORSE=2.
if VOTEGENA_W21=3 or VOTEGENB_W21=3 VOTEGENHORSE=3.
if VOTEGENA_W21=4 or VOTEGENB_W21=4 VOTEGENHORSE=4.
if VOTEGENB_W21 ge 5 VOTEGENHORSE=9.
end if.
exe.

var lab VOTEGENHORSE ‘2016 Horserace summary variable’.
val lab VOTEGENHORSE 1 ‘Trump/Lean Trump’ 2 ‘Clinton/Lean Clinton’ 3 ‘Johnson/Lean Johnson’ 4 ‘Stein/Lean Stein’ 9 ‘DK-refused to lean’.

Please create VOTEGENHORSEGP as follows and include variable in dataset:
compute VOTEGENHORSEGP=0.
if VOTEGENA_W21=1 or VOTEGENB_W21=1 VOTEGENHORSEGP=1.
if VOTEGENA_W21=2 or VOTEGENB_W21=2 VOTEGENHORSEGP=2.
if VOTEGENA_W21=3 or VOTEGENB_W21=3 VOTEGENHORSEGP=3.
if VOTEGENA_W21=4 or VOTEGENB_W21=4 VOTEGENHORSEGP=4.
if VOTEGENB_W21 ge 5 VOTEGENHORSEGP=9.
exe.

var lab VOTEGENHORSEGP ‘2016 Horserace summary variable’.
val lab VOTEGENHORSEGP 1 ‘Trump/Lean Trump’ 2 ‘Clinton/Lean Clinton’ 3 ‘Johnson/Lean Johnson’ 4 ‘Stein/Lean Stein’ 9 ‘DK-refused to lean’.

Please create VOTEGENHORSE2 as follows and include variable in dataset:
do if F_REG_FINAL=1.
compute VOTEGENHORSE2=0.
if (VOTEGENA_W21=1 or VOTEGENB_W21=1 or VOTEGEND_W21=1) VOTEGENHORSE2=1.
if (VOTEGENA_W21=2 or VOTEGENB_W21=2 or VOTEGEND_W21=2) VOTEGENHORSE2=2.
if VOTEGENB_W21=5 VOTEGENHORSE2=3.
if VOTEGENB_W21=99 or VOTEGEND_W21=99 VOTEGENHORSE2=9.
end if.
exe.

var lab VOTEGENHORSE2 ‘2016 Horserace summary variable’.
val lab VOTEGENHORSE2 1 ‘Trump/Lean Trump’ 2 ‘Clinton/Lean Clinton’ 3 ‘Neither/other-refused to lean’ 9 ‘DK-refused to lean’.

Please create VOTEGENHORSE2GP as follows and include variable in dataset:
compute VOTEGENHORSE2GP=0.
if (VOTEGENA_W21=1 or VOTEGENB_W21=1 or VOTEGEND_W21=1) VOTEGENHORSE2GP=1.
if (VOTEGENA_W21=2 or VOTEGENB_W21=2 or VOTEGEND_W21=2) VOTEGENHORSE2GP=2.
if VOTEGENB_W21=5 VOTEGENHORSE2GP=3.
if VOTEGENB_W21=99 or VOTEGEND_W21=99 VOTEGENHORSE2GP=9.
end if.
exe.

var lab VOTEGENHORSE2 ‘2016 Horserace summary variable’.
val lab VOTEGENHORSE2 1 ‘Trump/Lean Trump’ 2 ‘Clinton/Lean Clinton’ 3 ‘Neither/other-refused to lean’ 9 ‘DK-refused to lean’.

Please create CONTESTEDSENATE as follows and include variable in dataset:
compute CONTESTEDSENATE = F_STATE_FINAL.
recode CONTESTEDSENATE (1,2,4,5,8,9,12,13,15,16,17,18,19,20,21,22,24,29,32,33,36,37,38,39,40,41,42,45,46,49,50,53,55=1) (6,10,11,23,25,26,27,28,30,31,34,35,44,47,48,51,54,56,99=0).
var label CONTESTEDSENATE “States with both major party candidates on the ballot”.
val label CONTESTEDSENATE 0 “No contested race” 1 “Contested senate race”.

Please create STRAIGHTTICKET as follows and include variable in dataset:

compute STRAIGHTTICKET = 0.

if (votegena ge 3 or votegenb ge 3) straightticket=7.

do if contestedsenate=0 and (F_STCD_W21 ne (0617 or 0629 or 0632 or 0634 or 0637 or 0644 or 0646)).
if (votegena=1 or votegenb=1) and (cong=1 or conga=1) straightticket=1.
if (votegena=1 or votegenb=1) and (cong=3 or conga ge 3) straightticket=3.
if (votegena=2 or votegenb=2) and (cong=2 or conga=2) straightticket=4.
if (votegena=2 or votegenb=2) and (cong=3 or conga ge 3) straightticket=6.
if (votegena=1 or votegenb=1) and (cong=2 or conga=2) straightticket=2.
if (votegena=2 or votegenb=2) and (cong=1 or conga=1) straightticket=5.
end if.

do if contestedsenate=1.
if (votegena=1 or votegenb=1) and (cong=1 or conga=1) and (sen=1 or sena=1) straightticket=1.
if (votegena=1 or votegenb=1) and ((cong=3 or conga ge 3) or (sen=3 or sena ge 3)) straightticket=3.
if (votegena=2 or votegenb=2) and (cong=2 or conga=2) and (sen=2 or sena=2) straightticket=4.
if (votegena=2 or votegenb=2) and ((cong=3 or conga ge 3) or (sen=3 or sena ge 3)) straightticket=6.
if (votegena=1 or votegenb=1) and ((cong=2 or conga=2) or (sen=2 or sena=2)) straightticket=2.
if (votegena=2 or votegenb=2) and ((cong=1 or conga=1) or (sen=1 or sena=1)) straightticket=5.
end if.

do if F_STCD_W21 eq (0617 or 0629 or 0632 or 0634 or 0637 or 0644 or 0646).
if (votegena=1 or votegenb=1) straightticket=3.
if (votegena=2 or votegenb=2) straightticket=6.
end if.

var label STRAIGHTTICKET “Straight ticket voting”.
val label STRAIGHTTICKET 1 “Republican straight ticket” 2 “Rep pres/Dem cong” 3 “Rep pres/other cong” 4 “Democrat straight ticket” 5 “Dem pres/Rep cong” 6 “Dem pres/other cong” 7 “Other Pres”.
