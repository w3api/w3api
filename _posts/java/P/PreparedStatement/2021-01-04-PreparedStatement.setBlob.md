---
title: PreparedStatement.setBlob()
permalink: Java/PreparedStatement/setBlob
date: 2021-01-04
key: JavaJava.P.PreparedStatement
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
* **InputStream inputStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream inputStream" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}
* **Blob x**,  {% include w3api/param_description.html metodo=_data parametro="Blob x" %}
* **long length**,  {% include w3api/param_description.html metodo=_data parametro="long length" %}

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
{%- for _ldc in site.data.Java.P.PreparedStatement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
