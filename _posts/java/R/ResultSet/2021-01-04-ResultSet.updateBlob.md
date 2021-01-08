---
title: ResultSet.updateBlob()
permalink: Java/ResultSet/updateBlob
date: 2021-01-04
key: JavaJava.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="updateBlob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void updateBlob(int columnIndex, InputStream inputStream) throws SQLException
void updateBlob(int columnIndex, InputStream inputStream, long length) throws SQLException
void updateBlob(int columnIndex, Blob x) throws SQLException
void updateBlob(String columnLabel, InputStream inputStream) throws SQLException
void updateBlob(String columnLabel, InputStream inputStream, long length) throws SQLException
void updateBlob(String columnLabel, Blob x) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_data parametro="String columnLabel" %}
* **Blob x**,  {% include w3api/param_description.html metodo=_data parametro="Blob x" %}
* **InputStream inputStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream inputStream" %}
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
