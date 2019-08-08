#include <stdio.h>

main(){
	int i, j, n, k, a;
	scanf("%d %d", &n, &k);
	
	int arr[n+1][n+1];
	for(i=0;i<n;i++) for(j=0;j<n;j++) arr[i][j]=-1;
	a=1;
	i = j = 0;
	while(a<=n*n){
		while(1){
			if(arr[i][j]==-1) arr[i][j++] = a++;
			else break;
			
			if(a>n*n) break;
		}j--; i++;
		while(1){
			if(arr[i][j]==-1) arr[i++][j] = a++;
			else break;
			
			if(a>n*n) break;
		}i--; j--;
		while(1){
			if(arr[i][j]==-1) arr[i][j--] = a++;
			else break;
			
			if(a>n*n) break;
		}j++; i--;
		while(1){
			if(arr[i][j]==-1) arr[i--][j] = a++;
			else break;
			
			if(a>n*n) break;
		}i++; j++;
	}
	
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			if(arr[i][j]==k){
				printf("%d %d", j+1, i+1);
				return 0;
			}
		}
	}
	
}
