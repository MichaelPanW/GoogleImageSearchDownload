import simple_image_download.simple_image_download as simp

search = input("search keyword:") or 'dog'
limit = input("limit(10):") or 10
my_downloader = simp.Downloader()
# Change Direcotory
my_downloader.directory = 'downloads/'
# Change File extension type
my_downloader.extensions = '.jpg'
print(my_downloader.extensions)
my_downloader.download(search, limit=limit, verbose=True)
