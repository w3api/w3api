---
title: CallableStatement.setNCharacterStream()
permalink: /Java/CallableStatement/setNCharacterStream/
date: 2021-01-11
key: Java.C.CallableStatement
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="setNCharacterStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setNCharacterStream(String parameterName, Reader value) throws SQLException
void setNCharacterStream(String parameterName, Reader value, long length) throws SQLException
~~~

## Parámetros
* **Reader value**,  {% include w3api/param_description.html metodo=_dato parametro="Reader value" %}
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_dato parametro="String parameterName" %}

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
