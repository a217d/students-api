from fastapi import FastAPI
from routers import students

app = FastAPI(title="Student API")

# ربط الـ router
app.include_router(students.router)

@app.get("/")
def root():
    return {"message": "أهلاً بك في أول API لك يا هندسة!"}