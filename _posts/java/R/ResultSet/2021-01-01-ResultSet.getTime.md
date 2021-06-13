---
title: ResultSet.getTime()
permalink: Java/ResultSet/getTime
date: 2021-01-11
key: Java.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="getTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Time getTime(int columnIndex) throws SQLException
Time getTime(int columnIndex, Calendar cal) throws SQLException
Time getTime(String columnLabel) throws SQLException
Time getTime(String columnLabel, Calendar cal) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **Calendar cal**,  {% include w3api/param_description.html metodo=_dato parametro="Calendar cal" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_dato parametro="String columnLabel" %}

## Excepciones
[SQLException](/Java/SQLException/)

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
