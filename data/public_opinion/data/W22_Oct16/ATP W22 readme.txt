PEW RESEARCH CENTER
Wave W22 American Trends Panel 
Dates: October 25-November 8, 2016
Mode: Web
Language: English and Spanish
N=4,265

***************************************************************************************************************************
NOTES

There was a programming error for question PTYPRIMARYPAST. The answer choices were not randomized when they were supposed to have been. 


Pew Research Center reports from W22 used W16 primary preference (first choice) to analyze the results. Values were 
imputed for respondents to W22 who did not respond to W16. These variables are available upon request.


The following coded variables are included at the end of the dataset. Syntax is provided below. 
VOTEGENHORSE_W22
VOTEGENHORSEGP_W22
VOTEGENHORSE2_W22
VOTEGENHORSE2GP_W22



***************************************************************************************************************************
WEIGHTS 


WEIGHT_W22 is the weight for the sample.
Data for all Pew Research Center reports are analyzed using this weight.


***************************************************************************************************************************
SYNTAX (if applicable)


Please create VOTEGENHORSE as follows and include variable in dataset:
do if F_REG_FINAL=1.
compute VOTEGENHORSE=0.
if VOTEGENA_W22=1 or VOTEGENB_W22=1 VOTEGENHORSE=1.
if VOTEGENA_W22=2 or VOTEGENB_W22=2 VOTEGENHORSE=2.
if VOTEGENA_W22=3 or VOTEGENB_W22=3 VOTEGENHORSE=3.
if VOTEGENA_W22=4 or VOTEGENB_W22=4 VOTEGENHORSE=4.
if VOTEGENB_W22 ge 5 VOTEGENHORSE=9.
end if.
exe.

var lab VOTEGENHORSE ‘2016 Horserace summary variable’.
val lab VOTEGENHORSE 1 ‘Trump/Lean Trump’ 2 ‘Clinton/Lean Clinton’ 3 ‘Johnson/Lean Johnson’ 4 ‘Stein/Lean Stein’ 9 ‘DK-refused to lean’.

Please create VOTEGENHORSEGP as follows and include variable in dataset:
compute VOTEGENHORSEGP=0.
if VOTEGENA_W22=1 or VOTEGENB_W22=1 VOTEGENHORSEGP=1.
if VOTEGENA_W22=2 or VOTEGENB_W22=2 VOTEGENHORSEGP=2.
if VOTEGENA_W22=3 or VOTEGENB_W22=3 VOTEGENHORSEGP=3.
if VOTEGENA_W22=4 or VOTEGENB_W22=4 VOTEGENHORSEGP=4.
if VOTEGENB_W22 ge 5 VOTEGENHORSEGP=9.
exe.

var lab VOTEGENHORSEGP ‘2016 Horserace summary variable’.
val lab VOTEGENHORSEGP 1 ‘Trump/Lean Trump’ 2 ‘Clinton/Lean Clinton’ 3 ‘Johnson/Lean Johnson’ 4 ‘Stein/Lean Stein’ 9 ‘DK-refused to lean’.

Please create VOTEGENHORSE2 as follows and include variable in dataset:
do if F_REG_FINAL=1.
compute VOTEGENHORSE2=0.
if (VOTEGENA_W22=1 or VOTEGENB_W22=1 or VOTEGEND_W22=1) VOTEGENHORSE2=1.
if (VOTEGENA_W22=2 or VOTEGENB_W22=2 or VOTEGEND_W22=2) VOTEGENHORSE2=2.
if VOTEGENB_W22=5 VOTEGENHORSE2=3.
if VOTEGENB_W22=99 or VOTEGEND_W22=99 VOTEGENHORSE2=9.
end if.
exe.

var lab VOTEGENHORSE2 ‘2016 Horserace summary variable’.
val lab VOTEGENHORSE2 1 ‘Trump/Lean Trump’ 2 ‘Clinton/Lean Clinton’ 3 ‘Neither/other-refused to lean’ 9 ‘DK-refused to lean’.

Please create VOTEGENHORSE2GP as follows and include variable in dataset:
compute VOTEGENHORSE2GP=0.
if (VOTEGENA_W22=1 or VOTEGENB_W22=1 or VOTEGEND_W22=1) VOTEGENHORSE2GP=1.
if (VOTEGENA_W22=2 or VOTEGENB_W22=2 or VOTEGEND_W22=2) VOTEGENHORSE2GP=2.
if VOTEGENB_W22=5 VOTEGENHORSE2GP=3.
if VOTEGENB_W22=99 or VOTEGEND_W22=99 VOTEGENHORSE2GP=9.
end if.
exe.

var lab VOTEGENHORSE2GP ‘2016 Horserace summary variable’.
val lab VOTEGENHORSE2GP 1 ‘Trump/Lean Trump’ 2 ‘Clinton/Lean Clinton’ 3 ‘Neither/other-refused to lean’ 9 ‘DK-refused to lean’.

