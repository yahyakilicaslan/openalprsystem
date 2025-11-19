# MongoDB Veritabanı Şeması

Bu doküman, ANPR sisteminin kullandığı MongoDB koleksiyonlarının yapılarını tanımlar.

## `sites`

- `_id`: `ObjectId`
- `name`: `String`
- `block_count`: `Integer`
- `block_names`: `Array<String>`
- `apartments_per_block`: `Integer`

## `plates`

- `_id`: `ObjectId`
- `plate_number`: `String`
- `owner_name`: `String`
- `site_id`: `String` (referans `sites._id`)
- `block_name`: `String`
- `apartment_number`: `Integer`
- `valid_until`: `DateTime` (opsiyonel)
- `status`: `String` ("allowed", "banned", "guest")

## `doors`

- `_id`: `ObjectId`
- `name`: `String`
- `nodemcu_ip`: `String`
- `endpoint`: `String`

## `cameras`

- `_id`: `ObjectId`
- `name`: `String`
- `camera_type`: `String` ("webcam", "rtsp", "http", "onvif")
- `url_or_index`: `String`
- `associated_door_id`: `String` (referans `doors._id`)
- `fps`: `Integer`
- `onvif_settings`: `Object` (opsiyonel)

## `users` (Güvenlik modülü için)

- `_id`: `ObjectId`
- `username`: `String`
- `hashed_password`: `String`

## `logs` (Raporlama modülü için)

- `_id`: `ObjectId`
- `timestamp`: `DateTime`
- `plate_number`: `String`
- `status`: `String`
- `image_path`: `String`
