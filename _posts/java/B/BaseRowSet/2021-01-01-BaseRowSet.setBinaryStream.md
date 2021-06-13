---
title: BaseRowSet.setBinaryStream()
permalink: /Java/BaseRowSet/setBinaryStream/
date: 2021-01-11
key: Java.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setBinaryStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setBinaryStream(int parameterIndex, InputStream x) throws SQLException
public void setBinaryStream(int parameterIndex, InputStream x, int length) throws SQLException
public void setBinaryStream(String parameterName, InputStream x) throws SQLException
public void setBinaryStream(String parameterName, InputStream x, int length) throws SQLException
~~~

## Parámetros
* **InputStream x**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream x" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_dato parametro="String parameterName" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
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
