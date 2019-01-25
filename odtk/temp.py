# UMONS dataset, Random Forest, 0.8 train ratio
result = \
    {'Temperature': {'Without': {'Accuracy': 0.9968385214007782,
                                 'F1Score': 0.9888983774551665,
                                 'Fallout': 0.0011350737797956867,
                                 'FalseNegative': 9,
                                 'FalsePositive': 4,
                                 'Missrate': 0.015306122448979591,
                                 'Precision': 0.9931389365351629,
                                 'Recall': 0.9846938775510204,
                                 'Selectivity': 0.9988649262202043,
                                 'TrueNegative': 3520,
                                 'TruePositive': 579},
                     'With only': {'Accuracy': 0.8745136186770428,
                                   'F1Score': 0.4901185770750988,
                                   'Fallout': 0.049943246311010214,
                                   'FalseNegative': 340,
                                   'FalsePositive': 176,
                                   'Missrate': 0.5782312925170068,
                                   'Precision': 0.5849056603773585,
                                   'Recall': 0.4217687074829932,
                                   'Selectivity': 0.9500567536889898,
                                   'TrueNegative': 3348,
                                   'TruePositive': 248}},
     'Light': {'Without': {'Accuracy': 0.9270428015564203,
                           'F1Score': 0.7098646034816247,
                           'Fallout': 0.022417707150964812,
                           'FalseNegative': 221,
                           'FalsePositive': 79,
                           'Missrate': 0.3758503401360544,
                           'Precision': 0.8228699551569507,
                           'Recall': 0.6241496598639455,
                           'Selectivity': 0.9775822928490352,
                           'TrueNegative': 3445,
                           'TruePositive': 367},
               'With only': {'Accuracy': 0.9965953307392996,
                             'F1Score': 0.9880341880341881,
                             'Fallout': 0.0011350737797956867,
                             'FalseNegative': 10,
                             'FalsePositive': 4,
                             'Missrate': 0.017006802721088437,
                             'Precision': 0.993127147766323,
                             'Recall': 0.9829931972789115,
                             'Selectivity': 0.9988649262202043,
                             'TrueNegative': 3520,
                             'TruePositive': 578}},
     'CO2': {'Without': {'Accuracy': 0.9910019455252919,
                         'F1Score': 0.9676855895196507,
                         'Fallout': 0.000851305334846765,
                         'FalseNegative': 34,
                         'FalsePositive': 3,
                         'Missrate': 0.05782312925170068,
                         'Precision': 0.9946140035906643,
                         'Recall': 0.9421768707482994,
                         'Selectivity': 0.9991486946651532,
                         'TrueNegative': 3521,
                         'TruePositive': 554},
             'With only': {'Accuracy': 0.8818093385214008,
                           'F1Score': 0.49269311064718163,
                           'Fallout': 0.038024971623155504,
                           'FalseNegative': 352,
                           'FalsePositive': 134,
                           'Missrate': 0.5986394557823129,
                           'Precision': 0.6378378378378379,
                           'Recall': 0.4013605442176871,
                           'Selectivity': 0.9619750283768445,
                           'TrueNegative': 3390,
                           'TruePositive': 236}},
     'Humidity': {'Without': {'Accuracy': 0.995136186770428,
                              'F1Score': 0.9828178694158075,
                              'Fallout': 0.0011350737797956867,
                              'FalseNegative': 16,
                              'FalsePositive': 4,
                              'Missrate': 0.027210884353741496,
                              'Precision': 0.9930555555555556,
                              'Recall': 0.9727891156462585,
                              'Selectivity': 0.9988649262202043,
                              'TrueNegative': 3520,
                              'TruePositive': 572},
                  'With only': {'Accuracy': 0.8056906614785992,
                                'F1Score': 0.23540669856459331,
                                'Fallout': 0.09477866061293984,
                                'FalseNegative': 465,
                                'FalsePositive': 334,
                                'Missrate': 0.7908163265306123,
                                'Precision': 0.26914660831509846,
                                'Recall': 0.20918367346938777,
                                'Selectivity': 0.9052213393870602,
                                'TrueNegative': 3190,
                                'TruePositive': 123}},
     'HumidityRatio': {'Without': {'Accuracy': 0.9953793774319066,
                                   'F1Score': 0.9836909871244636,
                                   'Fallout': 0.0011350737797956867,
                                   'FalseNegative': 15,
                                   'FalsePositive': 4,
                                   'Missrate': 0.025510204081632654,
                                   'Precision': 0.9930675909878682,
                                   'Recall': 0.9744897959183674,
                                   'Selectivity': 0.9988649262202043,
                                   'TrueNegative': 3520,
                                   'TruePositive': 573},
                       'With only': {'Accuracy': 0.6670719844357976,
                                     'F1Score': 0.33186920448999513,
                                     'Fallout': 0.3181044267877412,
                                     'FalseNegative': 248,
                                     'FalsePositive': 1121,
                                     'Missrate': 0.4217687074829932,
                                     'Precision': 0.2327173169062286,
                                     'Recall': 0.5782312925170068,
                                     'Selectivity': 0.6818955732122588,
                                     'TrueNegative': 2403,
                                     'TruePositive': 340}}}
