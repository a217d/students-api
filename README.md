# Students API

REST API بسيط لإدارة الطلاب باستخدام FastAPI و MySQL.

## 🛠️ Technologies Used
- **FastAPI**: إطار عمل حديث لبناء APIs.
- **MySQL**: قاعدة بيانات علائقية.
- **Python 3.14**: لغة البرمجة.
- **Pydantic**: للتحقق من البيانات.

## 📌 Features
- ✅ جلب كل الطلاب
- ✅ جلب طالب واحد بالـ ID
- ✅ إضافة طالب جديد (مع منع التكرار)
- ✅ تحديث بيانات طالب
- ✅ حذف طالب

## 🚀 How to Run
1. ثبت المتطلبات:
   ```bash
   pip install fastapi uvicorn mysql-connector-python