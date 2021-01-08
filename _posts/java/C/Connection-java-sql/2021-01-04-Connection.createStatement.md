---
title: Connection.createStatement()
permalink: Java/Connection-java-sql/createStatement
date: 2021-01-04
key: JavaJava.C.Connection-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="createStatement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Statement createStatement() throws SQLException
Statement createStatement(int resultSetType, int resultSetConcurrency) throws SQLException
Statement createStatement(int resultSetType, int resultSetConcurrency, int resultSetHoldability) throws SQLException
~~~

## Parámetros
* **int resultSetType**,  {% include w3api/param_description.html metodo=_data parametro="int resultSetType" %}
* **int resultSetHoldability**,  {% include w3api/param_description.html metodo=_data parametro="int resultSetHoldability" %}
* **int resultSetConcurrency**,  {% include w3api/param_description.html metodo=_data parametro="int resultSetConcurrency" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[Connection](/Java/Connection-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Connection-java-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
