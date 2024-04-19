function openModal() {
        document.getElementsByClassName("items_news").addEventListener("click", () => {
                document.getElementById("modalBlock").classList.add("open")
        });
}

function closeModal() {
        document.getElementById("close").addEventListener("click", () => {
                document.getElementById("modalBlock").classList.remove("open")
        });
}