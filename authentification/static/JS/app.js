// Fonction pour récupérer les pays depuis l'API
async function getCountries() {
    try {
        // Appeler l'API pour récupérer la liste des pays
        const response = await fetch('https://restcountries.com/v2/all');
        const data = await response.json();

        // Récupérer la liste déroulante
        var select = document.getElementById("country-select");

        // Boucle sur les données de l'API pour ajouter les options de pays
        for (var i = 0; i < data.length; i++) {
            var option = document.createElement("option");
            option.value = data[i].alpha2Code;
            option.text = data[i].name;
            select.appendChild(option);
        }
    } catch (error) {
        console.log(error);
    }
}
// Appeler la fonction pour récupérer les pays
getCountries();

