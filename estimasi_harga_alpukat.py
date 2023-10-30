import pickle
import streamlit  as st

model = pickle.load(open('estimasi_harga_alpukat.sav', 'rb'))

st.title('Estimasi Harga Alpukat')

Total_Volume = st.number_input('Masukan Jumlah Volume : ')
Total_Bags = st.number_input('Masukan Jumlah Kantong : ')
Small_Bags = st.number_input('Masukan Jumlah Kantong Kecil : ')
Large_Bags = st.number_input('Masukan Jumlah Kantong Besar : ')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict (
        [[Total_Volume, Total_Bags, Small_Bags, Large_Bags]]
    )
    st.write ('Estimasi Harga Alpukat Dalam Dollar',predict)