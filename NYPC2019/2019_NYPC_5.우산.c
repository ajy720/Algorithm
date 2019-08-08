#include <stdio.h>

main(){
	int n, m, start, i;
	scanf("%d %d %d", &n, &m, &start);
	
	int b[m], r[m];
	for(i=0;i<m;i++) scanf("%d %d", &b[i], &r[i]);
	
	int ws[m];
	for(i=0;i<n;i++) ws[i]=0;
	
	if(r[0]==1) ws[b[0]-1]++;
	
	for(i=1;i<m;i++) if(r[i]==1){
		 if(ws[b[i-1]-1]==0) ;
		 else ws[b[i-1]-1]--;
		 ws[b[i]-1]++;
	}
	
	int total=0;
	for(i=0;i<n;i++) total+=ws[i];
	
	printf("%d", total);
}
