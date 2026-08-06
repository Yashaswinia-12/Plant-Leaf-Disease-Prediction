from bing_image_downloader import downloader

downloader.download(
    "Kingfishers",
    limit=100,
    output_dir="my_dir",
    adult_filter_off=True,
    force_replace=False,
    timeout=60
)
