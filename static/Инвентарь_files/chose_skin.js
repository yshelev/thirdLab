function on_skin_click(element, amount) {
    amount = Number(amount)
    let chosen_skins_cost = document.getElementById("chosen_skins_cost")
    let num_of_chosen_skins_container = document.getElementById("nums-of-chosen-skins")
    if (!element.classList.contains("chosen_item")) {
        console.log(num_of_chosen_skins_container.innerHTML.split("<div")[0])
        chosen_skins_cost.innerHTML = (Number(chosen_skins_cost.innerHTML.split("₽")[0]) + amount).toString() + `₽<div class="text-nano font-medium text-[#a6adcd]">Выбрано скинов в
                                        инвентаре
                                    </div>`
        num_of_chosen_skins_container.innerHTML = (Number(num_of_chosen_skins_container.innerHTML.split("<div")[0]) + 1).toString() + `<div class="text-nano font-medium text-[#a6adcd]">Выбрано скинов</div>`
        element.classList.add("chosen_item")
    } else {
        chosen_skins_cost.innerHTML = (Number(chosen_skins_cost.innerHTML.split("₽")[0]) - amount).toString() + `₽<div class="text-nano font-medium text-[#a6adcd]">Выбрано скинов в
                                        инвентаре
                                    </div>`
        num_of_chosen_skins_container.innerHTML = (Number(num_of_chosen_skins_container.innerHTML.split("<div")[0]) - 1).toString() + `<div class="text-nano font-medium text-[#a6adcd]">Выбрано скинов</div>`
        element.classList.remove("chosen_item")
    }
}