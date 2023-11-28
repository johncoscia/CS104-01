
names = []

for _ in range(10):
    accepted_name = input("Enter name: ")
    names.append(accepted_name)

print("Initial list/queue:", names)

print("Dequeued names:")
for _ in range(len(names)):
    print(names.pop(0))

for _ in range(10):
    accepted_name = input("Enter name: ")
    names.append(accepted_name)

print("Updated list/queue:", names)
