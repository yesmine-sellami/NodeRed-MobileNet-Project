// testIrrigation.test.js
const checkIrrigation = require('./irrigationLogic');

describe('Tests logique irrigation', () => {

    test('Humidité 20% → IRRIGATION_ON', () => {
        expect(checkIrrigation(20)).toBe("IRRIGATION_ON");
    });

    test('Humidité 30% → IRRIGATION_OFF', () => {
        expect(checkIrrigation(30)).toBe("IRRIGATION_OFF");
    });

    test('Humidité 50% → IRRIGATION_OFF', () => {
        expect(checkIrrigation(50)).toBe("IRRIGATION_OFF");
    });

    test('Humidité 0% → IRRIGATION_ON', () => {
        expect(checkIrrigation(0)).toBe("IRRIGATION_ON");
    });

    test('Humidité 100% → IRRIGATION_OFF', () => {
        expect(checkIrrigation(100)).toBe("IRRIGATION_OFF");
    });

});
