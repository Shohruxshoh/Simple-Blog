# 📝 Simple Blog API

Ushbu loyiha — Django Rest Framework (DRF) yordamida yaratilgan **RESTful Blog API** bo‘lib, foydalanuvchilar postlar yaratish, tahrirlash, o‘chirish va ularga komment qoldirish imkoniyatiga ega.

## 🚀 Xususiyatlar

- JWT Authentication (Login, Logout, Register)
- Postlar CRUD
- Kommentlar
- Foydalanuvchi profillari
- Swagger hujjat (drf-spectacular)
- Docker orqali ishga tushirish imkoniyati

---

## ⚙️ Texnologiyalar

- Python 3.10+
- Django 4.x
- Django Rest Framework
- SimpleJWT (Tokenlar uchun)
- drf-spectacular (Swagger uchun)
- PostgreSQL (Dockerda)
- Docker & docker-compose

---

## 🔐 API Endpoints (asosiylari)

| Method | Endpoint                     | Tavsif                         |
|--------|------------------------------|--------------------------------|
| POST   | `/auth/register/`            | Ro‘yxatdan o‘tish              |
| POST   | `/auth/login/`               | Login (JWT token olish)        |
| POST   | `/auth/refresh/`             | Access token yangilash         |
| POST   | `/auth/logout/`              | Logout (tokenni blacklist qilish) |
| GET    | `/me/`                        | Foydalanuvchining profili      |
| GET    | `/users/<id>/`               | Boshqa foydalanuvchi profili   |
| GET    | `/posts/`                    | Barcha postlar (search, pagination) |
| POST   | `/posts/`                    | Yangi post yaratish            |
| GET    | `/posts/<id>/`               | Post detallari                 |
| PUT    | `/posts/<id>/`               | Postni tahrirlash (egasi)      |
| DELETE | `/posts/<id>/`               | Postni o‘chirish (egasi)       |
| GET    | `/posts/<post_id>/comments/` | Postga tegishli kommentlar     |
| POST   | `/posts/<post_id>/comments/` | Komment qoldirish              |
| DELETE | `/comments/<id>/`            | Kommentni o‘chirish (egasi/admin) |

---

## 🐳 Docker bilan ishga tushirish
 `.env` fayl yarating va quyidagilarni kiriting:

```env
DJANGO_SECRET_KEY=super-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=*
DB_NAME=blogdb
DB_USER=bloguser
DB_PASSWORD=blogpass
DB_HOST=db
DB_PORT=5432
```
Docker konteynerlarni ishga tushiring
```bash
docker-compose up --build -d
```
Migratsiyalar va Superuser yaratish:
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
Swagger hujjat
    
    http://localhost:8000/api/schema/swagger-ui/



## Docker’siz ishga tushirish

Virtual environment yarating
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
Kutubxonalarni o‘rnating
```bash
pip install -r requirements.txt
```
.env fayl yarating
```.env
DJANGO_SECRET_KEY=super-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=blogdb
DB_USER=bloguser
DB_PASSWORD=blogpass
DB_HOST=127.0.0.1
DB_PORT=5432
```
Migratsiyalar va superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```
Serverni ishga tushuring
```bash
python manage.py runserver
```
Swagger: http://127.0.0.1:8000/api/schema/swagger-ui/

🧑‍💻 Muallif
Shohrux Nasriddinov
GitHub: @Shohruxshoh
