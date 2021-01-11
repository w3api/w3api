---
title: BaseRowSet.setSQLXML()
permalink: Java/BaseRowSet/setSQLXML
date: 2021-01-11
key: JavaJava.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setSQLXML" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSQLXML(int parameterIndex, SQLXML xmlObject) throws SQLException
public void setSQLXML(String parameterName, SQLXML xmlObject) throws SQLException
~~~

## Parámetros
* **SQLXML xmlObject**,  {% include w3api/param_description.html metodo=_dato parametro="SQLXML xmlObject" %}
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
