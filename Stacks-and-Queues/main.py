from stack import SqStack

def decimal_to_binary(n):
    """十进制转二进制"""
    if n == 0:
        return "0"

    stack = SqStack()
    while n > 0:
        remainder = n % 2
        stack.push(remainder)
        n = n // 2

    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())

    return binary

def decimal_to_octal(n):
    """十进制转八进制"""
    if n == 0:
        return "0"

    stack = SqStack()
    while n > 0:
        remainder = n % 8
        stack.push(remainder)
        n = n // 8

    octal = ""
    while not stack.is_empty():
        octal += str(stack.pop())

    return octal

def decimal_to_hexadecimal(n):
    """十进制转十六进制"""
    if n == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"
    stack = SqStack()
    while n > 0:
        remainder = n % 16
        stack.push(hex_digits[remainder])
        n = n // 16

    hexadecimal = ""
    while not stack.is_empty():
        hexadecimal += str(stack.pop())

    return hexadecimal

# 测试函数
if __name__ == "__main__":
    test_number = 13

    print(f"十进制 {test_number} 转二进制: {decimal_to_binary(test_number)}")
    print(f"十进制 {test_number} 转八进制: {decimal_to_octal(test_number)}")
    print(f"十进制 {test_number} 转十六进制: {decimal_to_hexadecimal(test_number)}")

    # 测试栈的基本操作
    print("\n--- 栈的基本操作测试 ---")
    stack = SqStack()
    print("初始栈:", stack)

    stack.push('A')
    print("入栈 A:", stack)

    stack.push('B')
    print("入栈 B:", stack)

    print("栈顶元素:", stack.peek())

    popped = stack.pop()
    print(f"出栈: {popped}, 栈状态: {stack}")

    # 测试队列的基本操作
    from circular_queue import SqQueue
    print("\n--- 队列的基本操作测试 ---")
    queue = SqQueue()
    print("初始队列:", queue)

    queue.enqueue(10)
    print("入队 10:", queue)

    queue.enqueue(20)
    print("入队 20:", queue)

    print("队头元素:", queue.peek())

    dequeued = queue.dequeue()
    print(f"出队: {dequeued}, 队列状态: {queue}")