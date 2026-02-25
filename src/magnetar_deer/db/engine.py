from pathlib import Path
from sqlalchemy import create_engine, MetaData

# Define database directory
db_dir = Path(__file__).parent / "data"
db_dir.mkdir(exist_ok=True)

# Create database file path
db_path = db_dir / "test.db"
engine = create_engine(f"sqlite:///{db_path}")
metadata = MetaData()