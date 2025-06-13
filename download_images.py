from bing_image_downloader import downloader

# Final 5 famous breeds to complete 10 classes
breeds = [
    
   
    "sphynx cat cute"
]

for breed in breeds:
    downloader.download(breed, limit=200, output_dir='raw_images', adult_filter_off=True, force_replace=False, timeout=60)
