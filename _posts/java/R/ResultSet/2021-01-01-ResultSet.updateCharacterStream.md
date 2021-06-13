---
title: ResultSet.updateCharacterStream()
permalink: /Java/ResultSet/updateCharacterStream/
date: 2021-01-11
key: Java.R.ResultSet
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="updateCharacterStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void updateCharacterStream(int columnIndex, Reader x) throws SQLException
void updateCharacterStream(int columnIndex, Reader x, int length) throws SQLException
void updateCharacterStream(int columnIndex, Reader x, long length) throws SQLException
void updateCharacterStream(String columnLabel, Reader reader) throws SQLException
void updateCharacterStream(String columnLabel, Reader reader, int length) throws SQLException
void updateCharacterStream(String columnLabel, Reader reader, long length) throws SQLException
~~~

## Parámetros
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String columnLabel" %}
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **Reader x**,  {% include w3api/param_description.html metodo=_dato parametro="Reader x" %}

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
