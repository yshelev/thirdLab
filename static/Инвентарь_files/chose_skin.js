function on_skin_click(element, amount) {
    amount = Number(amount)
    chosen_skins_cost = document.getElementById("chosen_skins_cost")
    if (!element.classList.contains("chosen_item")) {
        console.log(chosen_skins_cost.innerHTML.split("₽")[0])
        chosen_skins_cost.innerHTML = (Number(chosen_skins_cost.innerHTML.split("₽")[0]) + amount).toString() + `₽<div class="text-nano font-medium text-[#a6adcd]">Выбрано скинов в
                                        инвентаре
                                    </div>`
        element.classList.add("chosen_item")
    } else {
        chosen_skins_cost.innerHTML = (Number(chosen_skins_cost.innerHTML.split("₽")[0]) - amount).toString() + `₽<div class="text-nano font-medium text-[#a6adcd]">Выбрано скинов в
                                        инвентаре
                                    </div>`
        element.classList.remove("chosen_item")
    }
}