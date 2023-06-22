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
   function openModal() {
    document.getElementById("myModal").style.display = "block";
    myModal = document.getElementById("myModal")
       myModal.style.zIndex=3;
    polosha = document.getElementById("polosha");
    carusel = document.getElementById("carusel_photo");
    polosha.style.zIndex=2;
    carusel.style.zIndex=0;



  }

  function closeModal() {
    document.getElementById("myModal").style.display = "none";
    polosha = document.getElementById("polosha");
    polosha.style.zIndex=2;
  }
