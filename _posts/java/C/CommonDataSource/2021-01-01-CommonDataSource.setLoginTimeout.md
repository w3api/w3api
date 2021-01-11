---
title: CommonDataSource.setLoginTimeout()
permalink: Java/CommonDataSource/setLoginTimeout
date: 2021-01-11
key: JavaJava.C.CommonDataSource
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CommonDataSource.metodos valor="setLoginTimeout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setLoginTimeout(int seconds) throws SQLException
~~~

## Parámetros
* **int seconds**,  {% include w3api/param_description.html metodo=_dato parametro="int seconds" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[CommonDataSource](/Java/CommonDataSource/)

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
