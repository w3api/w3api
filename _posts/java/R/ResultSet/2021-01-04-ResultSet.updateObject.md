---
title: ResultSet.updateObject()
permalink: Java/ResultSet/updateObject
date: 2021-01-04
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
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}
* **int scaleOrLength**,  {% include w3api/param_description.html metodo=_data parametro="int scaleOrLength" %}
* **Object x**,  {% include w3api/param_description.html metodo=_data parametro="Object x" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_data parametro="String columnLabel" %}
* **SQLType targetSqlType**,  {% include w3api/param_description.html metodo=_data parametro="SQLType targetSqlType" %}

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
{%- for _ldc in site.data.Java.R.ResultSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
