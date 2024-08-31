$(document).ready(function () {
    $.ajax({
        url: '/api/update_circuit_limit/',
        method: 'GET',
        success: function(data) {
            $('#circuit_up_below_200').val(data.circuit_up_below_200);
            $('#circuit_down_below_200').val(data.circuit_down_below_200);
            $('#circuit_up_between_200_500').val(data.circuit_up_between_200_500);
            $('#circuit_down_between_200_500').val(data.circuit_down_between_200_500);
            $('#circuit_up_between_500_1000').val(data.circuit_up_between_500_1000);
            $('#circuit_down_between_500_1000').val(data.circuit_down_between_500_1000);
            $('#circuit_up_between_1000_2000').val(data.circuit_up_between_1000_2000);
            $('#circuit_down_between_1000_2000').val(data.circuit_down_between_1000_2000);
            $('#circuit_up_between_2000_5000').val(data.circuit_up_between_2000_5000);
            $('#circuit_down_between_2000_5000').val(data.circuit_down_between_2000_5000);
            $('#circuit_up_above_5000').val(data.circuit_up_above_5000);
            $('#circuit_down_above_5000').val(data.circuit_down_above_5000);
        },
        error: function(xhr, status, error) {
            console.log("Error: " + error);
        }
    });
});

$('#updateCircuitLimitForm').on('click', function(e) {
    e.preventDefault();

    var formData = {
        circuit_up_below_200: $('#circuit_up_below_200').val(),
        circuit_down_below_200: $('#circuit_down_below_200').val(),
        circuit_up_between_200_500: $('#circuit_up_between_200_500').val(),
        circuit_down_between_200_500: $('#circuit_down_between_200_500').val(),
        circuit_up_between_500_1000: $('#circuit_up_between_500_1000').val(),
        circuit_down_between_500_1000: $('#circuit_down_between_500_1000').val(),
        circuit_up_between_1000_2000: $('#circuit_up_between_1000_2000').val(),
        circuit_down_between_1000_2000: $('#circuit_down_between_1000_2000').val(),
        circuit_up_between_2000_5000: $('#circuit_up_between_2000_5000').val(),
        circuit_down_between_2000_5000: $('#circuit_down_between_2000_5000').val(),
        circuit_up_above_5000: $('#circuit_up_above_5000').val(),
        circuit_down_above_5000: $('#circuit_down_above_5000').val(),
    };

    $.ajax({
        url: '/api/update_circuit_limit/',
        method: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function(response) {
            alert('Circuit limits updated successfully!');
        },
        error: function(xhr, status, error) {
            console.log("Error: " + error);
        }
    });
});