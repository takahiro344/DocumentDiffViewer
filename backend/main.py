import debugpy
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from backend.models import Diff
from backend.services.word_diff import extract_word_diff

debugpy.listen(("0.0.0.0", 5678))
print("Waiting for debugger attach...")
debugpy.wait_for_client()

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Document Diff Viewer API"}


@app.post("/diff/word", response_model=list[Diff])
async def get_diff_word(
    file1: UploadFile = File(...),
    file2: UploadFile = File(...)
):
    diffs = await extract_word_diff(file1, file2)
    return diffs
