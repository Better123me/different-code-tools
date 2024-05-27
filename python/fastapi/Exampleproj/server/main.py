from fastapi import FastAPI, File
from starlette.responses import FileResponse
from PIL import Image 
import uvicorn
import io
app = FastAPI()

def get_image_from_bytes(binary_image: bytes) -> Image:
    """Convert image from bytes to PIL RGB format
    
    Args:
        binary_image (bytes): The binary representation of the image
    
    Returns:
        PIL.Image: The image in PIL RGB format
    """
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
    return input_image


@app.get("/")
def img():
    img = "./ski.jpg"
    return FileResponse(img, filename="ski.jpg")

@app.post("/hello")
def file(file:bytes=File()):
    result = {"detect_obj":None}
    input_img = get_image_from_bytes(file)

    img = "./ski.jpg"
    return FileResponse(input_img, filename="ski.jpg")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)