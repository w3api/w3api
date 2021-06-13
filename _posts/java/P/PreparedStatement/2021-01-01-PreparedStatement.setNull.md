---
title: PreparedStatement.setNull()
permalink: /Java/PreparedStatement/setNull/
date: 2021-01-11
key: Java.P.PreparedStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setNull" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setNull(int parameterIndex, int sqlType) throws SQLException
void setNull(int parameterIndex, int sqlType, String typeName) throws SQLException
~~~

## Parámetros
* **int sqlType**,  {% include w3api/param_description.html metodo=_dato parametro="int sqlType" %}
* **String typeName**,  {% include w3api/param_description.html metodo=_dato parametro="String typeName" %}
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
