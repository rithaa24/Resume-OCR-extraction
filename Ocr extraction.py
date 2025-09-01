class OCR:
    
    class_variable = "Resume OCR"
    
    def __init__(self, image1, image2=None):
        self.instance_variable1 = image1
        self.instance_variable2 = image2
    
    def extract(self):
        return f"Value: {self.instance_variable1}"
    
    @classmethod
    def class_method(cls):
        return cls.class_variable
    
    @staticmethod
    def static_method():
        return "OCR scan is not successful"
    
    def extract_image(self, image_path=None, lang='eng'):
            img_path = image_path
            image = image.open(img_path)