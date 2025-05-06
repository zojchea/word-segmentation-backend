import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.divide_word_controller import DivideWordController

app = FastAPI()
divide_word_router = DivideWordController()
app.include_router(divide_word_router.router)

origins = [
    "https://word-segmentation.online",
    "https://graduate-thesis-714a1.web.app",
    "http://localhost:4200" # Replace with the domain of your Angular application
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    # load_dotenv()
    uvicorn.run(app)
