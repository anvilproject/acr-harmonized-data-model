package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A holder for Person objects
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PersonCollection  {

  private List<Person> people;


}