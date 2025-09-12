// head存储链表头，e[]存储节点的值，ne[]存储节点的next指针，idx表示当前用到了哪个节点
int head, e[N], ne[N], idx;

// 初始化
void init()
{
    head = -1;
    idx = 0;
}

// 在链表头插入一个数a
void insert(int a)
{
    e[idx] = a, ne[idx] = head, head = idx ++ ;
}

//在任意k位置后插入一个数a
void insert(int k , int a){
	e[idx] = a , ne[idx] = ne[k] , ne[k] = idx ++;
}

// 将头结点删除，需要保证头结点存在
void remove()
{
    head = ne[head];
}

//删除任意k位置的下一个位置
void remove(int k){
	ne[k] = ne[ne[k]];
} 
