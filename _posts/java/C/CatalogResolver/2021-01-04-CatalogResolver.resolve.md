---
title: CatalogResolver.resolve()
permalink: Java/CatalogResolver/resolve
date: 2021-01-04
key: JavaJava.C.CatalogResolver
category: java
tags: ['java se', 'javax.xml.catalog', 'java.xml', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CatalogResolver.metodos valor="resolve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Source resolve(String href, String base)
~~~

## Parámetros
* **String href**,  {% include w3api/param_description.html metodo=_data parametro="String href" %}
* **String base**,  {% include w3api/param_description.html metodo=_data parametro="String base" %}

## Excepciones
[CatalogException](/Java/CatalogException/)

## Clase Padre
[CatalogResolver](/Java/CatalogResolver/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CatalogResolver.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
