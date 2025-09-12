int f[N];
int n , m;

int main(){
	cin >> n >> m;
	for(int i = 0 ; i < n ; i ++){
		int v , w , s;
		cin >> v >> w >> s;
		for(int k = 1 ; k <= s ; k *= 2){
			for(int j = m ; j >= k * v ; j --){
				f[j] = max(f[j] , f[j - k * v] + k * w);
			}
			s -= k;
		}
		if(s){
			for(int j = m ; j >= s * v ; j --){
				f[j] = max(f[j] , f[j - s * v] + s * w);
			}
		}
	}
	
	cout << f[m];
}
