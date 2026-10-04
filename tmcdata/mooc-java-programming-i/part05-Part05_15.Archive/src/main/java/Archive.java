import java.util.Objects;

public class Archive {
    String identifier;
    String name;

    public Archive(String identifier, String name) {
        this.identifier = identifier;
        this.name = name;
    }

    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    @Override
    public boolean equals(Object comparedObject) {
        Archive comparedArchive = (Archive) comparedObject;
        if (this.identifier.equals(comparedArchive.getIdentifier())){
            return true;
        }
        else{
            return false;
        }

    }
}
