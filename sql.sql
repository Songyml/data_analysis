
--SELECT count(id) from ZHZWW_MAN_ZDJ;


--男   类型数量统计
-- SELECT kind AS 类型,count(id) AS 数量
-- from ZHZWW_MAN_ZDJ
-- GROUP BY kind
-- ORDER BY count(id) DESC;

-- SELECT kind AS 类型,count(id) AS 数量
-- from ZHZWW_MAN_ZTJ
-- GROUP BY kind
-- ORDER BY count(id) DESC;

-- SELECT kind AS 类型,count(id) AS 数量
-- from ZHZWW_MAN_YHZDJ
-- GROUP BY kind
-- ORDER BY count(id) DESC;


--女 类型统计
-- SELECT kind AS 类型,count(id) AS 数量
-- from ZHZWW_WOMAN_ZDJ
-- GROUP BY kind
-- ORDER BY count(id) DESC;

-- SELECT kind AS 类型,count(id) AS 数量
-- from ZHZWW_WOMAN_ZTJ
-- GROUP BY kind
-- ORDER BY count(id) DESC;

-- SELECT kind AS 类型,count(id) AS 数量
-- from ZHZWW_WOMAN_YHZDJ
-- GROUP BY kind
-- ORDER BY count(id) DESC;


-- --作者数量  总点击，点击月榜，推荐月榜
-- SELECT author AS 作者,count(author) AS 数量
-- from ZHZWW_WOMAN_DJYB
-- GROUP BY author
-- ORDER BY count(author) DESC;



--SELECT * FROM ZHZWW_MAN_ZTJ;


--删除表
-- DROP TABLE ZHZWW_MAN_ZZS;


-- SELECT kind AS 类型,count(id) AS 数量
-- from ZHZWW_MAN_DJYB
-- GROUP BY kind
-- ORDER BY count(id) DESC;


--字数分类
--  SELECT count(id) AS 数量
--  FROM ZHZWW_WOMAN_ZZS
--  WHERE count
--  BETWEEN '0' AND '300000';
--BETWEEN '300000' AND '500000';
--  BETWEEN '500000' AND '1000000';
--  BETWEEN '1000000' AND '2000000';


--简介词频统计
-- SELECT info FROM ZHZWW_MAN_DJYB;


--联合查询
-- SELECT ZHZWW_MAN_ZDJ.id AS 总点击排名,ZHZWW_MAN_DJYB.id AS 点击月榜排名,ZHZWW_MAN_DJYB.kind as 类型,ZHZWW_MAN_DJYB.name AS 名字,ZHZWW_MAN_DJYB.author AS 作者,ZHZWW_MAN_ZDJ.status AS 状态
-- FROM ZHZWW_MAN_ZDJ
-- INNER JOIN ZHZWW_MAN_DJYB
-- ON ZHZWW_MAN_ZDJ.name = ZHZWW_MAN_DJYB.name;


    SELECT ZHZWW_MAN_ZDJ.id,ZHZWW_WOMAN_DJYB.id,ZHZWW_MAN_DJYB.kind,ZHZWW_MAN_DJYB.name,ZHZWW_MAN_DJYB.author,ZHZWW_MAN_ZDJ.status
    FROM ZHZWW_MAN_ZDJ
    INNER JOIN ZHZWW_MAN_DJYB
    ON ZHZWW_MAN_ZDJ.name = ZHZWW_MAN_DJYB.name;
