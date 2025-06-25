class Database:
    def __init__(self):
        self.data = {}
        self.transactions = []

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key, "NULL")

    def unset(self, key):
        if key in self.data:
            del self.data[key]

    def count(self, value):
        return list(self.data.values()).count(value)

    def find(self, value):
        found_keys = [key for key, val in self.data.items() if val == value]
        return found_keys

    def begin(self):
        self.transactions.append(self.data.copy())

    def rollback(self):
        if self.transactions:
            self.data = self.transactions.pop()

    def commit(self):
        if self.transactions:
            self.transactions = []

def main():
    db = Database()
    commands = {
        "SET": lambda key, value: db.set(key, value),
        "GET": lambda key: db.get(key),
        "UNSET": lambda key: db.unset(key),
        "COUNTS": lambda value: db.count(value),
        "FIND": lambda value: db.find(value),
        "BEGIN": lambda: db.begin(),
        "ROLLBACK": lambda: db.rollback(),
        "COMMIT": lambda: db.commit(),
        "END": lambda: exit(),
    }

    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                continue

            parts = user_input.split(" ")
            command = parts[0].upper()
            args = parts[1:]

            if command in commands:
                if len(args) == 0:
                    result = commands[command]()
                elif len(args) == 1:
                    result = commands[command](args[0])
                elif len(args) == 2:
                    result = commands[command](args[0], args[1])
                else:
                    print("Invalid command format")
                    continue

                if result is not None:
                    print(result)
            else:
                print(f"Unknown command > {command}")
                
        except EOFError:
            print("\nExiting...")
            break
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
