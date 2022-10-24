## Công cụ cần cài đặt
- xampp hoặc (php, mysql, apache/nginx)
- python bản mới nhất
- composer
- các thư viện của python: (pyvi, tqdm, numpy, gensim, pickle, time, sklearn)
## Các bước cài đặt web api
- clone dự án này và chuyển đến thư mục dự án
> git clone git@github.com:desod-vn/do-an-chuyen-nganh-trainer.git
> cd do-an-chuyen-nganh-trainer
- chạy composer
> composer install && composer update
- chạy lệnh tạo key
> php artisan key:generate
- sửa file ENV và database
> cp .env .env.example
> database thì tự sửa đi nhé :v.
- chạy migrate và seed dữ liệu
> php artisan migrate
> php artisan db:seed
- kiểm tra database và thông tin người dùng mẫu lưu ở App\Models\User.php
- chạy lệnh liên kết thư mục storage
> php artisan storage:link
## Đối với cài đặt python
- tạo thư mục assets bên trong thư mục public\services và giải nén 2 file Test_Full.zip và Train_Full.zip
![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")
- tạo thư mục module bên trong thư mục public và tạo các thư mục và các file rỗng tương tự
![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")
- ...

## Thông tin thêm
[Link API](https://docs.google.com/spreadsheets/d/1JD3ScHsA5Jr4_MpnxSW0n03JV3uKLhXyTSvJfGGfRow/edit#gid=0 "Link API")