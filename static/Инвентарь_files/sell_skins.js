function on_sell_button_click() {
    let skins_to_delete = [];
    let skins = document.querySelectorAll(".skin-container")
    let skin_list = document.getElementById("skin-list")
    skins.forEach((element) => {
        let elementChild = element.querySelector(".data-container")
        if (elementChild.classList.contains("chosen_item")) {
            skins_to_delete.push({
                "skin_name": elementChild.dataset.skinName,
                "gun_name": elementChild.dataset.gunName,
                "skin_quality": elementChild.dataset.qualityId,
                "is_souvenir": elementChild.dataset.isSouvenir,
                "is_statTrack": elementChild.dataset.isStattrak,
                "skin_cost": elementChild.dataset.skinCost
            })
            on_skin_click(elementChild, elementChild.dataset.skinCost)
            skin_list.removeChild(element)
        }
    })
    console.log(skins_to_delete)
    fetch(
        '/sell_skins', {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token}',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(skins_to_delete)
        }
    )
    .then((response) => response.json())
    .then((data) => {
        let balance = data['user_balance']

        let balance_container = document.getElementById("balance-container")
        console.log(balance_container)
        balance_container.innerHTML = balance.toString() + '₽'
    })
    .catch()
}