# Curtain Configurator

Module Odoo 18 pour la configuration et la vente de rideaux.

## Installation

1. Copiez le module dans le dossier addons de votre instance Odoo
2. Mettez à jour la liste des modules (bouton "Update Apps List")
3. Recherchez "Curtain Configurator" dans la liste des applications
4. Installez le module

## Fonctionnalités

- Ajout d'un champ "Devis Confection" sur les devis
- Champs de configuration pour les rideaux (largeur, hauteur, nombre par tringle, etc.)
- Paramétrage des valeurs d'attributs produits pour la confection

## Structure du module

```
curtain_configurator/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── sale_order.py
│   ├── sale_order_line.py
│   └── product_attribute_value.py
└── views/
    ├── sale_views.xml
    └── product_views.xml
```
