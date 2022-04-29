//Include modules
const fetch = require('cross-fetch');
const Discord = require('discord.js');

//Defining modules
const { MessageEmbed } = require('discord.js');
const { Client, Intents } = require('discord.js');

//Authentication keys
const auth = require('./auth.json');
const riot = require('./riotauth.json');
const riotAuth = riot.token;

//Dictionary for champion names and ids
const all_champion_id = {
        1: 'Annie',
        2: 'Olaf',
        3: 'Galio',
        4: 'Twisted Fate',
        5: 'Xin Zhao',
        6: 'Urgot',
        7: 'LeBlanc',
        8: 'Vladimir',
        9: 'Fiddlesticks',
        10: 'Kayle',
        11: 'Master Yi',
        12: 'Alistar',
        13: 'Ryze',
        14: 'Sion',
        15: 'Sivir',
        16: 'Soraka',
        17: 'Teemo',
        18: 'Tristana',
        19: 'Warwick',
        20: 'Nunu & Willump',
        21: 'Miss Fortune',
        22: 'Ashe',
        23: 'Tryndamere',
        24: 'Jax',
        25: 'Morgana',
        26: 'Zilean',
        27: 'Singed',
        28: 'Evelynn',
        29: 'Twitch',
        30: 'Karthus',
        31: "Cho'Gath",
        32: 'Amumu',
        33: 'Rammus',
        34: 'Anivia',
        35: 'Shaco',
        36: 'Dr.Mundo',
        37: 'Sona',
        38: 'Kassadin',
        39: 'Irelia',
        40: 'Janna',
        41: 'Gangplank',
        42: 'Corki',
        43: 'Karma',
        44: 'Taric',
        45: 'Veigar',
        48: 'Trundle',
        50: 'Swain',
        51: 'Caitlyn',
        53: 'Blitzcrank',
        54: 'Malphite',
        55: 'Katarina',
        56: 'Nocturne',
        57: 'Maokai',
        58: 'Renekton',
        59: 'JarvanIV',
        60: 'Elise',
        61: 'Orianna',
        62: 'Wukong',
        63: 'Brand',
        64: 'LeeSin',
        67: 'Vayne',
        68: 'Rumble',
        69: 'Cassiopeia',
        72: 'Skarner',
        74: 'Heimerdinger',
        75: 'Nasus',
        76: 'Nidalee',
        77: 'Udyr',
        78: 'Poppy',
        79: 'Gragas',
        80: 'Pantheon',
        81: 'Ezreal',
        82: 'Mordekaiser',
        83: 'Yorick',
        84: 'Akali',
        85: 'Kennen',
        86: 'Garen',
        89: 'Leona',
        90: 'Malzahar',
        91: 'Talon',
        92: 'Riven',
        96: "Kog'Maw",
        98: 'Shen',
        99: 'Lux',
        101: 'Xerath',
        102: 'Shyvana',
        103: 'Ahri',
        104: 'Graves',
        105: 'Fizz',
        106: 'Volibear',
        107: 'Rengar',
        110: 'Varus',
        111: 'Nautilus',
        112: 'Viktor',
        113: 'Sejuani',
        114: 'Fiora',
        115: 'Ziggs',
        117: 'Lulu',
        119: 'Draven',
        120: 'Hecarim',
        121: "Kha'Zix",
        122: 'Darius',
        126: 'Jayce',
        127: 'Lissandra',
        131: 'Diana',
        133: 'Quinn',
        134: 'Syndra',
        136: 'AurelionSol',
        141: 'Kayn',
        142: 'Zoe',
        143: 'Zyra',
        145: "Kai'sa",
        147: "Seraphine",
        150: 'Gnar',
        154: 'Zac',
        157: 'Yasuo',
        161: "Vel'Koz",
        163: 'Taliyah',
        166: "Akshan",
        164: 'Camille',
        201: 'Braum',
        202: 'Jhin',
        203: 'Kindred',
        222: 'Jinx',
        223: 'TahmKench',
        234: 'Viego',
        235: 'Senna',
        236: 'Lucian',
        238: 'Zed',
        240: 'Kled',
        245: 'Ekko',
        246: 'Qiyana',
        254: 'Vi',
        266: 'Aatrox',
        267: 'Nami',
        268: 'Azir',
        350: 'Yuumi',
        360: 'Samira',
        412: 'Thresh',
        420: 'Illaoi',
        421: "Rek'Sai",
        427: 'Ivern',
        429: 'Kalista',
        432: 'Bard',
        497: 'Rakan',
        498: 'Xayah',
        516: 'Ornn',
        517: 'Sylas',
        526: 'Rell',
        518: 'Neeko',
        523: 'Aphelios',
        555: 'Pyke',
        875: "Sett",
        711: "Vex",
        777: "Yone",
        887: "Gwen",
        876: "Lillia",
    }

//Creating client object
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES]});

//Starting bot function
client.once('ready', () => {
  client.user.setPresence({
       game: {
           name: 'with depression',
           type: "STREAMING",
           url: "youtube.com"
       }
   });
console.log('Bot is online');
});

//Authentication
client.login(auth.token);

