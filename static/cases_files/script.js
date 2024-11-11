function generate(name) {
    fetch('/open_case_api/' + name.toString(), {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
})
.then(response => response.json())
.then(function (data) {
    if (!data["can_open"]) {
        return //TODO do some things here
    }
    const rouletteContainer = document.getElementById('roulette-container')
    const rotateButton = document.getElementById('rotate-button')
    const balanceContainer = document.querySelector(".balance-container")
    const items = rouletteContainer.children

    let isRotating = false
    let animationDuration = 5000
    let animationSpeed = 0.5
    let container = data["container"]
    let win_skin = data["win_skin"]

    console.log(win_skin)

    rouletteContainer.innerHTML = ""

    container[74] = win_skin
    container.forEach(
        function (skin) {
            rouletteContainer.innerHTML +=
                `
    <div class="px-px [&amp;:not(.active)]:opacity-20 [.roulette-initial-state_&amp;]:opacity-100 shrink-0 transition-opacity h-full"
         data-index="${skin["rarity"]["index"]}" style="width: 142px;">
        <div class="drop text-center h-full aspect-auto w-25 md:w-35 bg-[#293252]"
             data-item-color="${skin["rarity"]["index"]}">
            <img src="../../static/${skin["path_to_icon"]}" width="175"
                 height="175" alt=""/>
            <div class="drop__header max-md:top-2 max-md:inset-x-2">
                <div class="drop__quality">${skin["quality"]["name"]}</div>
                <div class="drop__price">${skin["cost"]}₽</div>
            </div>
            <div class="drop__footer max-md:bottom-1.5">
                <div class="text-white">${skin['gun_name']}</div>
                <div>${skin['name']}</div>
            </div>
        </div>
    </div>
    `

        }
    )
    balanceContainer.innerHTML = `
        ${data["new_user_balance"]}₽
    `

    if (isRotating) return
    isRotating = true

    rouletteContainer.style.transitionDuration = '0s'
    rouletteContainer.style.transform = 'translateX(0)'
    setTimeout(() => {
        for (let i = 0; i < 5; i++) {
            const clone = items[i].cloneNode(true)
            rouletteContainer.appendChild(clone)
        }

        rouletteContainer.style.transitionDuration = `${animationDuration * animationSpeed}ms`
        rouletteContainer.style.transitionTimingFunction = 'cubic-bezier(0.4, 0, 0.2, 1)'

        const itemWidth = 10000
        rouletteContainer.style.transform = `translateX(-${itemWidth}px)`
    }, 100)

    setTimeout(() => {
        isRotating = false
        rouletteContainer.style.transitionDuration = '0s'
    }, animationDuration * animationSpeed)
})
.catch(error => {
    console.error('Ошибка:', error);
});
}
