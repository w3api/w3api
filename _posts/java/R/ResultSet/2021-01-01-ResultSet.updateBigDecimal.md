---
title: ResultSet.updateBigDecimal()
permalink: /Java/ResultSet/updateBigDecimal/
date: 2021-01-11
key: Java.R.ResultSet
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="updateBigDecimal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void updateBigDecimal(int columnIndex, BigDecimal x) throws SQLException
void updateBigDecimal(String columnLabel, BigDecimal x) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **BigDecimal x**,  {% include w3api/param_description.html metodo=_dato parametro="BigDecimal x" %}
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
