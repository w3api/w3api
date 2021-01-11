---
title: ResultSet.setFetchSize()
permalink: Java/ResultSet/setFetchSize
date: 2021-01-11
key: JavaJava.R.ResultSet
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResultSet.metodos valor="setFetchSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setFetchSize(int rows) throws SQLException
~~~

## Parámetros
* **int rows**,  {% include w3api/param_description.html metodo=_dato parametro="int rows" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
