PEW RESEARCH CENTER
Wave W33 American Trends Panel 
Dates: March 27-April 9, 2018
Mode: Web 
Sample: Subsample
Language: English and Spanish
N=2,541

***************************************************************************************************************************
NOTES

The following variables are included in the dataset as coded open end responses that have been collapsed into fewer categories. Responses to the first three mentions have been included. 
CLIM10_W33_OE1_col
CLIM10_W33_OE2_col
CLIM10_W33_OE3_col


***************************************************************************************************************************
WEIGHTS 

WEIGHT_W33 is the weight for the sample. Data for all Pew Research Center reports are analyzed using this weight.


***************************************************************************************************************************
Releases from this survey:

A majority of U.S. teens fear a shooting could happen at their school, and most parents share their concern, April 18, 2018
http://www.pewresearch.org/fact-tank/2018/04/18/a-majority-of-u-s-teens-fear-a-shooting-could-happen-at-their-school-and-most-parents-share-their-concern/

Majorities see government efforts to protect the environment as insufficient, May 14, 2018
https://www.pewresearch.org/science/2018/05/14/majorities-see-government-efforts-to-protect-the-environment-as-insufficient/

Many Republican Millennials differ with older party members on climate change and energy issues, May 14, 2018
https://www.pewresearch.org/science/2018/06/06/majority-of-americans-believe-it-is-essential-that-the-u-s-remain-a-global-leader-in-space/

Most Americans say climate change affects their local community, including two-thirds living near coast, May 16, 2018
https://www.pewresearch.org/fact-tank/2018/05/16/most-americans-say-climate-change-affects-their-local-community-including-two-thirds-living-near-coast/

Majority of Americans believe it is essential that the U.S. remain a global leader in space, June 6, 2018
https://www.pewresearch.org/science/2018/06/06/majority-of-americans-believe-it-is-essential-that-the-u-s-remain-a-global-leader-in-space/

Space tourism? Majority of Americans say they wouldn’t be interested, June 7, 2018
https://www.pewresearch.org/fact-tank/2018/06/07/space-tourism-majority-of-americans-say-they-wouldnt-be-interested/

Many in U.S. have confidence in what private space companies will accomplish, June 22, 2018
https://www.pewresearch.org/fact-tank/2018/06/22/many-in-u-s-have-confidence-in-what-private-space-companies-will-accomplish/

As debris piles up, Americans are skeptical enough will be done to limit space junk, August 31, 2018
https://www.pewresearch.org/fact-tank/2018/08/31/as-debris-piles-up-americans-are-skeptical-enough-will-be-done-to-limit-space-junk/


***************************************************************************************************************************
SYNTAX

The following syntax can be used to compute the two-item index referenced in the the report:
Majority of Americans believe it is essential that the U.S. remain a global leader in space, June 6, 2018
https://www.pewresearch.org/science/2018/06/06/majority-of-americans-believe-it-is-essential-that-the-u-s-remain-a-global-leader-in-space/


compute SPACE_heard_index_W33=$sysmis.
if (SPACE1_W33=1 & SPACE9_W33=1) SPACE_heard_index_W33=1.
if (SPACE1_W33=1 & SPACE9_W33=2) SPACE_heard_index_W33=2.
if (SPACE1_W33=2 & SPACE9_W33=1) SPACE_heard_index_W33=2.
if (SPACE1_W33=2 & SPACE9_W33=2) SPACE_heard_index_W33=2.
if (SPACE1_W33=2 & SPACE9_W33=3) SPACE_heard_index_W33=2.
if (SPACE1_W33=3 & SPACE9_W33=2) SPACE_heard_index_W33=2.
if (SPACE1_W33=1 & SPACE9_W33=3) SPACE_heard_index_W33=2.
if (SPACE1_W33=3 & SPACE9_W33=1) SPACE_heard_index_W33=2.
if (SPACE1_W33=3 & SPACE9_W33=3) SPACE_heard_index_W33=3.
if (SPACE1_W33=1 & SPACE9_W33=99) SPACE_heard_index_W33=99.
if (SPACE1_W33=2 & SPACE9_W33=99) SPACE_heard_index_W33=99.
if (SPACE1_W33=3 & SPACE9_W33=99) SPACE_heard_index_W33=99.
if (SPACE1_W33=99 & SPACE9_W33=99) SPACE_heard_index_W33=99.
if (SPACE1_W33=99 & SPACE9_W33=1) SPACE_heard_index_W33=99.
if (SPACE1_W33=99 & SPACE9_W33=2) SPACE_heard_index_W33=99.
if (SPACE1_W33=99 & SPACE9_W33=3) SPACE_heard_index_W33=99.

freq SPACE_heard_index_W33.

variable labels SPACE_heard_index_W33 'SPACE1 and SPACE 9 combined'.
value labels SPACE_heard_index_W33
1 'A lot to both NASA and private space companies'
2 'A lot to one or a little to at least one to NASA and private space companies'
3 'Nothing at all to both NASA and private space companies'
99 'Refused to at least one NASA and private space companies'.

execute.
