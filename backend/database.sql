create database riftbound;


create table cardInformation(
    id serial Primary Key, 
    cardID varchar (5000),
    cardName varchar(5000),
    cardCost int,
    cardType varchar(2000),
    cardColor varchar (1500),
    cardMigth int,
    cardSubtype varchar(200),
    cardEffectt varchar (5000),
    cardSet varchar(5000),
    cardRarity varchar(2000),
    cardPower varchar(3000)
);