# django
from base64 import b64encode
import StringIO

# lib
import qrcode


def qrcode_datauri(data, pixel_size=5, border_pixels=1, error_correction="H"):
    qrcode_object = qrcode.QRCode(
        error_correction=getattr(
            qrcode.constants,
            "ERROR_CORRECT_%s" % error_correction,
            "H"
        ),
        box_size=max(1, min(100, pixel_size)),
        border=max(1, min(100, border_pixels)),
    )
    qrcode_object.add_data(data)
    qrcode_object.make(fit=True)
    qrcode_image = qrcode_object.make_image()
    byte_stream = StringIO.StringIO()
    qrcode_image.save(byte_stream)
    datauri = "data:image/png;base64,%s" % b64encode(byte_stream.getvalue())
    byte_stream.close()
    return datauri
