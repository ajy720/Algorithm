#include <stdio.h>

int get_dev(int n){
	int i, cnt=0;
	for(i=1;i*i<=n;i++)	if(n%i==0) cnt++;
	i--;
	if(i*i==n) return (cnt-1)*2+1;
	else return cnt*2;
}

int get_dev2(int n){
	int i, cnt[n+1], dev=1;
	for(i=0;i<n;i++) cnt[i]=0;
	for(i=2;n!=1;i++){
		while(n%i==0){
			cnt[i]++;
			n/=i; 
		}
	}i--;
	
	for(;i>=2;i--) dev=dev*(cnt[i]+1);
	
	return dev;
}

main(){
	int a, b, i, total=0;
	
	scanf("%d %d", &a, &b);
	
	for(i=a;i<=b;i++) total+=get_dev2(i);
	
	printf("%d", total);
}
