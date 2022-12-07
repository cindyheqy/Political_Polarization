PEW RESEARCH CENTER
Wave 18 American Trends Panel 
Dates: June 7-July 5, 2016
Mode: Web and Mail 
Language: English and Spanish
N=4,602

***************************************************************************************************************************
NOTES

Questionnaire and topline reflect questions presented in web mode. Mail mode questionnaires available upon request. 

The following variables are recoded based on open-end responses:
clergy_other_1_other_oe1_w18
clergy_other_1_other_oe2_w18


The following variables may include backcoding based on open-end responses:
clergy_support_w18
clergy_support2_1_w18
clergy_support2_2_w18
clergy_support2_3_w18
clergy_support2_4_w18
clergy_support2_5_w18
clergy_support2_6_w18
clergy_against_w18
clergy_against2_1_w18
clergy_against2_2_w18
clergy_against2_3_w18
clergy_against2_4_w18
clergy_against2_5_w18
clergy_against2_6_w18



***************************************************************************************************************************
WEIGHTS 


WEIGHT_W18 is the weight for the combined sample of all web and mail interviews. 
Data for all Pew Research Center reports are analyzed using this weight.



***************************************************************************************************************************
SYNTAX (if applicable)

*Create combination variables for 'Turned to any of the following for campaign news'.
compute candcntct_email = candcntct_a_w18.
if candcntct_b_w18 eq 1 candcntct_email eq 1. 
variable labels candcntct_email 'Got campaign news via email from either campaign'.
value labels candcntct_email 1 'Yes'.

compute candcntct_sns = candcntct_c_w18.
if candcntct_d_w18 eq 1 candcntct_sns eq 1. 
variable labels candcntct_sns 'Got campaign news via social media posts from either campaign'.
value labels candcntct_sns 1 'Yes'.

compute candcntct_website = candcntct_e_w18.
if candcntct_f_w18 eq 1 candcntct_website eq 1. 
variable labels candcntct_website 'Got campaign news via campaign website from either campaign'.
value labels candcntct_website 1 'Yes'.



