int primes[N], cnt;     // primes[]�洢��������
bool st[N];         // st[x]�洢x�Ƿ�ɸ��

void get_primes(int n)
{
    for (int i = 2; i <= n; i ++ )
    {
        if (st[i]) continue;
        primes[cnt ++ ] = i;
        for (int j = i + i; j <= n; j += i)
            st[j] = true;
    }
}
