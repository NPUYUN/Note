(1)���ز��鼯��

    int p[N]; //�洢ÿ��������ڽڵ�

    // ����x�����ڽڵ�
    int find(int x)
    {
        if (p[x] != x) p[x] = find(p[x]);
        return p[x];
    }

    // ��ʼ�����ٶ��ڵ�����1~n
    for (int i = 1; i <= n; i ++ ) p[i] = i;

    // �ϲ�a��b���ڵ��������ϣ�
    p[find(a)] = find(b);


(2)ά��size�Ĳ��鼯��

    int p[N], size[N];
    //p[]�洢ÿ��������ڽڵ�, size[]ֻ�����ڽڵ�������壬��ʾ���ڽڵ����ڼ����еĵ������

    // ����x�����ڽڵ�
    int find(int x)
    {
        if (p[x] != x) p[x] = find(p[x]);
        return p[x];
    }

    // ��ʼ�����ٶ��ڵ�����1~n
    for (int i = 1; i <= n; i ++ )
    {
        p[i] = i;
        size[i] = 1;
    }

    // �ϲ�a��b���ڵ��������ϣ�
    size[find(b)] += size[find(a)];
    p[find(a)] = find(b);


(3)ά�������ڽڵ����Ĳ��鼯��

    int p[N], d[N];
    //p[]�洢ÿ��������ڽڵ�, d[x]�洢x��p[x]�ľ���

    // ����x�����ڽڵ�
    int find(int x)
    {
        if (p[x] != x)
        {
            int u = find(p[x]);
            d[x] += d[p[x]];
            p[x] = u;
        }
        return p[x];
    }

    // ��ʼ�����ٶ��ڵ�����1~n
    for (int i = 1; i <= n; i ++ )
    {
        p[i] = i;
        d[i] = 0;
    }

    // �ϲ�a��b���ڵ��������ϣ�
    p[find(a)] = find(b);
    d[find(a)] = distance; // ���ݾ������⣬��ʼ��find(a)��ƫ����
