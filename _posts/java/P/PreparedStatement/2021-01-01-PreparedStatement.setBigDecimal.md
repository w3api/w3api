---
title: PreparedStatement.setBigDecimal()
permalink: /Java/PreparedStatement/setBigDecimal/
date: 2021-01-11
key: Java.P.PreparedStatement
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setBigDecimal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setBigDecimal(int parameterIndex, BigDecimal x) throws SQLException
~~~

## Parámetros
* **BigDecimal x**,  {% include w3api/param_description.html metodo=_dato parametro="BigDecimal x" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int parameterIndex" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[PreparedStatement](/Java/PreparedStatement/)

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
