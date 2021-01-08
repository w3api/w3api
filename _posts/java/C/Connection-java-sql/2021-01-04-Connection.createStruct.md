---
title: Connection.createStruct()
permalink: Java/Connection-java-sql/createStruct
date: 2021-01-04
key: JavaJava.C.Connection-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="createStruct" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Struct createStruct(String typeName, Object[] attributes) throws SQLException
~~~

## Parámetros
* **Object[] attributes**,  {% include w3api/param_description.html metodo=_data parametro="Object[] attributes" %}
* **String typeName**,  {% include w3api/param_description.html metodo=_data parametro="String typeName" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

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
