window.onload = function(){
	for(let btn of document.querySelectorAll(".increment-btn, .decrement-btn"))
    btn.onclick = plus_minus_button;
  for(let view of document.querySelectorAll(".count"))
    view.oninput = input_box;
  
}

function plus_minus_button(){
  let calculationBase = this.value == "+" ? 1 : -1;  
  let block = this.closest('.block');
  let count = block.querySelector(".count");
  let result = ( parseInt( count.value ) || 0 ) + calculationBase;
  if( result >= 0 )
    block.dataset.number = result;
  count.value = block.dataset.number
  update2Database( block.dataset.uid, block.dataset.number );
  updateGlobalPrice( );
}

function input_box(){
  let block = document.querySelector('.block');
  let result = ( parseInt( this.value ) || 0 );
  if( result >= 0 )
    block.dataset.number = result;
  this.value = block.dataset.number
  update2Database( block.dataset.uid, block.dataset.number );
  updateGlobalPrice( );
}

async function update2Database( uid, count ){
  
  let response = await fetch(`add_cart/${uid}/${count}`).then( res => res.json() );
  console.log( response );
}

function updateGlobalPrice( ){
  let global_price = 0;
  let last_section = document.querySelector('.total')
  let tax_rate = 0.05;
  let money_symbol = "$"
  for(let el of document.querySelectorAll(".block")){
    let local_price = el.dataset.number * el.dataset.price;
    global_price += local_price;
    el.querySelector('.price').innerText = money_symbol.concat(local_price);
  }
  
  let tax = Math.round(global_price*tax_rate);
  
  last_section.querySelector("#global_price").innerText = money_symbol.concat(global_price);
  last_section.querySelector("#tax").innerText = money_symbol.concat(tax);
  global_price += tax;
  last_section.querySelector("#global_price_taxed").innerText = money_symbol.concat(global_price);
  
}