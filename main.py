from binary_tree import Node, create_tree

if __name__ == '__main__':
    l = [2, 7, 3, 1, 6, 3, 9, 13]
    tree = create_tree(l)

    for i in range(len(l)):
        path = tree.path(l[i], "")
        print("Path for " + str(l[i]) + ": " + path)

    path = tree.path(5, "")
    print("Path for " + str(5) + ": " + path)
