---
title: ResultSet.getObject()
permalink: Java/ResultSet/getObject
date: 2021-01-11
key: Java.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="getObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getObject(int columnIndex) throws SQLException
<T> T getObject(int columnIndex, Class<T> type)
Object getObject(int columnIndex, Map<String,Class<?>> map) throws SQLException
Object getObject(String columnLabel) throws SQLException
<T> T getObject(String columnLabel, Class<T> type)
Object getObject(String columnLabel, Map<String,Class<?>> map) throws SQLException
~~~

## Parámetros
* **Class&lt;T&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> type" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String columnLabel" %}
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **Class&lt;?&gt;&gt; map**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>> map" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

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
