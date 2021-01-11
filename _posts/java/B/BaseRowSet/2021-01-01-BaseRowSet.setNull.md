---
title: BaseRowSet.setNull()
permalink: Java/BaseRowSet/setNull
date: 2021-01-11
key: JavaJava.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setNull" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setNull(int parameterIndex, int sqlType) throws SQLException
public void setNull(int parameterIndex, int sqlType, String typeName) throws SQLException
public void setNull(String parameterName, int sqlType) throws SQLException
public void setNull(String parameterName, int sqlType, String typeName) throws SQLException
~~~

## Parámetros
* **String parameterName**,  {% include w3api/param_description.html metodo=_dato parametro="String parameterName" %}
* **int sqlType**,  {% include w3api/param_description.html metodo=_dato parametro="int sqlType" %}
* **String typeName**,  {% include w3api/param_description.html metodo=_dato parametro="String typeName" %}
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
