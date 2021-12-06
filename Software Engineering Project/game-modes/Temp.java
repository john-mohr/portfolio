import java.sql.*;

public class Temp
{
    public static void main(String[] args) throws SQLException
    {
        DB_Interface database = new DB_Interface();

        // access database

        /// DB info: ///
        String checkDB = "SELECT * FROM Questions";
        Statement statement;
        statement = database.connect.createStatement();
        ResultSet rs = statement.executeQuery(checkDB);
        for (int i = 1; i <= rs.getMetaData().getColumnCount(); ++i) {
            System.out.println(rs.getMetaData().getColumnName(i) + "\t" + JDBCType.valueOf(rs.getMetaData().getColumnType(i)).getName());
        }

        /// DROP: ///
        // String drop = "DROP TABLE Questions";
        // Statement statement = database.connect.createStatement();
        // statement.execute(drop);

        /// CREATE: ///
        // String create = "CREATE TABLE Questions (" +
        //     "questionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, " +
        //     "questionType VARCHAR(7) NOT NULL, " +
        //     "leftNum INT, " +
        //     "operator CHAR(1), " +
        //     "rightNum INT, " +
        //     "number DOUBLE, " +
        //     "answer DOUBLE, " +
        //     "place VARCHAR(10))";
        // Statement statement = database.connect.createStatement();
        // statement.execute(create);

        /// ADD QUESTIONS: ///
        // database.addAddSubQuestion(5, "+", 15, 20);
        // database.addAddSubQuestion(10, "+", 13, 23);
        // database.addAddSubQuestion(18, "-", 3, 15);
        // database.addAddSubQuestion(7, "-", 4, 3);
        // database.addPlaceQuestion(312, "100", 3);
        // database.addPlaceQuestion(192, "10", 9);
        // database.addPlaceQuestion(21, "1", 1);
        // database.addPlaceQuestion(562, "10", 6);

        database.close();
    }
}
