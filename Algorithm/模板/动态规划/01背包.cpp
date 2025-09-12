int w[N] , v[N];
int f[N];

int n , V;

int main(){
	cin >> n >> V;
	for(int i = 1 ; i <= n ; i ++){
		cin >> v[i] >> w[i];
		for(int j = V ; j >= v[i] ; j --){
			f[j] = max(f[j] , f[j - v[i]] + w[i]);
		}
	}
	
	cout << f[V];
}
