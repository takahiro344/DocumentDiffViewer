from difflib import SequenceMatcher
from io import BytesIO

import mammoth
from fastapi import HTTPException, UploadFile

from backend.models.diff import Diff


async def extract_word_diff(
        file1: UploadFile,
        file2: UploadFile) -> list[Diff]:
    def extract_text(file_bytes: bytes) -> str:
        with BytesIO(file_bytes) as bio:
            try:
                result = mammoth.convert_to_html(bio)
                return result.value
            except Exception as e:
                print(f"Error extracting text: {e}")
                raise HTTPException(
                    status_code=400,
                    detail=f"Wordファイルの読み取りに失敗しました: {str(e)}")

    content1 = await file1.read()
    content2 = await file2.read()

    text1 = extract_text(content1)
    text2 = extract_text(content2)

    # 差分抽出（文字列ベース）
    matcher = SequenceMatcher(None, text1, text2)
    diffs: list[Diff] = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "replace" or tag == "delete" or tag == "insert":
            before = text1[i1:i2] if tag != "insert" else ""
            after = text2[j1:j2] if tag != "delete" else ""
            diffs.append(Diff(before=before, after=after, tag=tag))

    return diffs
