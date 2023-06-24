console.log('VADIK LOG');

document.querySelector('#sushi11').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#rolu_opuckania').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#pizza11').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#pizza_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#salate11').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#salate_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#hot11').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#hotter_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#basis11').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#ocnove_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#soup11').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#supu_id').scrollIntoView({behavior:"smooth"});
})
document.querySelector('#snacks11').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#zakysku_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#garnish11').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#garniru_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#nopoi11').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#xolod_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#puvo11').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#puvo_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#sushi111').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#rolu_opuckania').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#pizza111').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#pizza_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#salate111').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#salate_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#hot111').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#hotter_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#basis111').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#ocnove_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#soup111').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#supu_id').scrollIntoView({behavior:"smooth"});
})
document.querySelector('#snacks111').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#zakysku_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#garnish111').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#garniru_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#nopoi111').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#xolod_id').scrollIntoView({behavior:"smooth"});
})

document.querySelector('#puvo111').addEventListener('click', function (){
    console.log('as')
    document.querySelector('#puvo_id').scrollIntoView({behavior:"smooth"});
})

document.getElementById('searchButton').addEventListener('click', performSearch);
    document.getElementById('searchInput').addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            performSearch();
        }
    });

    function performSearch() {
        var searchValue = document.getElementById('searchInput').value.toLowerCase();
        var products = document.getElementsByClassName('col-md-3');

        for (var i = 0; i < products.length; i++) {
            var productName = products[i].querySelector('.card-title a').textContent.toLowerCase();

            if (productName.includes(searchValue)) {
                products[i].style.display = 'block';
            } else {
                products[i].style.display = 'none';
            }
        }
    }