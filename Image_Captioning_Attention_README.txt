Github Link: https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning

1. The model contains two inputs, images and captions

images - Make a folder containing all images (train, val and test in one)
captions: In Karpathy json format. The json_format.ipynb contains code that converts a folder containing captions into json format

2. The 'all_caption_files' Folder contains all the python scripts needed to run the model

The contents of the files are as follows:

caption_data/ (contains the caption file in json format)
media/ (contains the image folder)
create_input_files.py (to be run for data preprocessing after the image and captions are in the right folder)
train.py (to be run for training the model)
caption.py (to generate captions)
eval.py
models.py
utils.py
dataset.py

3. The json format can be created using the json_format notebook. The "json_format.ipynb" to be used when the data is not augmented or on the original dataset. 

4. For data augmentation, first create the json format using the original dataset. This will give us the correct split for training, validation and testing set. Then use the created json file to augment the training data. This can be done using the "image_augmentation_json.ipynb" which creates both, the augmented dataset as well as the json caption file. Then put the augmented data and the json file created into the respective folders as mentioned above in (2).

5. Training the Model

Step 1: The images folder and caption should be in the given folders

Step 2: Open the create_input_files.py. Modify the given parameters accordingly and run the script. The train, val and test files will be created.
python create_input_files.py

Step 3: Open the train.py file. Make changes in the parameters accordingly. Run the script.
python train.py

Step 4: Run the caption.py file to generate caption on the required image.

python caption.py --img='path/to/image.jpeg' --model='path/to/BEST_checkpoint_coco_5_cap_per_img_5_min_word_freq.pth.tar' --word_map='path/to/WORDMAP_coco_5_cap_per_img_5_min_word_freq.json' --beam_size=5




