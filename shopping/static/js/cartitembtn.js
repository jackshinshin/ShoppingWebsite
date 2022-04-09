window.onload = function(){
	for(let btn of document.querySelectorAll(".increment-btn, .decrement-btn"))
    btn.onclick = plus_minus_button;
  for(let view of document.querySelectorAll(".count"))
    view.oninput = input_box;
  
}

function plus_minus_button(){
  let calculationBase = this.value == "+" ? 1 : -1;
  let parent = this.parentElement;
  let grandparent = parent.parentElement;
  let count = grandparent.querySelector(".count");
  let result = ( parseInt( count.value ) || 0 ) + calculationBase;
  if( result >= 0 )
    grandparent.dataset.number = result;
  count.value = grandparent.dataset.number
  update2Database( grandparent.dataset.uid, grandparent.dataset.number );
  updateGlobalPrice( );
}

function input_box(){
  let parent = this.parentElement;
  let grandparent = parent.parentElement;
  let result = ( parseInt( this.value ) || 0 );
  if( result >= 0 )
    grandparent.dataset.number = result;
  this.value = grandparent.dataset.number
  update2Database( grandparent.dataset.uid, grandparent.dataset.number );
  updateGlobalPrice( );
}

async function update2Database( uid, count ){
  // let target_url = document.getElementById('add_item_url').textContent;
  let response = await fetch(`add_cart/${uid}/${count}`).then( res => res.json() );
  console.log( response );
}

function updateGlobalPrice(){
  let global_price = 0;
  let last_section = document.querySelector('.total')
  let tax_rate = 0.05;
  for(let el of document.querySelectorAll(".block")){
    global_price += el.dataset.number * el.dataset.price;
  }
  let money_symbol = "$"
  let tax = Math.round(global_price*tax_rate);
  last_section.querySelector("#global_price").innerText = money_symbol.concat(global_price);
  last_section.querySelector("#tax").innerText = money_symbol.concat(tax);
  global_price += tax;
  last_section.querySelector("#global_price_taxed").innerText = money_symbol.concat(global_price);
  
}