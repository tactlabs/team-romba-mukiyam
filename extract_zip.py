import zipfile

def extract_zip(path_to_zip_file):

    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall('extracted_files')


if __name__ == '__main__':
    extract_zip('uploads/client.zip')