let arr = ['nawaf', 'Bdor', 'Nothing']

for (let i = 0; i < arr.length; i++) {
    if (arr[i] == 'nawaf') {
        continue;
    };
    document.write(`
    <div class='cont'>
        <p class='test'>name: ${arr[i]}<span class='spn'></span></p>
    </div>
    `);
    if (arr[i] == 'Bdor') {
        document.querySelector('.spn').innerHTML = ' Lba 3yonh'
    };
}