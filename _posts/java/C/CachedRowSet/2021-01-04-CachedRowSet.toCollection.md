---
title: CachedRowSet.toCollection()
permalink: Java/CachedRowSet/toCollection
date: 2021-01-04
key: JavaJava.C.CachedRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CachedRowSet.metodos valor="toCollection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Collection<?> toCollection() throws SQLException
Collection<?> toCollection(int column) throws SQLException
Collection<?> toCollection(String column) throws SQLException
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_data parametro="int column" %}
* **String column**,  {% include w3api/param_description.html metodo=_data parametro="String column" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[CachedRowSet](/Java/CachedRowSet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CachedRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
