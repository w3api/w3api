---
title: Connection.setNetworkTimeout()
permalink: Java/Connection-java-sql/setNetworkTimeout
date: 2021-01-04
key: JavaJava.C.Connection-java-sql
category: java
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
* **int milliseconds**,  {% include w3api/param_description.html metodo=_data parametro="int milliseconds" %}
* **Executor executor**,  {% include w3api/param_description.html metodo=_data parametro="Executor executor" %}

## Excepciones
[SQLException](/Java/SQLException/), [SecurityException](/Java/SecurityException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[Connection](/Java/Connection-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Connection-java-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
