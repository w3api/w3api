---
title: ResultSet.updateCharacterStream()
permalink: Java/ResultSet/updateCharacterStream
date: 2021-01-04
key: JavaJava.R.ResultSet
category: java
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
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_data parametro="String columnLabel" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **Reader x**,  {% include w3api/param_description.html metodo=_data parametro="Reader x" %}
* **long length**,  {% include w3api/param_description.html metodo=_data parametro="long length" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_data parametro="Reader reader" %}

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
