function order() {
    let orderer = $("#order-name");
    let quantity = $("#order-quantity");
    let address = $("#order-address");
    let phone = $("#order_phone");

    if (orderer.val() == "") {
        alert("이름을 입력해주세요")
        orderer.focus()
        return
    }

    if (quantity.val() == 0) {
        alert("수량을 입력해주세요")
        quantity.focus()
        return
    }

    if (address.val() == "") {
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

    alert("주문 완료!")
}

function isPhoneNumber(number) {
    let phoneRe = /^[(]{0,1}[0-9]{3}[)]{0,1}[-\s\.]{0,1}[0-9]{3,4}[-\s\.]{0,1}[0-9]{4}$/;
    return phoneRe.test(number);
}