'''
{'All Features': {'RandomForest': {'Accuracy': 0.9953793774319066,
                                   'F1Score': 0.9836909871244636,
                                   'Fallout': 0.0011350737797956867,
                                   'FalseNegative': 15,
                                   'FalsePositive': 4,
                                   'Missrate': 0.025510204081632654,
                                   'Precision': 0.9930675909878682,
                                   'Recall': 0.9744897959183674,
                                   'Selectivity': 0.9988649262202043,
                                   'TrueNegative': 3520,
                                   'TruePositive': 573}}}
{'No Temperature': {'RandomForest': {'Accuracy': 0.9968385214007782,
                                     'F1Score': 0.9888983774551665,
                                     'Fallout': 0.0011350737797956867,
                                     'FalseNegative': 9,
                                     'FalsePositive': 4,
                                     'Missrate': 0.015306122448979591,
                                     'Precision': 0.9931389365351629,
                                     'Recall': 0.9846938775510204,
                                     'Selectivity': 0.9988649262202043,
                                     'TrueNegative': 3520,
                                     'TruePositive': 579}}}
{'No Humidity': {'RandomForest': {'Accuracy': 0.995136186770428,
                                  'F1Score': 0.9828178694158075,
                                  'Fallout': 0.0011350737797956867,
                                  'FalseNegative': 16,
                                  'FalsePositive': 4,
                                  'Missrate': 0.027210884353741496,
                                  'Precision': 0.9930555555555556,
                                  'Recall': 0.9727891156462585,
                                  'Selectivity': 0.9988649262202043,
                                  'TrueNegative': 3520,
                                  'TruePositive': 572}}}
{'No Light': {'RandomForest': {'Accuracy': 0.9270428015564203,
                               'F1Score': 0.7098646034816247,
                               'Fallout': 0.022417707150964812,
                               'FalseNegative': 221,
                               'FalsePositive': 79,
                               'Missrate': 0.3758503401360544,
                               'Precision': 0.8228699551569507,
                               'Recall': 0.6241496598639455,
                               'Selectivity': 0.9775822928490352,
                               'TrueNegative': 3445,
                               'TruePositive': 367}}}
{'No CO2': {'RandomForest': {'Accuracy': 0.9910019455252919,
                             'F1Score': 0.9676855895196507,
                             'Fallout': 0.000851305334846765,
                             'FalseNegative': 34,
                             'FalsePositive': 3,
                             'Missrate': 0.05782312925170068,
                             'Precision': 0.9946140035906643,
                             'Recall': 0.9421768707482994,
                             'Selectivity': 0.9991486946651532,
                             'TrueNegative': 3521,
                             'TruePositive': 554}}}
{'No HumidityRatio': {'RandomForest': {'Accuracy': 0.9953793774319066,
                                       'F1Score': 0.9836909871244636,
                                       'Fallout': 0.0011350737797956867,
                                       'FalseNegative': 15,
                                       'FalsePositive': 4,
                                       'Missrate': 0.025510204081632654,
                                       'Precision': 0.9930675909878682,
                                       'Recall': 0.9744897959183674,
                                       'Selectivity': 0.9988649262202043,
                                       'TrueNegative': 3520,
                                       'TruePositive': 573}}}
{'Only Temperature': {'RandomForest': {'Accuracy': 0.8745136186770428,
                                       'F1Score': 0.4901185770750988,
                                       'Fallout': 0.049943246311010214,
                                       'FalseNegative': 340,
                                       'FalsePositive': 176,
                                       'Missrate': 0.5782312925170068,
                                       'Precision': 0.5849056603773585,
                                       'Recall': 0.4217687074829932,
                                       'Selectivity': 0.9500567536889898,
                                       'TrueNegative': 3348,
                                       'TruePositive': 248}}}
{'Only Humidity': {'Only Humidity': {'Accuracy': 0.8056906614785992,
                                     'F1Score': 0.23540669856459331,
                                     'Fallout': 0.09477866061293984,
                                     'FalseNegative': 465,
                                     'FalsePositive': 334,
                                     'Missrate': 0.7908163265306123,
                                     'Precision': 0.26914660831509846,
                                     'Recall': 0.20918367346938777,
                                     'Selectivity': 0.9052213393870602,
                                     'TrueNegative': 3190,
                                     'TruePositive': 123}}}
{'Only Light': {'RandomForest': {'Accuracy': 0.9965953307392996,
                                 'F1Score': 0.9880341880341881,
                                 'Fallout': 0.0011350737797956867,
                                 'FalseNegative': 10,
                                 'FalsePositive': 4,
                                 'Missrate': 0.017006802721088437,
                                 'Precision': 0.993127147766323,
                                 'Recall': 0.9829931972789115,
                                 'Selectivity': 0.9988649262202043,
                                 'TrueNegative': 3520,
                                 'TruePositive': 578}}}
{'Only CO2': {'RandomForest': {'Accuracy': 0.8818093385214008,
                               'F1Score': 0.49269311064718163,
                               'Fallout': 0.038024971623155504,
                               'FalseNegative': 352,
                               'FalsePositive': 134,
                               'Missrate': 0.5986394557823129,
                               'Precision': 0.6378378378378379,
                               'Recall': 0.4013605442176871,
                               'Selectivity': 0.9619750283768445,
                               'TrueNegative': 3390,
                               'TruePositive': 236}}}
{'Only HumidityRatio': {'RandomForest': {'Accuracy': 0.6670719844357976,
                                         'F1Score': 0.33186920448999513,
                                         'Fallout': 0.3181044267877412,
                                         'FalseNegative': 248,
                                         'FalsePositive': 1121,
                                         'Missrate': 0.4217687074829932,
                                         'Precision': 0.2327173169062286,
                                         'Recall': 0.5782312925170068,
                                         'Selectivity': 0.6818955732122588,
                                         'TrueNegative': 2403,
                                         'TruePositive': 340}}}
'''

