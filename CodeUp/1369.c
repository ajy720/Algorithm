//1369 : 빗금 친 사각형 출력하기

#include <stdio.h>

main(){
	int i, j, r, c, n, k, board[200][200]={0};
	
	scanf("%d %d", &n, &k);
	
	for(i=k-1;i<n*2;i+=k){
		r=0;
		c=i;
		while(r<=n-1&&c>=0) board[r++][c--] = 1;
	}
	
	for(i=0;i<n;i++){
		board[0][i]=1;
		board[n-1][i]=1;
		board[i][0]=1;
		board[i][n-1]=1;
	}
	
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			if(board[i][j]==1) putchar('*');
			else putchar(' ');
		}putchar('\n');
	}
	
} 