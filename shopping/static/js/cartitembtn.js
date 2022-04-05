$(document).ready(function () {
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        const max = JSON.parse(document.getElementById('product-maximum').textContent);
        // console.log(max)
        var inc_val = $(this).closest('#btn-section').find('#qty-input').val();
        var val = parseInt(inc_val, 10);
        val = isNaN(val) ? 0 : val;
        if(val < 10)
        {
            val++;
            $(this).closest('#btn-section').find('#qty-input').val(val);
        }
        
    });

    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        const max = JSON.parse(document.getElementById('product-maximum').textContent);
        // console.log(max)
        var dec_val = $(this).closest('#btn-section').find('#qty-input').val();
        var val = parseInt(dec_val, 10);
        val = isNaN(val) ? 0 : val;
        if(val > 1)
        {
            val--;
            $(this).closest('#btn-section').find('#qty-input').val(val);
        }
        
    });
});