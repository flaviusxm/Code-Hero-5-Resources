import pandas as pd

df = pd.read_excel('date.xlsx')

venituri = df[df['Tip'] == 'Venit']['Suma'].sum()
cheltuieli = df[df['Tip'] == 'Cheltuieli']['Suma'].sum()

sold = venituri - cheltuieli

print(f"Total venituri: {venituri} RON")
print(f"Total cheltuieli: {cheltuieli} RON")
print(f"Sold final: {sold} RON")

cheltuieli_pe_categorii = df[df['Tip'] == 'Cheltuieli'].groupby('Categorie')['Suma'].sum()

print("\nCheltuieli pe categorii:")
print(cheltuieli_pe_categorii)
