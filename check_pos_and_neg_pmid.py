import pandas as pd

# pos
pos_df = pd.read_csv('./csv_data/output_pos.csv', header=None)
pos_pmid = pos_df[0].to_list()

#neg
neg_df = pd.read_csv('./csv_data/random_extract.csv', header=None)
neg_pmid = neg_df[1].to_list()

#check if pos pmid in neg
for pmid in pos_pmid:
    if pmid in neg_pmid:
        print('Pos pmid {} in Neg'.format(pmid))
