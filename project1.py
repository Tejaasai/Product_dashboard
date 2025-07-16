import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud




st.title(':blue[Product Analysis]:bar_chart:')



file_uploader=st.file_uploader('upload_csv_file',type='csv')

if file_uploader is None:
    st.write('Upload csv file')

else:

    df=pd.read_csv(file_uploader)
    st.dataframe(df)

    df['discount']=df['discount'].str.replace('%','').astype('int')

    columns=df.columns.to_list()
    selected_column=st.sidebar.selectbox('Select the value',columns)

    tab1,tab2,tab3,tab4= st.tabs(['Price analysis','Rating analysis','Top 10 discount products','Word cloud analysis'])


    with tab1:
        if selected_column=='price':
            fig=plt.figure(figsize=(12,6))
            sns.histplot(x=df[selected_column],kde=True,color='skyblue')
            plt.title('Price analysis for histogram')
            st.pyplot(fig)

        else:
            st.info('Select on price column to get histogram')

    with tab2:
        if selected_column=='rating':
            fig=plt.figure(figsize=(12,6))
            sns.countplot(x=df[selected_column],palette='viridis')
            plt.title('Rating analysis')
            st.pyplot(fig)

        else:
            st.info('Select on rating column to get rating analysis')

    with tab3:
        if selected_column=='discount':
            df1=df.nlargest(10,selected_column)[['name','price','discount']]
            st.write(df1)

        else:
            st.info('Select on discount column to get top10 discounted products')

    with tab4:
        if selected_column=='name':
            fig=plt.figure(figsize=(12,6))
            wordcloud=WordCloud(width=800,height=400,background_color='white').generate(' '.join(df[selected_column]))
            plt.imshow(wordcloud,interpolation='bilinear')
            plt.axis('off')
            st.pyplot(fig)

        else:
            st.info('select name column to get Wordcloud analysis')



        



    











