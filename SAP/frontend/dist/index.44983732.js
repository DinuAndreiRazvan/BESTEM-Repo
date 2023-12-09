document.addEventListener("DOMContentLoaded", function() {
    // Sample data
    const salesData = [
        50,
        120,
        80,
        200,
        100,
        150
    ];
    const categoryData = [
        30,
        20,
        25,
        15,
        10
    ];
    // Sales chart
    const salesCtx = document.getElementById("salesChart").getContext("2d");
    new Chart(salesCtx, {
        type: "bar",
        data: {
            labels: [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun"
            ],
            datasets: [
                {
                    label: "Sales",
                    data: salesData,
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    borderColor: "rgba(75, 192, 192, 1)",
                    borderWidth: 1
                }
            ]
        }
    });
    // Category chart
    const categoryCtx = document.getElementById("categoryChart").getContext("2d");
    new Chart(categoryCtx, {
        type: "doughnut",
        data: {
            labels: [
                "Electronics",
                "Clothing",
                "Books",
                "Home",
                "Toys"
            ],
            datasets: [
                {
                    data: categoryData,
                    backgroundColor: [
                        "#FF6384",
                        "#36A2EB",
                        "#FFCE56",
                        "#4CAF50",
                        "#9966FF"
                    ]
                }
            ]
        }
    });
});

//# sourceMappingURL=index.44983732.js.map
