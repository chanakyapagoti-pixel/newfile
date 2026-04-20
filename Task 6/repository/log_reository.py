from db_config import get_db_connection

def get_daily_activity_report():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT DATE(changed_at) AS log_date,
               COUNT(*) AS total_changes
        FROM employee_log
        GROUP BY DATE(changed_at)
        ORDER BY log_date DESC
        """

        cursor.execute(query)
        result = cursor.fetchall()

        return result

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_detailed_logs():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT *
        FROM employee_log
        ORDER BY changed_at DESC
        """

        cursor.execute(query)
        result = cursor.fetchall()

        return result

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()