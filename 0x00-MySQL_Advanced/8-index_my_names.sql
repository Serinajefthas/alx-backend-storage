-- Create index on names and first letter of name of mysql db
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
