-- SQL script that creates a stored procedure ComputeAverageScoreForUser
--that computes and store the average score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    SELECT SUM(score), COUNT(*) INTO total_score, total_projects
    FROM corrections
    WHERE user_id = user_id;

    IF total_projects > 0 THEN
        SET avg_score = total_score / total_projects;
        UPDATE users SET average_score = avg_score WHERE id = user_id;
    END IF;
END$$
DELIMITER ;
