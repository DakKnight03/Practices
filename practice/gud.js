let x = [];
for (i = 0; i < 11; i++) {
    x.push(i);
};
x.forEach(number => {
    number++;
    console.log(`${number}`);
    if (number > 10) {
        console.log('the number', `${number}`, 'is bigger than 10');
    };
});