def minimum_effort(n, k, boxes):
    k -= 1

    max_box = max(boxes)
    sorted_boxes = sorted(boxes)

    sorted_boxes.remove(max_box)
    sorted_boxes.insert(k, max_box)

    min_box = min(boxes)

    effort = 0

    pos = {value: i for i, value in enumerate(boxes)}

    for i in range(n):
        while boxes[i] != sorted_boxes[i]:
            
            correct_box = sorted_boxes[i]

            # Index of the correct box
            j = pos[correct_box]

            if boxes[i] != min_box and correct_box != min_box:
                m = pos[min_box]
                effort += boxes[i] * min_box
                pos[boxes[i]] = m
                boxes[m] = boxes[i]
                boxes[i] = min_box
                pos[min_box] = i
            else:
                effort += boxes[i] * boxes[j]
                pos[boxes[i]] = j
                pos[boxes[j]] = i
                boxes[i], boxes[j] = boxes[j], boxes[i]

    return effort

n, k = map(int, input("Enter N and K: ").split())
boxes = list(map(int, input("Enter weights: ").split()))

print(minimum_effort(n, k, boxes))