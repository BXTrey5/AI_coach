# Virtual Coach Using Customized Basketball Detector


### About
- Used python and implementation of custom object detector using [The AI Guy's](https://www.youtube.com/watch?v=10joRJt39Ns&feature=emb_logo&ab_channel=TheAIGuy) notebook and tutorial to train a basketball detector that can detect made or missed shots within a given frame
- This project was inspired by [Ryan Werth](https://medium.com/swlh/automating-basketball-highlights-with-object-tracking-b134ce9afec2)


**Purpose:** Be able to count made and misses shots within a given frame so that basketball coaches can know exactly where a player missed a shot.


### Program details and Results
The detector was trained on 200 unique images of labelled basketballs, and is able to detect basketballs within images. The detection was run on the image below with the given results:

<img src=/images/lebron_detected.png alt="Interface Instructions" width="600"/>

The detector recognized the basketball in the image with approximately 53% certainty.

### What's Next
Eventually, I would like to improve the model by making it more likely to detect images of basketballs, and use it to detect made baskets. Additionally, I plan on implementing video detection, which will be done by using my video to image(video2imgs.py) and image to video(video2imgs.py) file converter in python to break up the video into images and run detections on each image.
