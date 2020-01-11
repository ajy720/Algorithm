//2605 : 캔디팡

#include <stdio.h>
#define SIZE 7

int board[SIZE][SIZE]= {0}, depth;
int px[4] = {1,0,-1,0};
int py[4] = {0,1,0,-1};
int count = 0;

void src(int x, int y, int color){
	int i;
	board[x][y] = 0;
	depth += 1;
	for(i=0;i<4;i++){
		if(board[x+px[i]][y+py[i]] == color && (x+px[i]>=0 && x+px[i]<7) && (y+py[i]>=0 && y+py[i]<7)){
			src(x+px[i], y+py[i], color);	
		}
	}
	
	
}

main(){
	int i, j;
	
	for(i=0;i<SIZE;i++) for(j=0;j<SIZE;j++) scanf("%d", &board[i][j]);
	for(i=0;i<SIZE;i++) for(j=0;j<SIZE;j++){
		if(board[i][j]!=0){
			depth = 0;
			src(i,j, board[i][j]);	
			if(depth>=3) count += 1;
		}
	} 
	
	printf("%d", count);
} 
