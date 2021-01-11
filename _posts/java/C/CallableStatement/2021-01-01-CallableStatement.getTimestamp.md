---
title: CallableStatement.getTimestamp()
permalink: Java/CallableStatement/getTimestamp
date: 2021-01-11
key: JavaJava.C.CallableStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="getTimestamp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Timestamp getTimestamp(int parameterIndex) throws SQLException
Timestamp getTimestamp(int parameterIndex, Calendar cal) throws SQLException
Timestamp getTimestamp(String parameterName) throws SQLException
Timestamp getTimestamp(String parameterName, Calendar cal) throws SQLException
~~~

## Parámetros
* **Calendar cal**,  {% include w3api/param_description.html metodo=_dato parametro="Calendar cal" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_dato parametro="String parameterName" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int parameterIndex" %}

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
