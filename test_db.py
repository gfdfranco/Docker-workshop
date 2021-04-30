from db_helper import DatabaseHelper

if __name__ == "__main__":
    db_manager = DatabaseHelper()
    db_manager.create_users_table()
    db_manager.insert_values_users_table("Franco")