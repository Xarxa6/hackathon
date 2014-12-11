drop table analyses;
create table analyses (analysis_id int, tags varchar(300), analysis_type varchar(30),payload text,url text);
load data infile '/home/mike/OpenTok/analysis/Xarxa6/Xarxa6.csv' into table analyses fields terminated by ',';
drop table Xarxa6Analyses;
create table Xarxa6Analyses (analysis_id integer PRIMARY KEY AUTO_INCREMENT, tags varchar(300) , payload text);
insert ignore into Xarxa6Analyses select analysis_id,replace(lower(tags),';',',') as tags, concat('{"',analysis_type,"','",replace(url,';',','),'}') as payload from analyses;
select * from Xarxa6Analyses where tags like '%Connection%';
show create table Xarxa6Analyses;
insert ignore into Xarxa6Analyses (tags,payload) select distinct concat('{"',lower(partnername),'","',contact_email,'","minutes"}') as tags, concat('{"viz","',"http://viz.tokbox.com/partners/email/",contact_email,'#minutes"}') payload from partnerproduction inner join hadoop.PartnerStreamedMinutes using(partner_id) where sum_minutes > 0 and partnergroup = 'Application';
insert ignore into Xarxa6Analyses (tags,payload) select distinct concat('{"',lower(partnername),'","',contact_email,'","connectivity"}') as tags, concat('{"viz","',"http://viz.tokbox.com/partners/email/",contact_email,'#connectivity"}') payload from partnerproduction inner join hadoop.PartnerStreamedMinutes using(partner_id) where sum_minutes > 0 and partnergroup = 'Application';
insert ignore into Xarxa6Analyses (tags,payload) select distinct concat('{"',lower(partnername),'","',contact_email,'","topology"}') as tags, concat('{"viz","',"http://viz.tokbox.com/partners/email/",contact_email,'#topology"}') payload from partnerproduction inner join hadoop.PartnerStreamedMinutes using(partner_id) where sum_minutes > 0 and partnergroup = 'Application';
insert ignore into Xarxa6Analyses (tags,payload) select distinct concat('{"',lower(partnername),'","',contact_email,'","archiving"}') as tags, concat('{"viz","',"http://viz.tokbox.com/partners/email/",contact_email,'#archiving"}') payload from partnerproduction inner join analytics.archive_storage using(partner_id) where size > 0 and partnergroup = 'Application';
select * from Xarxa6Analyses where tags like '%roll20%' and tags like '%topology%' limit 10;

select * from Xarxa6Analyses order by analysis_id  and tags like lower('%WSCFailures%') and tags like lower('Top25') desc limit 10;

