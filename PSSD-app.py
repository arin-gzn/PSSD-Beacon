import gradio as gr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def return_plot2(category):

#     plt.style.use(['unhcrpyplotstyle','streamgraph'])
    df = pd.read_csv('https://raw.githubusercontent.com/GDS-ODSSS/unhcr-dataviz-platform/master/data/change_over_time/streamgraph.csv')
    df = df.pivot_table(index='year', columns='population_type', values='population_number')
    df = df.reset_index()
    df= df.fillna(0)

    #compute data for plotting
    x = df['year']
    y1 = df['VDA']
    y2 = df['OOC']
    y3 = df['STA']
    y4 = df['IDP']
    y5 = df['ASY']
    y6 = df['REF']

    #plot the chart
    fig, ax = plt.subplots()
    ax.stackplot(x, y1, y2, y3, y4, y5, y6, colors = ['#EF4A60', '#999999', '#E1CC0D', '#00B398', '#18375F', '#0072BC'], labels = [ 'Venezuelans displaced abroad', 'Others of concern', 'Stateless persons', 'IDPs', 'Asylum-seekers', 'Refugees' ], baseline='weighted_wiggle')

    #set chart title
    ax.set_title('Evolution of people of concern to UNHCR | 1991-2020', pad=50)

    #set chart legend
    ax.legend(loc=(0,1), ncol=3)

    #set y-axis label
    ax.set_ylabel('Number of people (millions)')


    #set chart source and copyright
    plt.annotate('Source: UNHCR Refugee Data Finder', (0,0), (0, -25), xycoords='axes fraction', textcoords='offset points', va='top', color = '#666666', fontsize=9)
    plt.annotate('©UNHCR, The UN Refugee Agency', (0,0), (0, -35), xycoords='axes fraction', textcoords='offset points', va='top', color = '#666666', fontsize=9)

    #adjust chart margin and layout
    fig.tight_layout()
    return fig

def trends_plot_data():
    df = pd.DataFrame({ 
        'Treatments': ['Clomid', 'Sibo', 'TRT'], 
        'Frequency': [45, 38, 90] 
    }) 
    return df
    
def search(keywords):
    df = pd.DataFrame({
    "name" : ["John", "Alice", "Robert", "Edward", "Richard"], 
    "age" : [5, 2, 54, 3, 2], 
    "gender" : ["M", "F", "M", "M", "M"]}) 
    return gr.Dataframe(df)

def recommend(about_you):
    df = pd.DataFrame({
    "name" : ["John", "Alice", "Robert", "Edward", "Richard"], 
    "age" : [5, 2, 54, 3, 2], 
    "gender" : ["M", "F", "M", "M", "M"]}) 
    return gr.Dataframe(df)

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Tab("Search"):
        gr.Interface(search, "text", gr.Dataframe(
            headers=["name", "age", "gender"],
            datatype=["str", "number", "str"]
        ))
    with gr.Tab("Recommender"):
        gr.Interface(recommend, "text", gr.Dataframe(
            headers=["name", "age", "gender"],
            datatype=["str", "number", "str"]
        ))
    with gr.Tab("Trends"):
#           gr.BarPlot(trends_plot_data(), x="Treatments", y="Frequency")
            with gr.Row():
                 with gr.Column(scale=0, min_width=200):
                    dropdown=gr.Dropdown(["all", "treatment", "symptoms"], label="category")
            plot=gr.Plot()
            dropdown.change(fn=return_plot2, inputs=[dropdown], outputs=[plot])


if __name__ == "__main__":
    demo.launch()