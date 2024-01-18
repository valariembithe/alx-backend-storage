-- Task 3 module
SELECT band_name, (IFNULL(split, '2022') - formed) as lifespan
	FROM metal_bands
	WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
	ORDER BY lifespan DESC;
