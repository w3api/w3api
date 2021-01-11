---
title: Connection.createArrayOf()
permalink: Java/Connection-java-sql/createArrayOf
date: 2021-01-11
key: JavaJava.C.Connection-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="createArrayOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Array createArrayOf(String typeName, Object[] elements) throws SQLException
~~~

## Parámetros
* **String typeName**,  {% include w3api/param_description.html metodo=_dato parametro="String typeName" %}
* **Object[] elements**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] elements" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
