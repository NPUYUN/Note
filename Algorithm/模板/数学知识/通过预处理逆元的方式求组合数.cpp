����Ԥ��������н׳�ȡģ������fact[N]���Լ����н׳�ȡģ����Ԫinfact[N]
���ȡģ�����������������÷���С��������Ԫ
int qmi(int a, int k, int p)    // ������ģ��
{
    int res = 1;
    while (k)
    {
        if (k & 1) res = (LL)res * a % p;
        a = (LL)a * a % p;
        k >>= 1;
    }
    return res;
}

// Ԥ����׳˵������ͽ׳���Ԫ������
fact[0] = infact[0] = 1;
for (int i = 1; i < N; i ++ )
{
    fact[i] = (LL)fact[i - 1] * i % mod;
    infact[i] = (LL)infact[i - 1] * qmi(i, mod - 2, mod) % mod;
}
