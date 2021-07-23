from soccerplots.radar_chart import Radar
import matplotlib.pyplot as plt

def createRadar(df, metricasSelected, nombresSelected):

    cabeceras = df.columns.values.tolist()
    df_filter = df[[cabeceras[0]]+metricasSelected]
    params = list(df_filter.columns)
    params = params[1:]

    values = getValueComparate(df_filter, nombresSelected)
    ranges = getRanges(df_filter, params)

    title = dict(
        title_name=nombresSelected[0],
        title_color='#B6282F',
        title_name_2=nombresSelected[1],
        title_color_2='#344D94',
        title_fontsize=18,
        subtitle_fontsize=15
    )

    endnote = 'By Rafael Hidalgo'

    radar = Radar()

    fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values,
                               radar_color=['red', 'blue'],
                               alphas=[.75, .6], title=title, endnote=endnote,
                               compare=True)

    df_final = createDF(df_filter, nombresSelected, cabeceras)

    return fig, df_final

def createDF(df_filter, nombresSelected, cabeceras):
    return df_filter[df_filter[cabeceras[0]].isin(nombresSelected)]

def getValueComparate(df, nombresSelected):

    for i in range(0, len(df.index)):

        if nombresSelected[0] in list(df.loc[i]):
            a_values = df.iloc[i].values.tolist()
        if nombresSelected[1] in list(df.loc[i]):
            b_values = df.iloc[i].values.tolist()

    a_values = a_values[1:]
    b_values = b_values[1:]

    values = [a_values, b_values]

    return values

def getRanges(df, params):
    ranges = []
    print(params)
    for x in params:
        a = min(df[params][x])
        a = a - (a * .25)

        b = max(df[params][x])
        b = b + (b * .25)

        ranges.append((a, b))

    return ranges