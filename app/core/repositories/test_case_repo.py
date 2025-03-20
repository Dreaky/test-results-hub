# app/core/repositories/test_case_repo.py
from app.infrastructure.database import get_db_connection
import uuid


class TestCaseRepository:
    @staticmethod
    def insert_test_case(name, team, link, test_ids, app_name):
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO test_case (id, name, team, link, test_ids, app_name) 
            VALUES (%s, %s, %s, %s, %s, %s) 
            ON CONFLICT (id) DO NOTHING;
        """
        cur.execute(query, (str(uuid.uuid4()), name, team, link, test_ids, app_name))
        conn.commit()
        cur.close()
        conn.close()
        
    @staticmethod
    def test_case_exists(test_ids):
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            SELECT id
            FROM test_case 
            WHERE test_ids LIKE %s
            LIMIT 1;
        """
        # Use a wildcard '%' to check if the test_ids appear as a part of the list
        cur.execute(query, (f"%{test_ids}%",))
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result

    @staticmethod
    def update_test_case(id, name=None, team=None, link=None, test_ids=None, app_name=None):
        conn = get_db_connection()
        cur = conn.cursor()
        if isinstance(id, list):
            id = id[0]  

        # Fetch existing test_case to get current test_ids
        query_select = "SELECT name, team, link, test_ids, app_name FROM test_case WHERE id = %s;"
        cur.execute(query_select, (id,))
        result = cur.fetchone()

        if result:
            # If the test case exists, get current values
            existing_name, existing_team, existing_link, existing_test_ids, existing_app_name = result

            # Update only the provided values, otherwise keep the existing ones
            name = name if name else existing_name
            team = team if team else existing_team
            link = link if link else existing_link
            test_ids = test_ids if test_ids else existing_test_ids
            app_name = app_name if app_name else existing_app_name

            # Update the test_case record with new values (only those that changed)
            query_update = """
                UPDATE test_case
                SET name = %s, team = %s, link = %s, test_ids = %s, app_name = %s
                WHERE id = %s;
            """
            cur.execute(query_update, (name, team, link, test_ids, app_name, id))

            # Commit the changes to the database
            conn.commit()
        else:
            print(f"Test case with ID {id} does not exist.")

        cur.close()
        conn.close()
