# ImgToPdf

This Python script automates the conversion of images into a PDF file while optimizing their size and reducing quality to save space.

## Features  
- Automatic resizing of images before conversion.  
- Compression to reduce file size without significant quality loss.  
- PDF conversion with automatic page orientation.  
- Deletes original images after adding them to the PDF.  

## Requirements  
🔹 Python 3+  
🔹 Required libraries:  
```bash
pip install fpdf pillow
```

## Usage  
1. Place the images inside the specified folder.  
2. Run the script.  
3. The generated PDF will be saved in the same folder.  

⚠️ **Note:** The script deletes the original images after conversion!  

📄 **License:** MIT  
