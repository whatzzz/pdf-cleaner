import fitz  # PyMuPDF
import os
from PIL import Image
import numpy as np

def is_blank_page(page, tolerance=5):
    zoom = 2
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)

    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    gray = image.convert("L")
    arr = np.array(gray)

    white_ratio = np.sum(arr > 255 - tolerance) / arr.size
    return white_ratio > 0.99

def remove_blank_pages(filepath):
    doc = fitz.open(filepath)
    new_doc = fitz.open()

    for i in range(len(doc)):
        page = doc[i]
        if not is_blank_page(page):
            new_doc.insert_pdf(doc, from_page=i, to_page=i)

    new_path = filepath.replace(".pdf", "_cleaned.pdf")
    new_doc.save(new_path)
    return new_path

def parse_pages(pages_str):
    result = set()
    parts = pages_str.split(",")
    for part in parts:
        if "-" in part:
            start, end = part.split("-")
            result.update(range(int(start)-1, int(end)))
        else:
            result.add(int(part.strip()) - 1)
    return sorted(result)

def remove_specified_pages(filepath, pages_to_delete):
    doc = fitz.open(filepath)
    new_doc = fitz.open()

    for i in range(len(doc)):
        if i not in pages_to_delete:
            new_doc.insert_pdf(doc, from_page=i, to_page=i)

    new_path = filepath.replace(".pdf", "_manual_cleaned.pdf")
    new_doc.save(new_path)
    return new_path
def parse_pages(pages_str):
    result = set()
    parts = pages_str.split(",")
    for part in parts:
        if "-" in part:
            start, end = part.split("-")
            result.update(range(int(start)-1, int(end)))
        else:
            result.add(int(part.strip()) - 1)
    return sorted(result)
