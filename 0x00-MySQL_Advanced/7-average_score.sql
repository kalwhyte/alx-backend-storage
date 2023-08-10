-- SQL script that creates a stored procedure ComputeAverageScoreForUser
--that computes and store the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score INT DEFAULT 0;
    DECLARE projects_count INT DEFAULT 0;

    SELECT SUM(score), COUNT(*) INTO total_score, projects_count
    FROM corrections
    WHERE user_id = user_id;

    IF total_projects > 0 THEN
        SET avg_score = total_score / total_projects;
        UPDATE users SET average_score = avg_score WHERE id = user_id;
    END IF;
END$$
DELIMITER ;
