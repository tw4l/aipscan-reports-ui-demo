from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


class StorageService:

    def __init__(self, id=1, name="Some name"):
        self.id = id
        self.name = name


STORAGE_SERVICES = [
    StorageService(),
    StorageService(id=2, name="Another name"),
    StorageService(id=3, name="A third name"),
]


@app.route('/')
def index():
    file_formats = ["Plain text file", "Comma Separated Values", "PDF 1.4", "something else"]
    puids = ["fmt/1", "fmt/2", "fmt/15", "fmt/200", "x-fmt/333"]

    now = datetime.now()
    start_date = str(datetime(now.year, 1, 1))[:-9]
    end_date = str(datetime(now.year, now.month, now.day))[:-9]

    return render_template(
        "index.html",
        storage_services=[x.__dict__ for x in STORAGE_SERVICES],
        storage_service=STORAGE_SERVICES[0],
        file_formats=file_formats,
        puids=puids,
        start_date=start_date,
        end_date=end_date,
    )
