---
title: ResultSet.updateClob()
permalink: Java/ResultSet/updateClob
date: 2021-01-04
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
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_data parametro="String columnLabel" %}
* **Clob x**,  {% include w3api/param_description.html metodo=_data parametro="Clob x" %}
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
