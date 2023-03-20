import java.util.List;
import java.util.ArrayList;

public class SoftwareDirectory implements SoftwareDisplay{
    private List<Software> softwareList = new ArrayList<Software>();

    public void addSoftware(Software software)
    {
        softwareList.add(software);
    }

    public void removeSoftware(Software software)
    {
        softwareList.remove(software);
    }

    @Override
    public void displaySoftwareInformation()
    {
        for(Software software:softwareList)
        {
            software.displaySoftwareInformation();
        }
    }
}
