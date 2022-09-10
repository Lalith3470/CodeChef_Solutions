#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int n,m,k;
	    scanf("%d %d %d",&n,&m,&k);
	    if(n+k <= m) printf("Yes\n");
	    else printf("No\n");
	}
	return 0;
}
