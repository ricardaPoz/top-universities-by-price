from icrawler import ImageDownloader


class CustomLinkPrinter(ImageDownloader):
    file_urls = []

    def get_filename(self, task, default_ext):
        file_idx = self.fetched_num + self.file_idx_offset
        return "{:04d}.{}".format(file_idx, default_ext)

    def download(
        self, task, default_ext, timeout=5, max_retry=3, overwrite=False, **kwargs
    ):
        file_url = task["file_url"]
        filename = self.get_filename(task, default_ext)

        task["success"] = True
        task["filename"] = filename

        if not self.signal.get("reach_max_num"):
            self.file_urls.append(file_url)

        self.fetched_num += 1

        if self.reach_max_num():
            self.signal.set(reach_max_num=True)

        return
