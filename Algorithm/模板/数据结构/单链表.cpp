// head�洢����ͷ��e[]�洢�ڵ��ֵ��ne[]�洢�ڵ��nextָ�룬idx��ʾ��ǰ�õ����ĸ��ڵ�
int head, e[N], ne[N], idx;

// ��ʼ��
void init()
{
    head = -1;
    idx = 0;
}

// ������ͷ����һ����a
void insert(int a)
{
    e[idx] = a, ne[idx] = head, head = idx ++ ;
}

//������kλ�ú����һ����a
void insert(int k , int a){
	e[idx] = a , ne[idx] = ne[k] , ne[k] = idx ++;
}

// ��ͷ���ɾ������Ҫ��֤ͷ������
void remove()
{
    head = ne[head];
}

//ɾ������kλ�õ���һ��λ��
void remove(int k){
	ne[k] = ne[ne[k]];
} 
