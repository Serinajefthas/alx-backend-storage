-- Create stored procedure that adds new correction for student
DELIMITER $$ ;
CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
)
BEGIN
	DECLARE project_id INT;
	-- create project if not exists
	SELECT name FROM projects WHERE name = project_name;

	IF project_name NOT EXISTS THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;

	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END ; $$
DELIMITER ;
