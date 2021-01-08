---
title: BaseRowSet.setFloat()
permalink: Java/BaseRowSet/setFloat
date: 2021-01-04
key: JavaJava.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setFloat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFloat(int parameterIndex, float x) throws SQLException
public void setFloat(String parameterName, float x) throws SQLException
~~~

## Parámetros
* **float x**,  {% include w3api/param_description.html metodo=_data parametro="float x" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_data parametro="String parameterName" %}

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
