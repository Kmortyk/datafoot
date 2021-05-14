class Formats:
    Video = [
        'mp4',
        'mov',
        'webm',
        'mkv',
        'flv',
        'avi',
        'wmv',
        'mpeg',
        'mov',
    ]

    def append_video_format(self, video_format: str):
        self.Video.append(video_format.replace('.', ''))

    Image = [
        'jpg',
        'jpeg',
        'png',
        'tiff'
    ]

    def append_image_format(self, video_format: str):
        self.Image.append(video_format.replace('.', ''))
