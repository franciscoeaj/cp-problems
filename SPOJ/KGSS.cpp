#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct SegmentTreeNode {
	int max1, max2;

	void assignLeaf(int val) {
		max1 = val;
		max2 = -1;
	}

	void merge(SegmentTreeNode& left, SegmentTreeNode& right) {
		max1 = max(left.max1, right.max1);
		max2 = min(max(left.max1, right.max2), max(right.max1, left.max2));
	}

	int getValue() {
		return max1 + max2;
	}
};

int arr[100001];
SegmentTreeNode st[400004];

void build(int pos, int l, int r) {
	if (l == r) {
		st[pos].assignLeaf(arr[l]);
		return;
	}

	int leftNode = pos * 2, rightNode = pos * 2 + 1, mid = (l + r) / 2;

	build(leftNode, l, mid);
	build(rightNode, mid + 1, r);
	st[pos].merge(st[leftNode], st[rightNode]);
}

void update(int pos, int l, int r, int p, int val) {
	if (l == r) {
		st[pos].assignLeaf(val);
		return;
	}

	int leftNode = pos * 2, rightNode = pos * 2 + 1, mid = (l + r) / 2;

	if (p <= mid) {
		update(leftNode, l, mid, p, val);
	} else {
		update(rightNode, mid + 1, r, p, val);
	}

	st[pos].merge(st[leftNode], st[rightNode]);
}

SegmentTreeNode query(int pos, int l, int r, int x, int y) {
	if (l >= x && r <= y) {
		return st[pos];
	}

	int leftNode = pos * 2, rightNode = pos * 2 + 1, mid = (l + r) / 2;

	if (y <= mid) {
		return query(leftNode, l, mid, x, y);
	} else if (x > mid) {
		return query(rightNode, mid + 1, r, x, y);
	}

	SegmentTreeNode leftRes = query(leftNode, l, mid, x, y);
	SegmentTreeNode rightRes = query(rightNode, mid + 1, r, x, y);
	SegmentTreeNode res;
	res.merge(leftRes, rightRes);
	return res;
}

int main() {
	int n, q, x, y;
	char op;

	cin >> n;

	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}

	build(1, 1, n);

	cin >> q;

	for (int i = 0; i < q; i++) {
		cin >> op >> x >> y;

		if (op == 'Q') {
			cout << query(1, 1, n, x, y).getValue() << endl;
		} else if (op == 'U') {
			update(1, 1, n, x, y);
		}
	}

	return 0;
}
