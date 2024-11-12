import qrcode
import io

def fzr_qrcode(url):
    qr = qrcode.make(url)
    img_bytes = io.BytesIO()
    qr.save(img_bytes, format="PNG")
    return img_bytes
