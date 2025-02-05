import os
import pandas as pd

# Define dataset path
DATASET_PATH = r"C:\Users\yogit\Downloads\archive (6)\docs-sm"

# Define selected categories to use
selected_classes = ["invoice", "budget", "email"]

# Prepare dataset
data = []

# Loop through selected categories and add images
for category in selected_classes:
    folder_path = os.path.join(DATASET_PATH, category)
    
    # Check if folder exists for the category
    if os.path.exists(folder_path):
        print(f"Found folder: {folder_path}")  # Debugging print
        files = os.listdir(folder_path)
        
        # Skip if no files are in the folder
        if not files:
            print(f"⚠️ No files in {category} folder!")
        
        # Loop through files and append image paths with labels
        for filename in files:
            file_path = os.path.join(folder_path, filename)
            
            # Check for valid image or PDF formats
            if filename.endswith(('.jpg', '.png', '.jpeg', '.pdf')):  
                data.append([file_path, category])
            else:
                print(f"❌ Skipped non-image file: {file_path}")
    else:
        print(f"⚠️ Folder not found: {folder_path}")

# Convert list to DataFrame
df = pd.DataFrame(data, columns=["file_path", "category"])

# Save the cleaned dataset with file paths and categories
os.makedirs("dataset", exist_ok=True)  # Ensure the 'dataset' directory exists
df.to_csv('dataset/cleaned_data.csv', index=False)

print(f"✅ Dataset saved with {len(df)} records!")
