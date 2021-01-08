---
title: BaseRowSet.setBlob()
permalink: Java/BaseRowSet/setBlob
date: 2021-01-04
key: JavaJava.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setBlob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setBlob(int parameterIndex, InputStream inputStream) throws SQLException
public void setBlob(int parameterIndex, InputStream inputStream, long length) throws SQLException
public void setBlob(int parameterIndex, Blob x) throws SQLException
public void setBlob(String parameterName, InputStream inputStream) throws SQLException
public void setBlob(String parameterName, InputStream inputStream, long length) throws SQLException
public void setBlob(String parameterName, Blob x) throws SQLException
~~~

## Parámetros
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_data parametro="String parameterName" %}
* **Blob x**,  {% include w3api/param_description.html metodo=_data parametro="Blob x" %}
* **InputStream inputStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream inputStream" %}
* **long length**,  {% include w3api/param_description.html metodo=_data parametro="long length" %}

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
