---
title: ResultSet.getBigDecimal()
permalink: /Java/ResultSet/getBigDecimal/
date: 2021-01-11
key: Java.R.ResultSet
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="getBigDecimal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
BigDecimal getBigDecimal(int columnIndex) throws SQLException
@Deprecated(since="1.2") BigDecimal getBigDecimal(int columnIndex, int scale) throws SQLException
BigDecimal getBigDecimal(String columnLabel) throws SQLException
@Deprecated(since="1.2") BigDecimal getBigDecimal(String columnLabel, int scale) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **int scale**,  {% include w3api/param_description.html metodo=_dato parametro="int scale" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String columnLabel" %}

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
