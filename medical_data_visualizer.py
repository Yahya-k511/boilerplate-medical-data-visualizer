import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['BMI']=df['weight']/(df['height']/100)**2
df['overweight'] = (df['BMI']>25).astype(int)

# 3
df.loc[df['cholesterol']==1,'cholesterol']=0
df.loc[df['cholesterol']>1,'cholesterol']=1
df.loc[df['gluc']==1,'gluc']=0
df.loc[df['gluc']>1,'gluc']=1





# 4
def draw_cat_plot():
   
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol',' gluc',' smoke',' alco', 'active', 'overweight'],
        var_name='variable'
    )


    # 6
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')
    
    # Step 7: Draw plot
    g = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar',
        height=4,
        aspect=1.5
    )
    
    # Step 8: Get figure
    fig = g.fig
    
    # Step 9: Do not modify
    fig.savefig('catplot.png')
    return fig

# Step 10-16: Heatmap
def draw_heat_map():
    # Step 11: Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Step 12: Correlation matrix
    corr = df_heat.corr()
    
    # Step 13: Mask
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Step 14: Set up figure
    fig, ax = plt.subplots(figsize=(10,8))
    
    # Step 15: Heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=0.5
    )
    
    # Step 16: Do not modify
    fig.savefig('heatmap.png')
    return fig
    

    
