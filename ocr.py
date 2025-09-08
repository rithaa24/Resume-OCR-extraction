import time
from doctr_extraction import DocTrOCR

# Measure start time
start_time = time.time()

# Initialize OCR engine
ocr_engine = DocTrOCR()

# Run OCR
result = ocr_engine.read_text("C:\\Users\\shari\\Desktop\\Zoho\\data science resumes\\Image_80.png")

# Measure end time
end_time = time.time()
elapsed_time = end_time - start_time

# Check if OCR succeeded
if result.get("success"):
    print("Full Text:", result.get("full_text", ""))

    print("\nDetailed Results:")
    for item in result.get("detailed_results", []):
        print(item.get("line_text", ""))
else:
    print("OCR Failed:", result)

# Print engine info
print("\n", DocTrOCR.recognition())
print(DocTrOCR.info())

# Print runtime
print(f"\nRuntime: {elapsed_time:.2f} seconds")


