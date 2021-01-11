---
title: CachedRowSet.columnUpdated()
permalink: Java/CachedRowSet/columnUpdated
date: 2021-01-11
key: JavaJava.C.CachedRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CachedRowSet.metodos valor="columnUpdated" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean columnUpdated(int idx) throws SQLException
boolean columnUpdated(String columnName) throws SQLException
~~~

## Parámetros
* **int idx**,  {% include w3api/param_description.html metodo=_dato parametro="int idx" %}
* **String columnName**,  {% include w3api/param_description.html metodo=_dato parametro="String columnName" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
