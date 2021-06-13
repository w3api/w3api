---
title: Connection.setNetworkTimeout()
permalink: /Java/Connection-java-sql/setNetworkTimeout/
date: 2021-01-11
key: Java.C.Connection-java-sql
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="setNetworkTimeout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setNetworkTimeout(Executor executor, int milliseconds) throws SQLException
~~~

## Parámetros
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}
* **int milliseconds**,  {% include w3api/param_description.html metodo=_dato parametro="int milliseconds" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[Connection](/Java/Connection-java-sql/)

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