'''
result = {'0.2': {'NNv2': {'Accuracy': 0.9655885214007782,
                           'F1Score': 0.9187248707639287,
                           'Fallout': 0.02685490677510934,
                           'FalseNegative': 216,
                           'FalsePositive': 350,
                           'Missrate': 0.06325036603221083,
                           'Precision': 0.9013806706114399,
                           'Recall': 0.9367496339677892,
                           'Selectivity': 0.9731450932248906,
                           'TrueNegative': 12683,
                           'TruePositive': 3199}},
          '0.4': {'NNv2': {'Accuracy': 0.9705739299610895,
                           'F1Score': 0.9369463262115685,
                           'Fallout': 0.024605678233438486,
                           'FalseNegative': 129,
                           'FalsePositive': 234,
                           'Missrate': 0.045647558386411886,
                           'Precision': 0.9201637666325486,
                           'Recall': 0.9543524416135881,
                           'Selectivity': 0.9753943217665615,
                           'TrueNegative': 9276,
                           'TruePositive': 2697}},
          '0.6': {'NNv2': {'Accuracy': 0.9764105058365758,
                           'F1Score': 0.9469365426695843,
                           'Fallout': 0.02883132901634289,
                           'FalseNegative': 7,
                           'FalsePositive': 187,
                           'Missrate': 0.004027617951668585,
                           'Precision': 0.9025026068821689,
                           'Recall': 0.9959723820483314,
                           'Selectivity': 0.9711686709836571,
                           'TrueNegative': 6299,
                           'TruePositive': 1731}},
          '0.8': {'NNv2': {'Accuracy': 0.9980544747081712,
                           'F1Score': 0.9932088285229203,
                           'Fallout': 0.0014188422247446084,
                           'FalseNegative': 3,
                           'FalsePositive': 5,
                           'Missrate': 0.00510204081632653,
                           'Precision': 0.9915254237288136,
                           'Recall': 0.9948979591836735,
                           'Selectivity': 0.9985811577752554,
                           'TrueNegative': 3519,
                           'TruePositive': 585}}}
'''
'''
# 0.8 split
result = \
    {'umons-all': {'RandomForest': {'Accuracy': 0.9961089494163424,
                                    'F1Score': 0.9863013698630136,
                                    'Fallout': 0.0011350737797956867,
                                    'FalseNegative': 12,
                                    'FalsePositive': 4,
                                    'Missrate': 0.02040816326530612,
                                    'Precision': 0.993103448275862,
                                    'Recall': 0.9795918367346939,
                                    'Selectivity': 0.9988649262202043,
                                    'TrueNegative': 3520,
                                    'TruePositive': 576},
                   'HMM': {'Accuracy': 0.9982976653696498,
                           'F1Score': 0.9940627650551315,
                           'Fallout': 0.0014188422247446084,
                           'FalseNegative': 2,
                           'FalsePositive': 5,
                           'Missrate': 0.003401360544217687,
                           'Precision': 0.9915397631133672,
                           'Recall': 0.9965986394557823,
                           'Selectivity': 0.9985811577752554,
                           'TrueNegative': 3519,
                           'TruePositive': 586},
                   'PF': {'Accuracy': 0.9973249027237354,
                          'F1Score': 0.9906700593723494,
                          'Fallout': 0.0019863791146424517,
                          'FalseNegative': 4,
                          'FalsePositive': 7,
                          'Missrate': 0.006802721088435374,
                          'Precision': 0.988155668358714,
                          'Recall': 0.9931972789115646,
                          'Selectivity': 0.9980136208853575,
                          'TrueNegative': 3517,
                          'TruePositive': 584},
                   'NNv2': {'Accuracy': 0.9980544747081712,
                            'F1Score': 0.9932088285229203,
                            'Fallout': 0.0014188422247446084,
                            'FalseNegative': 3,
                            'FalsePositive': 5,
                            'Missrate': 0.00510204081632653,
                            'Precision': 0.9915254237288136,
                            'Recall': 0.9948979591836735,
                            'Selectivity': 0.9985811577752554,
                            'TrueNegative': 3519,
                            'TruePositive': 585},
                   'RNN': {'Accuracy': 0.9980544747081712,
                           'F1Score': 0.9932088285229203,
                           'Fallout': 0.0014188422247446084,
                           'FalseNegative': 3,
                           'FalsePositive': 5,
                           'Missrate': 0.00510204081632653,
                           'Precision': 0.9915254237288136,
                           'Recall': 0.9948979591836735,
                           'Selectivity': 0.9985811577752554,
                           'TrueNegative': 3519,
                           'TruePositive': 585},
                   'SVM': {'Accuracy': 0.9970817120622568,
                           'F1Score': 0.9898819561551433,
                           'Fallout': 0.0031214528944381384,
                           'FalseNegative': 1,
                           'FalsePositive': 11,
                           'Missrate': 0.0017006802721088435,
                           'Precision': 0.9816053511705686,
                           'Recall': 0.9982993197278912,
                           'Selectivity': 0.9968785471055619,
                           'TrueNegative': 3513,
                           'TruePositive': 587},
                   'NMF': {'Accuracy': 0.9229085603112841,
                           'F1Score': 0.6864490603363007,
                           'Fallout': 0.021566401816118047,
                           'FalseNegative': 241,
                           'FalsePositive': 76,
                           'Missrate': 0.4098639455782313,
                           'Precision': 0.8203309692671394,
                           'Recall': 0.5901360544217688,
                           'Selectivity': 0.978433598183882,
                           'TrueNegative': 3448,
                           'TruePositive': 347}},
'sdu-all': {'NMF': {'Accuracy': 0.4038895730706076,
                     'F1Score': 0.6402240896358543,
                     'Fallout': 0.09200938619241694,
                     'FalseNegative': 5677,
                     'FalsePositive': 745,
                     'Missrate': 0.4983759108067773,
                     'Precision': 0.8846570676575322,
                     'Recall': 0.5016240891932228,
                     'Selectivity': 0.9079906138075831,
                     'TrueNegative': 7352,
                     'TruePositive': 5714}},
'NNv2': {'Accuracy': 0.6139675697865353,
                      'F1Score': 0.7146595865731082,
                      'Fallout': 0.6858095590959614,
                      'FalseNegative': 1970,
                      'FalsePositive': 5553,
                      'Missrate': 0.17294355192695987,
                      'Precision': 0.6291572058234273,
                      'Recall': 0.8270564480730401,
                      'Selectivity': 0.3141904409040385,
                      'TrueNegative': 2544,
                      'TruePositive': 9421},
             'PF': {'Accuracy': 0.6672311165845649,
                    'F1Score': 0.6366336078892811,
                    'Fallout': 0.095714462146474,
                    'FalseNegative': 5710,
                    'FalsePositive': 775,
                    'Missrate': 0.5012729347730664,
                    'Precision': 0.8799566294919455,
                    'Recall': 0.49872706522693355,
                    'Selectivity': 0.904285537853526,
                    'TrueNegative': 7322,
                    'TruePositive': 5681},
             'RandomForest': {'Accuracy': 0.6451149425287356,
                              'F1Score': 0.6613787700744223,
                              'Fallout': 0.2814622699765345,
                              'FalseNegative': 4637,
                              'FalsePositive': 2279,
                              'Missrate': 0.4070757615661487,
                              'Precision': 0.7477028672644747,
                              'Recall': 0.5929242384338513,
                              'Selectivity': 0.7185377300234654,
                              'TrueNegative': 5818,
                              'TruePositive': 6754}}}

'''

