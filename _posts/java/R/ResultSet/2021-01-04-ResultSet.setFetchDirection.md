---
title: ResultSet.setFetchDirection()
permalink: Java/ResultSet/setFetchDirection
date: 2021-01-04
key: JavaJava.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="setFetchDirection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setFetchDirection(int direction) throws SQLException
~~~

## Parámetros
* **int direction**,  {% include w3api/param_description.html metodo=_data parametro="int direction" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[ResultSet](/Java/ResultSet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResultSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
