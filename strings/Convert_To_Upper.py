'''python program to convert a string of each word's begining character to upper case'''

st = input("Enter a string")
st=' '.join(word[0].upper()+word[1:] for word in st.split())
print(st)