---
title: Statement.getMoreResults()
permalink: Java/Statement-java-sql/getMoreResults
date: 2021-01-11
key: JavaJava.S.Statement-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-sql.metodos valor="getMoreResults" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean getMoreResults() throws SQLException
boolean getMoreResults(int current) throws SQLException
~~~

## Parámetros
* **int current**,  {% include w3api/param_description.html metodo=_dato parametro="int current" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

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
