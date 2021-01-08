---
title: CallableStatement.getObject()
permalink: Java/CallableStatement/getObject
date: 2021-01-04
key: JavaJava.C.CallableStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallableStatement.metodos valor="getObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getObject(int parameterIndex) throws SQLException
<T> T getObject(int parameterIndex, Class<T> type)
Object getObject(int parameterIndex, Map<String,Class<?>> map) throws SQLException
Object getObject(String parameterName) throws SQLException
<T> T getObject(String parameterName, Class<T> type)
Object getObject(String parameterName, Map<String,Class<?>> map) throws SQLException
~~~

## Parámetros
* **Class&lt;T&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> type" %}
* **Class&lt;?&gt;&gt; map**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>> map" %}
* **String parameterName**,  {% include w3api/param_description.html metodo=_data parametro="String parameterName" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}

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
