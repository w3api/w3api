---
title: CallableStatement.getClob()
permalink: /Java/CallableStatement/getClob/
date: 2021-01-11
key: Java.C.CallableStatement
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="getClob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Clob getClob(int parameterIndex) throws SQLException
Clob getClob(String parameterName) throws SQLException
~~~

## Parámetros
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
