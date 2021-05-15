# Datafoot

## Split videos to images and remove similar images

```python
from workflow import Pipeline
from file import Formats
import stage

base_path = "/dataset/processing/vids"

Pipeline(
    stage.ListFiles(base_path, Formats.Video),
    stage.SplitVideos(dir_name="splitted"),
    stage.img.RemoveSimilarImages(threshold=0.9),
)()
```

# Take 712 files, copy them to separate directory and overlay each with random image from list

```python
from workflow import Pipeline
from file import Formats
import stage
import convert

base_path = "/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/processing/vids/splitted_copy"

Pipeline(
    stage.ListFiles(base_path, Formats.Image),
    stage.Take(1000 - 288),
    stage.CopyTo(base_path + '/synthetic'),
    convert.img.OverlayChooseRandom([
        '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/empty_to_synthetic/bottle_blue_1.png',
        '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/empty_to_synthetic/bottle_green_2.png'
    ]),
)()
```

