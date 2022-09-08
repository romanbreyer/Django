

    var bildungsgradButton = document.getElementById('bildungsgradButton');
    var inputAbschluss = document.getElementById('abschluss');

    var abitur = document.getElementById('abitur');
    var fachabitur = document.getElementById('fachabitur');
    var ausbildung = document.getElementById('ausbildung');
    var keinabschluss = document.getElementById('keinabschluss');

    abitur.addEventListener('click', () => {
        bildungsgradButton.textContent = 'Allgemeine Hochschulreife';
        inputAbschluss.value = 'abitur';
    });

    fachabitur.addEventListener('click', () => {
        bildungsgradButton.textContent = 'Fachgebundene Hochschulreife';
        inputAbschluss.value = 'fachabitur';
    });

    ausbildung.addEventListener('click', () => {
        bildungsgradButton.textContent = 'Ausbildung';
        inputAbschluss.value = 'ausbildung';
    });

    keinabschluss.addEventListener('click', () => {
        bildungsgradButton.textContent = 'Kein Abschluss';
        inputAbschluss.value = 'keinabschluss';
    });


    var auslandserfahrungButton = document.getElementById('auslandserfahrungButton');
    var inputAuslandserfahrung = document.getElementById('auslandserfahrung');

    var auslandserfahrung_ja = document.getElementById('auslandserfahrung_ja');
    var auslandserfahrung_nein = document.getElementById('auslandserfahrung_nein');

    auslandserfahrung_ja.addEventListener('click', () => {
        auslandserfahrungButton.textContent = 'Ja';
        inputAuslandserfahrung.value = 'ja';
    });

    auslandserfahrung_nein.addEventListener('click', () => {
        auslandserfahrungButton.textContent = 'Nein';
        inputAuslandserfahrung.value = 'nein';
    });
