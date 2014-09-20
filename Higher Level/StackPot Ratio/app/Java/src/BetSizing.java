
public class BetSizing {
	
	// print out sizing by street (eventually return an array)
	public static void returnSizes(Street c, double pct, int streetsRem){
		for(int i = 1; i <= streetsRem; i++){			
			Street prev = c;
			c = new Street(prev.returnFinalPot(), prev.returnFinalStack(), -1);
			c.setBetPct(pct);
			c.output();
		}
	}

	public static double testSize(Street c, double pct, int streetsRem){
		for(int i = 1; i < streetsRem; i++){			
			Street prev = c;
			c = new Street(prev.returnFinalPot(), prev.returnFinalStack(), -1);
			c.setBetPct(pct);
		}
		return c.error();
	}
	
	public static double binarySearch(double guess, double pot, double stack, int streets, double villbet){
		double mini = 0;
		double maxi = 10;
		Street prev = null;
		double err;
		double oldGuess = 0;
		double tempOld = 0;
		Street curr;
		
		while(true){
			curr = new Street(pot, stack, villbet);
			curr.setBetPct(guess);
			err = testSize(curr, guess, streets);
			
			if (Math.abs(err) < 0.0000001)
				return guess;
			else {
				if (prev == null) { // first iteration
					prev = curr;
					oldGuess = guess;
					if (err < 0) // bet size too big
						guess = guess/2; // halfway between 0 and curr
					else // bet size too small, halfway between 10 and curr
						guess = (maxi+guess)/2;
				}
				else{ // not first iteration
					if (guess < oldGuess){ // last attempt too big
						if (err < 0) {// still too big
							oldGuess = guess;
							guess = (guess+mini)/2; //halfway between min and prior guess
						}
						else { // was too big; now too small
							maxi = oldGuess; // the value has to be lower than this
							tempOld = guess;
							guess = (guess + oldGuess) / 2;
							oldGuess = tempOld;
						}
					}
					else { // last attempt too small
						if(err < 0){ // now too big
							mini = oldGuess;
							tempOld = guess;
							guess = (guess + oldGuess)/2;
							oldGuess = tempOld;
						}
						else{
							oldGuess = guess;
							guess = (maxi + guess)/2;
						}
					}
				}
			}
		}
	}
	
	public static void main(String []args){
		double pot = 10;
		double stack = 100;
		double villbet = 5;
		double guess = 0.5;
		int streets = 3;
		
		// start.output();		
		// returnSizes(start, pct, streetsRem, pct);
		// System.out.println(testSize(start, pct, streetsRem));
		double optimal = binarySearch(guess, pot, stack, streets, villbet);
		returnSizes(new Street(pot, stack, villbet), optimal, streets);
	
		/* TODO:
		 * - simple web app: takes the 5 inputs in a form, return bet %
		 * - gradually build from there
		 */
	}
}
