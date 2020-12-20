from azure.storage.blob import BlobServiceClient
import numpy
import os

connection_string = ""
service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "01-brondata"
client = service_client.get_container_client(container_name)
source_dir = "2019-winter-20cm-LAZ-DSM-Trueortho/2019_9_R5/Ortho/"
destdir = "winter"


def download_file(source, dest):
    '''
    Download a single file to a path on the local filesystem
    '''
    # dest is a directory if ending with '/' or '.', otherwise it's a file
    if dest.endswith('.'):
        dest += '/'
    blob_dest = dest + os.path.basename(source) if dest.endswith('/') else dest

    print(f'Downloading {source} to {blob_dest}')
    os.makedirs(os.path.dirname(blob_dest), exist_ok=True)
    bc = client.get_blob_client(blob=source)
    # bc=client.get_blob_client(blob="beeldmateriaal",container="01-brondata")
    with open(blob_dest, 'wb') as file:
        data = bc.download_blob()
        file.write(data.readall())


with open("winter\\filelist2.txt", "r") as f:
    data = f.read().split('\n')
    tifList = numpy.array(data)  # convert array to numpy type array

for file_name in tifList:
    # shutil.move(os.path.join(source_dir, file_name), train_dir)
    # ENS_259851_467200.tif  geoms_252299_466560.geojson
    if len(file_name) > 0:
        if os.path.isfile(os.path.join("winter",file_name)):
            print(file_name+" exists")
        else:
            download_file(os.path.join(source_dir, file_name), os.path.join(destdir, file_name))


# def download(source, dest):
#     '''
#     Download a file or directory to a path on the local filesystem
#     '''
#     if not dest:
#         raise Exception('A destination must be provided')
#
#     blobs = ls_files(source, recursive=True)
#     if blobs:
#         # if source is a directory, dest must also be a directory
#         if not source == '' and not source.endswith('/'):
#             source += '/'
#         if not dest.endswith('/'):
#             dest += '/'
#         # append the directory name from source to the destination
#         dest += os.path.basename(os.path.normpath(source)) + '/'
#
#         blobs = [source + blob for blob in blobs]
#         for blob in blobs:
#             blob_dest = dest + os.path.relpath(blob, source)
#            download_file(blob, blob_dest)
#     else:
#        download_file(source, dest)


def ls_files(self, path, recursive=False):
    '''
    List files under a path, optionally recursively
    '''
    if not path == '' and not path.endswith('/'):
        path += '/'

    blob_iter = client.list_blobs(name_starts_with=path)
    files = []
    for blob in blob_iter:
        relative_path = os.path.relpath(blob.name, path)
        if recursive or not '/' in relative_path:
            files.append(relative_path)
    return files
