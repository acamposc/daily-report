
def query(hostname, dataset ,days, ga):
    if ga == '360':
            for i in hostname:
                for j in dataset:
                    for k in days:
                        query = f"""
                        SELECT
                        PARSE_DATE('%Y%m%d',
                        date) AS date,
                        COUNT(DISTINCT(fullVisitorId)) AS users
                        FROM
                        `{j}` AS GA,
                        UNNEST(hits) AS hits
                        WHERE
                        hits.page.hostname LIKE '%{i}'
                        AND _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d',DATE_SUB(CURRENT_DATE(), INTERVAL {k} DAY))
                        AND FORMAT_DATE('%Y%m%d',DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
                        GROUP BY
                        1
                        ORDER BY
                        1 ASC

                        """
            return query
    
    elif ga == 'app+web':
        pass
    
    else: 
        print('error: ga argument should be 360 or app+web')