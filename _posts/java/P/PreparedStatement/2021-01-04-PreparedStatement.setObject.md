---
title: PreparedStatement.setObject()
permalink: Java/PreparedStatement/setObject
date: 2021-01-04
key: JavaJava.P.PreparedStatement
category: java
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
* **int scaleOrLength**,  {% include w3api/param_description.html metodo=_data parametro="int scaleOrLength" %}
* **Object x**,  {% include w3api/param_description.html metodo=_data parametro="Object x" %}
* **SQLType targetSqlType**,  {% include w3api/param_description.html metodo=_data parametro="SQLType targetSqlType" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}
* **int targetSqlType**,  {% include w3api/param_description.html metodo=_data parametro="int targetSqlType" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[PreparedStatement](/Java/PreparedStatement/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PreparedStatement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
