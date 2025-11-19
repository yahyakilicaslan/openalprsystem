# Sistem Mimarisi

Bu doküman, Evo Teknoloji Plaka Tanıma Sistemi'nin genel mimarisini ve bileşenlerinin etkileşimini açıklar.

## Ana Bileşenler

1.  **Frontend (React):**
    -   Kullanıcı arayüzünü oluşturur.
    -   Kullanıcı etkileşimlerini (form gönderimleri, buton tıklamaları vb.) yönetir.
    -   Backend API'leri ile HTTP (REST) ve WebSocket üzerinden iletişim kurar.
    -   Kamera görüntülerini WebRTC veya benzeri bir teknoloji ile canlı olarak gösterir.

2.  **Backend (FastAPI):**
    -   RESTful API servislerini sağlar.
    -   Veritabanı (MongoDB) ile etkileşim kurar.
    -   OpenALPR ve OpenCV kullanarak plaka tanıma işlemlerini gerçekleştirir.
    -   Canlı log verilerini WebSocket üzerinden frontend'e iletir.
    -   NodeMCU'lara kapı açma komutları gönderir.

3.  **Veritabanı (MongoDB):**
    -   Uygulamanın tüm verilerini (siteler, plakalar, kameralar, loglar vb.) saklar.
    -   NoSQL yapısı sayesinde esnek veri modellemesi sağlar.

4.  **Plaka Tanıma Motoru (OpenALPR + OpenCV):**
    -   Kamera akışlarından gelen görüntüleri işler.
    -   Görüntülerdeki plakaları tespit eder ve metne dönüştürür.
    -   CPU ve GPU üzerinde çalışabilir.

5.  **Kurulum Betikleri (`.bat`):**
    -   Tüm sistemin Windows üzerinde tek tıkla kurulmasını sağlar.
    -   Gerekli bağımlılıkları (Python, Node.js, MongoDB) kurar.
    -   Uygulama sunucularını başlatır.

## İş Akışı

1.  Kullanıcı, web tarayıcısı üzerinden React arayüzüne erişir.
2.  Frontend, backend'den gerekli verileri (kamera listesi, plaka kayıtları vb.) API aracılığıyla çeker.
3.  Backend, kamera akışlarını (RTSP, Webcam vb.) OpenCV ile yakalar.
4.  Yakalanan her bir kare, plaka tespiti için OpenALPR motoruna gönderilir.
5.  Bir plaka tespit edildiğinde, backend bu plakayı MongoDB'deki kayıtlarla karşılaştırır.
6.  Sonuç (tanımlı, tanımsız, yasaklı) frontend'e WebSocket üzerinden canlı olarak iletilir ve veritabanına log olarak kaydedilir.
7.  Eğer plaka tanımlıysa, backend ilgili kapının NodeMCU'suna bir HTTP isteği göndererek kapıyı açma komutu verir.
