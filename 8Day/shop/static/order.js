$(document).ready(function() {
    getOrderItems()
})

function getOrderItems() {
    $.ajax({
        type: "GET",
        url: "/order",
        data: {},
        success: function(response) {
            if (response["result"] == "success") {
                let ordersItems = response['orders_item'];
                ordersItems.forEach(item => {
                    make_tables(item.orderer, item.quantity, item.address, item.phone);
                })
            }
        }
    })
}

function order() {

    let orderer = $("#order-name");
    let quantity = $("#order-quantity");
    let address = $("#order-address");
    let phone = $("#order_phone");

    if (orderer.val() == "") {
        alert("이름을 입력해주세요")
        orderer.focus()
        return
    } else if (quantity.val() == 0) {
        alert("수량을 입력해주세요")
        quantity.focus()
        return
    } else if (address.val() == "") {
        alert("주소를 입력해주세요")
        address.focus()
        return
    }

    if (phone.val() == "") {
        alert("휴대폰번호를 입력해주세요")
        phone.focus()
        return
    } else if (!isPhoneNumber(phone.val())) {
        alert('휴대폰번호 입력 형식이 틀립니다. \n예)010-0000-0000')
        phone.focus()
        return
    }

    postOrder(orderer.val(), quantity.val(), address.val(), phone.val())
}

function isPhoneNumber(number) {
    let phoneRe = /^[(]{0,1}[0-9]{3}[)]{0,1}[-\s\.]{0,1}[0-9]{3,4}[-\s\.]{0,1}[0-9]{4}$/;
    return phoneRe.test(number);
}

function postOrder(orderer, quantity, address, phone) {
    $.ajax({
        type: 'POST',
        url: '/order',
        data: {
            "orderer": orderer,
            "quantity": quantity,
            "address": address,
            "phone": phone
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert(response['msg']);
                reload();
            }
        }
    });
}

function reload() {
    window.location.reload();
}

function make_tables(orderer, quantity, address, phone) {
    let table_html = '<tr>\
        <td>'+ orderer +'</td>\
        <td>'+ quantity +'</td>\
        <td>'+ address +'</td>\
        <td>'+ phone +'</td>\
    </tr>';

    $('#orders_table').append(table_html)
}