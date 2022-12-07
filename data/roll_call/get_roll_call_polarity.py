import pandas as pd
import os

def get_roll_call_polarity():
    path = '/Users/guangbo_niu/Library/Mobile Documents/com~apple~CloudDocs/Academics/Autumn 2022/DPPP 2/Political_Polarization/data/roll_call/rollcall_data'
    rollcalls_data = pd.read_csv(os.path.join(path, 'Hall_rollcalls.csv'), low_memory=False)
    members_data = pd.read_csv(os.path.join(path, 'Hall_members.csv'))
    h113_votes = pd.read_csv(os.path.join(path, 'H113_votes.csv'))
    h114_votes = pd.read_csv(os.path.join(path, 'H114_votes.csv'))
    h115_votes = pd.read_csv(os.path.join(path, 'H115_votes.csv'))

    # merge votes, members data, and roll call data
    def merge_votes_members_rollcalls(votes, members, roll_calls, congress):
        df = pd.merge(votes, 
                    members[members['congress']==congress].loc[:, ['icpsr', 'party_code']], 
                    on='icpsr')
        df = pd.merge(df, 
                    roll_calls[roll_calls['congress']==congress].loc[:, ['rollnumber', 'date', 'bill_number', 'vote_result', 'vote_desc', 'vote_question']],
                    on='rollnumber')
        #df['rollnumber']=df['congress'].astype(str) + '_' + df['rollnumber'].astype(str)
        return df
        
    h113_votes = (merge_votes_members_rollcalls(h113_votes, members_data, rollcalls_data, 113))
    h114_votes = (merge_votes_members_rollcalls(h114_votes, members_data, rollcalls_data, 114))
    h115_votes = (merge_votes_members_rollcalls(h115_votes, members_data, rollcalls_data, 115))

    def tabulate_merge(df1, df2, df3):
        def tab(df):
            return df.groupby(['congress', 'rollnumber', 'date', 'cast_code'])['party_code'].value_counts()
        df1 = tab(df1)
        df2 = tab(df2)
        df3 = tab(df3)
        df_out = pd.DataFrame(pd.concat([df1, df2, df3], axis=0))
        return df_out.rename({'party_code': 'counts'}, axis=1)


    votes_counts = tabulate_merge(h113_votes, h114_votes, h115_votes)

    roll_call_idx = votes_counts.groupby(['congress', 'rollnumber', 'date']).groups.keys()
    polarity_df = pd.DataFrame(index=roll_call_idx, columns=['yes_d', 'yes_r', 'no_d', 'no_r', 'polarity'])
    for i in roll_call_idx:
        try:
            yes_d = votes_counts.loc[i].loc[(1, 100)].item()
        except KeyError:
            yes_d = 0
            
        try:
            yes_r = votes_counts.loc[i].loc[(1, 200)].item()
        except KeyError:
            yes_r = 0
            
        try:
            no_d = votes_counts.loc[i].loc[(6, 100)].item()
        except KeyError:
            no_d = 0
            
        try:
            no_r = votes_counts.loc[i].loc[(6, 200)].item()
        except KeyError:
            no_r = 0
            
        polarity = ((yes_d - yes_r) + (no_r - no_d))/(yes_d + yes_r + no_d + no_r)
        
        polarity_df.loc[i, 'yes_d'] = yes_d
        polarity_df.loc[i, 'yes_r'] = yes_r
        polarity_df.loc[i, 'no_d'] = no_d
        polarity_df.loc[i, 'no_r'] = no_r
        polarity_df.loc[i, 'polarity'] = polarity

    # how to access each row: df.loc[(113, 1, '2013-01-03'),:]
    polarity_df = polarity_df.reset_index(level=[2])
    return polarity_df