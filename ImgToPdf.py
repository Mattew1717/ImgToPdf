import os
from fpdf import FPDF
from PIL import Image

image_folder = "./images"  # Generic path for the image folder
output_pdf = "./output_images.pdf"  # Generic path for the PDF file

imagelist = os.listdir(image_folder)
pdf = FPDF()
pdf.set_auto_page_break(0)

# Image size optimization
for image in imagelist:
    complete_path = os.path.join(image_folder, image)
    try:
        img = Image.open(complete_path)
        width, height = img.size
        wr, hr = width * 0.70, height * 0.70
        img = img.resize((int(wr), int(hr)))
        img.save(complete_path, optimize=True, quality=50)
    except Exception as e:
        print(f"Error processing {image}: {e}")

for image in imagelist:
    complete_path = os.path.join(image_folder, image)
    print(complete_path)
    try:
        # Image resizing for PDF
        im = Image.open(complete_path)
        width, height = im.size
        width, height = float(width * 0.264583), float(height * 0.264583)
        pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
        orientation = 'P' if width < height else 'L'
        width = min(width, pdf_size[orientation]['w'])
        height = min(height, pdf_size[orientation]['h'])
        pdf.add_page(orientation=orientation)
        pdf.image(complete_path, 0, 0, width, height)
        # Remove image after adding to PDF
        im.close()
        os.remove(complete_path)
    except Exception as e:
        print(f"Image transfer failed ({image}): {e}")

pdf.output(output_pdf, "F")