//Starting the bot eventListener
client.on('message', function (message) {

    //Parsing command from user
    if (message.content.substring(0, 1) == '!') {
        var args = message.content.substring(1).split(' ');
        var cmd = args[0];

        //Basic command logic
        if (cmd == 'account') {

          //Parsing user message for API requests
          var summonerName = message.content.substring(9);
          summonerName = encodeURIComponent(summonerName.trim());

          //Call to command function
          account(summonerName, message);
        }

        if(cmd == "free") {

          //Call to command function
          freeRotation(message);
        }

        if(cmd == 'rank') {

          //Parsing user message for API requests
          var summonerName = message.content.substring(5);
          summonerName = encodeURIComponent(summonerName.trim());

          //Call to command function
          rank(summonerName, message);
        }

        if(cmd == 'tftrank') {

          //Parsing user message for API requests
          var summonerName = message.content.substring(8);
          summonerName = encodeURIComponent(summonerName.trim());

          //Call to command function
          tftrank(summonerName, message);
        }

        if(cmd == 'summary') {

          //Parsing user message for API requests
          var summonerName = message.content.substring(8);
          summonerName = encodeURIComponent(summonerName.trim());

          //Call to command function
          summary(summonerName, message);
        }

        if(cmd == 'tftsummary') {

          //Parsing user message for API requests
          var summonerName = message.content.substring(11);
          summonerName = encodeURIComponent(summonerName.trim());

          //Call to command function
          tftsummary(summonerName, message);
        }

        if(cmd == 'compare') {

          //Parsing user message for API requests
          var summonerNames = message.content.substring(8).split(',');

          //Checking that two summoner names were enter properly
          if(summonerNames === undefined ) {

            //Formatting response
            const embed = new MessageEmbed()
            .setAuthor("League BOT")
            .setColor('#f7a1a1')
            .setTitle('Please enter two valid summoner names, seperated by a single comma.')
            .setDescription('!compare [summoner name 1], [summoner name 2]')
            .setTimestamp()

            //Sending response
            message.reply({embeds: [embed]});
            return
          }
          compare(summonerNames[0], summonerNames[1], message)
        }
          if(cmd == 'match') {

            //Parsing user message for API requests
            var params = message.content.substring(6).split(',');

            //Checking that two parameters were enter properly
            if(params[0] === undefined || params[1] === undefined) {

              //Formatting response
              const embed = new MessageEmbed()
              .setAuthor("League BOT")
              .setColor('#f7a1a1')
              .setTitle('Please enter a valid summoner name and number [1-75], seperated by a single comma.')
              .setDescription('!match [summoner name 1], [1-75]')
              .setTimestamp()

              //Sending response
              message.reply({embeds: [embed]});
              return
            }

          summonerName = encodeURIComponent(params[0].trim());
          number = encodeURIComponent(params[1].trim());
          if(number > 75) {

            //Formatting response
            const embed = new MessageEmbed()
            .setAuthor("League BOT")
            .setColor('#f7a1a1')
            .setTitle('Please enter a valid  number between 1-75.')
            .setDescription('!match [summoner name 1], [1-75]')
            .setTimestamp()

            //Sending response
            message.reply({embeds: [embed]});
            return
          }
          //Call to command function
          match(number, summonerName, message);
        }

          if(cmd == 'help') {

          //Formatting response
          const embed = new MessageEmbed()
          .setAuthor("League BOT")
          .setColor('#f7a1a1')
          .setTitle('Command Information')
          .addField('**!account [summoner name]**:',' Provides details about the given summoner. Only available for accounts on the North American server.\n')
          .addField('**!free:**', 'Provides a list of the free champions available this week.\n')
          .addField('**!rank [summoner name]**:', 'Provides the rank, wins, losses, win/lose ratio, and hot streak status for the given summoner.\n')
          .addField('**!tftrank [summoner name]**:', 'Provides the TFT rank, wins, losses, win/lose ratio, and hot streak status for the given summoner.\n')
          .addField('**!summary [summoner name]**:', 'Provides a summary of the last match played by the summoner, it gives the match type, victory or defeat status, champion played, KDA, KDA ratio, CS, CS per minute, gold per minute, total damage, and the items.\n')
          .addField('**!tftsummary [summoner name]**:', 'Provides a summary of the last tft match played by the summoner, it gives the placement, level, traits, player kills, and player damage.\n')
          .addField('**!match [summoner name], [number of games]**:', 'Provides compiled statistics from the number of games given. This command may take a moment to return a response.\n')
          .addField('**!compare [summoner name 1], [summoner name 2]**:', 'Provides a comparison of two summoners statistics compiled from 20 games. This command may take a moment to return a response.\n')
          .addField('\n**Application Information**', "Currently League BOT is in testing, only North American accounts are supported, and the bot may be off or API keys might expire.\n"
           + '\nMade by John David Mohr. [GitHub](https://github.com/john-mohr/Senior-Project). \n Functionality provided by Riot Games API, Discord.io, and Riot Games Data Dragon.')
          .setTimestamp()

          //Sending response
          message.reply({embeds: [embed]});
        }

        if (cmd != 'help' && cmd != 'tftrank' && cmd != 'rank' && cmd != "free" && cmd != 'account' && cmd != 'summary' && cmd != 'tftsummary' && cmd != 'compare' && cmd != 'match') {

          //Formatting response
          const embed = new MessageEmbed()
          .setAuthor("League BOT")
          .setDescription('Invalid command. Type **[!help]** for a list of commands and other information.')
          .setTimestamp()

          //Sending response
          message.reply({embeds: [embed]});
        }
   }
});

