
public class Street {
	/* a street has a starting pot, stack, villain bet size */
	
	private double pot; // pot size entering the street
	private double stack; // effective stack
	private double villbet; // villain's bet size (-1 if none)
	private double betpct; // % pot bet
	
	public Street(double p, double s, double v){
		
		this.pot = p;
		this.stack = s;
		this.villbet = v;
	}
	
	public void setBetPct(double b){
		this.betpct = b;
	}
	
	public double returnBetOrRaise(){
		if (villbet == -1)
			return this.betpct*this.pot;
		else
			return (this.villbet*2 + this.pot)*this.betpct+this.villbet;
	}
	
	public double returnFinalPot(){
		if (villbet == -1)
				return this.betpct*this.pot*2 + pot;
		else {
			return 2*this.returnBetOrRaise() + this.pot;
		}
	}
	
	public double returnFinalStack(){
		return this.stack - this.returnBetOrRaise();
	}
	
	// final street difference
	public double error(){
		return this.stack - this.returnBetOrRaise();
	}
	
	// remove this eventually
	public void output(){
		System.out.printf("Bet Size: %f\n", this.returnBetOrRaise());
		System.out.printf("Vill Bet: %f\n", this.villbet);
		System.out.printf("Final Pot: %f \n", this.pot);
		System.out.printf("Final Stack: %f\n\n", this.stack);
	}

}
