import requests


NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def search_cve(keyword: str):

    params = {
        "keywordSearch": keyword,
        "resultsPerPage": 5
    }


    response = requests.get(
        NVD_URL,
        params=params
    )


    if response.status_code != 200:
        return {
            "error": "Unable to query NVD",
            "status_code": response.status_code
        }


    data = response.json()


    vulnerabilities = []


    for item in data.get("vulnerabilities", []):

        cve = item["cve"]


        description = cve["descriptions"][0]["value"]


        vulnerabilities.append(
            {
                "id": cve["id"],
                "description": description,
                "published": cve.get("published"),
                "last_modified": cve.get("lastModified")
            }
        )


    return {
        "keyword": keyword,
        "total_results": len(vulnerabilities),
        "vulnerabilities": vulnerabilities
    }
