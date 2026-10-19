from pathlib import Path
import pymupdf


def extract_pdf_text(pdf_bytes: bytes) -> dict:
    """Extract selectable text from a PDF and retain page-level evidence."""
    if not pdf_bytes:
        raise ValueError("The uploaded PDF is empty.")

    pages = []
    try:
        with pymupdf.open(stream=pdf_bytes, filetype="pdf") as doc:
            if doc.is_encrypted:
                raise ValueError("Password-protected PDFs are not supported in this version.")
            for index, page in enumerate(doc, start=1):
                text = page.get_text("text").strip()
                pages.append({"page": index, "text": text})
    except ValueError:
        raise
    except Exception as exc:
        raise ValueError("Could not read this PDF. Check that it is a valid PDF file.") from exc

    full_text = "\n\n".join(
        f"[Page {item['page']}]\n{item['text']}" for item in pages if item["text"]
    )
    if not full_text.strip():
        raise ValueError(
            "No selectable text was found. This may be a scanned PDF; OCR support is a later phase."
        )
    return {"page_count": len(pages), "pages": pages, "text": full_text}
