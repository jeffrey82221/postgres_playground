from sql_tool import SQLTool

if __name__ == '__main__':
    sql_tool = SQLTool()
    create_schema_sql = """
    CREATE SCHEMA IF NOT EXISTS fund_price_crawler;
    """
    sql_tool.execute_sql(create_schema_sql)

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS fund_price_crawler.csv_updated (
        isin CHAR(12) NOT NULL,
        currency VARCHAR(10) NOT NULL,
        company VARCHAR NOT NULL,
        etl_dt DATE NOT NULL,
        PRIMARY KEY (isin,currency, company)
    );
    """
    sql_tool.execute_sql(create_table_sql)
    table = sql_tool.select_table('SELECT * FROM fund_price_crawler.csv_updated')
    print(table)