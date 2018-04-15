
import pandas as pd
import numpy as np

# Load data as DataFrame

data_set = pd.read_csv('Sample_bond_data_A_CSV.csv', sep=';')

# Create empty columns to store both the spread risk SCR percentage and the SCR in terms of MV for each instrument

data_set["SCR_percentage"] = np.nan
data_set["SCR_instrument"] = np.nan

# Cap durations for bonds and loans other than residential mortgage loans

for row in data_set.itertuples():

    if (row.Rating_class == 0 and
            row.Modified_duration > 176 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 176

    elif (row.Rating_class == 1 and
            row.Modified_duration > 173 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 173

    elif (row.Rating_class == 2 and
            row.Modified_duration > 169 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 169

    elif (row.Rating_class == 3 and
            row.Modified_duration > 140 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 140

    elif (row.Rating_class == 4 and
            row.Modified_duration > 107 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 107

    elif (row.Rating_class == 5 and
            row.Modified_duration > 73 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 73

    elif (row.Rating_class == 6 and
            row.Modified_duration > 73 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 73

    elif (row.Rating_class == 7 and
            row.Modified_duration > 130 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 130
    else:
        pass

# Cap durations for covered bonds

for row in data_set.itertuples():
    if (row.Rating_class == 0 and
            row.Modified_duration > 178 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 178

    elif (row.Rating_class == 1 and
            row.Modified_duration > 176 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 176

    elif (row.Rating_class == 2 and
            row.Modified_duration > 169 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 169

    elif (row.Rating_class == 3 and
            row.Modified_duration > 140 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 140

    elif (row.Rating_class == 4 and
            row.Modified_duration > 107 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 107

    elif (row.Rating_class == 5 and
            row.Modified_duration > 73 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 73

    elif (row.Rating_class == 6 and
            row.Modified_duration > 73 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
        data_set.at[row.Index, 'Modified_duration'] = 73

    elif (row.Rating_class == 7 and
            row.Modified_duration > 130 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):
            data_set.at[row.Index, 'Modified_duration'] = 130
    else:
        pass


# Calculate the spread risk SCR percentage and SCR in terms of MV for bonds and loans other than residential mortgages with credit quality steps 0 to 7 and covered bonds with credit quality steps 2 to 7

for row in data_set.itertuples():

    if (row.Rating_class == 0 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):

        if row.Modified_duration <= 5:
            SCR_percentage = (0.9*row.Modified_duration)/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 5 < row.Modified_duration <= 10:
            SCR_percentage = (4.5 + (0.5 * (row.Modified_duration-5)))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 10 < row.Modified_duration <= 15:
            SCR_percentage = (7.2 + (0.5 * (row.Modified_duration-10)))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 15 < row.Modified_duration <= 20:
            SCR_percentage = (9.7 + (0.5 * (row.Modified_duration-15)))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        else:
            SCR_percentage = (12.2 + (0.5 * (row.Modified_duration-20)))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument

    elif (row.Rating_class == 1 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):

        if row.Modified_duration <= 5:
            SCR_percentage = (1.1*row.Modified_duration)/100
            SCR_instrument = SCR_percentage*row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 5 < row.Modified_duration <= 10:
            SCR_percentage = (5.5 + (0.6 * (row.Modified_duration-5)))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 10 < row.Modified_duration <= 15:
            SCR_percentage = (8.4 + (0.5 * (row.Modified_duration-10)))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 15 < row.Modified_duration <= 20:
            SCR_percentage = (10.9 + (0.5 * (row.Modified_duration-15)))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        else:
            SCR_percentage = (13.4 + (0.5 * (row.Modified_duration-20)))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument

    elif (row.Rating_class == 2 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0 or
            row.Rating_class == 2 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):

        if row.Modified_duration <= 5:
            SCR_percentage = (1.4*row.Modified_duration)/100
            SCR_instrument = SCR_percentage*row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 5 < row.Modified_duration <= 10:
            SCR_percentage = (7.0 + (0.7 * (row.Modified_duration-5)))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 10 < row.Modified_duration <= 15:
            SCR_percentage = (10.5 + (0.5 * (row.Modified_duration-10)))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 15 < row.Modified_duration <= 20:
            SCR_percentage = (13.0 + (0.5 * (row.Modified_duration - 15))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        else:
            SCR_percentage = (15.5 + (0.5 * (row.Modified_duration - 20))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument

    elif (row.Rating_class == 3 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0 or
            row.Rating_class == 3 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):

        if row.Modified_duration <= 5:
            SCR_percentage = (2.5 * row.Modified_duration) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 5 < row.Modified_duration <= 10:
            SCR_percentage = (12.5 + (1.5 * (row.Modified_duration - 5))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 10 < row.Modified_duration <= 15:
            SCR_percentage = (20.0 + (1.0 * (row.Modified_duration - 10))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 15 < row.Modified_duration <= 20:
            SCR_percentage = (25.0 + (1.0 * (row.Modified_duration - 15))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        else:
            SCR_percentage = (30.0 + (0.5 * (row.Modified_duration - 20))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument

    elif (row.Rating_class == 4 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0 or
            row.Rating_class == 4 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):

        if row.Modified_duration <= 5:
            SCR_percentage = (4.5 * row.Modified_duration) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 5 < row.Modified_duration <= 10:
            SCR_percentage = (22.5 + (2.5 * (row.Modified_duration - 5))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 10 < row.Modified_duration <= 15:
            SCR_percentage = (35.0 + (1.8 * (row.Modified_duration - 10))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 15 < row.Modified_duration <= 20:
            SCR_percentage = (44.0 + (0.5 * (row.Modified_duration - 15))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        else:
            SCR_percentage = (46.6 + (0.5 * (row.Modified_duration - 20))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument

    elif (row.Rating_class == 5 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0 or
            row.Rating_class == 5 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):

        if row.Modified_duration <= 5:
            SCR_percentage = (7.5 * row.Modified_duration) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 5 < row.Modified_duration <= 10:
            SCR_percentage = (37.5 + (4.2 * (row.Modified_duration - 5))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 10 < row.Modified_duration <= 15:
            SCR_percentage = (58.5 + (0.5 * (row.Modified_duration - 10))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 15 < row.Modified_duration <= 20:
            SCR_percentage = (61.0 + (0.5 * (row.Modified_duration - 15))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        else:
            SCR_percentage = (63.5 + (0.5 * (row.Modified_duration - 20))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument

    elif (row.Rating_class == 6 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0 or
            row.Rating_class == 6 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):

        if row.Modified_duration <= 5:
            SCR_percentage = (7.5 * row.Modified_duration) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 5 < row.Modified_duration <= 10:
            SCR_percentage = (37.5 + (4.2 * (row.Modified_duration - 5))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 10 < row.Modified_duration <= 15:
            SCR_percentage = (58.5 + (0.5 * (row.Modified_duration - 10))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 15 < row.Modified_duration <= 20:
            SCR_percentage = (61.0 + (0.5 * (row.Modified_duration - 15))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        else:
            SCR_percentage = (63.5 + (0.5 * (row.Modified_duration - 20))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument

    elif (row.Rating_class == 7 and
            row.Covered_bond == 0 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0 or
            row.Rating_class == 7 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):

        if row.Modified_duration <= 5:
            SCR_percentage = (3.0 * row.Modified_duration) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 5 < row.Modified_duration <= 10:
            SCR_percentage = (15.0 + (1.7 * (row.Modified_duration - 5))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        elif 10 < row.Modified_duration <= 20:
            SCR_percentage = (23.5 + (1.2 * (row.Modified_duration - 10))) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        else:
            SCR_percentage = (min(35.5 + (0.5 * (row.Modified_duration - 20)), 100)) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument

    else:
        pass

print(data_set)


# Calculate the spread risk SCR percentage and SCR in terms of MV for covered bonds with credit quality steps 0 to 1

for row in data_set.itertuples():

    if (row.Rating_class == 0 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):

        if row.Modified_duration <= 5:
            SCR_percentage = (0.7*row.Modified_duration)/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        else:
            SCR_percentage = (min(3.5 + (0.5 * (row.Modified_duration-5)), 100))/100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument

    elif (row.Rating_class == 1 and
            row.Covered_bond == 1 and
            row.Non_EEA_sovereign_issue_in_dom_curr == 0 and
            row.Issue_from_entity_not_meeting_MCR == 0):

        if row.Modified_duration <= 5:
            SCR_percentage = (0.9 * row.Modified_duration) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument
        else:
            SCR_percentage = (min(4.5 + (0.5 * (row.Modified_duration - 5)), 100)) / 100
            SCR_instrument = SCR_percentage * row.MV_EUR
            data_set.at[row.Index, 'SCR_percentage'] = SCR_percentage
            data_set.at[row.Index, 'SCR_instrument'] = SCR_instrument

# Print resulting DataFrame

print(data_set)

# Export DataFrame to csv

data_set.to_csv("SCR.csv", sep=';', encoding='utf-8')
