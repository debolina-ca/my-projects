import java.awt.*;
public class Bear extends Critter{
    //getColor
        // determines which color the critter will be displayed as
    public Color getColor() {
        return Color.WHITE;
    }
    //toString
        //Determines which character the critter will be displayed as
    public String toString() {
        return "/";
    }

    //getMove
        //Determines the movement behavior of your critter
    public Action getMove(CritterInfo info) {
        if (info.getFront() == Neighbor.OTHER) {
            return Action.INFECT;
        } else {
            return Action.LEFT;
        }
    }
}
