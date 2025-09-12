bool check(int x) {/* ... */} // ���x�Ƿ�����ĳ������

// ����[l, r]�����ֳ�[l, mid]��[mid + 1, r]ʱʹ�ã�
int bsearch_1(int l, int r)
{
    while (l < r)
    {
        int mid = l + r >> 1;
        if (check(mid)) r = mid;    // check()�ж�mid�Ƿ���������
        else l = mid + 1;
    }
    return l;
}
// ����[l, r]�����ֳ�[l, mid - 1]��[mid, r]ʱʹ�ã�
int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1;
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}
