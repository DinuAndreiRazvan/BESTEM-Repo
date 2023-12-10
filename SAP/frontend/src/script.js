document.addEventListener("DOMContentLoaded", function () {
    // Fetch the JSON data from the file
    fetch("table_recommendation.json")
        .then((response) => response.json())
        .then((data) => {
            // Get the table element
            const table = document.querySelector(".restock");

            // Convert the JSON data to an array of objects for sorting
            const dataArray = Object.entries(data).map(
                ([id, recommendation]) => ({ id, recommendation })
            );

            // Sort the array based on recommendation values in ascending order
            dataArray.sort((a, b) => a.recommendation - b.recommendation);

            // Loop through the sorted array and populate the table
            for (const { id, recommendation } of dataArray) {
                const row = table.insertRow();
                const cell = row.insertCell(0);
                cell.textContent = `${id}: ${recommendation}`;
            }
        })
        .catch((error) => console.error("Error fetching JSON:", error));
});
