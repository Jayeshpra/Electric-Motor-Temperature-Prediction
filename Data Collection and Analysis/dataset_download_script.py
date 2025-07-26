import kagglehub
import shutil
import os

path = kagglehub.dataset_download("wkirgsn/electric-motor-temperature")
print("Path to dataset files:", path)

# Copy files to current directory
target_dir = os.path.dirname(__file__)
for filename in os.listdir(path):
    shutil.copy(os.path.join(path, filename), target_dir)
print("Files copied to:", target_dir)
