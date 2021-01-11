---
title: Predicate.evaluate()
permalink: Java/Predicate-javax-sql-rowset/evaluate
date: 2021-01-11
key: JavaJava.P.Predicate-javax-sql-rowset
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Predicate-javax-sql-rowset.metodos valor="evaluate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean evaluate(Object value, int column) throws SQLException
boolean evaluate(Object value, String columnName) throws SQLException
boolean evaluate(RowSet rs)
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_dato parametro="int column" %}
* **RowSet rs**,  {% include w3api/param_description.html metodo=_dato parametro="RowSet rs" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **String columnName**,  {% include w3api/param_description.html metodo=_dato parametro="String columnName" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[Predicate](/Java/Predicate-javax-sql-rowset/)

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
