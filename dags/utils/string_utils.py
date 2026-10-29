"""Tiện ích xử lý chuỗi tiếng Việt.

Hàm chính: to_slug(text) -> str
    Bỏ dấu tiếng Việt, chuyển về chữ thường, nối các từ bằng dấu gạch ngang.
    Ví dụ: "Nguyễn Minh Nhựt" -> "nguyen-minh-nhut"
"""

import re
import unicodedata


def to_slug(text: str) -> str:
    """Chuyển chuỗi tiếng Việt có dấu thành slug không dấu.

    Input : text (str), ví dụ "Nguyễn Minh Nhựt"
    Output: str, ví dụ "nguyen-minh-nhut"
    """
    if not isinstance(text, str):
        raise TypeError("text phải là chuỗi (str)")

    # "đ"/"Đ" không tách dấu được bằng unicodedata nên thay tay
    text = text.replace("đ", "d").replace("Đ", "D")
    # Tách chữ và dấu (NFD) rồi bỏ các ký tự dấu (category Mn)
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    text = text.lower()
    # Mọi cụm ký tự không phải chữ/số -> 1 dấu gạch ngang
    words = re.findall(r"[a-z0-9]+", text)
    return "-".join(words)


if __name__ == "__main__":
    samples = ["Nguyễn Minh Nhựt", "Lesson 16: Git & GitHub", "  Đặng   Thị   Ánh  "]
    for s in samples:
        print(f"to_slug({s!r}) -> {to_slug(s)!r}")
