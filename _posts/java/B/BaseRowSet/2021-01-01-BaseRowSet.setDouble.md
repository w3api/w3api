---
title: BaseRowSet.setDouble()
permalink: /Java/BaseRowSet/setDouble/
date: 2021-01-11
key: Java.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setDouble(int parameterIndex, double x) throws SQLException
public void setDouble(String parameterName, double x) throws SQLException
~~~

## Parámetros
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
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
