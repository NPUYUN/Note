int n1, n2;     // n1��ʾ��һ�������еĵ�����n2��ʾ�ڶ��������еĵ���
int h[N], e[M], ne[M], idx;     // �ڽӱ�洢���бߣ��������㷨��ֻ���õ��ӵ�һ������ָ��ڶ������ϵıߣ���������ֻ�ô�һ������ı�
int match[N];       // �洢�ڶ��������е�ÿ���㵱ǰƥ��ĵ�һ�������еĵ����ĸ�
bool st[N];     // ��ʾ�ڶ��������е�ÿ�����Ƿ��Ѿ���������

bool find(int x)
{
    for (int i = h[x]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!st[j])
        {
            st[j] = true;
            if (match[j] == 0 || find(match[j]))
            {
                match[j] = x;
                return true;
            }
        }
    }

    return false;
}

// �����ƥ����������ö�ٵ�һ�������е�ÿ�����ܷ�ƥ��ڶ��������еĵ�
int res = 0;
for (int i = 1; i <= n1; i ++ )
{
    memset(st, false, sizeof st);
    if (find(i)) res ++ ;
}
