## 在Linux中使用python
>在Linux系统中编写python代码：

实例1：5人分鱼，第一个人将鱼分为5等份，多出1条，将多出的一条扔了，自己取走一份；第二个人也将鱼分为5等份，多出一条，将其扔了，自己取走一份。。。直到最后一人也是如此，求最开始有多少鱼；
```
#!/usr/bin/python3
def main():
    fish = 1
    while True:
        total = fish
        # 模拟5个人分鱼的过程
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 1


if __name__ == '__main__':
    main()

```
实例2：用自己的代码实现Linux系统下输入月份，年显示对应的日历的功能；
```
#!/usr/bin/python3
"""
万年历
"""
import sys
from datetime import datetime


def is_leap(year):
    """判断闰年"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_month_days(year, month):
    """获得某年某月的天数"""
    month_days = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]
    return month_days[is_leap(year)][month - 1]


def main():
    """主函数"""
    if len(sys.argv) == 3:
        year = int(sys.argv[2])
        month = int(sys.argv[1])
    else:
        now = datetime.now()
        year = now.year
        month = now.month
    y = year if month >= 3 else year - 1
    c = y // 100
    y = y % 100
    m = month if month >= 3 else month + 12
    w = y + y // 4 + c // 4 - 2 * c + 26 * (m + 1) // 10
    w %= 7
    month_names = [
        '', 'January', 'Feburary', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    print(f'{month_names[month]} {year}'.center(20))
    print('Su Mo Tu We Th Fr Sa')
    print(' ' * 3 * w, end='')
    days = get_month_days(year, month)
    for day in range(1, days + 1):
        print(f'{day}'.rjust(2), end=' ')
        w += 1
        if w == 7:
            print()
            w = 0
    print()


if __name__ == '__main__':
    main()

```
实例3：有30个人，其中有15个基督徒，15个非基督徒，从0开始报数，报数为9的人死去，接着从0开始，直到剩余15个人为止，并且15个全部为基督徒；
```
#!/usr/bin/python3
"""
约瑟夫环问题
"""


def main():
    """主函数"""
    persons = [True] * 30
    counter, num, index = 0, 0, 0
    while counter < 15:
        if persons[index]:
            num += 1
            if num == 9:
                persons[index] = False
                counter += 1
                num = 0
        index += 1
        index %= 30
    for person in persons:
        print("基" if person else "非", end="")
    print()


if __name__ == '__main__':
    main()

```
## 简述递归
>实例1：小孩爬楼梯，他可以一步可以跨1阶，2阶，3阶；问小孩爬10阶楼梯，有多少种方式
```
#!/usr/bin/python3

def walk(num, temp={}):
    if num <= 0:
        return 1 if num == 0 else 0
    try:
        return temp[num]
    except KeyError: 
        temp[num] = walk(num - 1) + walk(num - 2) + walk(num - 3)
        return temp[num]


def walk2(num):
    s1, s2, s3 = 1, 2, 4
    for _ in range(num - 1):
        s1, s2, s3 = s2, s3, s1 + s2 + s3
    return s1


def main():
    for num in range(1, 21):
        print(f'{num}: {fib2(num)}')
    print('-' * 50)
    for num in range(1, 11):
        print(f'{num}: {walk2(num)}')


if __name__ == '__main__':
    main()

```
>实例2：汉诺塔问题
```
#!/usr/bin/python3
def move(num, a, b, c):
    if num > 0:
        # 把n-1个盘子从A搬到C
        move(num - 1, a, c, b)
        # 把最大的盘子从A搬到B
        print(f'{a} ---> {b}')
        # 把n-1个盘子从C搬到B
        move(num - 1, c, b, a)


def main():
    num = int(input('盘子个数: '))
    move(num, 'A', 'B', 'C')


if __name__ == '__main__':
    main()

```
## 面向对象编程
>面向对象的程序设计基本上就是三步走:
1. 定义类
    - 数据抽象: 属性(名词)
    - 行为抽象: 方法(动词)
