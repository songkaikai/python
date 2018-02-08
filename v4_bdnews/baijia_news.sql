CREATE TABLE `baijia_news` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(255) NOT NULL COMMENT '文章标题',
	`content` LONGTEXT NOT NULL COMMENT '文章内容',
	`pic_array` TEXT NOT NULL COMMENT '图片路径',
	`create_time` VARCHAR(50) NOT NULL COMMENT '创建时间',
	`add_time` VARCHAR(50) NOT NULL COMMENT '添加时间',
	`read_count` VARCHAR(255) NOT NULL COMMENT '评论数量',
	PRIMARY KEY (`id`)
)
COMMENT='百度百家新闻词条'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=118
;
