"""Đổi nền ảnh khung sản phẩm (images/san-pham/khung/*.jpg) từ đỏ sang xanh lá của logo Phát Lộc (30/10/2026).
Giữ nguyên ảnh sản phẩm trong vòng tròn, thẻ quà tặng/cam kết bên trái và nhãn GIAN HÀNG CHÍNH HÃNG.
Chạy: python3 tools/doi-khung-xanh.py [mã...]   (không có mã = tất cả). Ghi đè .jpg và tạo lại .webp, nho/khung/*.webp
"""
import sys, os, glob
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
K = R + "images/san-pham/khung/"
GREEN_H = 148 / 360          # xanh lá logo

def mask_keep(size):
    m = Image.new("L", size, 0); d = ImageDraw.Draw(m)
    cx, cy, r = 572, 555, 237
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)   # ảnh sản phẩm + viền vàng
    d.rounded_rectangle((30, 468, 268, 750), 14, fill=255)  # phần kem của thẻ quà / cam kết
    return np.asarray(m.filter(ImageFilter.GaussianBlur(1.5))) / 255.0

def convert(path):
    im = Image.open(path).convert("RGB")
    hsv = np.asarray(im.convert("HSV")).astype(float) / 255.0
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    red = ((h > 0.92) | (h < 0.045)) & (s > 0.30)
    # vùng thẻ bên trái: chỉ đổi nền đỏ tối, giữ nơ đỏ tươi
    yy, xx = np.mgrid[0:im.size[1], 0:im.size[0]]
    sticker = (xx >= 14) & (xx <= 285) & (yy >= 385) & (yy <= 775)
    red = red & ~(sticker & (v > 0.62))
    w = red * (1 - mask_keep(im.size))
    h2 = np.where(w > 0, GREEN_H, h)
    v2 = np.where(w > 0, v * 0.78, v)          # xanh đậm như mặt chữ PL
    s2 = np.where(w > 0, np.minimum(1, s * 0.95), s)
    out = Image.fromarray((np.stack([h2, s2, v2], -1) * 255).astype("uint8"), "HSV").convert("RGB")
    # trộn mép theo trọng số để không răng cưa
    a = np.asarray(im).astype(float); b = np.asarray(out).astype(float)
    res = (a * (1 - w[..., None]) + b * w[..., None]).astype("uint8")
    return Image.fromarray(res)

if __name__ == "__main__":
    ids = sys.argv[1:]
    files = [K + f"{i}.jpg" for i in ids] if ids else sorted(glob.glob(K + "*.jpg"))
    os.makedirs(R + "images/san-pham/nho/khung", exist_ok=True)
    for f in files:
        img = convert(f); n = os.path.basename(f)[:-4]
        img.save(f, quality=86, optimize=True, progressive=True)
        img.save(K + n + ".webp", quality=82)
        img.resize((450, 450), Image.LANCZOS).save(R + f"images/san-pham/nho/khung/{n}.webp", quality=80)
    print("Đã đổi", len(files), "ảnh")
