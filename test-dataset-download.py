import os
import urllib.request
import zipfile

# Download the dataset from Github
data_url = "https://github.com/staslebedenko/transform_cognitive_services/raw/main/dataset/download/test-images.zip"
data_path = "./data-test"
download_path = os.path.join(data_path,"test-images.zip")
if not os.path.exists(data_path):
    os.mkdir(data_path);
urllib.request.urlretrieve(data_url, filename=download_path)

# Unzip the dataset
zip_ref = zipfile.ZipFile(download_path, 'r')
zip_ref.extractall(data_path)
zip_ref.close()
print("Data extracted in: {}".format(data_path))

os.remove(download_path)
print("Downloaded file removed: {}".format(download_path))