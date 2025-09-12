int a[N] , f[N];

int main(){
	int n;
	cin >> n;
	
	f[0] = -0x3f3f3f3f;
	int len = 0; 
	for(int i = 0 ; i < n ; i ++){
		cin >> a[i];
		int l = 0 , r = len;
		while(l < r){
			int mid = l + r + 1 >> 1;
			if(f[mid] < a[i]) l = mid;
			else r = mid - 1;
		}
		len = max(len , r + 1);
		f[r + 1] = a[i];
	}
	
	cout << len;
}
