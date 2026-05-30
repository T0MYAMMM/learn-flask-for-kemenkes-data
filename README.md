# Rumah Sakit Search Engine

A lightweight Flask web application for searching Indonesian hospitals
(*Rumah Sakit*). It serves a searchable table backed by a CSV dataset of roughly
2,700 hospitals sourced from medicalclinic.id, allowing users to filter records
by name, type, address, or city through a simple web interface and a JSON API.

## Architecture / Tech Stack

- **Language:** Python 3.9+
- **Web framework:** Flask
- **Data processing:** pandas
- **Frontend:** Server-rendered Jinja2 templates with Bootstrap 4 and vanilla
  JavaScript for asynchronous search
- **Deployment:** Vercel (`@vercel/python`)

The application uses the Flask application-factory pattern. Data loading,
search logic, and HTTP routing are separated into dedicated modules, and the
dataset is read once and cached in memory.

## Project Structure

```
.
├── api/
│   └── app.py                 # Vercel serverless entry point
├── data/
│   └── rumahsakit_medicalclinicid_cleaned.csv
├── src/
│   └── hospital_search/
│       ├── __init__.py        # create_app() application factory
│       ├── config.py          # Configuration and environment variables
│       ├── data.py            # Dataset loading and caching
│       ├── search.py          # Search/filter logic
│       ├── routes.py          # Flask blueprint (routes)
│       └── templates/
│           └── index.html     # Search UI
├── main.py                    # Local development entry point
├── pyproject.toml             # Project metadata and dependencies
├── requirements.txt           # Pinned runtime dependencies
├── vercel.json                # Vercel build/route configuration
├── .env.example               # Documented environment variables
└── README.md
```

## Local Setup & Installation

1. Clone the repository and enter the directory:

   ```bash
   git clone https://github.com/T0MYAMMM/learn-flask-for-kemenkes-data.git
   cd learn-flask-for-kemenkes-data
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Configure environment variables:

   ```bash
   cp .env.example .env
   ```

5. Run the development server:

   ```bash
   python main.py
   ```

   The application is available at `http://localhost:5000`.

## Usage

### Web interface

Open `http://localhost:5000` in a browser. The table shows an initial set of
hospitals. Enter a term in the search box and submit to filter by name, type,
address, or city. The result count and query processing time are displayed
above the table.

### JSON API

The search is also available as a JSON endpoint:

```bash
curl "http://localhost:5000/api/search?query=gombong"
```

Example response:

```json
{
  "query": "gombong",
  "count": 5,
  "processing_time_ms": 4.95,
  "results": [
    {
      "Nama Rumah Sakit": "RSU PKU Muhamadiyah Gombong",
      "Jenis Rumah Sakit": "RSU",
      "Alamat": "Jl. Yos Sudarso 461 Gombong Kebumen",
      "Kab/Kota": "Kebumen"
    }
  ]
}
```

An empty `query` returns the first records so the table is never blank.

## Future Improvements

- Add pagination and server-side sorting for large result sets.
- Introduce fuzzy matching and relevance ranking instead of plain substring
  search.
- Expose more dataset fields (class, director, contact details) with a detail
  view per hospital.
- Replace the in-memory CSV with an indexed data store (for example SQLite with
  full-text search) for faster queries.
- Add automated tests and continuous integration.
- Provide filter controls for hospital type and region.
