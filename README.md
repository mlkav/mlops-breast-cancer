![created](https://img.shields.io/badge/created-05/09/2024-blue)
[![Open Notebook](https://img.shields.io/badge/Open_Notebook!-blue?logo=jupyter)](https://maulanakavaldo.github.io/mlops-breast-cancer/notebook.html)
<a href="https://bc-prediction-app-mkavaldo.up.railway.app/" target="_blank">
  <img src="https://img.shields.io/badge/Open_Prototype!-blue?logo=railway" alt="Prototype">
</a>
<a href="https://www.linkedin.com/in/maulana-kavaldo/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin" alt="LinkedIn">
</a>
<a href="https://www.dicoding.com/users/mkavaldo/academies" target="_blank">
  <img src="https://img.shields.io/badge/Dicoding_Profile-blue?logo=browser" alt="Dicoding Profile">
</a>

___

# Breast Cancer Prediction (MLOPS)

![breast-cancer](https://github.com/user-attachments/assets/34f4f52d-c5b0-4b73-adcb-f25744a08e2f)

|         | Deskripsi|
|---------|----------|
|Dataset  |	[Breast Cancer Dataset on Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data). Dataset ini berisi fitur diagnostik tumor kanker payudara, termasuk pengukuran seperti radius, tekstur, perimeter, dan area. Dataset ini digunakan untuk klasifikasi biner dalam memprediksi apakah suatu tumor bersifat jinak atau ganas berdasarkan karakteristik sel. Kolom target diberi label diagnosis, dengan 'M' menunjukkan ganas dan 'B' untuk jinak. Dataset ini memiliki 569 baris dan 31 kolom dan cocok untuk melatih model machine learning dalam deteksi dini kanker payudara. |
|Masalah| Deteksi dini kanker payudara adalah kunci untuk meningkatkan peluang kesembuhan dan kelangsungan hidup pasien, karena kanker payudara yang tidak terdeteksi dapat menimbulkan berbagai risiko kesehatan. World Health Organization (WHO) menekankan pentingnya deteksi dini kanker payudara untuk mencegah komplikasi lanjut dan meningkatkan efektivitas pengobatan [^1]. Proyek ini bertujuan mengklasifikasikan kanker payudara sebagai "malignant" (ganas) atau "benign" (jinak), menggunakan data fitur seperti radius, tekstur, perimeter, dan area. Centers for Disease Control and Prevention (CDC) menyatakan bahwa deteksi dini kanker payudara adalah langkah penting untuk perlindungan kesehatan [^2]. Hal ini juga didukung oleh laporan dari Union for International Cancer Control (UICC) yang menyoroti pentingnya akses ke layanan kesehatan berkualitas [^3] dan pedoman dari National Cancer Institute (NCI) mengenai standar deteksi dan pengobatan kanker [^4].|
|Solusi machine learning| Untuk mendeteksi kanker payudara, berbagai parameter dari hasil biopsi atau citra medis biasanya diuji. Namun, penilaian apakah tumor bersifat ganas atau jinak hanya berdasarkan hasil pengujian tersebut bisa memakan waktu dan memerlukan interpretasi klinis yang kompleks. Dengan menggunakan model Sequential dalam deep learning, yang merupakan struktur jaringan saraf sederhana namun efektif, diharapkan dapat memberikan penilaian yang lebih cepat dan akurat mengenai jenis tumor. Model Sequential terdiri dari lapisan-lapisan yang terhubung secara linier dan mampu memproses data input untuk menghasilkan prediksi apakah tumor bersifat malignant (ganas) atau benign (jinak). Hasil dari sistem ini dapat digunakan sebagai alat bantu diagnostik dalam pengambilan keputusan medis lebih lanjut untuk perawatan dan penanganan kanker payudara.|
|Metode pengolahan| Dataset Breast Cancer terdiri dari 31 kolom, di mana 30 di antaranya digunakan untuk klasifikasi dan satu sebagai label klasifikasi (diagnosis). Semua fitur bersifat numerikal: radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, dan fitur lainnya memiliki tipe data float64, sedangkan fitur label diagnosis memiliki tipe data int64. Data dibagi menjadi 80% untuk pelatihan dan 20% untuk evaluasi. Proses transformasi data melibatkan normalisasi untuk fitur numerikal menggunakan z-score. Normalisasi ini dilakukan untuk memastikan bahwa semua fitur memiliki skala yang seragam, dengan rata-rata 0 dan deviasi standar 1, sehingga membantu model dalam proses pelatihan dengan mengurangi bias yang disebabkan oleh perbedaan skala antar fitur.
|Arsitektur model| Arsitektur model dimulai dengan mengintegrasikan input fitur yang kemudian diproses melalui beberapa lapisan dense. Model ini terdiri dari empat lapisan dense dengan jumlah unit 256, 128, 64, dan 32, di mana setiap lapisan menggunakan fungsi aktivasi ReLU, dilengkapi dengan Batch Normalization serta Dropout dengan rate 0.3. Lapisan output adalah dense dengan 1 unit yang menggunakan aktivasi sigmoid untuk klasifikasi biner. Model dikompilasi menggunakan optimizer Adam dengan learning rate 0.0001, loss binary crossentropy, dan metrik akurasi, yang bertujuan untuk mengklasifikasikan tumor sebagai "malignant" (ganas) atau "benign" (jinak).
| Metrik evaluasi  |  Metrik evaluasi yang digunakan dalam proyek ini meliputi AUC, Precision, Recall, ExampleCount, dan BinaryAccuracy. ExampleCount digunakan untuk menghitung jumlah contoh yang dievaluasi, sementara BinaryCrossentropy menghitung kerugian model pada tugas klasifikasi biner. BinaryAccuracy menilai tingkat akurasi prediksi model, sedangkan Precision dan Recall mengukur ketepatan dan sensitivitas model dalam mendeteksi kasus positif dengan ambang batas 0.5. Evaluasi ini dirancang untuk menilai performa model secara menyeluruh guna memastikan keefektifannya dalam menentukan apakah tumor bersifat ganas atau jinak.|
| Performa model  |  Hasil evaluasi model setelah tuning menunjukkan akurasi **97.5%** pada pelatihan dan **99%** pada data validasi. Loss yang diperoleh adalah **0.0759** selama pelatihan dan **0.0342** pada validasi. Model menunjukkan kinerja yang sangat baik dan dapat digunakan untuk melakukan prediksi.|
| Opsi Deployment  | Model yang sudah dibuat, project ini dideploy menggunakan Railway. Railway memiliki kemudahan dalam proses deployment dengan user friendly dan dukungan untuk berbagai teknologi. Selain bisa juga dideploy dengan menggunakan heroku, namun untuk menggunakan heroku harus subscribe. |
| Web App | Menggunkan Flask untuk web aplikasi serta deploy model menggunakan Railwal. Akses pada link berikut: [Breast Prediction App](https://bc-prediction-app-mkavaldo.up.railway.app/) / [Metadata Model](https://mlops-bc-mkavaldo.up.railway.app/v1/models/bc-model/metadata).|
| Monitoring | Model dipantau kinerjanya dengan menggunakan Prometheus dan Grafana. Prometheus bertugas mengumpulkan data dan metrik dari model secara real-time namun terdapat juga visualisasi sederhana, sedangkan Grafana membantu  melihat semua informasi tersebut dalam bentuk dashboard yang mudah dipahami. Dari hasil monitoring, didapati hampir mencapai 1000 (1k) request yang berarti baik dari web app maupun dilakukan testing dengan file `testing.ipynb` mampu menerima request dan mengembalikan respon untuk menghasilkan prediksi yang ditampilkan pada grafik visualisasi. Akses ke [Monitoring Metrics](https://mlops-bc-mkavaldo.up.railway.app/monitoring/prometheus/metrics). |



## Deployment Model on Railway

Untuk melakukan deployment model yang telah dibuat yaitu dengan menggunakan Railway. Selain itu digunakan Prometheus dan Grafana untuk menampilkan visualisasi hasil monioring. Unduh terlebih dahulu [Railway CLI](https://docs.railway.app/quick-start) dan [Grafana](https://grafana.com/grafana/download?platform=windows) serta lakukan proses instalasi. 


### Membuat file yang diperlukan:
1. Dockerfile
    ```docker
    # Dockerfile
    
    FROM tensorflow/serving:latest
    
    COPY ./output/serving_model /models/breast-model
    COPY ./config /model_config
    ENV MODEL_NAME=breast-model
    
    ENV MONITORING_CONFIG="/model_config/prometheus.config"
    ENV PORT=8501
    RUN echo '#!/bin/bash \n\n\
    env \n\
    tensorflow_model_server --port=8500 --rest_api_port=${PORT} \
    --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} \
    --monitoring_config_file=${MONITORING_CONFIG} \
    "$@"' > /usr/bin/tf_serving_entrypoint.sh \
    && chmod +x /usr/bin/tf_serving_entrypoint.sh
    ```

    ```docker
    # monitoring/Dockerfile

    FROM prom/prometheus:latest
    COPY prometheus.yml /etc/prometheus/prometheus.yml

    ```

2. Membuat file `prometheus.config` yang disimpan dalam folder config.

    ```python
    # config/prometheus.config

    prometheus_config {
    enable: true,
    path: "/monitoring/prometheus/metrics"
    }
    ```

### Deploy in Local

Dengan melakukannya dilocal untuk memastikan bahwa model dapat berjalan dengan baik sebelum dilakukan deploy ke Railway.

```docker
docker build -t breast-prediction-tf-serving .
docker run -p 8080:8501 breast-prediction-tf-serving
```
Copy dan paste url berikut:
```
localhost:8080/v1/models/bc-model/metadata
```
Jika berhasil akan tampil seperti ini:

<img width="572" alt="mkavaldo-metadata-local" src="https://github.com/user-attachments/assets/966da9ee-c526-4a36-bd31-f73463425a7f">


Jika pada tahap pembuatan di local sudah berhasil dapat langsung dilakukan uji coba pada sub Prediction dengan menggunakan file `testing.ipynb`.


### Deploy in Railway

1. Membuka cmd dan melakukan command-command berikut:
    ```bash
    railway login
    railway init # Memasukkan nama project 'bc-model'
    railway link -p 262bf577-2ac3-4e55-a2ac-9aeeedfa2cd7 # ID project pada railway
    railway up # Railway akan otomatif membaca Dockerfile
    ```
2. Buka halaman project -> Setting, melakukan generate domain dan didapatkan url:
    ```
    https://mlops-bc-mkavaldo.up.railway.app/
    ```

### Metadata on Railway

Copy paste url berikut ke browser untuk melihat metadata dan monitoring:
1. Metadata Model
    ```
    https://mlops-bc-mkavaldo.up.railway.app/v1/models/bc-model/metadata
    ```
    Jika berhasil akan muncul seperti ini:
   
   <img width="572" alt="mkavaldo-metadata" src="https://github.com/user-attachments/assets/2a62b086-702c-41e9-a5e9-1f67652d9030">


3. Monitoring
    ```
    https://mlops-bc-mkavaldo.up.railway.app/monitoring/prometheus/metrics
    ```
    Jika berhasil akan muncul seperti ini:

   <img width="572" alt="mkavaldo-metrics" src="https://github.com/user-attachments/assets/2e2b17d4-8d6b-4d34-8601-301ead46b250">


### Monitoring in Prometheus

1. Membuka CMD dan run beberapa command berikut:
    ```bash
    docker build -t bc-monitoring .\monitoring\
    docker run -p 9090:9090 cc-monitoring
    ```
2. Salin link berikut ke browser:
    ```
    http://localhost:9090/
    ```

3. Hasil tampilan pada Prometheus.

    <img width="945" alt="mkavaldo-monitoring-prometheus" src="https://github.com/user-attachments/assets/e7de6c63-eee7-4c59-92a5-8a787cfc66f1">

### Monitoring Grafana
1. Pastikan sudah dilakukan instalasi pada tahap sebelumnya, _copy paste_ link berikut dan buka pada browser.
    ```
    http://localhost:3000/
    ```
2. Masukkan username dan password defaultnya, yaitu:
    ```teks
    username: admin
    password: admin
    ```
3. Membuat _datasource_ baru dan pilih prometheus sebagai sumbernya serta pada **_field connection_** masukkan:
    ```
    http://localhost:9090
    ```

4. Pada bagian **HTTP Method** pilih method **GET**, karena kita akan mengambil data dan menvisualisasikannya pada dashboard Grafana.

5. Klik tombol **Save & Test** dan memilih metrik yang akan ditampilkan.
6. Hasil tampilan pada Grafana.

   <img width="959" alt="mkavaldo-monitoring-grafana" src="https://github.com/user-attachments/assets/be11be09-d52b-4e34-96b5-09b932d8e2d7">



### Prediction

Melakukan prediksi pada data sample dengan menentukan index tertentu.

- Buka file *testing.ipynb dan lakukan run cell apakah model tersedia pada endpoint.
    ```
    http://localhost:8080/v1/models/bc-model
    ```
    ```
    https://mlops-bc-mkavaldo.up.railway.app/v1/models/bc-model
    ```
- Lakukan run hingga cell akhir.
- Ubah index data sesuai kebutuhan untuk melihat hasil prediksi.
- Pada file ini juga bisa melakukan _request_ dengan jumlah tertentu agar dapat terlihat perbedaan pada grafik monitoring.


## Reference:

[^1]: World Health Organization. "Breast Cancer Awareness and Screening Guidelines". 2024. Diakses pada 06 September 2024 melalui  [WHO: Breast Cancer](https://www.who.int/activities/preventing-cancer). 

[^2]: Centers for Disease Control and Prevention. "Breast Cancer: Early Detection". 2024. Diakses pada 06 September 2024 melalui  [CDC: Breast Cancer](https://www.cdc.gov/breast-cervical-cancer-screening/about/index.html).

[^3]: Union for International Cancer Control. "Universal Health Coverage and Cancer Prevention". 2023. Diakses pada 06 September 2024 melalui [UICC: Breast Cancer](https://www.uicc.org/news/universal-health-coverage-and-cancer-prevention).

[^4]: National Cancer Institute. "Breast Cancer Treatment (PDQ®)–Health Professional Version". 2024. Diakses pada 06 September 2024 melalui [NCI: Breast Cancer](https://www.cancer.gov/types/breast/hp/breast-treatment-pdq). 
