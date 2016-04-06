clear();
clf();
signals = csvread('parsedSignals.csv');
X=signals(:, (1:2));
y=signals(:,3);
for i = 1:size(y,1),
	switch(y(i))
	case 0
		marker='rx';
	case 1
		marker='ro';
	case 2
		marker='bx';
	case 3
		marker='bo';
	case 4
		marker='mo';
	case 5
		marker='mx';
	case 6
		marker='gx';
	case 7
		marker='go';
	case 8
		marker='r+';
	case 9
		marker='b+';
	case 10
		marker='g+';
	case 11
		marker='m+';
	endswitch
axis([0, 10, -90, -30])
plot(X(i,1), X(i,2), marker, 'MarkerSize', 5)
hold on; 
end;
