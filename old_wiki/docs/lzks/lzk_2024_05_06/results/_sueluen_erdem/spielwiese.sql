SELECT schuelerin.rufname, schuelerin.familienname
FROM schuelerin
JOIN klasse ON klasse.id = schuelerin.klasse_id
WHERE klasse.name = '5a' AND schuelerin.geburtsdatum = (
    SELECT MAX(schuelerin.geburtsdatum)
    FROM schuelerin
    WHERE schuelerin.klasse_id = klasse.id
)
GROUP BY schuelerin.rufname, schuelerin.familienname;
