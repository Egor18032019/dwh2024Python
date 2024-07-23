
SELECT 'CREATE ROLE read_user'
WHERE NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'read_user')
ALTER USER read_user WITH PASSWORD 'pass';

SELECT 'CREATE ROLE write_user'
WHERE NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'read_user')
ALTER USER write_user WITH PASSWORD 'pass' VALID UNTIL '2025-12-31';

DROP SEQUENCE IF EXISTS global_seq CASCADE;
CREATE SEQUENCE global_seq START WITH 100000;
DROP TABLE IF EXISTS example;
CREATE TABLE example (active integer, alco integer, ap_hi integer, ap_lo integer, cardio integer, cholesterol integer, gluc integer, height integer, smoke integer, weight float(53), id bigint not null, age varchar(255), gender varchar(255), primary key (id));