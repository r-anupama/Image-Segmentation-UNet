from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import glob

datagen = ImageDataGenerator(
         horizontal_flip=True,
         fill_mode='nearest')

#list all the images present in the mentioned directory
image_list = glob.glob('data/wooden-logs/train/labels/*')

#print(image_list)

#print(len(image_list))

#for every image in the directory
for index in range(0,len(image_list),1):
        img = load_img(image_list[index])
        print(img)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)

        i = 0
        # prefiex for the generated image will be 'logs' and format 'jpeg'
        for batch in datagen.flow(x,batch_size=1,
                        save_to_dir='data/wooden-logs/train/aug/labels', save_prefix='logs', save_format='jpeg'):
                i += 1
                if i > 2:
                        break
# end of code 
