package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Represents a Person
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Person extends NamedThing {

  private String primaryEmail;
  private LocalDate birthDate;
  private Integer ageInYears;
  private String vitalStatus;


}