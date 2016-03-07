#include <stdio.h>
#include <algorithm>
#define INF 2000000000;

using namespace std;

int st[400400], arr[100100];

void build(int pos, int l, int r) {
    if (l == r) {
        st[pos] = arr[l];
        return;
    }

    int m = (l + r) / 2;
    build(pos * 2, l, m);
    build(pos * 2 + 1, m + 1, r);
    st[pos] = min(st[pos * 2], st[pos * 2 + 1]);
}

int query(int pos, int l, int r, int x, int y) {
    if (x > r || y < l) {
        return INF;
    }

    if (x <= l && r <= y) {
        return st[pos];
    }

    int m = (l + r) / 2;
    int p1 = query(pos * 2, l, m, x, y);
    int p2 = query(pos * 2 + 1, m + 1, r, x, y);

    return min(p1, p2);
}

int main() {
    int t, n, q, a, b;

    scanf("%d", &t);

    for (int i = 1; i <= t; i++) {
        scanf("%d %d", &n, &q);

        for (int j = 1; j <= n; j++) {
            scanf("%d", &arr[j]);
        }

        build(1, 1, n);

        printf("Scenario #%d:\n\n", i);
        for (int j = 1; j <= q; j++) {
            scanf("%d %d", &a, &b);
            printf("%d\n", query(1, 1, n, a, b));
        }
    }
}
