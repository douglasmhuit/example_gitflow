# Calculadora App

Proyecto de demostración para aprender **Git Flow** con buenas prácticas.

## Estructura

```
example_gitflow/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── operations/
│       ├── __init__.py   ← expone todas las operaciones
│       ├── suma.py
│       ├── resta.py
│       ├── multiplicar.py
│       └── dividir.py
├── .gitignore
├── CHANGELOG.md
└── README.md
```

## Ejecutar

```bash
cd src
python main.py
```

## Convención de commits

| Prefijo      | Uso                                  |
|-------------|---------------------------------------|
| `feat:`     | Nueva funcionalidad                   |
| `fix:`      | Corrección de bug                     |
| `docs:`     | Cambios en documentación              |
| `refactor:` | Mejora interna sin cambio de lógica   |
| `chore:`    | Tareas de mantenimiento               |

## Semantic Versioning

`MAJOR.MINOR.PATCH`
- `feat` → sube MINOR  (1.0.0 → 1.1.0)
- `fix`  → sube PATCH   (1.0.0 → 1.0.1)
- Breaking change → sube MAJOR (1.0.0 → 2.0.0)
