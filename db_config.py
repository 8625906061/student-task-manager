import mysql.connector
def get_database_connection():
    connection = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="rNPJrXvYd6ZwrmC.root",
        password="MA3e9lCdoUmnxM9i",
        database="STUDENT_TASK_MANAGER",
        port="4000"
    )
    return connection