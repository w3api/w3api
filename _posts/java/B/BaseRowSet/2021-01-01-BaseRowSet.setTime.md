---
title: BaseRowSet.setTime()
permalink: /Java/BaseRowSet/setTime/
date: 2021-01-11
key: Java.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTime(int parameterIndex, Time x) throws SQLException
public void setTime(int parameterIndex, Time x, Calendar cal) throws SQLException
public void setTime(String parameterName, Time x) throws SQLException
public void setTime(String parameterName, Time x, Calendar cal) throws SQLException
~~~

## Parámetros
* **Calendar cal**,  {% include w3api/param_description.html metodo=_dato parametro="Calendar cal" %}
* **Time x**,  {% include w3api/param_description.html metodo=_dato parametro="Time x" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_dato parametro="String parameterName" %}
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
