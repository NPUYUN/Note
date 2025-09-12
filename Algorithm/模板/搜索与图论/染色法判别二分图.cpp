int n;      // n��ʾ����
int h[N], e[M], ne[M], idx;     // �ڽӱ�洢ͼ
int color[N];       // ��ʾÿ�������ɫ��-1��ʾδȾɫ��0��ʾ��ɫ��1��ʾ��ɫ

// ������u��ʾ��ǰ�ڵ㣬c��ʾ��ǰ�����ɫ
bool dfs(int u, int c)
{
    color[u] = c;
    for (int i = h[u]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (color[j] == -1)
        {
            if (!dfs(j, !c)) return false;
        }
        else if (color[j] == c) return false;
    }

    return true;
}

bool check()
{
    memset(color, -1, sizeof color);
    bool flag = true;
    for (int i = 1; i <= n; i ++ )
        if (color[i] == -1)
            if (!dfs(i, 0))
            {
                flag = false;
                break;
            }
    return flag;
}
