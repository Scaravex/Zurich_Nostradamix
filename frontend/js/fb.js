var client = new Keen({
  projectId: '5368fa5436bf5a5623000000',
  readKey: '3f324dcb5636316d6865ab0ebbbbc725224c7f8f3e8899c7733439965d6d4a2c7f13bf7765458790bd50ec76b4361687f51cf626314585dc246bb51aeb455c0a1dd6ce77a993d9c953c5fc554d1d3530ca5d17bdc6d1333ef3d8146a990c79435bb2c7d936f259a22647a75407921056'
});

Keen.ready(function(){

  // Pageviews by browser
  var sampleData1 = [
      ["Conservative and Traditional", "Liberal and Artistic", 0.6625392409386361],
      ["Impulsive and Spontaneous", "Organized and Hard Working", 0.4771745931633382],
      ["Contemplative", "Engaged with outside world", 0.06852020443012857],
      ["Competitive", "Team working and Trusting", 0.5242589938711448],
      ["Laid back and Relaxed", "Easily Stressed and Emotional", 0.02308082639082526]
  ]

  $(document).ready(function() {
      $("#example1").drawCSSBipolarChart({
          data: sampleData1,
          bipolar: true
      })

  })



  // Impressions timeline
  //
  // var impressions_timeline = new Keen.Dataviz()
  //   .el('#chart-03')
  //   .type('horizontal-bar')
  //    .colors(['#9BCA58', 'orange', 'green'])
  //   .height(280)
  //   .stacked(true)
  //   .title('Consumer Needs')
  //   .prepare();
  //   var data2 = {
  //       "result": [{
  //           "color": "Number of followers",
  //           "result": 66
  //         },
  //         {
  //           "color": "Number of confirmed competances",
  //           "result": 55
  //         },
  //         {
  //           "color": "Current Job duration",
  //           "result": 45
  //         }]
  //   };


    // impressions_timeline
    // .data(data2)
    // .sortGroups('desc')
    // .render();


  //
  // client
  //   .query('count', {
  //     event_collection: 'impressions',
  //     group_by: 'ad.advertiser',
  //     interval: 'hourly',
  //     timeframe: {
  //       start: '2014-05-04T00:00:00.000Z',
  //       end: '2014-05-05T00:00:00.000Z'
  //     }
  //   })
  //   .then(function(res) {
  //     impressions_timeline
  //       .data(res)
  //       .sortGroups('desc')
  //       .render();
  //   })
  //   .catch(function(err) {
  //     impressions_timeline.message(err.message)
  //   });

  // Impressions by device
  //
  // var widget4 = new Keen.Dataviz()
  //   .el('#chart-04')
  //   .type('horizontal-bar')
  //   .height(280)
  //   .colors(['#175689', 'orange', 'green'])
  //   .stacked(true)
  //   .title('Financial Stability')
  //   .prepare();
  //   var data3 = {
  //       "result": [{
  //           "color": "Linekdin Popularity",
  //           "result": 96
  //         }, {
  //           "color": "Salary (est.)",
  //           "result": 25
  //         },
  //         {
  //           "color": "Education score",
  //           "result": 80
  //         }]
  //   };
  //
  //
  //   widget4
  //   .data(data3)
  //   .sortGroups('desc')
  //   .render();
  //
  //
    var widget4 = new Keen.Dataviz()
      .el('#chart-04')
      .type('horizontal-bar')
      .height(280)
      .colors(['#175689', 'orange', 'green'])
      .stacked(true)
      .title('Values')
      .prepare();
      var data4 = {
          "result": [{
              "color": "Tradition",
              "result": 0.9
            }, {
              "color": "Stimulation",
              "result": 0.8
            },
            {
              "color": "Helping others",
              "result": 0.3
            },
            {
              "color": "Achivment",
              "result": 0.6
            }]
      };


      widget4
      .data(data4)
      .render();


        var widget5 = new Keen.Dataviz()
          .el('#chart-05')
          .type('horizontal-bar')
           .colors(['#9BCA58', 'orange', 'green'])
          .height(280)
          .stacked(true)
          .title('Consumer Needs')
          .prepare();
          var data5 = {
              "result": [{
                  "color": "Harmony",
                  "result": 76
                }, {
                  "color": "Curiosity",
                  "result": 55
                },
                {
                  "color": "Self-expression",
                  "result": 76
                },
                {
                  "color": "Stability",
                  "result": 25
                },
                {
                  "color": "Closeness",
                  "result": 87
                }]
          };


          widget5
          .data(data5)
          .sortGroups('desc')
          .render();

});
