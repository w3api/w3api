---
title: Connection.setAutoCommit()
permalink: Java/Connection-java-sql/setAutoCommit
date: 2021-01-04
key: JavaJava.C.Connection-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="setAutoCommit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setAutoCommit(boolean autoCommit) throws SQLException
~~~

## Parámetros
* **boolean autoCommit**,  {% include w3api/param_description.html metodo=_data parametro="boolean autoCommit" %}

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
