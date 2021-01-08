---
title: CatalogManager.catalogResolver()
permalink: Java/CatalogManager/catalogResolver
date: 2021-01-04
key: JavaJava.C.CatalogManager
category: java
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
* **CatalogFeatures features**,  {% include w3api/param_description.html metodo=_data parametro="CatalogFeatures features" %}
* **Catalog catalog**,  {% include w3api/param_description.html metodo=_data parametro="Catalog catalog" %}
* **URI... uris**,  {% include w3api/param_description.html metodo=_data parametro="URI... uris" %}

## Excepciones
[CatalogException](/Java/CatalogException/), [SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CatalogManager](/Java/CatalogManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CatalogManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
