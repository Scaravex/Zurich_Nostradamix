new Chart(document.getElementById("radar-chart"), {
    type: 'radar',
    data: {
      labels: ["Extraversion", "Agreeableness", "Conscentiousness", "Openess", "Emotional range"],
      datasets: [
        {
          label: "",
          fill: true,
          backgroundColor: "rgba(155, 202, 88, 1)",
          borderColor: "rgba(155, 202, 88, 1)",
          pointBorderColor: "#fff",
          pointBackgroundColor: "rgba(155, 202, 88, 1)",
          data: [8.77,55.61,21.69,6.62,6.82]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Big Five'
      }
    }
});
