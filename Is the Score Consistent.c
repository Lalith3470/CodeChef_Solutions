#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int a,b,c,d;
	    scanf("%d %d\n %d %d",&a,&b,&c,&d);
	    if(c >= a && d >= b)
	        printf("POSSIBLE\n");
	    else printf("IMPOSSIBLE\n");
	}
	return 0;
}

