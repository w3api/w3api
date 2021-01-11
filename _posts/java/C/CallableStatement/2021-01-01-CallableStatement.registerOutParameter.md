---
title: CallableStatement.registerOutParameter()
permalink: Java/CallableStatement/registerOutParameter
date: 2021-01-11
key: JavaJava.C.CallableStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="registerOutParameter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void registerOutParameter(int parameterIndex, int sqlType) throws SQLException
void registerOutParameter(int parameterIndex, int sqlType, int scale) throws SQLException
void registerOutParameter(int parameterIndex, int sqlType, String typeName) throws SQLException
default void registerOutParameter(int parameterIndex, SQLType sqlType) throws SQLException
default void registerOutParameter(int parameterIndex, SQLType sqlType, int scale) throws SQLException
default void registerOutParameter(int parameterIndex, SQLType sqlType, String typeName) throws SQLException
void registerOutParameter(String parameterName, int sqlType) throws SQLException
void registerOutParameter(String parameterName, int sqlType, int scale) throws SQLException
void registerOutParameter(String parameterName, int sqlType, String typeName) throws SQLException
default void registerOutParameter(String parameterName, SQLType sqlType) throws SQLException
default void registerOutParameter(String parameterName, SQLType sqlType, int scale) throws SQLException
default void registerOutParameter(String parameterName, SQLType sqlType, String typeName) throws SQLException
~~~

## Parámetros
* **String parameterName**,  {% include w3api/param_description.html metodo=_dato parametro="String parameterName" %}
* **String typeName**,  {% include w3api/param_description.html metodo=_dato parametro="String typeName" %}
* **SQLType sqlType**,  {% include w3api/param_description.html metodo=_dato parametro="SQLType sqlType" %}
* **int sqlType**,  {% include w3api/param_description.html metodo=_dato parametro="int sqlType" %}
* **int scale**,  {% include w3api/param_description.html metodo=_dato parametro="int scale" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int parameterIndex" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
