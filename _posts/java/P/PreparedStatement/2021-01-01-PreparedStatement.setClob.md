---
title: PreparedStatement.setClob()
permalink: /Java/PreparedStatement/setClob/
date: 2021-01-11
key: Java.P.PreparedStatement
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setClob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setClob(int parameterIndex, Reader reader) throws SQLException
void setClob(int parameterIndex, Reader reader, long length) throws SQLException
void setClob(int parameterIndex, Clob x) throws SQLException
~~~

## Parámetros
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **Clob x**,  {% include w3api/param_description.html metodo=_dato parametro="Clob x" %}
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
