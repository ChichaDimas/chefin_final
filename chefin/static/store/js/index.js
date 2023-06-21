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

$(document).ready(function () {
        $(".card-title.my-title a").each(function () {
            if ($(this).text().length > 21) {
                $(this).addClass("short-name");
            }
        });
    });
 function openModal() {
    document.getElementById("myModal").style.display = "block";
  }

  function closeModal() {
    document.getElementById("myModal").style.display = "none";
  }

function modal(el){
    console.log('modal')
}