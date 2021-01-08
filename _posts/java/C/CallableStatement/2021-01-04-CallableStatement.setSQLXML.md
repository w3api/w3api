---
title: CallableStatement.setSQLXML()
permalink: Java/CallableStatement/setSQLXML
date: 2021-01-04
key: JavaJava.C.CallableStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="setSQLXML" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setSQLXML(String parameterName, SQLXML xmlObject) throws SQLException
~~~

## Parámetros
* **String parameterName**,  {% include w3api/param_description.html metodo=_data parametro="String parameterName" %}
* **SQLXML xmlObject**,  {% include w3api/param_description.html metodo=_data parametro="SQLXML xmlObject" %}

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
{%- for _ldc in site.data.Java.C.CallableStatement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
