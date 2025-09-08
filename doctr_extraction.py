from doctr.io import DocumentFile
from doctr.models import ocr_predictor


class DocTrOCR:
    """
    DocTrOCR class handles text extraction and recognition using Mindee Doctr
    """

    class_variable = "DocTR OCR Engine"

    def __init__(self):
        """
        Initialize OCR predictor (detection + recognition)
        """
        # load both text detection + recognition pretrained models
        self.model = ocr_predictor(pretrained=True)

    def read_text(self, image_path):
        """
        Extract text from image using doctr.io

        Args:
            image_path (str): Path to image file

        Returns:
            dict: Extracted text details (full text, blocks, lines, words)
        """
        try:
            if not image_path:
                return {"error": "No image path provided"}

            # Load document (can be one or multiple images)
            doc = DocumentFile.from_images(image_path)

            # Run OCR
            result = self.model(doc)

            # Export as dict for detailed parsing
            exported = result.export()

            # Collect text
            full_text = []
            detailed_data = []

            for page in exported.get("pages", []):
                for block in page.get("blocks", []):
                    for line in block.get("lines", []):
                        line_text = " ".join([word["value"] for word in line["words"]])
                        full_text.append(line_text)
                        detailed_data.append({
                            "line_text": line_text,
                            "words": line["words"],
                        })

            if full_text:
                return {
                    "success": True,
                    "full_text": " ".join(full_text),
                    "detailed_results": detailed_data,
                    "total_lines": len(detailed_data),
                }
            else:
                return {
                    "success": False,
                    "message": "No text detected in the image"
                }

        except FileNotFoundError:
            return {"error": f"Image file not found at {image_path}"}
        except Exception as e:
            return {"error": f"OCR extraction failed: {str(e)}"}

    @classmethod
    def recognition(cls):
        """
        Class-level method for recognition engine details
        """
        return f"OCR Engine in use: {cls.class_variable}"

    @staticmethod
    def info():
        """
        Static method providing general info
        """
        return "This class performs OCR text extraction using Mindee DocTR."
