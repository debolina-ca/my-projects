import java.awt.*;

public class Tiger extends Critter{


    //getColor
        // determines which color the critter will be displayed as
    public Action getMove(CritterInfo info) {
        if (info.getFront() == Neighbor.OTHER) {
            return Action.INFECT;
        } else {
            return Action.LEFT;
        }
    }

    //toString
        //Determines which character the critter will be displayed as
    public Color getColor() {
        
        return Color.RED;
    }
    //getMove
        //Determines the movement behavior of your critter
    public String toString() {
        return "TGR";
    }

}
