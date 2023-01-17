# Political_Polarization
### Introduction
In this project, we attempt to gauge political polarization in the United States by analyzing legislative data. We explore the possibility of measuring polarization by studying voting records and congressional floor debates. We also corroborate the results by showing the polarization trend among the general public using public opinion polls. 

### Method
First, we analyze legislative voting records and calculate a polarity score for each vote/roll call. Using the naïve formula we developed: [(Yes_Dem – Y_Rep) + (No_Rep – No_Dem)]/All_Votes, we assign a numerical value from -1 to 1 to each vote/roll call based on how each party voted. For example, if all Democrats voted Yes for a legislation while all Republicans voted No, we assign 1 to it, indicating that it is extremely polarized towards the Democrats, and vice versa. Then we plot all the polarity values against date to show the trend of polarization over years.

Next, we analyze congressional floor debates and see if we can use NLP to get a measure of polarity for each debate based what was said. We use SpacyTextBlob combined with Spacy to analyze what legislators said during each congressional session and get a polarity score for each day. We then plot the polarity score against date to see if there’s a trend.

After that, we analyze public opinion polls to see if the polarization trend among the American public aligns with the trend in American politics at the federal level. 

### Obtaining and Cleaning Data
First, we need to specify a time range for the data we analyze. We decide that the data ranges from 2015 to 2018, the last two years of Obama’s presidency and the first two years of Trump’s presidency, which we think is a volatile period of American poltics.

The legislative voting records were downloaded from voteview.com developed by UCLA researchers. The files are stored at /data/roll_call/rollcall_data. The Python file that manipulates the data is /data/roll_call/get_roll_call_polarity.py. The first file “Members’ Votes” (H113/4/5_votes.csv) documents the voting record of each member for each roll call. The second file “Congressional Votes” (Hall_rollcalls.csv) has the pertaining information for each roll call. The third file “Member Ideology” (Hall_members.csv) contains party affiliation for each member. The files are linked by the member_ID column which is unique for each member. We then merge the datasets and calculate polarity scores for each vote/roll call.

The floor debates data were obtained from govinfo.gov using the API provided by the website. Under the /data/speech folder, get_speech_rawdata.py uses the API to download the PDF files of the official Congressional Record, get_speech_content.py extracts text from the PDFs and subset the text to only speech made by congressional members, and text_analysis.py uses Spacy and SpacyTextBlob to obtain a polarity score for each day based on the text.

Finally, the public opinion data was downloaded from Pew Research Center which conducts periodic polls. The files are under /data/public_opinion, and manipulated by public_opinion.py under the same folder. Each file contains the political ideology (a spectrum) of the poll participants, and we use that data to see how polarized American people are in each poll. 

### Challenges and Weaknesses
First, we had a lot of troubles accessing voting records data. The data is widely available online but mostly in granular forms. Thanks to voteview.com developed by UCLA researchers, we were able to download the aggregated dataset without having to scrape it. Second, congressional debates data was a huge hassle for us: they were all in forms of PDF and half of the texts were not actual speech/debate. We had to extract actual speech/debate data with trial and error and it took a long time for us to reach the optimal results.
One weakness of this project is about polarity measurement. The polarity formula we developed for the vote/roll call data may not have the same intuition as the polarity score generated by SpacyTextBlob, resulting in incoherent definitions of polarity. Another weakness is that, despite our enormous efforts in extracting speech/debate text from Congressional Record, there is still some noise in the data which may impede with polarity accuracies.

### Results and Conclusions
First, shown by the roll_call.png, we can see that there is no clear pattern of how vote/roll call polarization has changed over years. But we do see that Democrats tend to have more polarized voting behaviors than Republicans, as Republicans have many data points near zero. Second, shown by the speech_plot.png, we can see that congressional speech/debate polarity has increased slightly since 2015. Third, shown by the public_opinion.png, we can see that American public opinion has seen increased polarization over years. It is especially the case since 2017, when Trump began his presidency.

In addition to visualization, we would also like to analyze the data quantitatively. We ran a simple OLS regression which regresses the vote/roll call polarity data on debate polarity data. The actual regression process is in regression.py under the home folder. Before running regression, we need to get the absolute values of the vote/roll call polarity scores so that they align with the debate polarity scores. Our expectation is that the coefficient would be positive which shows that how members vote correlates positively with what they say. However, the actual coefficient is -4.4224 with a standard error 0.685 and p-value 0. That means that when debates polarity increases by 0.1 on a particular day, the voting/roll call polarity actually decreases by -0.44, which is to our surprise.

Finally, this research is only a rudimentary realization of our ideas and has much room for improvement. For example, we should have a deeper understanding of how SpacyTextBlob generates the polarity scores so that we can better refine our definitions. Also, we could dive deeper into why the vote/roll call polarity trends diverges from debate polarity trends.
