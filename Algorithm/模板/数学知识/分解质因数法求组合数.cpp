��������Ҫ������������ʵֵ�����Ƕ�ĳ����������ʱ���ֽ��������ķ�ʽ�ȽϺ��ã�
    1. ɸ�������Χ�ڵ���������
    2. ͨ�� C(a, b) = a! / b! / (a - b)! �����ʽ���ÿ�������ӵĴ����� n! ��p�Ĵ����� n / p + n / p^2 + n / p^3 + ...
    3. �ø߾��ȳ˷����������������

int primes[N], cnt;     // �洢��������
int sum[N];     // �洢ÿ�������Ĵ���
bool st[N];     // �洢ÿ�����Ƿ��ѱ�ɸ��


void get_primes(int n)      // ����ɸ��������
{
    for (int i = 2; i <= n; i ++ )
    {
        if (!st[i]) primes[cnt ++ ] = i;
        for (int j = 0; primes[j] <= n / i; j ++ )
        {
            st[primes[j] * i] = true;
            if (i % primes[j] == 0) break;
        }
    }
}


int get(int n, int p)       // ��n���еĴ���
{
    int res = 0;
    while (n)
    {
        res += n / p;
        n /= p;
    }
    return res;
}


vector<int> mul(vector<int> a, int b)       // �߾��ȳ˵;���ģ��
{
    vector<int> c;
    int t = 0;
    for (int i = 0; i < a.size(); i ++ )
    {
        t += a[i] * b;
        c.push_back(t % 10);
        t /= 10;
    }

    while (t)
    {
        c.push_back(t % 10);
        t /= 10;
    }

    return c;
}

get_primes(a);  // Ԥ����Χ�ڵ���������

for (int i = 0; i < cnt; i ++ )     // ��ÿ���������Ĵ���
{
    int p = primes[i];
    sum[i] = get(a, p) - get(b, p) - get(a - b, p);
}

vector<int> res;
res.push_back(1);

for (int i = 0; i < cnt; i ++ )     // �ø߾��ȳ˷����������������
    for (int j = 0; j < sum[i]; j ++ )
        res = mul(res, primes[i]);
