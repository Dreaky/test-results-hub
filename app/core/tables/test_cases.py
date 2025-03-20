# app/core/repositories/test_case_repo.py
from app.infrastructure.database import execute_query
import uuid


class TestCaseTable:
    @staticmethod
    def insert_test_case(name, team, link, test_ids, app_name):
        tc_id = str(uuid.uuid4())
        query = """
            INSERT INTO test_case (id, name, team, link, test_ids, app_name) 
            VALUES (%s, %s, %s, %s, %s, %s) 
            ON CONFLICT (id) DO NOTHING;
        """
        execute_query(query, (tc_id, name, team, link, test_ids, app_name))
        return tc_id
        
    @staticmethod
    def test_case_exists(test_ids):
        query = """
            SELECT id
            FROM test_case 
            WHERE test_ids LIKE %s
            LIMIT 1;
        """
        # Use a wildcard '%' to check if the test_ids appear as a part of the list
        result = execute_query(query, (f"%{test_ids}%",), True)
        return result

    @staticmethod
    def update_test_case(tc_id, name=None, team=None, link=None, test_ids=None, app_name=None):
        if isinstance(tc_id, list):
            tc_id = tc_id[0]

        # Fetch existing test_case to get current test_ids
        query_select = "SELECT name, team, link, test_ids, app_name FROM test_case WHERE id = %s;"
        result = execute_query((query_select, (tc_id,)), True)

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
            execute_query(query_update, (name, team, link, test_ids, app_name, tc_id))
        else:
            print(f"Test case with ID {tc_id} does not exist.")
