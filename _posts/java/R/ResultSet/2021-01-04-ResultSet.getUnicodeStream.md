---
title: ResultSet.getUnicodeStream()
permalink: Java/ResultSet/getUnicodeStream
date: 2021-01-04
key: JavaJava.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="getUnicodeStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="1.2") InputStream getUnicodeStream(int columnIndex) throws SQLException
@Deprecated(since="1.2") InputStream getUnicodeStream(String columnLabel) throws SQLException
~~~

## Parámetros
* **String columnLabel**,  {% include w3api/param_description.html metodo=_data parametro="String columnLabel" %}
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}

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
