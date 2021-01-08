---
title: ResultSet.updateBinaryStream()
permalink: Java/ResultSet/updateBinaryStream
date: 2021-01-04
key: JavaJava.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="updateBinaryStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void updateBinaryStream(int columnIndex, InputStream x) throws SQLException
void updateBinaryStream(int columnIndex, InputStream x, int length) throws SQLException
void updateBinaryStream(int columnIndex, InputStream x, long length) throws SQLException
void updateBinaryStream(String columnLabel, InputStream x) throws SQLException
void updateBinaryStream(String columnLabel, InputStream x, int length) throws SQLException
void updateBinaryStream(String columnLabel, InputStream x, long length) throws SQLException
~~~

## Parámetros
* **InputStream x**,  {% include w3api/param_description.html metodo=_data parametro="InputStream x" %}
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_data parametro="String columnLabel" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **long length**,  {% include w3api/param_description.html metodo=_data parametro="long length" %}

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
