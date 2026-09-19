from pathlib import Path

ROOT = Path(__file__).resolve().parent
PDF_PATH = r"C:\Users\snuepc\Documents\4차시_실습파일\4차시_실습파일\data\pokemon_guide_text.pdf"

MODEL = "qwen2.5:7b "
REVIEW_MODEL = "qwen3:8b"
EMBED_MODEL = "bge-m3"
TOP_K = 3
CHUNK_SIZE = 700
CHUNK_OVERLAP = 100
