---
title: Connection.nativeSQL()
permalink: Java/Connection-java-sql/nativeSQL
date: 2021-01-04
key: JavaJava.C.Connection-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="nativeSQL" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String nativeSQL(String sql) throws SQLException
~~~

## Parámetros
* **String sql**,  {% include w3api/param_description.html metodo=_data parametro="String sql" %}

## Excepciones
[SQLException](/Java/SQLException/)

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
