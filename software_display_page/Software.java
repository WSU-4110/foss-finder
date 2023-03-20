public class Software implements SoftwareDisplay{
    private String thumbnailLink;
    private String name;
    private double rating;
    private String downloadLink;
    private String developers;
    private String operatingSystems;
    private String license;
    private String description;

    public Software(String thumbnailLink, String name, double rating, String downloadLink, String developers, String operatingSystems, String license, String description)
    {
        this.thumbnailLink = thumbnailLink;
        this.name = name;
        this.rating = rating;
        this.downloadLink = downloadLink;
        this.developers = developers;
        this.operatingSystems = operatingSystems;
        this.license = license;
        this.description = description;
    }

    @Override
    public void displaySoftwareInformation() {
        System.out.println("Thumbnail Link: " + thumbnailLink);
        System.out.println("Name: " + name);
        System.out.println("Rating: " + rating);
        System.out.println("Download Link: " + downloadLink);
        System.out.println("Developers: " + developers);
        System.out.println("Operating Systems: " + operatingSystems);
        System.out.println("License: " + license);
        System.out.println("Description: " + description);
        System.out.println("---------------------------------------------------------------------------")
    }
}