---
title: CatalogManager.catalog()
permalink: Java/CatalogManager/catalog
date: 2021-01-04
key: JavaJava.C.CatalogManager
category: java
tags: ['java se', 'javax.xml.catalog', 'java.xml', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CatalogManager.metodos valor="catalog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Catalog catalog(CatalogFeatures features, URI... uris)
~~~

## Parámetros
* **CatalogFeatures features**,  {% include w3api/param_description.html metodo=_data parametro="CatalogFeatures features" %}
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
