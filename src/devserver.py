import uvicorn

# from dotenv import load_dotenv

if __name__ == "__main__":
    # load_dotenv()
    uvicorn.run(
        app="main:app", host="0.0.0.0", port=5001, reload=True
    )
