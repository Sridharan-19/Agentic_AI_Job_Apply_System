import sqlite3

from pathlib import Path

class SQLiteManager:

    def __init__(

            self,

            db_path=None

    ):
        base_dir = Path(__file__).parent
        if db_path is None:
            db_path = base_dir / "jobs.db"

        base_dir.mkdir(

            parents=True,

            exist_ok=True

        )

        self.conn = sqlite3.connect(

            str(db_path)

        )

        self.cursor = self.conn.cursor()

        self.create_tables()

        self.upgrade_applications_table()   

    def create_tables(

            self

    ):

        self.cursor.execute(

            """

            CREATE TABLE IF NOT EXISTS jobs(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                title TEXT,

                company TEXT,

                url TEXT UNIQUE,

                location TEXT,

                salary TEXT,

                remote BOOLEAN,

                jd TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )

            """

        )

        self.cursor.execute(

            """

            CREATE TABLE IF NOT EXISTS resumes(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                job_id INTEGER,

                resume_path TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )

            """

        )

        self.cursor.execute(

            """

            CREATE TABLE IF NOT EXISTS applications(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                job_id INTEGER,

                status TEXT,

                applied_at TIMESTAMP

            )

            """

        )

        self.conn.commit()

    def upgrade_applications_table(self):

        columns = [

            (

                "resume_path",

                "TEXT"

            ),

            (

                "response",

                "TEXT"

            ),

            (

                "notes",

                "TEXT"

            ),

            (

                "last_updated",

                "TIMESTAMP"

            )

        ]

        self.cursor.execute(

            "PRAGMA table_info(applications)"

        )

        existing_columns = [

            row[1]

            for row in self.cursor.fetchall()

        ]

        for column_name, column_type in columns:

            if column_name not in existing_columns:

                self.cursor.execute(

                    f"""

                    ALTER TABLE applications

                    ADD COLUMN

                    {column_name}

                    {column_type}

                    """

                )

        self.conn.commit()



    def save_job(

            self,

            job

    ):

        self.cursor.execute(

            """

            INSERT OR IGNORE INTO jobs(

                title,

                company,

                url,

                location,

                salary,

                remote,

                jd

            )

            VALUES(

                ?,?,?,?,?,?,?

            )

            """,

            (

                job.title,

                job.company,

                job.url,

                job.location,

                job.salary,

                job.remote,

                job.jd

            )

        )

        self.conn.commit()

    def get_job_id(

            self,

            url

    ):

        self.cursor.execute(

            """

            SELECT id

            FROM jobs

            WHERE url=?

            """,

            (

                url,

            )

        )

        row = self.cursor.fetchone()

        if row:

            return row[0]

        return None

    def save_resume(

            self,

            job_id,

            resume_path

    ):

        self.cursor.execute(

            """

            INSERT INTO resumes(

                job_id,

                resume_path

            )

            VALUES(

                ?,?

            )

            """,

            (

                job_id,

                resume_path

            )

        )

        self.conn.commit()

    def save_application(
        self,
        job_id,
        status,
        applied_at,
        resume_path="",
        response="",
        notes=""
        ):

        self.cursor.execute(

            """

            INSERT INTO applications(

                job_id,

                status,

                applied_at,

                resume_path,

                response,

                notes,

                last_updated

            )

            VALUES(

                ?,?,?,?,?,?,?

            )

            """,

            (

                job_id,

                status,

                applied_at,

                resume_path,

                response,

                notes,

                applied_at

            )

        )

        self.conn.commit()

    def get_jobs(

            self

    ):

        self.cursor.execute(

            """

            SELECT *

            FROM jobs

            """

        )

        return self.cursor.fetchall()

    def get_applications(

            self

    ):

        self.cursor.execute(

            """

            SELECT *

            FROM applications

            """

        )

        return self.cursor.fetchall()
    
    def update_application(
        self,
        job_id,
        status,
        notes,
        last_updated
        ):

        self.cursor.execute(

            """

            UPDATE applications

            SET

                status=?,

                notes=?,

                last_updated=?

            WHERE

                job_id=?

            """,

            (

                status,

                notes,

                last_updated,

                job_id

            )

        )

        self.conn.commit()

    def get_by_status(
        self,
        status
        ):
        self.cursor.execute(

            """

            SELECT *

            FROM applications

            WHERE status=?

            """,

            (

                status,

            )

        )

        return self.cursor.fetchall()
    
    def get_application_summary(self):

        self.cursor.execute(

            """

            SELECT

                status,

                COUNT(*)

            FROM applications

            GROUP BY status

            """

        )

        return self.cursor.fetchall()
    
    def get_all_applications(self):

        self.cursor.execute(

            """

            SELECT *

            FROM applications

            ORDER BY applied_at DESC

            """

        )

        return self.cursor.fetchall()