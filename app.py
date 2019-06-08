const line = require('@line/bot-sdk');

const config = {
  channelAccessToken: '+NVJIn8NLXRz0W+iCUmtcxNg/YhjgvGqq++PiGyxu0pb/O3ZdFPxc9vnDSnO3pasVqpon83WAck8NCDO4Udo2H/cSRhn7MgDP/Dge/GjEgXnBjfz0Tb819nJ4fw+b68avXJ3Zv0CMccduBY5o/MFrQdB04t89/1O/w1cDnyilFU=',
  channelSecret: '5af2e4c822dda3bd3af061c7e06480e3'
};

const app = express();
app.post('/', line.middleware(config), (req, res) => {
  Promise
    .all(req.body.events.map(handleEvent))
    .then((result) => res.json(result));
});

const client = new line.Client(config);
function handleEvent(event) {
  if (event.type !== 'message' || event.message.type !== 'text') {
    return Promise.resolve(null);
  }

  return client.replyMessage(event.replyToken, {
    type: 'text',
    text: event.message.text
  });
}

app.listen(process.env.PORT || 8080, function() {
  console.log("App now running on port");
});
