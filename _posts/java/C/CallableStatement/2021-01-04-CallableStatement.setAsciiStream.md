---
title: CallableStatement.setAsciiStream()
permalink: Java/CallableStatement/setAsciiStream
date: 2021-01-04
key: JavaJava.C.CallableStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="setAsciiStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setAsciiStream(String parameterName, InputStream x) throws SQLException
void setAsciiStream(String parameterName, InputStream x, int length) throws SQLException
void setAsciiStream(String parameterName, InputStream x, long length) throws SQLException
~~~

## Parámetros
* **InputStream x**,  {% include w3api/param_description.html metodo=_data parametro="InputStream x" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_data parametro="String parameterName" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
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
