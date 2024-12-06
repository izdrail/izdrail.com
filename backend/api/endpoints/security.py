from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
import sqlite3
import requests


class ScanRequest(BaseModel):
    query_type: str
    query_value: str


class ScanResult:
    query_type: str
    query_value: str
    results: dict


class SpiderFoot:
    def scan(self, query):
        # Implement SpiderFoot logic here
        url = "http://localhost:5001/startscan"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'osint/0.0.1'
        }
        data = {
            'scanname': f"{query}",
            'scantarget': f"{query}",
            'usecase': 'all',
            'modulelist': '',
            'typelist': ''
        }
        response = requests.post(url, headers=headers, data=data, allow_redirects=False)
        return response.json()


class BBot:
    def scan(self, query):
        return {}


class ScanManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.db_connection = sqlite3.connect(db_file)

    def check_if_scanned(self, query_type, query_value):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM scans WHERE query_type=? AND query_value=?", (query_type, query_value))
        return cursor.fetchone() is not None

    def store_scan(self, query_type, query_value, results):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO scans (query_type, query_value, results) VALUES (?, ?, ?)",
                       (query_type, query_value, results))
        self.db_connection.commit()

    def dispatch_scan(self, query_type, query_value):
        if self.check_if_scanned(query_type, query_value):
            # Fetch results from the database
            pass
        else:
            if query_type in ["email", "domain"]:
                scanner = SpiderFoot()
            elif query_type in ["phone", "company"]:
                scanner = BBot()
            else:
                raise HTTPException(status_code=400, detail="Invalid query type")

            results = scanner.scan(query_value)
            self.store_scan(query_type, query_value, results)
            return results


router = APIRouter()
app = FastAPI()
app.include_router(router)


@app.post("/scan")
async def scan(request: ScanRequest):
    scan_manager = ScanManager("scans.db")
    results = scan_manager.dispatch_scan(request.query_type, request.query_value)
    return {"results": results}