//Summary of the last tft match played, given summonerName and message object, returns placement, level, traits, player damage, player kills.
async function tftsummary(summonerName, message) {
  var summonerIndex = 0;
  var color = '#f7a1a1';
  var winLose = "";

  //Fetching and parsing response
  let data = await fetch('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + riotAuth);
  data = await data.json();
  let matchId = await fetch('https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/' + data.puuid + '/ids?count=1&api_key=' + riotAuth);
  matchId = await matchId.json();
  let matchData = await fetch('https://americas.api.riotgames.com/tft/match/v1/matches/' + matchId[0] + '?api_key=' + riotAuth);
  matchData = await matchData.json();

  //Checking if summoner exist
  if (data.name === undefined) {

    //Formatting response
    const embed = new MessageEmbed()
    .setAuthor("League BOT")
    .setColor('#f7a1a1')
    .setTitle('Summoner not found.')
    .setDescription('Please enter a valid summoner name.')
    .setTimestamp()

    //Sending response
    message.reply({embeds: [embed]});
    return
  }

  //Searching participants to find index of origin summonerName query
  for(i = 0; i < 8; i++) {
    if(matchData.info.participants[i].puuid === data.puuid) {
      summonerIndex = i;
    }
  }

  var traits = '';

  for(i = 0; i < matchData.info.participants[summonerIndex].traits.length; i++) {
    if(matchData.info.participants[summonerIndex].traits[i].tier_current > 0) {
      traits += matchData.info.participants[summonerIndex].traits[i].name.substring(5) + ": Tier " + matchData.info.participants[summonerIndex].traits[i].tier_current + "\n";
    }
  }

  const attachment = new Discord.MessageAttachment('./placement-images/' + matchData.info.participants[summonerIndex].placement + '.png',  matchData.info.participants[summonerIndex].placement + '.png');

  //Formatting response
  const embed = new MessageEmbed()
  .setAuthor("TFT Match")
  .setColor(color)
  .setTitle(data.name + ' (#'+ matchData.info.participants[summonerIndex].placement +')\nLevel '
  + matchData.info.participants[summonerIndex].level + "\n")
  .setDescription("Traits:\n" + traits + "\n" + 'Player Kills: ' + matchData.info.participants[summonerIndex].players_eliminated
  + '\nTotal Player Damage: ' + matchData.info.participants[summonerIndex].total_damage_to_players)
  .setThumbnail('attachment://' + matchData.info.participants[summonerIndex].placement + '.png')
  .setTimestamp()

  //Sending response
  message.reply({embeds: [embed], files: ['./placement-images/' + matchData.info.participants[summonerIndex].placement + '.png']});
}

//Summary of the last match played, given summonerName and message object, returns matchType, win/lose, champion played, KDA, and KDA ratio.
async function summary(summonerName, message) {

  //summary variables
  var summonerIndex = 0;
  var color = '#f7a1a1';
  var winLose = "";

  //Fetching and parsing response
  let itemJson = await fetch('http://ddragon.leagueoflegends.com/cdn/12.5.1/data/en_US/item.json');
  itemJson = await itemJson.json();
  let data = await fetch('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + riotAuth);
  data = await data.json();
  let matchId = await fetch('https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + data.puuid + '/ids?start=0&count=1&api_key=' + riotAuth);
  matchId = await matchId.json();
  let matchData = await fetch('https://americas.api.riotgames.com/lol/match/v5/matches/' + matchId[0] + '?api_key=' + riotAuth);
  matchData = await matchData.json();

  //Checking if summoner exist
  if (data.name === undefined) {

    //Formatting response
    const embed = new MessageEmbed()
    .setAuthor("League BOT")
    .setColor('#f7a1a1')
    .setTitle('Summoner not found.')
    .setDescription('Please enter a valid summoner name.')
    .setTimestamp()

    //Sending response
    message.reply({embeds: [embed]});
    return
  }

  //Searching participants to find index of origin summonerName query
  for(i = 0; i < 10; i++) {
    if(matchData.info.participants[i].summonerName === data.name) {
      summonerIndex = i;
    }
  }

  //Determing win/lose status
  if(matchData.info.participants[summonerIndex].win === true) {
    color = '1b9905';
    winLose = 'Victory';
  }
  else {
    color = '#ff1100';
    winLose = 'Defeat';
  }

  var itemIds = [matchData.info.participants[summonerIndex].item0, matchData.info.participants[summonerIndex].item1,
  matchData.info.participants[summonerIndex].item2, matchData.info.participants[summonerIndex].item3,
  matchData.info.participants[summonerIndex].item4, matchData.info.participants[summonerIndex].item5,
  matchData.info.participants[summonerIndex].item6];

  var itemNames = '';
  for(i = 0; i < 6; i++) {
    if(itemJson.data[itemIds[i]] !== undefined) {
    itemNames += itemJson.data[itemIds[i]].name + ", ";
    }
    if(i == 2) {
      itemNames += "\n";
    }
  }

  itemNames = itemNames.substring(0,itemNames.length-2);

  //Formatting response
  const embed = new MessageEmbed()
  .setAuthor(matchData.info.gameType.replaceAll("_", " "))
  .setColor(color)
  .setTitle(matchData.info.participants[summonerIndex].summonerName + ' ('+ matchData.info.participants[summonerIndex].championName +')\n' + winLose + ' (' + parseInt(matchData.info.gameDuration/60) + 'm ' + parseInt(matchData.info.gameDuration%60) + 's' +')\n')
  .setDescription(matchData.info.participants[summonerIndex].kills + ' / ' + matchData.info.participants[summonerIndex].deaths + ' / ' + matchData.info.participants[summonerIndex].assists
  + "\nKDA: " + (parseFloat(matchData.info.participants[summonerIndex].kills + matchData.info.participants[summonerIndex].assists )/parseFloat(matchData.info.participants[summonerIndex].deaths)).toFixed(2)
  + '\nCS: ' + matchData.info.participants[summonerIndex].totalMinionsKilled + ' (' + parseFloat(matchData.info.participants[summonerIndex].totalMinionsKilled / (matchData.info.gameDuration/60)).toFixed(2) + '/min)'
  + '\nGold/Min: ' + matchData.info.participants[summonerIndex].challenges.goldPerMinute.toFixed(2)
  + '\nTotal Damage: ' + matchData.info.participants[summonerIndex].totalDamageDealtToChampions + ' (' + (matchData.info.participants[summonerIndex].challenges.teamDamagePercentage * 100).toFixed(2) + '% of Team Damge)'
  + "\nItems:\n" + itemNames)
  .setThumbnail('http://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/' + matchData.info.participants[summonerIndex].championName + '.png')
  .setTimestamp()
  //Sending response
  message.reply({embeds: [embed]});
}

//account rank for tft, given summonerName and message object, responds with rank, queueType, wins, losses, W/L ratio, hotStreak
async function tftrank(summonerName, message) {

  var queueIndex = 0;

  //Fetching and parsing response
  let data = await fetch('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + riotAuth);
  data = await data.json();
  let summonerID = String(data.id);
  let leagueData = await fetch('https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/'+ summonerID +'?api_key=' + riotAuth);
  https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/8MM7NDssgEZnQFgUaZQtj1Ywkur1Akt4EeAmslm9PYNOmKA?api_key=RGAPI-7974d2f0-38a8-49a2-b643-27442b3f0652
  leagueData = await leagueData.json();
  //Checking if summoner exist
  if (data.name === undefined) {

    //Formatting response
    const embed = new MessageEmbed()
    .setAuthor("League BOT")
    .setColor('#f7a1a1')
    .setTitle('Summoner not found.')
    .setDescription('Please enter a valid summoner name.')
    .setTimestamp()

    //Sending response
    message.reply({embeds: [embed]});
    return
  }

  //Checking if player is unranked
  if (leagueData[0] === undefined) {

    //Formatting response
    const embed = new MessageEmbed()
    .setAuthor("League BOT")
    .setColor('#f7a1a1')
    .setTitle(data.name)
    .setDescription('Player is unranked')
    .setThumbnail("https://ddragon.leagueoflegends.com/cdn/12.4.1/img/profileicon/" + data.profileIconId +".png")
    .setTimestamp()

    //Sending response
    message.reply({embeds: [embed]});
  }
  else {

    for(i = 0; i < leagueData.length; i++) {
      if(leagueData[i].queueType === "RANKED_TFT") {
        queueIndex = i;
      }
    }

  //Creating new message attachment
  const attachment = new Discord.MessageAttachment('./ranked-emblems/Emblem_' + leagueData[0].tier + '.png', 'Emblem_' + leagueData[0].tier + '.png');

  //Formatting response
  const embed = new MessageEmbed()
  .setAuthor("League BOT")
  .setColor('#f7a1a1')
  .setTitle(String(leagueData[queueIndex].summonerName) + "\nRank: " + String(leagueData[queueIndex].tier) + " " + String(leagueData[queueIndex].rank) + "\n" + String(leagueData[queueIndex].leaguePoints) + " LP")
  .setDescription("Queue type: " + leagueData[queueIndex].queueType.replaceAll("_", " ") + "\nWins: " + leagueData[queueIndex].wins + "\nLosses: "
  + leagueData[queueIndex].losses + "\nW/L Ratio : " + (parseFloat(leagueData[queueIndex].wins)/parseFloat(leagueData[queueIndex].losses)).toFixed(2)
  + "\nHot Streak: " + leagueData[queueIndex].hotStreak)
  .setThumbnail('attachment://Emblem_' + leagueData[queueIndex].tier + '.png')
  .setTimestamp()

  //Sending response
  message.reply({embeds: [embed], files: ['./ranked-emblems/Emblem_' + leagueData[queueIndex].tier + '.png']});
} }

//account rank, given summonerName and message object, responds with rank, queueType, wins, losses, W/L ratio, hotStreak
async function rank(summonerName, message) {

  //Fetching and parsing response
  let data = await fetch('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + riotAuth);
  data = await data.json();
  let summonerID = String(data.id);
  let leagueData = await fetch('https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+ summonerID +'?api_key=' + riotAuth);
  leagueData = await leagueData.json();

  //Checking if summoner exist
  if (data.name === undefined) {

    //Formatting response
    const embed = new MessageEmbed()
    .setAuthor("League BOT")
    .setColor('#f7a1a1')
    .setTitle('Summoner not found.')
    .setDescription('Please enter a valid summoner name.')
    .setTimestamp()

    //Sending response
    message.reply({embeds: [embed]});
    return
  }

  //Checking if player is unranked
  if (leagueData[0] === undefined) {

    //Formatting response
    const embed = new MessageEmbed()
    .setAuthor("League BOT")
    .setColor('#f7a1a1')
    .setTitle(data.name)
    .setDescription('Player is unranked')
    .setThumbnail("https://ddragon.leagueoflegends.com/cdn/12.4.1/img/profileicon/" + data.profileIconId +".png")
    .setTimestamp()

    //Sending response
    message.reply({embeds: [embed]});
  }
  else {

  //Creating new message attachment
  const attachment = new Discord.MessageAttachment('./ranked-emblems/Emblem_' + leagueData[0].tier + '.png', 'Emblem_' + leagueData[0].tier + '.png');

  //Formatting response
  const embed = new MessageEmbed()
  .setAuthor("League BOT")
  .setColor('#f7a1a1')
  .setTitle(leagueData[0].summonerName + "\nRank: " + leagueData[0].tier + " " + leagueData[0].rank)
  .setDescription("Queue type: " + leagueData[0].queueType.replaceAll("_", " ") + "\nWins: " + leagueData[0].wins + "\nLosses: "
  + leagueData[0].losses + "\nW/L Ratio : " + ((parseFloat(leagueData[0].wins)/(parseFloat(leagueData[0].losses) + parseFloat(leagueData[0].wins))).toFixed(2))*100 + "%"
  + "\nHot Streak: " + leagueData[0].hotStreak)
  .setThumbnail('attachment://Emblem_' + leagueData[0].tier + '.png')
  .setTimestamp()

  //Sending response
  message.reply({embeds: [embed], files: ['./ranked-emblems/Emblem_' + leagueData[0].tier + '.png']});
} }

//free rotation, message object, list of free champions
async function freeRotation(message) {

    let list = new Array(15);

    //Fetching and parsing response
    let response = await fetch('https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=' + riotAuth);
    response = await response.json();
    var args = String(response.freeChampionIds).replaceAll(',', ' ').split(' ');

    //Checking query
    if (response === undefined) {

      //Formatting response
      const embed = new MessageEmbed()
      .setAuthor("League BOT")
      .setColor('#f7a1a1')
      .setTitle('Sorry, looks like we ran out of queries. Please wait 1-2 minutes before trying again.')
      .setTimestamp()

      //Sending response
      message.reply({embeds: [embed]});
      return
    }

    //Matching id:key with champion_name:value
    for (let i = 0; i < args.length; i++) {
      list[i] = all_champion_id[args[i]]; }

    //Formatting response
    const embed = new MessageEmbed()
    .setAuthor("League BOT")
    .setColor('#f7a1a1')
    .setTitle("Free Rotation")
    .setDescription(list[0] + "\n" +
    list[1] + "\n" +
    list[2] + "\n" +
    list[3] + "\n" +
    list[4] + "\n" +
    list[5] + "\n" +
    list[6] + "\n" +
    list[7] + "\n" +
    list[8] + "\n" +
    list[9] + "\n" +
    list[10] + "\n" +
    list[11] + "\n" +
    list[12] + "\n" +
    list[13] + "\n" +
    list[14] + "\n" +
    list[15] + "\n")
    .setTimestamp()

    //Sending response
    message.reply({embeds: [embed]});
}

//account summary, given a summonerName responds with summonerName, summonerLevel, lastPLayed, and profileIconId
async function account(summonerName,message) {

  //Fetching and parsing response
  let data = await fetch('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + riotAuth);
  data = await data.json();

  //Checking if summoner exist
  if (data.name === undefined) {

    //Formatting response
    const embed = new MessageEmbed()
    .setAuthor("League BOT")
    .setColor('#f7a1a1')
    .setTitle('Summoner not found.')
    .setDescription('Please enter a valid summoner name.')
    .setTimestamp()

    //Sending response
    message.reply({embeds: [embed]});
    return
  }

  //Creating dateObject to turn epoch into human-readable date
  var dateObject = new Date(data.revisionDate);

  //Formatting response
  const embed = new MessageEmbed()
  .setAuthor("League BOT")
  .setColor('#f7a1a1')
  .setTitle(String(data.name))
  .setDescription("Summoner level: " + data.summonerLevel + "\nLast Played: " + dateObject.toUTCString())
  .setThumbnail("https://ddragon.leagueoflegends.com/cdn/12.4.1/img/profileicon/" + data.profileIconId +".png")
  .setTimestamp()

  //Sending response
  message.reply({embeds: [embed]});
}

//match summary, given a number of games, summoner name, and message object, returns a dictionary with statistics compiled from numGames.
async function matchSummary(numGames, summonerName, message) {

  //variables needed for summary
  var count = 0;
  var summonerIndex = 0;
  var summonerMatchSummary = {
  'summonername' : '',
  'rank' : '',
  'wins' : 0,
  'kills' : 0,
  'assists' : 0,
  'deaths' : 0,
  'goldpermin' : 0,
  'killingsprees' : 0,
  'timespentdead' : 0,
  'visionscore' : 0,
  'cctime' : 0,
  'totaldamageplayers' : 0,
  'totaltimeplayed' : 0,
  'totalMinionsKilled' : 0,
  'damagedealtobjectives' : 0,
  'multikills' : 0,
  'teamDamagePercentage' : 0,
  'validGames': 0
}

  //Fetching and parsing response
  let data = await fetch('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + riotAuth);
  data = await data.json();
  let matchId = await fetch('https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + data.puuid + '/ids?start=0&count=' + numGames + '&api_key=' + riotAuth);
  matchId = await matchId.json();
  let leagueData = await fetch('https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+ String(data.id) +'?api_key=' + riotAuth);
  leagueData = await leagueData.json();

  //Checking if summoner exist
  if (data.name === undefined) {

    //Formatting response
    const embed = new MessageEmbed()
    .setAuthor("League BOT")
    .setColor('#f7a1a1')
    .setTitle('Summoner not found.')
    .setDescription('Please enter a valid summoner name.')
    .setTimestamp()

    //Sending response
    message.reply({embeds: [embed]});
    return
  }

  //Checking if the summoner is ranked
  if (leagueData[0] === undefined) {
    summonerMatchSummary['rank'] = 'UNRANKED';
  } else {
    summonerMatchSummary['rank'] = leagueData[0].tier + " " + leagueData[0].rank;
  }

  summonerMatchSummary['summonername'] = data.name;

  //Looping through all game ids requested
  for(i = 0; i < numGames; i++) {

    //Fetching and parsing match response
    let matchData = await fetch('https://americas.api.riotgames.com/lol/match/v5/matches/' + matchId[i] + '?api_key=' + riotAuth);
    matchData = await matchData.json();

    //Error checking
    if (matchData.info === undefined) {

      //Formatting response
      const embed = new MessageEmbed()
      .setAuthor("League BOT")
      .setColor('#f7a1a1')
      .setTitle('Sorry, looks like we ran out of queries. Please wait 1-2 minutes before trying again.')
      .setTimestamp()

      //Sending response
      message.reply({embeds: [embed]});
      return
    }

    //Searching participants to find index of origin summonerName query
    for(j = 0; j < 10; j++) {
      if(matchData.info.participants[j].summonerName === data.name) {
        summonerIndex = j;
      }
    }

    //Checking if the summoner won this match
    if(matchData.info.participants[summonerIndex].win === true) {
      summonerMatchSummary['wins'] += 1;
    }

    //Making sure we are only pulling statistics from Classic gamemodes and that any invalid games are skipped
    if(matchData.info.gameMode === 'CLASSIC' && matchData.info.participants[summonerIndex].challenges != undefined) {
    count += 1;

    //Compiling the stats from all requested games
    summonerMatchSummary['kills'] += matchData.info.participants[summonerIndex].kills;
    summonerMatchSummary['assists'] += matchData.info.participants[summonerIndex].assists;
    summonerMatchSummary['deaths'] += matchData.info.participants[summonerIndex].deaths;
    summonerMatchSummary['goldpermin'] += matchData.info.participants[summonerIndex].challenges.goldPerMinute;
    summonerMatchSummary['multikills'] += matchData.info.participants[summonerIndex].challenges.multikills;
    summonerMatchSummary['teamDamagePercentage'] += matchData.info.participants[summonerIndex].challenges.teamDamagePercentage;
    summonerMatchSummary['totaldamageplayers'] += matchData.info.participants[summonerIndex].totalDamageDealtToChampions;
    summonerMatchSummary['totaltimeplayed'] += matchData.info.participants[summonerIndex].timePlayed;
    summonerMatchSummary['totalMinionsKilled'] += matchData.info.participants[summonerIndex].totalMinionsKilled;
    summonerMatchSummary['killingsprees'] += matchData.info.participants[summonerIndex].killingSprees;
    summonerMatchSummary['visionscore'] += matchData.info.participants[summonerIndex].visionScore;
    summonerMatchSummary['cctime'] += matchData.info.participants[summonerIndex].totalTimeCCDealt;
    summonerMatchSummary['timespentdead'] += matchData.info.participants[summonerIndex].totalTimeSpentDead;
    summonerMatchSummary['damagedealtobjectives'] += matchData.info.participants[summonerIndex].damageDealtToObjectives;
    }
  }

  //Calculating averages and per/min statistics
  summonerMatchSummary['validGames'] = count;
  summonerMatchSummary['goldpermin'] = summonerMatchSummary['goldpermin'] / count;
  summonerMatchSummary['multikills'] = summonerMatchSummary['multikills'] / count;
  summonerMatchSummary['teamDamagePercentage'] = summonerMatchSummary['teamDamagePercentage'] / count;
  summonerMatchSummary['totaltimeplayed'] = summonerMatchSummary['totaltimeplayed'] / 60;
  summonerMatchSummary['killingsprees'] = summonerMatchSummary['killingsprees'] / count;
  summonerMatchSummary['visionscore'] = summonerMatchSummary['visionscore'] / count;
  summonerMatchSummary['cctime'] = summonerMatchSummary['cctime'] / count;
  summonerMatchSummary['timespentdead'] = summonerMatchSummary['timespentdead'] / count;
  summonerMatchSummary['damagedealtobjectives'] = summonerMatchSummary['damagedealtobjectives'] / count;

  //Returning the dictionary of the given summoners statistics
  return summonerMatchSummary
}

//Compares the compiled stats of two summoners, given two summonernames
async function compare(summonerName1, summonerName2, message) {

  //Calling matchSumamry on each summoner name
  let summonerSummary1 = await matchSummary(20,summonerName1, message);
  if(summonerSummary1 === undefined) {
    return
  }

  let summonerSummary2 = await matchSummary(20,summonerName2, message);
  if(summonerSummary2 === undefined) {
    return
  }
  
  //Simple math to calculate the KDA ratio
  var summonerKDA1 = (parseFloat(summonerSummary1['kills'] + summonerSummary1['assists'] )/parseFloat(summonerSummary1['deaths'])).toFixed(2);
  var summonerKDA2 = (parseFloat(summonerSummary2['kills'] + summonerSummary2['assists'] )/parseFloat(summonerSummary2['deaths'])).toFixed(2);

  var summonerWins1 = 0
  var kdaemoji1 = ""
  var goldemoji1 = ""
  var csemoji1 = ""
  var percentdmgemoji1 = ""
  var avgdmgemoji1 = ""
  var objdmgemoji1 = ""
  var multiemoji1 = ""
  var visionemoji1 = ""
  var ccemoji1 = ""
  var deademoji1 = ""
  var overall1 = ""

  var summonerWins2 = 0
  var kdaemoji2 = ""
  var goldemoji2 = ""
  var csemoji2 = ""
  var percentdmgemoji2 = ""
  var avgdmgemoji2 = ""
  var objdmgemoji2 = ""
  var multiemoji2 = ""
  var visionemoji2 = ""
  var ccemoji2 = ""
  var deademoji2 = ""
  var overall2 = ""

  //Determining what emojis are sent based on who has better stats
  if(summonerKDA1 > summonerKDA2) { kdaemoji1 = ":white_check_mark:"; kdaemoji2 = ":x:"; summonerWins1++; } else { kdaemoji1 = ":x:";  kdaemoji2 = ":white_check_mark:"; summonerWins2++;}
  if(summonerSummary1['goldpermin'] > summonerSummary2['goldpermin']) { goldemoji1 = ":white_check_mark:"; goldemoji2 = ":x:"; summonerWins1++; } else { goldemoji1 = ":x:";  goldemoji2 = ":white_check_mark:"; summonerWins2++;}
  if((summonerSummary1['totalMinionsKilled'] / summonerSummary1['totaltimeplayed']) > (summonerSummary2['totalMinionsKilled'] / summonerSummary2['totaltimeplayed'])) { csemoji1 = ":white_check_mark:"; csemoji2 = ":x:"; summonerWins1++; } else { csemoji1 = ":x:";  csemoji2 = ":white_check_mark:"; summonerWins2++;}
  if(summonerSummary1['teamDamagePercentage'] > summonerSummary2['teamDamagePercentage']) { percentdmgemoji1 = ":white_check_mark:"; percentdmgemoji2 = ":x:"; summonerWins1++; } else { percentdmgemoji1 = ":x:";  percentdmgemoji2 = ":white_check_mark:"; summonerWins2++;}
  if((summonerSummary1['totaldamageplayers'] / summonerSummary1['validGames']) > (summonerSummary2['totaldamageplayers'] / summonerSummary2['validGames'])) { avgdmgemoji1 = ":white_check_mark:"; avgdmgemoji2 = ":x:"; summonerWins1++; } else { avgdmgemoji1 = ":x:";  avgdmgemoji2 = ":white_check_mark:"; summonerWins2++;}
  if(summonerSummary1['damagedealtobjectives'] > summonerSummary2['damagedealtobjectives']) { objdmgemoji1 = ":white_check_mark:"; objdmgemoji2 = ":x:"; summonerWins1++; } else { objdmgemoji1 = ":x:";  objdmgemoji2 = ":white_check_mark:"; summonerWins2++;}
  if(summonerSummary1['multikills'] > summonerSummary2['multikills']) { multiemoji1 = ":white_check_mark:"; multiemoji2 = ":x:"; summonerWins1++; } else { multiemoji1 = ":x:";  multiemoji2 = ":white_check_mark:"; summonerWins2++;}
  if(summonerSummary1['visionscore'] > summonerSummary2['visionscore']) { visionemoji1 = ":white_check_mark:"; visionemoji2 = ":x:"; summonerWins1++; } else { visionemoji1 = ":x:";  visionemoji2 = ":white_check_mark:"; summonerWins2++;}
  if(summonerSummary1['cctime'] > summonerSummary2['cctime']) { ccemoji1 = ":white_check_mark:"; ccemoji2 = ":x:"; summonerWins1++; } else { ccemoji1 = ":x:";  ccemoji2 = ":white_check_mark:"; summonerWins2++;}
  if(summonerSummary1['timespentdead'] < summonerSummary2['timespentdead']) { deademoji1 = ":white_check_mark:"; deademoji2 = ":x:"; summonerWins1++; } else { deademoji1 = ":x:";  deademoji2 = ":white_check_mark:"; summonerWins2++;}

  if(summonerWins1 > summonerWins2) {
    overall1 = ":white_check_mark:"
    overall2 = ":x:"
  } else {
    overall1 = ":x:"
    overall2 = ":white_check_mark:"
  }

  //Formatting response
  const embed = new MessageEmbed()
  .setAuthor('League BOT')
  .setColor('#f7a1a1')
  .setTitle('Comparison of the last 20 games:')

  //Field for summoner 1
  .addField(summonerSummary1['summonername'] + ' (' + summonerSummary1['rank'] + ') ' + overall1 ,
  'KDA: ' + summonerKDA1 + " " + kdaemoji1 +
  '\nGold/Min: ' + (summonerSummary1['goldpermin']).toFixed(2) + " " + goldemoji1 +
  '\nCS/Min: ' + (summonerSummary1['totalMinionsKilled'] / summonerSummary1['totaltimeplayed']).toFixed(2) + " " + csemoji1 +
  '\n% of Team Damage: ' + (100 * summonerSummary1['teamDamagePercentage']).toFixed(2) + '%' + " " + percentdmgemoji1 +
  '\nAvg. Damage: ' + (summonerSummary1['totaldamageplayers'] / summonerSummary1['validGames']).toFixed(2) + " " + avgdmgemoji1 +
  '\nAvg. Objective Damage: ' + summonerSummary1['damagedealtobjectives'].toFixed(2) + " " + objdmgemoji1 +
  '\nAvg. Multikills: ' + (summonerSummary1['multikills']).toFixed(2) + " " + multiemoji1 +
  '\nAvg. Vision Score: ' + (summonerSummary1['visionscore']).toFixed(2) + " " + visionemoji1 +
  '\nAvg. CC Time: ' + summonerSummary1['cctime'].toFixed(2) + ' (sec)' + " " + ccemoji1 +
  '\nAvg. Time Spent Dead: ' + summonerSummary1['timespentdead'].toFixed(2) + ' (sec)' + " " + deademoji1, true)

  //Field for summoner 2
  .addField(summonerSummary2['summonername'] + ' (' + summonerSummary2['rank'] + ') ' + overall2,
  'KDA: ' + summonerKDA2 +  " " + kdaemoji2 +
  '\nGold/Min: ' + (summonerSummary2['goldpermin']).toFixed(2) + " " + goldemoji2 +
  '\nCS/Min: ' + (summonerSummary2['totalMinionsKilled'] / summonerSummary2['totaltimeplayed']).toFixed(2) +  " " + csemoji2 +
  '\n% of Team Damage: ' + (100 * summonerSummary2['teamDamagePercentage']).toFixed(2) + '%' +  " " + percentdmgemoji2 +
  '\n Avg. Damage: ' + (summonerSummary2['totaldamageplayers'] / summonerSummary2['validGames']).toFixed(2) +  " " + avgdmgemoji2 +
  '\nAvg. Objective Damage: ' + summonerSummary2['damagedealtobjectives'].toFixed(2) +  " " + objdmgemoji2 +
  '\nAvg. Multikills: ' + (summonerSummary2['multikills']).toFixed(2) +  " " + multiemoji2 +
  '\nVision Score: ' + (summonerSummary2['visionscore']).toFixed(2) +  " " + visionemoji2 +
  '\nAvg. CC Time: ' + summonerSummary2['cctime'].toFixed(2) + ' (sec)' +  " " + ccemoji2 +
  '\nAvg. Time Spent Dead: ' + summonerSummary2['timespentdead'].toFixed(2) + ' (sec) ' + deademoji2, true)

  .setTimestamp()
  //Sending response
  message.reply({embeds: [embed]});
}

//Compile statistics from the last numGames, given numGames, summonername
async function match(numGames, summonerName, message) {

    //Calling matchSumamry on the summoner name
    let summonerSummary = await matchSummary(numGames, summonerName, message);
    if(summonerSummary === undefined) {
      return
    }

    //Simple math to calculate the KDA ratio
    var summonerKDA = (parseFloat(summonerSummary['kills'] + summonerSummary['assists'] )/parseFloat(summonerSummary['deaths'])).toFixed(2);

    //Fetching and parsing resposne
    let data = await fetch('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + riotAuth);
    data = await data.json();

    var dateObject = new Date(data.revisionDate);

    //Formatting response
    const embed = new MessageEmbed()
    .setAuthor('League BOT')
    .setColor('#f7a1a1')
    .setTitle('Showing results from the last ' + numGames + ' games.')
    .addField(summonerSummary['summonername'] + ' (' + summonerSummary['rank'] + ')\n' + "Summoner level: " + data.summonerLevel + "\nLast Played: " + dateObject.toUTCString(),
    'KDA: ' + summonerKDA +
    '\nGold/Min: ' + (summonerSummary['goldpermin']).toFixed(2) +
    '\nCS/Min: ' + (summonerSummary['totalMinionsKilled'] / summonerSummary['totaltimeplayed']).toFixed(2) +
    '\n% of Team Damage: ' + (100 * summonerSummary['teamDamagePercentage']).toFixed(2) + '%' +
    '\nAvg. Damage: ' + (summonerSummary['totaldamageplayers'] / summonerSummary['validGames']).toFixed(2) +
    '\nAvg. Objective Damage: ' + summonerSummary['damagedealtobjectives'].toFixed(2) +
    '\nAvg. Multikills: ' + (summonerSummary['multikills']).toFixed(2) +
    '\nAvg. Vision Score: ' + (summonerSummary['visionscore']).toFixed(2) +
    '\nAvg. CC Time: ' + summonerSummary['cctime'].toFixed(2) + ' (sec)' +
    '\nAvg. Time Spent Dead: ' + summonerSummary['timespentdead'].toFixed(2) + ' (sec)', true)
    .setThumbnail("https://ddragon.leagueoflegends.com/cdn/12.4.1/img/profileicon/" + data.profileIconId +".png")
    .setTimestamp()

    //Sending response
    message.reply({embeds: [embed]});
  }
