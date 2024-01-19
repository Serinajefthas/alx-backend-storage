-- Create trigger to reset attribute when email is updated
DELIMITER $$;
CREATE TRIGGER reset_email BEFORE UPDATE ON users FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = NULL;
	END IF;
END;$$
DELIMITER :
