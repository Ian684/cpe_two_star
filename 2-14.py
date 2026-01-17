def traversal(a , b):
        def cal(aim):
                if len(aim) == 0:
                        return ''
                elif len(aim) == 1:
                        return aim
                root_index = 1 << 60
                for i in range(len(aim)):
                        root_index = min(a.index(aim[i]) , root_index)
                root = a[root_index]
                left , right = aim.split(root)
                return cal(left) + cal(right) + root
        return cal(b)
while True:
        try:
                preo , ino = input().split()
                print(traversal(preo , ino))
        except EOFError:
                break