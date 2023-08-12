# data_extraction/dropbox_extractor.py
import dropbox


def extract_data(access_token):
    dbx = dropbox.Dropbox(access_token)
    files = dbx.files_list_folder('').entries

    extracted_data = []
    for file in files:
        _, response = dbx.files_download(file.path_display)
        data = response.content
        extracted_data.append(data)

    return extracted_data