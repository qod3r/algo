import pandas as pd
import random
import matplotlib.pyplot as plt


def first(items):
    boxes = [[]]
    
    for item in items:
        flag = False
        for box in boxes:
            if 1 - sum(box) >= item:
                box.append(item)
                flag = True
                break
        if not flag:
            boxes.append([item])
    
    return boxes

def most(items):
    boxes = [[]]
    
    for item in items:
        max_idx = 0
        flag = False
        for i in range(len(boxes)):
            s = sum(boxes[i]) + item
            if s <= 1.0 and s > sum(boxes[max_idx]) + item:
                max_idx = i
                flag = True
        if not flag:
            boxes.append([item])
        else:
            boxes[max_idx].append(item)
    boxes.pop(0)
    return boxes

def next(items):
    boxes = [[]]
    
    curr = 0
    while len(items) > 0:
        if sum(boxes[curr]) + items[0] <= 1.0:
            boxes[curr].append(items.pop(0))
        else:
            boxes.append([])
            curr += 1
            
    return boxes
            
def least(items):
    boxes = [[]]
    
    for item in items:
        min_idx = 0
        flag = False
        for i in range(len(boxes)):
            s = sum(boxes[i]) + item
            if s <= 1.0 and s <= sum(boxes[min_idx]) + item:
                min_idx = i
                flag = True
        if not flag:
            boxes.append([item])
        else:
            boxes[min_idx].append(item)
    return boxes


if __name__ == "__main__":
    # items = [0.5, 0.7, 0.3, 0.9, 0.6, 0.8, 0.1, 0.4, 0.2, 0.5]
    # print(f"{items=}")
    # print("Первый подходящий ящик:   ", first(items.copy()))
    # print("Наиболее подходящий ящик: ", most(items.copy()))
    # print("Следующий подходящий ящик:", next(items.copy()))
    # print("Наименее подходящий ящик: ", least(items.copy()))
    random.seed(123)
    ranges = [50, 100, 200, 500]
    df = pd.DataFrame(columns=['first', 'most', 'next', 'least'])
    fs = [first, most, next, least]
    for r in ranges:
        items = [random.randint(1, 9)/10 for _ in range(r)]
        d = {}
        for f in fs:
            d[f.__name__] = len(f(items.copy()))
        df = pd.concat([df, pd.DataFrame(d, index=[r])], axis=0)
    print(df)
    df.plot(marker='.')
    plt.xlabel("elements")
    plt.ylabel("boxes")
    plt.legend()
    plt.savefig("6.png", dpi=240)
    