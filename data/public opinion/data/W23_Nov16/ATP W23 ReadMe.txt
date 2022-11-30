PEW RESEARCH CENTER
Wave 23 American Trends Panel 
Dates: November 29-December 12, 2016
Mode: Web
Language: English and Spanish
N=4,183

***************************************************************************************************************************
NOTES

Pew Research Center reports from W23 used W16 primary preference (first choice) to analyze the results. Values were imputed for respondents to W23 who did not respond to W16. These variables are available upon request.

VALIDATED_VOTER_2016_W23 is a computed variable indicating whether or not the respondent voted in the 2016 general election. An effort was made to match nearly all panelists (excluding noncitizens and those who declined to provide their names) to five different national commercial voter files. Panelists who had a 2016 turnout record in any of the five voter files are considered to have voted; those for whom no turnout record could be located in any of the five files are considered to be nonvoters. Additional detail about the computation of this variable can be found in Chapter 3 of this report: http://www.pewresearch.org/2018/02/15/commercial-voter-files-and-the-study-of-u-s-politics/
The validated voter variable was used in this report:
http://www.people-press.org/2018/08/09/an-examination-of-the-2016-electorate-based-on-validated-voters/

Coding of VALIDATED_VOTER_2016_W23
0 = Nonvoter
1 = Voter
System missing = Noncitizen or panelist for whom a voter file match could not be attempted because they have not provided their name

The dataset also includes a variable named COMPORT_W23. This variable has four categories, each corresponding to a combination of VALIDATED_VOTER_2016_W23 and the self-reported voter turnout question, VOTED_W23. The four categories of COMPORT are:
1=Validated voters who said they voted
2= Nonvoters who said they did not vote or were not sure
3=Overreporters (nonvoters who said they voted)
4=Underreporters (validated voters who said they did not vote or were not sure) 

In order to replicate the vote preference analysis published the report above, use the following syntax or similar logic:

*FOR VALIDATED VOTERS.
do if COMPORT_W23=1.
compute candprefvoter= votegenpost_w23.
missing values candprefvoter (5,99).
end if.
value labels candprefvoter 1 'Trump' 2 'Clinton' 3 'Johnson' 4 'Stein' 5 'Other' 99 'DK, Refused'.
var labels candprefvoter '2016 vote among validated voters'.
In order to replicate the profile of nonvoters, simply restrict the analysis to respondents who are listed as COMPORT_W23 = 2,3,4. 

***************************************************************************************************************************
WEIGHTS 

Data for all Pew Research Center reports are analyzed using the weight variable named WEIGHT_W23.


***************************************************************************************************************************
