int w[N] , v[N];
int f[N];
int n , m;

int main(){
	cin >> n >> m;
	for(int i = 1 ; i <= n ; i ++){
		cin >> v[i] >> w[i];
		for(int j = v[i] ; j <= m ; j ++){
			f[j] = max(f[j] , f[j - v[i]] + w[i]);
		}
	}
	
	cout << f[m];
}
