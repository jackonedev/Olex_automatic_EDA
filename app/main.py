from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import FileResponse
from .tools import funciones_db, profiler
import os

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), title: str = Query(...)):

    # change directory to app
    cwd = os.getcwd()
    appd = os.path.join(cwd, "app")
    os.chdir(appd)

    input_file_path = "input_data/" + file.filename
    report_file_path = "output/" + file.filename

    ##TODO: Verify if the file is a csv

    # Save the uploaded file to disk
    with open(input_file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Convert the file to a Pandas DataFrame
    dataframe = funciones_db.convert_path_to_dataframe(input_file_path)
    
    # Create instance of report file to disk
    report = profiler.from_dataframe_to_report(
        df=dataframe, title=title, output_file=report_file_path)
    
    # Return the profile report
    report_file_path = report_file_path.replace(".csv", ".html")
    try:
        headers = {
        "Content-Disposition": f"attachment; filename={report_file_path}"
    }
        return FileResponse(report_file_path, media_type="application/octet-stream", headers=headers)
    except Exception as e:
        # Print any exception that occurs for debugging purposes
        print("Exception:", e)
        raise e