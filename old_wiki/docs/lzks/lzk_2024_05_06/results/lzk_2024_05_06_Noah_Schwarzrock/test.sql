-- SELECT COUNT(Lehrkraft.id)
-- FROM Lehrkraft;

-- SELECT COUNT(schuelerin.id)
-- FROM schuelerin JOIN klasse
-- ON klasse.id = schuelerin.klasse_id
-- WHERE klasse.name == '6a';

-- SELECT DISTINCT COUNT(pruefung.id)
-- FROM pruefung
-- WHERE pruefung.datum
-- BETWEEN '2022-11-03' AND '2022-11-05';

-- SELECT schuelerin.rufname, schuelerin.familienname, klasse.name
-- FROM schuelerin JOIN klasse
-- ON schuelerin.klasse_id = klasse.id
-- WHERE schuelerin.ist_klassensprecher == 1
-- ORDER BY schuelerin.familienname DESC;

-- SELECT AVG(note.wert)
-- From note JOIN pruefung
-- ON note.id = pruefung.id
-- WHERE pruefung.laufende_nr = 1;

-- SELECT schuelerin.rufname, schuelerin.familienname
-- (SELECT MIN(schuelerin.geburtsdatum)
-- FROM schuelerin) AS m
-- FROM schuelerin;

SELECT DISTINCT COUNT(pruefung.id)
FROM pruefung
WHERE pruefung.datum
IN ('2022-11-03', '2022-11-05')
AND pruefung.typ = 'Ex';