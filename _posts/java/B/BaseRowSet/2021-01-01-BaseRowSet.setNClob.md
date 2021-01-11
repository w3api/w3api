---
title: BaseRowSet.setNClob()
permalink: Java/BaseRowSet/setNClob
date: 2021-01-11
key: JavaJava.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setNClob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setNClob(int parameterIndex, Reader reader) throws SQLException
public void setNClob(int parameterIndex, Reader reader, long length) throws SQLException
public void setNClob(int parameterIndex, NClob value) throws SQLException
public void setNClob(String parameterName, Reader reader) throws SQLException
public void setNClob(String parameterName, Reader reader, long length) throws SQLException
public void setNClob(String parameterName, NClob value) throws SQLException
~~~

## Parámetros
* **NClob value**,  {% include w3api/param_description.html metodo=_dato parametro="NClob value" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_dato parametro="String parameterName" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int parameterIndex" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
