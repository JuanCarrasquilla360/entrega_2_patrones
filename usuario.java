// Clase User existente (no se puede modificar)
public class User {
    private String firstname;
    private String lastname;
    private String username;
    private String password;

    public String getFirstname() { return firstname; }
    public String getUsername() { return username; }
    public void setPassword(String password) { this.password = password; }
    // Otros métodos...
}

// Interfaz para el patrón Composite
public interface OrganizationalComponent {
    String getName();
    void add(OrganizationalComponent component);
    void remove(OrganizationalComponent component);
    OrganizationalComponent getChild(int index);
}

// Implementación de Employee
public class Employee implements OrganizationalComponent {
    private User user;

    public Employee(User user) {
        this.user = user;
    }

    @Override
    public String getName() {
        return user.getFirstname();
    }

    @Override
    public void add(OrganizationalComponent component) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void remove(OrganizationalComponent component) {
        throw new UnsupportedOperationException();
    }

    @Override
    public OrganizationalComponent getChild(int index) {
        throw new UnsupportedOperationException();
    }

    public void setPassword(String password) {
        user.setPassword(password);
    }
}

// Implementación de Department
public class Department implements OrganizationalComponent {
    private String name;
    private List<OrganizationalComponent> components = new ArrayList<>();

    public Department(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void add(OrganizationalComponent component) {
        components.add(component);
    }

    @Override
    public void remove(OrganizationalComponent component) {
        components.remove(component);
    }

    @Override
    public OrganizationalComponent getChild(int index) {
        return components.get(index);
    }
}

// Implementación del Adapter
public class UserAdapter extends User {
    private Employee employee;

    public UserAdapter(Employee employee) {
        this.employee = employee;
    }

    @Override
    public String getFirstname() {
        return employee.getName();
    }

    @Override
    public void setPassword(String password) {
        employee.setPassword(password);
    }

    // Implementar otros métodos de User según sea necesario
}