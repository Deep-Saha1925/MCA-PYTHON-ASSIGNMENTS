def football_tournament():
    n = int(input("Enter no. of teams: "))
    teams = input("Enter teams: ").split()
    matches = int(input("Enter no. of matches: "))

    d = dict()
    for t in teams:
        d[t] = [0,0,0] #[POINTS, GF, GA]

    for _ in range(matches):
        data = input("Enter HOST AWAY HOSTSCORE AWAYSCORE: ").split()
        host, away, hostScore, awayScore = data[0], data[1], int(data[2]), int(data[3])
        
        if host.lower() == away.lower():
            print("Invalid input")
            return
        
        d[host][1] += hostScore  # Host GF
        d[host][2] += awayScore  # Host GA
        d[away][1] += awayScore  # Away GF
        d[away][2] += hostScore  # Away GA
            
        if hostScore > awayScore:
            d[host][0] += 2
        elif awayScore > hostScore:
            d[away][0] += 2
        else:
            d[host][0] += 1
            d[away][0] += 1
            
    ranking = []
    for name, stats in d.items():
        p, gf, ga = stats
        gd = gf - ga
        ranking.append((name, p, gd, gf))
        
    # Key: (-Points, -GD, -GF, TeamName Lowercase)
    ranking.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0].lower()))

    for team_tuple in ranking:
        team_name = team_tuple[0]
        print(team_name)
        
football_tournament()