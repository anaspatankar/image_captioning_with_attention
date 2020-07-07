from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='DAMICA',
                       karpathy_json_path='caption_data/dataset_DAMICA_aug.json',
                       image_folder='media/images_augmented/',
                       captions_per_image=1,
                       min_word_freq=5,
                       output_folder='media/',
                       max_len=50)
