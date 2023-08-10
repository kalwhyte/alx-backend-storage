--SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers(user_id INT)
BEGIN
    DECLARE project_count INT DEFAULT 0;
    DECLARE total_score INT DEFAULT 0;
    

    SELECT SUM(score)
        INTO total_score
        FROM corrections
        WHERE corrections.user_id = user_id;
    SELECT COUNT(*) 
        INTO project_count
        FROM corrections
        WHERE corrections.user_id = user_id;

    UPDATE users
        SET average_weighted_score = total_score / project_count
        WHERE users.id = user_id;
END$$
DELIMITER ;
        