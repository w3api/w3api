---
title: ResultSet.updateTimestamp()
permalink: Java/ResultSet/updateTimestamp
date: 2021-01-04
key: JavaJava.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="updateTimestamp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void updateTimestamp(int columnIndex, Timestamp x) throws SQLException
void updateTimestamp(String columnLabel, Timestamp x) throws SQLException
~~~

## Parámetros
* **Timestamp x**,  {% include w3api/param_description.html metodo=_data parametro="Timestamp x" %}
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}
* **String columnLabel**,  {% include w3api/param_description.html metodo=_data parametro="String columnLabel" %}

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
