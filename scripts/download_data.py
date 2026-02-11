from kaggle.api.kaggle_api_extended import KaggleApi

def download_eye_dataset():
    api = KaggleApi()
    api.authenticate()

    dataset = "kayvanshah/eye-dataset"

    print("Downloading Eye Dataset from Kaggle...")

    api.dataset_download_files(
        dataset,
        path="data",
        unzip=True
    )
    print("Download complete. Files are saved in the 'data' directory.")
if __name__ == "__main__":
    download_eye_dataset()