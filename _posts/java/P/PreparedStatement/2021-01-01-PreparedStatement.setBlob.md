---
title: PreparedStatement.setBlob()
permalink: /Java/PreparedStatement/setBlob/
date: 2021-01-11
key: Java.P.PreparedStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setBlob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setBlob(int parameterIndex, InputStream inputStream) throws SQLException
void setBlob(int parameterIndex, InputStream inputStream, long length) throws SQLException
void setBlob(int parameterIndex, Blob x) throws SQLException
~~~

## Parámetros
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **InputStream inputStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream inputStream" %}
* **Blob x**,  {% include w3api/param_description.html metodo=_dato parametro="Blob x" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int parameterIndex" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[PreparedStatement](/Java/PreparedStatement/)

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
