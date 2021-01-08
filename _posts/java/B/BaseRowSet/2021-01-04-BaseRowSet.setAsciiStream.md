---
title: BaseRowSet.setAsciiStream()
permalink: Java/BaseRowSet/setAsciiStream
date: 2021-01-04
key: JavaJava.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setAsciiStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setAsciiStream(int parameterIndex, InputStream x) throws SQLException
public void setAsciiStream(int parameterIndex, InputStream x, int length) throws SQLException
public void setAsciiStream(String parameterName, InputStream x) throws SQLException
public void setAsciiStream(String parameterName, InputStream x, int length) throws SQLException
~~~

## Parámetros
* **InputStream x**,  {% include w3api/param_description.html metodo=_data parametro="InputStream x" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_data parametro="String parameterName" %}

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
{%- for _ldc in site.data.Java.B.BaseRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
