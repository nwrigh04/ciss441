import sqlite3
DB_FILE = 'payroll_dc_small.db'
conn = sqlite3.connect(DB_FILE)

def main():
    print('a6 - standard report 1')
    strsql = """select 
                    l.loct location, 
                    max(ft.salary) sal_max, 
                    min(ft.salary) sal_min, 
                    count(ft.salary) people_count
                from factdata_mar2016 ft, loc l
                where ft.loc = l.loc
                group by location
                order by sal_max desc
                limit 20;
        """
    cursor = conn.execute(strsql)
    # the formating string for each row of the report
    report_string_format = '{0:<40}\t{1:<10}{2:<10}{3:<10}'
    # printing the header of the report. 
    print(
        report_string_format.format(
            'location', 'sal_max', 'sal_min', 'people_count'
            )
        )

    for row in cursor:  
        location, sal_max, sal_min, people_count = row
        print(
            report_string_format.format(
                location, sal_max, sal_min, people_count
                )
            )

    cursor.close()      # close cursor
    conn.close()       # close connection to the db

if __name__ == "__main__":
    main()
