import dropbox
 
class TransferData: #létrehozom a TransferData osztályt
    def __init__(self, access_token):
        self.access_token = access_token
 
    def upload_file(self, file_from, file_to): #upload_file függvény létrehozása
        dbx = dropbox.Dropbox(self.access_token)
 
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
 
def main():
    access_token = 'gAn1wHVkcYAAAAAAAAAAFIeAqBzT3F6AiJ685dR_JDrEuJFLwuP0zyDjiKo5yjSX'
    transferData = TransferData(access_token)
 
    file_from = 'D:/Dokumentumok/Biznisz/Code/Site/webstore.github.io/py_app/dbx/dbx_proba.xlsx' # This is name of the file to be uploaded
    file_to = '/dbx_proba.xlsx'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
 
    # API v2
    transferData.upload_file(file_from, file_to)
 
if __name__ == '__main__':
    main()