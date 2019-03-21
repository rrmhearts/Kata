function nexus(users) {
	  var eval, closest = -1;
	  var str = -1;
	  for (var prop in users) {
		      eval = Math.abs(Number(prop) - users[prop]);
		      if (eval < closest || closest === -1)
			      {
			            closest = eval;
			            str = prop;
			          }
		    }
	  return Number(str);
}

const nexusBetter = x => +Object.keys(x).reduce((a,e) => Math.abs(e - x[e]) < Math.abs(a - x[a]) ? e : a);


nexus({"1":3,"3":3,"5":3});
