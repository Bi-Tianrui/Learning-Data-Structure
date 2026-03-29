# Learning-Data-Structure

数据结构学习项目 - 同济教材第3章 栈与队列

## 项目结构

```
Stacks-and-Queues/
├── visual.py         # GUI可视化学习工具 (需要桌面环境)
├── stack.py          # 栈的实现 (顺序栈和链栈)
├── circular_queue.py # 队列的实现 (循环队列)
├── main.py           # 测试和应用示例
└── app.py            # Streamlit Web应用 (推荐在GitHub Codespaces中使用)
```

## 功能特性

### 栈 (Stack)
- **顺序栈 (SqStack)**: 基于数组的栈实现
- **链栈 (LinkStack)**: 基于链表的栈实现
- 支持入栈(push)、出栈(pop)、查看栈顶(peek)等操作

### 队列 (Queue)
- **循环队列 (SqQueue)**: 循环数组实现的队列
- 支持入队(enqueue)、出队(dequeue)、查看队头(peek)等操作

### 应用示例
- 数制转换: 十进制转二进制、八进制、十六进制

## 使用方法

### 运行测试
```bash
python main.py
```

### GUI可视化工具
```bash
python visual.py
```
注意: GUI工具需要在桌面环境中运行，具有图形界面的系统。

### Streamlit Web应用 (推荐)
```bash
pip install streamlit
streamlit run app.py
```
在GitHub Codespaces中，可以直接运行此Web应用进行交互式学习。

## 数据结构说明

### 栈的特点
- 后进先出 (LIFO)
- 顺序栈: 连续存储，空间固定
- 链栈: 动态存储，空间灵活

### 队列的特点
- 先进先出 (FIFO)
- 循环队列: 避免假溢出，空间利用率高