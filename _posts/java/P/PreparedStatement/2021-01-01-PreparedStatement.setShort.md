---
title: PreparedStatement.setShort()
permalink: Java/PreparedStatement/setShort
date: 2021-01-11
key: JavaJava.P.PreparedStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setShort" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setShort(int parameterIndex, short x) throws SQLException
~~~

## Parámetros
* **short x**,  {% include w3api/param_description.html metodo=_dato parametro="short x" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int parameterIndex" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[PreparedStatement](/Java/PreparedStatement/)

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
