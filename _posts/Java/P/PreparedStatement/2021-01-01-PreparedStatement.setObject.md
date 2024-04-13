---
title: PreparedStatement.setObject()
permalink: /Java/PreparedStatement/setObject/
date: 2021-01-11
key: Java.P.PreparedStatement
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setObject(int parameterIndex, Object x) throws SQLException
void setObject(int parameterIndex, Object x, int targetSqlType) throws SQLException
void setObject(int parameterIndex, Object x, int targetSqlType, int scaleOrLength) throws SQLException
default void setObject(int parameterIndex, Object x, SQLType targetSqlType) throws SQLException
default void setObject(int parameterIndex, Object x, SQLType targetSqlType, int scaleOrLength) throws SQLException
~~~

## Parámetros
* **int scaleOrLength**,  {% include w3api/param_description.html metodo=_dato parametro="int scaleOrLength" %}
* **SQLType targetSqlType**,  {% include w3api/param_description.html metodo=_dato parametro="SQLType targetSqlType" %}
* **int targetSqlType**,  {% include w3api/param_description.html metodo=_dato parametro="int targetSqlType" %}
* **Object x**,  {% include w3api/param_description.html metodo=_dato parametro="Object x" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int parameterIndex" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[PreparedStatement](/Java/PreparedStatement/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
