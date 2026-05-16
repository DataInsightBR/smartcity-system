// API pública de exemplo para fins didáticos
const API = "https://api-exemplo.com";

// lista de marcadores do mapa
let markers = [];


// =========================================
// CARREGAR PROBLEMAS
// =========================================

async function carregarProblemas() {

  try {

    // requisita dados da API
    const res = await fetch(`${API}/api/problemas`);

    const data = await res.json();

    // remove marcadores antigos
    markers.forEach(marker => {
      map.removeLayer(marker);
    });

    markers = [];

    // adiciona novos marcadores
    data.forEach(problema => {

      const marker = L.marker([
        parseFloat(problema.lat),
        parseFloat(problema.lng)
      ])

      .addTo(map)

      .bindPopup(`
        <b>${problema.tipo}</b><br>
        ${problema.descricao || ""}
      `);

      markers.push(marker);

    });

  } catch (erro) {

    console.error(
      "Erro ao carregar problemas:",
      erro
    );

  }

}

// iniciar carregamento
carregarProblemas();