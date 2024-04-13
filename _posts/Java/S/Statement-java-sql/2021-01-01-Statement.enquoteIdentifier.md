---
title: Statement.enquoteIdentifier()
permalink: /Java/Statement-java-sql/enquoteIdentifier/
date: 2021-01-11
key: Java.S.Statement-java-sql
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-sql.metodos valor="enquoteIdentifier" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default String enquoteIdentifier(String identifier, boolean alwaysQuote) throws SQLException
~~~

## Parámetros
* **boolean alwaysQuote**,  {% include w3api/param_description.html metodo=_dato parametro="boolean alwaysQuote" %}
* **String identifier**,  {% include w3api/param_description.html metodo=_dato parametro="String identifier" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/), [NullPointerException](/Java/NullPointerException/)

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
