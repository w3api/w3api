---
title: ResultSet.getBigDecimal()
permalink: Java/ResultSet/getBigDecimal
date: 2021-01-04
key: JavaJava.R.ResultSet
category: java
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
* **String columnLabel**,  {% include w3api/param_description.html metodo=_data parametro="String columnLabel" %}
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}
* **int scale**,  {% include w3api/param_description.html metodo=_data parametro="int scale" %}

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
