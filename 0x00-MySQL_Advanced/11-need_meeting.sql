-- Create view to list all students with score < 80
CREATE OR REPLACE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL -1 MONTH));