result = \
    {'15 sec': {'NNv2': {'Accuracy': 0.9981758482305728,
                         'F1Score': 0.9936305732484076,
                         'Fallout': 0.0016313213703099511,
                         'FalseNegative': 7,
                         'FalsePositive': 23,
                         'Missrate': 0.002982530890498509,
                         'Precision': 0.9902666102412188,
                         'Recall': 0.9970174691095015,
                         'Selectivity': 0.99836867862969,
                         'TrueNegative': 14076,
                         'TruePositive': 2340}},
     '30 sec': {'NNv2': {'Accuracy': 0.9970817120622568,
                         'F1Score': 0.9897959183673469,
                         'Fallout': 0.0022688598979013048,
                         'FalseNegative': 2,
                         'FalsePositive': 4,
                         'Missrate': 0.006825938566552901,
                         'Precision': 0.9864406779661017,
                         'Recall': 0.9931740614334471,
                         'Selectivity': 0.9977311401020987,
                         'TrueNegative': 1759,
                         'TruePositive': 291}},
     '60 sec': {'NNv2': {'Accuracy': 0.9980544747081712,
                         'F1Score': 0.9932088285229203,
                         'Fallout': 0.0014188422247446084,
                         'FalseNegative': 3,
                         'FalsePositive': 5,
                         'Missrate': 0.00510204081632653,
                         'Precision': 0.9915254237288136,
                         'Recall': 0.9948979591836735,
                         'Selectivity': 0.9985811577752554,
                         'TrueNegative': 3519,
                         'TruePositive': 585}},
     '90 sec': {'NNv2': {'Accuracy': 0.9974461875228019,
                         'F1Score': 0.9910828025477707,
                         'Fallout': 0.0017028522775649213,
                         'FalseNegative': 3,
                         'FalsePositive': 4,
                         'Missrate': 0.007653061224489796,
                         'Precision': 0.989821882951654,
                         'Recall': 0.9923469387755102,
                         'Selectivity': 0.998297147722435,
                         'TrueNegative': 2345,
                         'TruePositive': 389}},
     '120 sec': {'NNv2': {'Accuracy': 0.9970817120622568,
                          'F1Score': 0.9897959183673469,
                          'Fallout': 0.0022688598979013048,
                          'FalseNegative': 2,
                          'FalsePositive': 4,
                          'Missrate': 0.006825938566552901,
                          'Precision': 0.9864406779661017,
                          'Recall': 0.9931740614334471,
                          'Selectivity': 0.9977311401020987,
                          'TrueNegative': 1759,
                          'TruePositive': 291}}}
