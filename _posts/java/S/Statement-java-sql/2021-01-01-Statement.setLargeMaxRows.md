---
title: Statement.setLargeMaxRows()
permalink: Java/Statement-java-sql/setLargeMaxRows
date: 2021-01-11
key: JavaJava.S.Statement-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-sql.metodos valor="setLargeMaxRows" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void setLargeMaxRows(long max) throws SQLException
~~~

## Parámetros
* **long max**,  {% include w3api/param_description.html metodo=_dato parametro="long max" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[Statement](/Java/Statement-java-sql/)

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
