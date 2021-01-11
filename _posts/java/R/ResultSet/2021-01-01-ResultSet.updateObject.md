---
title: ResultSet.updateObject()
permalink: Java/ResultSet/updateObject
date: 2021-01-11
key: JavaJava.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="updateObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void updateObject(int columnIndex, Object x) throws SQLException
void updateObject(int columnIndex, Object x, int scaleOrLength) throws SQLException
default void updateObject(int columnIndex, Object x, SQLType targetSqlType) throws SQLException
default void updateObject(int columnIndex, Object x, SQLType targetSqlType, int scaleOrLength) throws SQLException
void updateObject(String columnLabel, Object x) throws SQLException
void updateObject(String columnLabel, Object x, int scaleOrLength) throws SQLException
default void updateObject(String columnLabel, Object x, SQLType targetSqlType) throws SQLException
default void updateObject(String columnLabel, Object x, SQLType targetSqlType, int scaleOrLength) throws SQLException
~~~

## Parámetros
* **int scaleOrLength**,  {% include w3api/param_description.html metodo=_dato parametro="int scaleOrLength" %}
* **SQLType targetSqlType**,  {% include w3api/param_description.html metodo=_dato parametro="SQLType targetSqlType" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String columnLabel" %}
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **Object x**,  {% include w3api/param_description.html metodo=_dato parametro="Object x" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[ResultSet](/Java/ResultSet/)

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
