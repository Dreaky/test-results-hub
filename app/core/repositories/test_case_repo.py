from db_config import get_db_connection

class TestCaseRepository:
    @staticmethod
    def insert_test_case(tc_id, name, team, link, test_ids, app_name):
        conn = get_db_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO test_case (id, name, team, link, test_ids, app_name) 
            VALUES (%s, %s, %s, %s, %s, %s) 
            ON CONFLICT (id) DO NOTHING;
        """
        cur.execute(query, (tc_id, name, team, link, test_ids, app_name))
        conn.commit()
        cur.close()
        conn.close()