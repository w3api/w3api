---
title: BaseRowSet.setObject()
permalink: /Java/BaseRowSet/setObject/
date: 2021-01-11
key: Java.B.BaseRowSet
category: Java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setObject(int parameterIndex, Object x) throws SQLException
public void setObject(int parameterIndex, Object x, int targetSqlType) throws SQLException
public void setObject(int parameterIndex, Object x, int targetSqlType, int scale) throws SQLException
public void setObject(String parameterName, Object x) throws SQLException
public void setObject(String parameterName, Object x, int targetSqlType) throws SQLException
public void setObject(String parameterName, Object x, int targetSqlType, int scale) throws SQLException
~~~

## Parámetros
* **String parameterName**,  {% include w3api/param_description.html metodo=_dato parametro="String parameterName" %}
* **int targetSqlType**,  {% include w3api/param_description.html metodo=_dato parametro="int targetSqlType" %}
* **int scale**,  {% include w3api/param_description.html metodo=_dato parametro="int scale" %}
* **Object x**,  {% include w3api/param_description.html metodo=_dato parametro="Object x" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int parameterIndex" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[BaseRowSet](/Java/BaseRowSet/)

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
