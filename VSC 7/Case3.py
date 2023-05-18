# # mengimpor library yang dibutuhkan
# import numpy as np
# import keras
# from keras.preprocessing import image
# from keras.applications.vgg16 import preprocess_input, decode_predictions
# from IPython.display import Image

# # memuat model VGG16 pre-trained
# model = keras.applications.vgg16.VGG16(weights='imagenet')

# # memuat gambar yang ingin diklasifikasikan
# img_path = input("Masukkan path gambar yang ingin diklasifikasikan: ")
# img = image.load_img(img_path, target_size=(224, 224))

# # menampilkan gambar yang akan diklasifikasikan
# display(Image(filename=img_path, width=224, height=224))

# # mengubah gambar menjadi format yang dapat diproses oleh model
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)

# # melakukan prediksi kategori gambar
# preds = model.predict(x)
# decoded_preds = decode_predictions(preds, top=3)[0]

# # menampilkan hasil prediksi kategori gambar
# print("Hasil klasifikasi gambar:")
# for i, (pred_id, name, likelihood) in enumerate(decoded_preds):
#     print(f"{i+1}. {name} ({likelihood:.2f})")
