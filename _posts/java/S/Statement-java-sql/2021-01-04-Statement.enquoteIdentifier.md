---
title: Statement.enquoteIdentifier()
permalink: Java/Statement-java-sql/enquoteIdentifier
date: 2021-01-04
key: JavaJava.S.Statement-java-sql
category: java
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
* **String identifier**,  {% include w3api/param_description.html metodo=_data parametro="String identifier" %}
* **boolean alwaysQuote**,  {% include w3api/param_description.html metodo=_data parametro="boolean alwaysQuote" %}

## Excepciones
[SQLException](/Java/SQLException/), [NullPointerException](/Java/NullPointerException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[Statement](/Java/Statement-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Statement-java-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
