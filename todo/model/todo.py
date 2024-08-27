class Todo:
    def __init__(self, code_id: int, title: str, description: str) -> None:
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed = False
        self.tags = []

    def mark_completed(self):
        self.completed = True
    
    def add_tag(self, tag: str):

        if tag not in self.tags:
            self.tags.append(tag)
    
    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self) -> None:
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        todo_id = len(self.todos) + 1
        todo = Todo(todo_id, title, description)
        self.todos[todo_id] = todo
        return todo_id

    def pending_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self) -> dict[str, int]:
        tags_count: dict[str, int] = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tags_count:
                    tags_count[tag] += 1
                else:
                    tags_count[tag] = 1
        return tags_count


        





        