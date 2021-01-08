---
title: CallableStatement.setObject()
permalink: Java/CallableStatement/setObject
date: 2021-01-04
key: JavaJava.C.CallableStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="setObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setObject(String parameterName, Object x) throws SQLException
void setObject(String parameterName, Object x, int targetSqlType) throws SQLException
void setObject(String parameterName, Object x, int targetSqlType, int scale) throws SQLException
default void setObject(String parameterName, Object x, SQLType targetSqlType) throws SQLException
default void setObject(String parameterName, Object x, SQLType targetSqlType, int scaleOrLength) throws SQLException
~~~

## Parámetros
* **int scaleOrLength**,  {% include w3api/param_description.html metodo=_data parametro="int scaleOrLength" %}
* **Object x**,  {% include w3api/param_description.html metodo=_data parametro="Object x" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_data parametro="String parameterName" %}
* **int scale**,  {% include w3api/param_description.html metodo=_data parametro="int scale" %}
* **SQLType targetSqlType**,  {% include w3api/param_description.html metodo=_data parametro="SQLType targetSqlType" %}
* **int targetSqlType**,  {% include w3api/param_description.html metodo=_data parametro="int targetSqlType" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[CallableStatement](/Java/CallableStatement/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CallableStatement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
