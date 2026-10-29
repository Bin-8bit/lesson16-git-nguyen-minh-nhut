"""Unit test cho utils/string_utils.py."""

import pytest

from utils.string_utils import to_slug


def test_ho_ten_co_dau():
    assert to_slug("Nguyễn Minh Nhựt") == "nguyen-minh-nhut"


def test_chu_d_gach():
    assert to_slug("Đặng Thị Ánh") == "dang-thi-anh"


def test_ky_tu_dac_biet_va_khoang_trang_thua():
    assert to_slug("  Lesson 16: Git & GitHub  ") == "lesson-16-git-github"


def test_input_khong_phai_chuoi_phai_bao_loi():
    with pytest.raises(TypeError):
        to_slug(123)
