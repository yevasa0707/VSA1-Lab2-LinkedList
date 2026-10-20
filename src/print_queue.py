class PrintJobNode:
    def __init__(self, job_id, student_name, pages):
        self.job_id = job_id
        self.student_name = student_name
        self.pages = pages
        self.next = None


class PrintQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, job_id, student_name, pages):
        node = PrintJobNode(job_id, student_name, pages)
        if self.size == 0:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size = self.size + 1
        return node

    def dequeue(self):
        if self.size == 0:
            return None
        node = self.front
        self.front = node.next
        node.next = None
        if self.front is None:    
            self.rear = None
        self.size = self.size - 1
        return node

    def peek(self):
        return self.front

    def displayQueue(self):
        if self.size == 0:
            print("Boşdur.")
            return
        lines = []
        node = self.front
        while node is not None:
            lines.append(f"  {node.student_name} - {node.pages} pages (Job {node.job_id})")
            node = node.next
        print("Əvəlki")
        print("\n".join(lines))
        print("Geriyə")

    def countJobs(self):
        return self.size


def main():
    q = PrintQueue()
    next_id = 1
    while True:
        print("\n1. İş Əlavə Et\n2. Növbəti İş Çap Et\n3. Növbəti İşə Bax\n4. Növbəti İşləri Göstər\n5. İşlərin Sayı\n6. Çıxış")
        choice = input("Seçim: ").strip()
        if choice == "1":
            name = input("Tələbə adı: ")
            pages = int(input("Səhifə sayı: "))
            q.enqueue(next_id, name, pages)
            next_id += 1
            print("İş əlavə olundu.")
        elif choice == "2":
            job = q.dequeue()
            if job is None:
                print("Boşdur.")
            else:
                print(job.student_name + " Çap olundu.")
        elif choice == "3":
            job = q.peek()
            if job is None:
                print("Boşdur.")
            else:
                print(f"Növbəti: {job.student_name} - {job.pages} pages")
        elif choice == "4":
            q.displayQueue()
        elif choice == "5":
            print("İşlər:", q.countJobs())
        elif choice == "6":
            break
        else:
            print("yoxdur.")


if __name__ == "__main__":
    main()
