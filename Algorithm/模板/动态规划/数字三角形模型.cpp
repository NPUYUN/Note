int a[N][N];
int f[N][N];

int main(){
	int n;
	cin >> n;
	
	for(int i = 1 ; i <= n ; i ++){
		for(int j = 0 ; j <= i + 1 ; j ++){
			f[i][j] = -0x3f3f3f3f;
		}
	}
	
	for(int i = 1 ; i <= n ; i ++){
		for(int j = 1 ; j <= i ; j ++){
			cin >> a[i][j];
			f[i][j] = max(f[i - 1][j] , f[i - 1][j - 1]) + a[i][j];
		}
	}
	
	int res = -0x3f3f3f3f;
	for(int i = 1 ; i <= n ; i ++){
		res = max(res , f[n][i]);
	}
	
	cout << res;
}
