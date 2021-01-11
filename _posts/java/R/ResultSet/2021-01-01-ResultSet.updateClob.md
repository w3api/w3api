---
title: ResultSet.updateClob()
permalink: Java/ResultSet/updateClob
date: 2021-01-11
key: JavaJava.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="updateClob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void updateClob(int columnIndex, Reader reader) throws SQLException
void updateClob(int columnIndex, Reader reader, long length) throws SQLException
void updateClob(int columnIndex, Clob x) throws SQLException
void updateClob(String columnLabel, Reader reader) throws SQLException
void updateClob(String columnLabel, Reader reader, long length) throws SQLException
void updateClob(String columnLabel, Clob x) throws SQLException
~~~

## Parámetros
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String columnLabel" %}
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **Clob x**,  {% include w3api/param_description.html metodo=_dato parametro="Clob x" %}

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
