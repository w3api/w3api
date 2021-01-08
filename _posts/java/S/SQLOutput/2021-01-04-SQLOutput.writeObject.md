---
title: SQLOutput.writeObject()
permalink: Java/SQLOutput/writeObject
date: 2021-01-04
key: JavaJava.S.SQLOutput
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLOutput.metodos valor="writeObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void writeObject(Object x, SQLType targetSqlType) throws SQLException
void writeObject(SQLData x) throws SQLException
~~~

## Parámetros
* **SQLType targetSqlType**,  {% include w3api/param_description.html metodo=_data parametro="SQLType targetSqlType" %}
* **SQLData x**,  {% include w3api/param_description.html metodo=_data parametro="SQLData x" %}
* **Object x**,  {% include w3api/param_description.html metodo=_data parametro="Object x" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[SQLOutput](/Java/SQLOutput/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLOutput.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
