from arrstack import ArrayStack


def main():
    val = 0
    stack_1 = ArrayStack()
    stack_2 = ArrayStack()
    stack_1.push(0)
    while True:
        print("current value: {}".format(val))
        choice = input(
            "Enter a choice:\n1. use an operand\n2. Undo\n3. redo\n4. quit:\nAnswer: "
        )
        if choice == "1":
            num = int(input("Enter a value: "))
            operand = input("Enter an operand: ")
            val = eval("{} {} {}".format(val, operand, num))
            stack_1.push(val)
        elif choice == "2":
            if stack_1.is_empty():
                print("There is nothing in the stack to undo")
            else:
                stack_2.push(val)
                stack_1.pop()
                val = stack_1.pop()

        elif choice == "3":
            if stack_2.is_empty():
                print("There is nothing in the stack to redo")
            else:
                stack_1.push(val)
                val = stack_2.pop()
        elif choice == "4":
            break
        else:
            print("Invalid input")
main()