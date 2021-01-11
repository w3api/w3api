---
title: Statement.setFetchDirection()
permalink: Java/Statement-java-sql/setFetchDirection
date: 2021-01-11
key: JavaJava.S.Statement-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-sql.metodos valor="setFetchDirection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setFetchDirection(int direction) throws SQLException
~~~

## Parámetros
* **int direction**,  {% include w3api/param_description.html metodo=_dato parametro="int direction" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[Statement](/Java/Statement-java-sql/)

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
