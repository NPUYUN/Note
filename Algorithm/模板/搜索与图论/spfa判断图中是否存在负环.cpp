int n;      // �ܵ���
int h[N], w[N], e[N], ne[N], idx;       // �ڽӱ�洢���б�
int dist[N], cnt[N];        // dist[x]�洢1�ŵ㵽x����̾��룬cnt[x]�洢1��x�����·�о����ĵ���
bool st[N];     // �洢ÿ�����Ƿ��ڶ�����

// ������ڸ������򷵻�true�����򷵻�false��
bool spfa()
{
    // ����Ҫ��ʼ��dist����
    // ԭ�����ĳ�����·������n���㣨�����Լ�������ô�����Լ�֮��һ����n+1���㣬�ɳ���ԭ��һ������������ͬ�����Դ��ڻ���

    queue<int> q;
    for (int i = 1; i <= n; i ++ )
    {
        q.push(i);
        st[i] = true;
    }

    while (q.size())
    {
        auto t = q.front();
        q.pop();

        st[t] = false;

        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > dist[t] + w[i])
            {
                dist[j] = dist[t] + w[i];
                cnt[j] = cnt[t] + 1;
                if (cnt[j] >= n) return true;       // �����1�ŵ㵽x�����·�а�������n���㣨�������Լ�������˵�����ڻ�
                if (!st[j])
                {
                    q.push(j);
                    st[j] = true;
                }
            }
        }
    }

    return false;
}
