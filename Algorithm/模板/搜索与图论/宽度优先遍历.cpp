queue<int> q;
st[1] = true; // ��ʾ1�ŵ��Ѿ���������
q.push(1);

while (q.size())
{
    int t = q.front();
    q.pop();

    for (int i = h[t]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!st[j])
        {
            st[j] = true; // ��ʾ��j�Ѿ���������
            q.push(j);
        }
    }
}

