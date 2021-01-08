---
title: CallableStatement.setBlob()
permalink: Java/CallableStatement/setBlob
date: 2021-01-04
key: JavaJava.C.CallableStatement
category: java
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
* **InputStream inputStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream inputStream" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_data parametro="String parameterName" %}
* **Blob x**,  {% include w3api/param_description.html metodo=_data parametro="Blob x" %}
* **long length**,  {% include w3api/param_description.html metodo=_data parametro="long length" %}

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
{%- for _ldc in site.data.Java.C.CallableStatement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
