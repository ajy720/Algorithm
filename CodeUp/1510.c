//1510 : 홀수 마방진

#include <stdio.h>

main(){
	int i, j, n, r, c, board[49][49]={0};
	
	scanf("%d", &n);
	
	r=0;
	c=n/2;
	
	for(i=1;i<=n*n;i++){
		board[r--][c++] = i;
		if(i%n==0){
			r+=2;
			c--;
			continue;
		}
		if(r<0) r=n-1;
		if(c>n-1) c = 0;
		
	}
	
	for(i=0;i<n;i++){
		for(j=0;j<n;j++) printf("%d ", board[i][j]);
		putchar('\n');
	}
	
} 