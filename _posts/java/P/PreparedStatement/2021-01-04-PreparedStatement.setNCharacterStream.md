---
title: PreparedStatement.setNCharacterStream()
permalink: Java/PreparedStatement/setNCharacterStream
date: 2021-01-04
key: JavaJava.P.PreparedStatement
category: java
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
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}
* **long length**,  {% include w3api/param_description.html metodo=_data parametro="long length" %}
* **Reader value**,  {% include w3api/param_description.html metodo=_data parametro="Reader value" %}

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
