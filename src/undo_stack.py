from datetime import datetime


class ActionNode:
    def __init__(self, action_id, name):
        self.action_id = action_id
        self.name = name
        self.time = datetime.now().strftime("%H:%M:%S")
        self.next = None


class UndoStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def pushAction(self, action_id, name):
        node = ActionNode(action_id, name)
        self.top, node.next = node, self.top   
        self.size = self.size + 1
        return node

    def undoAction(self):
        if self.size == 0:
            return None
        node = self.top
        self.top = node.next
        node.next = None
        self.size = self.size - 1
        return node

    def currentAction(self):
        return self.top

    def displayHistory(self):
        if self.size == 0:
            print("Tarixçə boşdur.")
            return
        lines = []
        node = self.top
        while node is not None:
            lines.append(f"  [{node.action_id}] {node.name} ({node.time})")
            node = node.next
        print("Tam Tarixçə:")
        print("\n".join(lines))

    def countActions(self):
        return self.size


def main():
    st = UndoStack()
    next_id = 1
    while True:
        print("\n1. Əməl yerinə yetir\n2. Ləğv et\n3. Cari Əməl\n4. Tam Tarixçə\n5. Çıxış")
        choice = input("seçim: ").strip()
        if choice == "1":
            name = input("Əməl adı: ")
            st.pushAction(next_id, name)
            next_id += 1
            print("Əməl yerinə yetirildi.")
        elif choice == "2":
            removed = st.undoAction()
            if removed is None:
                print("Ləğv etmək üçün heç bir əməl yoxdur.")
            else:
                print("Ləğv olunur: " + removed.name)
        elif choice == "3":
            act = st.currentAction()
            if act is None:
                print("Cari Əməl yoxdur.")
            else:
                print("Cari Əməl: " + act.name + " (" + act.time + ")")
        elif choice == "4":
            st.displayHistory()
        elif choice == "5":
            break
        else:
            print("yoxdur.")


if __name__ == "__main__":
    main()