2. 创建对象
3. 给对象发消息
实例：程序员工资为200元/小时，总经理工资为15000元/月，销售员工资为底薪1800，提成为5%;计算员工工资；
```
#!/usr/bin/python3
from abc import ABCMeta, abstractmethod

# 面向对象的程序设计基本上就是三步走:
# 1. 定义类
#     - 数据抽象: 属性(名词)
#     - 行为抽象: 方法(动词)
# 2. 创建对象
# 3. 给对象发消息
class Employee(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):
    
    @property
    def salary(self):
        return 15000


class Programmer(Employee):

    def __init__(self, name):
        self.name = name
        self.working_hour = 0

    @property
    def salary(self):
        return 200 * self.working_hour


class Salesman(Employee):

    def __init__(self, name):
        self.name = name
        self.sales = 0

    @property
    def salary(self):
        return 1800 + self.sales * 0.05


def main():
    emps = [
        Manager("刘备"), Manager("曹操"),
        Programmer("诸葛亮"), Programmer("荀彧"),
        Salesman("貂蝉")
    ]
    for emp in emps:
        # isinstance函数可以进行运行时类型识别
        if isinstance(emp, Programmer):
            emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
        elif isinstance(emp, Salesman):
            emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
        print('%s: %.2f元' % (emp.name, emp.salary))


if __name__ == '__main__':
    main()

```
## python中的函数
>终极原则: 高内聚 低耦合(high cohesion low coupling)
- 在Python中函数是一等公民
- 函数可以赋值给变量，可以作为函数的参数和返回值
- 装饰器函数: 
- 用一个函数装饰另一个函数 给它增加额外的功能
- 装饰器函数的参数是被装饰的函数 返回的是附带装饰功能的函数
- 当调用被装饰的函数时 其实执行的是装饰器中返回的那个带装饰功能的函数
- 执行函数时如果需要装饰功能 加上装饰器就行不需要再书写重复的代码
- 给函数添加装饰器的语法就是在函数前面写上@装饰器函数名
```
#!/usr/bin/python3

import time


def calc(items, fn):
    result = items[0]
    for index in range(1, len(items)):
        result = fn(result, items[index])
    return result

def record(fn):

    def wrapper(*args, **kwargs):
        start = time.time()
        ret_value = fn(*args, **kwargs)
        end = time.time()
        print(f'{end - start}秒')
        return ret_value

    return wrapper

@record
def fac(num):
    result = 1
    for n in range(1, num + 1):
         result *= n
    return result

# 装饰器的本质是执行了下面的代码
# foo1 = record(foo1)
@record
def foo1(a, b, c=20):
    return a + b + c

# 可变参数: 不知道参数个数可以通过*args对参数进行打包
# keyword-arguments ---> kwargs
# 关键字参数: 如果函数接收带参数名和参数值的参数
def foo2(*args, **kwargs):
    result = 0
    for val in args:
        result += val
    return result


# *前面的参数是位置参数在传参时可以不用指定参数名直接对位置
# *后面的参数是命名关键字参数在传参时必须指定参数名否则报错
def foo3(a, *, b, c):
    return a + b + c


if __name__ == '__main__':
    for num in range(1, 101):
        print(fac(num))
    items = [1, 2, 3, 4, 5]
    start, *_, end = items
    print(start, end)
    print(foo1.__name__)
    print(foo1(1, 2)) # 使用参数的默认值
    print(foo1(1, 2, 3)) # 位置参数
    print(foo1(c=100, a=50, b=30)) # 关键字参数
```
>补充一些Linux操作命令：

- chown root salary.py 改变所有者；
- EOF ctrl + D：输入结束符
- write hellokitty: 和其他用户发信息；
- mesg n ：不想接受消息；
- mesg y ：又想接受消息了；
- wall：write all ：发所有用户；
- 生成式：浪费空间节省时间
- 生成器：浪费时间节省空间
- **kwargs:关键字参数；在传参的时候既给了参数名又给了参数值，是个字典
- *args:可变参数；是个元祖；
- def foo(a, *, b, c):
- *之前的是位置参数，在传参是可以不用指定参数名直接对位置，
- *号之后的是命名关键字参数,在传参是必须指定参数名否则报错；
- print(foo.__name__):打印函数的名字；
- 声明抽象类 使用abc库；不能声明对象
- from abc import ABCMeta, abstractmethod
- class Employee(metclass=ABCMeta):
- 在方法的头上加上装饰器，继承时必须重写该方法；
- @abstractmethod
- @property
把方法改造成一个属性；
- isinstance 函数可以进行运行时类型识别；
```if isinstance(emps,Programmer)```