import sqlite3
from datetime import datetime

class TODO():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create Categories table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Categories (
                category_id INTEGER PRIMARY KEY,
                category_name TEXT NOT NULL
            )
        ''')

        # Create Tasks table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tasks (
                task_id INTEGER PRIMARY KEY,
                task_name TEXT NOT NULL,
                is_completed INTEGER DEFAULT 0,
                created_at TEXT NOT NULL,
                completed_at TEXT,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES Categories(category_id)
            )
        ''')
        self.conn.commit()

    def add_category(self, category_name):
        self.cursor.execute('''
            INSERT INTO Categories (category_name) VALUES (?)
        ''', (category_name,))
        self.conn.commit()

    def add_task(self, task_name, created_at, category_id=None):
        self.cursor.execute('''
            INSERT INTO Tasks (task_name, created_at, category_id) VALUES (?, ?, ?)
        ''', (task_name, created_at, category_id))
        self.conn.commit()
    
    def complete_task(self, task_id, completed_at):
        self.cursor.execute('''
            UPDATE Tasks SET is_completed = 1, completed_at = ? WHERE task_id = ?
        ''', (completed_at, task_id))
        self.conn.commit()

    def list_all_tasks(self):
        self.cursor.execute('''
            SELECT * FROM Tasks
        ''')
        return self.cursor.fetchall()

    def list_tasks_by_category(self, category_id):
        self.cursor.execute('''
            SELECT * FROM Tasks WHERE category_id = ?
        ''', (category_id,))
        return self.cursor.fetchall()
    
    def list_categories(self):
        self.cursor.execute('''
            SELECT * FROM Categories
        ''')
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    todo = TODO("tasks.db")
    print("Welcome To KB-TODO")
    help_txt = '''
        KB-TODO
        
        Commands:
        
        i <task_name> <category_id>: Insert Task

        ic <category_name>: Add Category
        
        c <task_id> -> Complete Task
        
        l -> List All Task
        
        l <category_id> -> List Task By Category

        lc -> List all category
        
        e -> Exit
        '''

    running = True
    while running:
        input_cmd = input("> ")
        parts = input_cmd.split()

        # Check if the user entered a command
        if parts:
            command = parts[0].lower()

            # Insert Task
            if command == 'i' and len(parts) >= 3:
                task_name = ' '.join(parts[1:-1])
                category_id = int(parts[-1])
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                todo.add_task(task_name, current_time, category_id)
                print("Task added successfully!")

            # Complete Task
            elif command == 'c' and len(parts) == 2:
                task_id = int(parts[1])
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                todo.complete_task(task_id, current_time)
                print(f"Task {task_id} completed successfully!")

            # List All Tasks
            elif command == 'l' and len(parts) == 1:
                tasks = todo.list_all_tasks()
                print("Task_id | Task Name | isCompleted | Created At | Completed At | Category")
                for task in tasks:
                    print(task)

            # List Tasks By Category
            elif command == 'l' and len(parts) == 2:
                category_id = int(parts[1])
                tasks = todo.list_tasks_by_category(category_id)
                print("Task_id | Task Name | isCompleted | Created At | Completed At | Category")
                for task in tasks:
                    print(task)
            
            # List Categories
            elif command == 'lc':
                categories = todo.list_categories()
                print("Category_id | Category Name")
                for category in categories:
                    print(category)

            # Insert Category
            elif command == 'ic' and len(parts) >= 2:
                category_name = ' '.join(parts[1:])
                todo.add_category(category_name)
                print(f"Category '{category_name}' added successfully!")

            # Exit
            elif command == 'e':
                print("Exiting KB-TODO. Goodbye!")
                running = False

            # Help
            elif command == 'help' or command == 'h':
                print(help_txt)

            else:
                print("Invalid command. Type 'help' for instructions.")
        else:
            print("Invalid command. Type 'help' for instructions.")

    todo.close_connection()
