import pandas as pd

# Paths to the CSV files
term_freq_csv = r'C:\NLP_CW2\OUTPUT\1500\tf_vectors_validation_bypublisher.csv'
ground_truth_csv = r'C:\NLP_CW2\OUTPUT\1500\tf_groundtruth_validation_bypublisher.csv'
merged_output_csv = r'C:\NLP_CW2\OUTPUT\1500\Merged\merged_validation_bypublisher.csv'

# Load the term frequency vectors into a DataFrame
term_freq_df = pd.read_csv(term_freq_csv)
print("Term Frequency Vectors DataFrame:")
print(term_freq_df.head())
print(term_freq_df.columns)
print(term_freq_df.dtypes)

# Load the ground truth labels into a DataFrame
ground_truth_df = pd.read_csv(ground_truth_csv)
print("\nGround Truth Labels DataFrame:")
print(ground_truth_df.head())
print(ground_truth_df.columns)
print(ground_truth_df.dtypes)

# Check if 'article_id' exists in both DataFrames
if 'article_id' not in term_freq_df.columns:
    print("\nError: 'article_id' column not found in term_freq_df")
if 'article_id' not in ground_truth_df.columns:
    print("\nError: 'article_id' column not found in ground_truth_df")

# Ensure 'article_id' columns are of the same type
term_freq_df['article_id'] = term_freq_df['article_id'].astype(str)
ground_truth_df['article_id'] = ground_truth_df['article_id'].astype(str)

# Merge the term frequency DataFrame with the ground truth DataFrame on 'article_id'
merged_df = pd.merge(term_freq_df, ground_truth_df, on='article_id', how='inner')
print("\nMerged DataFrame:")
print(merged_df.head())
print(merged_df.columns)
print(merged_df.dtypes)

# Save the merged DataFrame to a CSV file
merged_df.to_csv(merged_output_csv, index=False)
print(f"\nMerged DataFrame has been saved to {merged_output_csv}")