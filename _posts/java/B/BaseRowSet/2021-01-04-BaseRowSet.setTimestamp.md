---
title: BaseRowSet.setTimestamp()
permalink: Java/BaseRowSet/setTimestamp
date: 2021-01-04
key: JavaJava.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setTimestamp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTimestamp(int parameterIndex, Timestamp x) throws SQLException
public void setTimestamp(int parameterIndex, Timestamp x, Calendar cal) throws SQLException
public void setTimestamp(String parameterName, Timestamp x) throws SQLException
public void setTimestamp(String parameterName, Timestamp x, Calendar cal) throws SQLException
~~~

## Parámetros
* **Timestamp x**,  {% include w3api/param_description.html metodo=_data parametro="Timestamp x" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}
* **Calendar cal**,  {% include w3api/param_description.html metodo=_data parametro="Calendar cal" %}
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
