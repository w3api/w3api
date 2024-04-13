---
title: ResultSet.updateNClob()
permalink: /Java/ResultSet/updateNClob/
date: 2021-01-11
key: Java.R.ResultSet
category: Java
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
* **NClob nClob**,  {% include w3api/param_description.html metodo=_dato parametro="NClob nClob" %}
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String columnLabel" %}
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}

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
