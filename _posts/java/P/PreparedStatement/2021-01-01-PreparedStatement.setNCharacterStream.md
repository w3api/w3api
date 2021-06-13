---
title: PreparedStatement.setNCharacterStream()
permalink: /Java/PreparedStatement/setNCharacterStream/
date: 2021-01-11
key: Java.P.PreparedStatement
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setNCharacterStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setNCharacterStream(int parameterIndex, Reader value) throws SQLException
void setNCharacterStream(int parameterIndex, Reader value, long length) throws SQLException
~~~

## Parámetros
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **Reader value**,  {% include w3api/param_description.html metodo=_dato parametro="Reader value" %}
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
