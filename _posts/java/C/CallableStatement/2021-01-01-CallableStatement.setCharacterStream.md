---
title: CallableStatement.setCharacterStream()
permalink: Java/CallableStatement/setCharacterStream
date: 2021-01-11
key: JavaJava.C.CallableStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="setCharacterStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setCharacterStream(String parameterName, Reader reader) throws SQLException
void setCharacterStream(String parameterName, Reader reader, int length) throws SQLException
void setCharacterStream(String parameterName, Reader reader, long length) throws SQLException
~~~

## Parámetros
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_dato parametro="String parameterName" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

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
