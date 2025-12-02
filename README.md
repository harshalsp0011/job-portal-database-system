# Job Portal Database System

A database-backed job portal built for DMQL coursework. This repository contains the ER model, schema DDL, synthetic data generation and loading scripts, example queries, and a simple application entry point to interact with the database.

**Highlights**
- **Schema-first design:** ER diagram with normalized tables.
- **Reproducible setup:** SQL DDL to create schema, Python scripts to generate and load fake data.
- **Query library:** Test queries and solutions for problematic cases.
- **Light app layer:** `app.py` for quick interaction or demo.

**Folder Guide**
- `ER Diagram/`: Visuals of the database entity-relationship model.
- `Fake data/database_generation.py`: Standalone script to synthesize realistic test data.
- `Milestone 2/Problematic queries.sql`: Known tricky queries and performance/logic fixes.
- `Milestone 2/solution for pro queries.sql`: Solutions for problematic queries.
- `Milestone 2/Test queries.sql`: Validation and example queries.
- `Milestone 2/Sumission/Milestone2/Setup/`: Setup assets:
	- `create.sql`: Database schema (tables, constraints, indexes).
	- `generation.py`: Data generation utilities.
	- `load.py`: Bulk loader to insert generated data.
	- `app.py`: Minimal application entry (CLI or simple server, depending on implementation).

## Prerequisites
- macOS with `zsh` (default shell)
- Python 3.10+ installed (`python3 --version`)
- PostgreSQL 14+ installed and running locally
- `pip` available

## Quick Start
Follow these steps to create the database, generate data, load it, and run the app.

1) Create a PostgreSQL database
```zsh
createdb job_portal_db
```

2) Apply schema (`create.sql`)
```zsh
psql -d job_portal_db -f "Milestone 2/Sumission/Milestone2/Setup/create.sql"
```

3) Set up a Python virtual environment
```zsh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

4) Install Python dependencies
- If a `requirements.txt` exists in `Setup/`, install from it; otherwise install common libs.
```zsh
# Option A: requirements file
pip install -r "Milestone 2/Sumission/Milestone2/Setup/requirements.txt" 2>/dev/null || true

# Option B: common dependencies (adjust as needed)
pip install psycopg2-binary faker pandas
```

5) Generate fake data
```zsh
python "Milestone 2/Sumission/Milestone2/Setup/generation.py"
# or use the standalone script
python "Fake data/database_generation.py"
```

6) Load data into PostgreSQL
```zsh
python "Milestone 2/Sumission/Milestone2/Setup/load.py" --db job_portal_db
```

7) Run the application
```zsh
python "Milestone 2/Sumission/Milestone2/Setup/app.py" --db job_portal_db
```

## Configuration
Set connection details via environment variables or CLI flags (if supported by the scripts):
- `DB_NAME`: default `job_portal_db`
- `DB_USER`: default PostgreSQL user (often your macOS username)
- `DB_PASSWORD`: if required
- `DB_HOST`: default `localhost`
- `DB_PORT`: default `5432`

Example with env vars:
```zsh
export DB_NAME=job_portal_db
export DB_USER="$USER"
export DB_HOST=localhost
export DB_PORT=5432
```

## Running Queries
Use the provided SQL files for testing and exploration:
- `Milestone 2/Test queries.sql`
- `Milestone 2/Problematic queries.sql`
- `Milestone 2/solution for pro queries.sql`

Example:
```zsh
psql -d job_portal_db -f "Milestone 2/Test queries.sql"
```

## Project Structure (key files)
- `Milestone 2/Sumission/Milestone2/Setup/create.sql`: DDL to create tables and constraints
- `Milestone 2/Sumission/Milestone2/Setup/generation.py`: Produces CSV/rows for loading
- `Milestone 2/Sumission/Milestone2/Setup/load.py`: Inserts generated data into DB
- `Milestone 2/Sumission/Milestone2/Setup/app.py`: Minimal app demo/CLI
- `Fake data/database_generation.py`: Alternate data generation script

## Troubleshooting
- psql not found: install via Homebrew
```zsh
brew install postgresql@14
brew services start postgresql@14
```
- Connection failures: verify `psql -d job_portal_db -c "\dt"` works and your env vars.
- Permission issues: ensure your PostgreSQL user owns `job_portal_db`.
- Missing modules: re-run `pip install` inside the virtualenv.

## Notes
- File paths include spaces; use quotes in commands.
- Adjust versions and package names based on your local environment.
- If `app.py` exposes a web server, check its output for the URL (e.g., http://127.0.0.1:5000).

## License
Academic project materials. Use responsibly per course guidelines.

