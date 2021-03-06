---
title: CatalogManager.catalogResolver()
permalink: /Java/CatalogManager/catalogResolver/
date: 2021-01-11
key: Java.C.CatalogManager
category: Java
tags: ['java se', 'javax.xml.catalog', 'java.xml', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CatalogManager.metodos valor="catalogResolver" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CatalogResolver catalogResolver(Catalog catalog)
public static CatalogResolver catalogResolver(CatalogFeatures features, URI... uris)
~~~

## Parámetros
* **URI... uris**,  {% include w3api/param_description.html metodo=_dato parametro="URI... uris" %}
* **Catalog catalog**,  {% include w3api/param_description.html metodo=_dato parametro="Catalog catalog" %}
* **CatalogFeatures features**,  {% include w3api/param_description.html metodo=_dato parametro="CatalogFeatures features" %}

## Excepciones
[CatalogException](/Java/CatalogException/), [SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CatalogManager](/Java/CatalogManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
