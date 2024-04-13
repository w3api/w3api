---
title: CallableStatement.setBlob()
permalink: /Java/CallableStatement/setBlob/
date: 2021-01-11
key: Java.C.CallableStatement
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="setBlob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setBlob(String parameterName, InputStream inputStream) throws SQLException
void setBlob(String parameterName, InputStream inputStream, long length) throws SQLException
void setBlob(String parameterName, Blob x) throws SQLException
~~~

## Parámetros
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **InputStream inputStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream inputStream" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_dato parametro="String parameterName" %}
* **Blob x**,  {% include w3api/param_description.html metodo=_dato parametro="Blob x" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[CallableStatement](/Java/CallableStatement/)

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
