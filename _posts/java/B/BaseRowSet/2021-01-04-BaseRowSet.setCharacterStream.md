---
title: BaseRowSet.setCharacterStream()
permalink: Java/BaseRowSet/setCharacterStream
date: 2021-01-04
key: JavaJava.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setCharacterStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setCharacterStream(int parameterIndex, Reader reader) throws SQLException
public void setCharacterStream(int parameterIndex, Reader reader, int length) throws SQLException
public void setCharacterStream(String parameterName, Reader reader) throws SQLException
public void setCharacterStream(String parameterName, Reader reader, int length) throws SQLException
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_data parametro="String parameterName" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_data parametro="Reader reader" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[BaseRowSet](/Java/BaseRowSet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BaseRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
