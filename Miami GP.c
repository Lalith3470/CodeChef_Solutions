#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int x;
	    float y;
	    scanf("%d %f",&x,&y);
	    float sum = x*107/100;
	    if(sum  >= y)
	        printf("YES\n");
	    else printf("NO\n");
	}
	return 0;
}
