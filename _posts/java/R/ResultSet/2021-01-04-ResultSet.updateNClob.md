---
title: ResultSet.updateNClob()
permalink: Java/ResultSet/updateNClob
date: 2021-01-04
key: JavaJava.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="updateNClob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void updateNClob(int columnIndex, Reader reader) throws SQLException
void updateNClob(int columnIndex, Reader reader, long length) throws SQLException
void updateNClob(int columnIndex, NClob nClob) throws SQLException
void updateNClob(String columnLabel, Reader reader) throws SQLException
void updateNClob(String columnLabel, Reader reader, long length) throws SQLException
void updateNClob(String columnLabel, NClob nClob) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_data parametro="String columnLabel" %}
* **NClob nClob**,  {% include w3api/param_description.html metodo=_data parametro="NClob nClob" %}
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
