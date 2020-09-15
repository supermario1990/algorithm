# 使用DFS递归遍历DAG，有向无环图
# https://www.koderdojo.com/blog/depth-first-search-in-python-recursive-and-non-recursive-programming

def dfs(dag, pos, path = []):
    path.append(pos)
    for item in dag[pos]:
        if item not in path:
            path = dfs(dag, item, path)
    return path

if __name__ == '__main__':
    # DAG
    dag = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [6],
        5: [6],
        6: [7],
        7: []
        }

    print(dfs(dag, 1))