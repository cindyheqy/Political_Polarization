from shiny import App, render, ui
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors





app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.input_date_range(
        "daterange1", "Date range:", start="2015-01-01", end="2018-12-31"
    ),
    ui.output_plot('show_rollcall_plot'), 
    ui.input_radio_buttons(id="dataset",
                            label="Choose a variable",
                            choices=["Income", "Crime"]),
    ui.output_plot('show_two_plot')
)

def server(input, output, session):
    polarity_change = pd.read_csv('/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/tables/roll_call.csv')
    speech = pd.read_csv('/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/tables/speech.csv')
    public_opinion = pd.read_csv('/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/tables/public_opinion.csv')
    polarity_change['Date'] = pd.to_datetime(polarity_change['Date'])
    
    polarity_change['party'] = np.sign(polarity_change['polarity'])
    
    
    @output
    # @render.text
    @render.plot
    def show_rollcall_plot():
        df = polarity_change.loc[polarity_change['Date']>=pd.to_datetime(input.daterange1()[0])]
        df = df.loc[polarity_change['Date']<=pd.to_datetime(input.daterange1()[1])]
        fig, ax = plt.subplots(figsize = (15, 10))
        cmap = colors.ListedColormap(['red', 'blue'])
        # ax.scatter('Date', 'polarity', data=polarity_change.loc[polarity_change['party']==1], s=1, c='party', cmap=cmap)
        ax.scatter('Date', 'polarity', data=df, s=1, c='party', cmap=cmap)
        #plt.xticks(np.arange())
        plt.axhline(y = 0, color = 'black', linestyle = '-', linewidth=0.3)
        # plt.show()
        return ax

        
    @output
    # @render.text
    @render.plot
    def show_two_plot(): 
        if input.dataset() == "Income": 
            f, ax = plt.subplots()
            f.set_figwidth(20)
            f.set_figheight(10)
            ax.scatter('Time', 'Polarity', data=speech, marker='.')
            plt.legend()
            return ax

app = App(app_ui, server)
