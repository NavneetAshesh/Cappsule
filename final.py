import pandas as pd

master_df = pd.read_excel('testfile.xlsx', sheet_name='Master')

test_df = pd.read_excel('testfile.xlsx', sheet_name='Test')

results_df = pd.DataFrame(columns=[ 'Item name' , 'Composition', 'Manufacturer', 'Product ID'])

for _, test_row in test_df.iterrows():
    match_row = master_df[(master_df['Item name'].str.lower() == test_row['Item Name'].lower()) |
                          (master_df['Composition'].str.lower() == test_row['Composition'].lower()) &
                          (master_df['Manufacturer'].str.lower() == test_row['Manufacturer'].lower())]
    if len(match_row) > 0:
        results_df = results_df.append({'Product ID': match_row['Product ID'].iloc[0],
                                        'Item name': test_row['Item Name'], 
                                       'Composition': test_row['Composition'] , 'Manufacturer': test_row['Manufacturer']},ignore_index=True)
    # else
    #   results_df = results_df.append({'Product ID': '',
    #                                     'Item name': test_row['Item Name']}, ignore_index=True)

# print(" This is master_df " ,master_df["Item name"]) 
# print("This is test_df ", test_df)
print(results_df)
with pd.ExcelWriter("testfile.xlsx",if_sheet_exists="replace", engine="openpyxl", mode="a") as writer:
    results_df.to_excel(writer, sheet_name="output_new")