---
title: Connection.setAutoCommit()
permalink: /Java/Connection-java-sql/setAutoCommit/
date: 2021-01-11
key: Java.C.Connection-java-sql
category: Java
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
* **boolean autoCommit**,  {% include w3api/param_description.html metodo=_dato parametro="boolean autoCommit" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[Connection](/Java/Connection-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
