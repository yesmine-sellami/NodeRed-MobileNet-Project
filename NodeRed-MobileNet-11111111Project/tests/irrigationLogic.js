// irrigationLogic.js
/**
 * Fonction simulant la logique de Node-RED pour l'irrigation
 * @param {number} humidite - valeur du capteur (0-100)
 * @returns {string} - "IRRIGATION_ON" ou "IRRIGATION_OFF"
 */
function checkIrrigation(humidite) {
    const seuil = 30; // seuil d'humidité
    return humidite < seuil ? "IRRIGATION_ON" : "IRRIGATION_OFF";
}

// Exporter pour les tests
module.exports = checkIrrigation;
