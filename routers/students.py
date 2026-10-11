from fastapi import APIRouter, HTTPException
from database import get_db # جلب الداله من صفحه database
from schemas import Student #  جلب كلاس التحقق من صفحه schemas

router = APIRouter()


# جلب جميع الطلاب
@router.get("/students")
def get_all_students():
    db = get_db()# استقبال الداله
    cursor = db.cursor(dictionary=True) # التحقق من الاتصال بقاعده البيانات
    cursor.execute("SELECT * FROM `students`")# تنفيذ الاستعلام
    students = cursor.fetchall()# جلب ناتج الاستعلام
    db.close()

    if not students:
        raise HTTPException(status_code=404, detail="لا يوجد طلاب")# رساله الخطا
    return students


# جلب طالب واحد
@router.get("/student/{myid}")
def get_student_by_id(myid: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM `students` WHERE id = %s", (myid,))# ادخال رقم id الخص بالطالب
    student = cursor.fetchone()# جلب بيانات الطالب هذا تحديدا
    db.close()

    if not student:
        raise HTTPException(status_code=404, detail="الطالب غير موجود")
    return student


# إضافة طالب
@router.post("/student/create")
def create_student(student: Student):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name FROM `students` where name = %s", (student.name,))# التحقق من عدم تكرار الاسم بداخل قاعده البيانات
    al_student_name = cursor.fetchone()# جلب نتيجه الاستعلام

    #توقف الاضافه بسبب تكرار الاسم
    if al_student_name :
        db.close()
        raise HTTPException(status_code=404, detail="عذرا لم تتم ااضافه الاسم هذا موجود مسبقا")

    else:
        # انتظار الادخال
        sql = ("INSERT INTO `students`(`name`, `age`, `department`) "
                                   "VALUES (%s, %s, %s)")
        val = (student.name, student.age, student.department)#  Student التحقق من صحه المدخل عبر الاوبجكت التابع ل كلاس
        cursor.execute(sql, val)# تنفيذ الاستعلم


        db.commit()# حفظ الاضافه بداخل قاعده البيانات
        db.close()
        return {"message": "تمت الإضافة بنجاح"}


# تحديث طالب
@router.put("/student/update/{id}")
def update_student(id: int, student: Student):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    # تحقق أولاً
    cursor.execute("SELECT * FROM `students` WHERE id = %s", (id,))
    if not cursor.fetchone():
        db.close()
        raise HTTPException(status_code=404, detail="الطالب غير موجود")

    # ثم حدّث
    sql = "UPDATE `students` SET `name`= %s, `age`= %s, `department`= %s WHERE id = %s"
    val = (student.name, student.age, student.department, id)
    cursor.execute(sql, val)
    db.commit()
    db.close()
    return {"message": "تم التحديث بنجاح"}


# حذف طالب
@router.delete("/student/{id}")
def delete_student(id: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    # تحقق أولاً
    cursor.execute("SELECT * FROM `students` WHERE id = %s", (id,))
    student = cursor.fetchone()
    if not student:
        db.close()
        raise HTTPException(status_code=404, detail="الطالب غير موجود")

    # ثم احذف
    cursor.execute("DELETE FROM `students` WHERE id = %s", (id,))
    db.commit()
    db.close()
    return {"message": "تم الحذف بنجاح", "student": student}