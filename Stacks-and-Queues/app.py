import streamlit as st
from stack import LinkStack

# 设置页面标题
st.title("Linked Stack Visualizer")

# 初始化session state中的栈对象
if 'stack' not in st.session_state:
    st.session_state.stack = LinkStack()

stack = st.session_state.stack

# 侧边栏：输入和操作按钮
with st.sidebar:
    st.header("Stack Operations")
    element = st.text_input("Enter element to push:", key="element_input")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Push", key="push_btn"):
            if element.strip():
                stack.push(element.strip())
                st.success(f"Pushed '{element.strip()}'")
            else:
                st.warning("Please enter a valid element")

    with col2:
        if st.button("Pop", key="pop_btn"):
            try:
                popped = stack.pop()
                st.success(f"Popped '{popped}'")
            except IndexError:
                st.error("Stack is empty! Cannot pop from an empty stack.")

# 主界面：显示栈大小和可视化图
st.header("Stack Visualization")

# 显示栈大小
st.metric("Stack Size", stack.size)

# 生成Graphviz图的函数
def generate_dot(stack):
    dot = "digraph G {\n"
    dot += "    rankdir=LR;\n"  # 从左到右布局
    dot += "    node [shape=record, fontsize=12];\n"
    dot += "    edge [fontsize=10];\n"

    current = stack.top
    node_id = 0
    nodes = []
    edges = []

    if stack.is_empty():
        dot += "    Empty [label=\"Stack is Empty\", shape=box];\n"
    else:
        while current:
            # 创建节点标签，显示data和next指针
            node_label = f"{{data: {current.data} | next}}"
            nodes.append(f"    node{node_id} [label=\"{node_label}\"];")

            if current.next:
                edges.append(f"    node{node_id} -> node{node_id+1} [label=\"next\"];")
            else:
                # 最后一个节点指向NULL
                dot += "    NULL [label=\"NULL\", shape=box, color=red];\n"
                edges.append(f"    node{node_id} -> NULL [label=\"next\"];")

            current = current.next
            node_id += 1

        # 添加所有节点和边
        dot += "\n".join(nodes) + "\n"
        dot += "\n".join(edges) + "\n"

    dot += "}\n"
    return dot

# 显示Graphviz图
st.subheader("Linked List Structure")
graphviz_code = generate_dot(stack)
st.graphviz_chart(graphviz_code)

# 显示当前栈内容（文本形式）
st.subheader("Current Stack Content")
if stack.is_empty():
    st.info("Stack is empty")
else:
    elements = []
    current = stack.top
    while current:
        elements.append(str(current.data))
        current = current.next
    st.code(" -> ".join(elements) + " -> NULL", language="text")