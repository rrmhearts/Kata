The quickest way is to use `NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE` for each struct, defined bottom-up (innermost/nested structs first, outermost last). Here's the pattern:

```cpp
#include <iostream>
#include "nlohmann/json.hpp"
#include <fstream>

using json = nlohmann::json;

namespace ns {
    // 1. Define structs bottom-up (leaf structs first)
    struct Database {
        std::string host;
        int port;
        std::string name;
    };

    struct Logging {
        std::string level;
        std::string file;
    };

    struct Server {
        std::string ip;
        int port;
    };

    // 2. Outermost struct last
    struct Config {
        Server server;
        Database database;
        Logging logging;
    };

    // 3. Macros also bottom-up, matching struct order
    NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE(Database, host, port, name)
    NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE(Logging, level, file)
    NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE(Server, ip, port)
    NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE(Config, server, database, logging)
}

int main() {
    std::ifstream f("config.json");
    json j = json::parse(f);

    auto config = j.get<ns::Config>();

    std::cout << config.server.ip << "\n";
    std::cout << config.database.host << "\n";
    return 0;
}
```

For a large config file, the fastest workflow is:

1. **Paste your JSON into an AI** (like me) and ask it to generate the structs and macros — this is by far the quickest approach for large configs
2. The field names in the macro **must exactly match the JSON keys** (case-sensitive)
3. If a JSON key uses `snake_case` or `camelCase`, your struct member must match it exactly
4. Any **optional fields** should use `std::optional<T>` and switch to `NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE_WITH_DEFAULT` instead, which fills in defaults rather than throwing on missing keys:

```cpp
NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE_WITH_DEFAULT(Database, host, port, name)
```

Just paste your config JSON here and I can generate all the structs and macros for you instantly.