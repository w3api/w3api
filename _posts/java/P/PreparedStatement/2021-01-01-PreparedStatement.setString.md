---
title: PreparedStatement.setString()
permalink: /Java/PreparedStatement/setString/
date: 2021-01-11
key: Java.P.PreparedStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setString(int parameterIndex, String x) throws SQLException
~~~

## Parámetros
* **String x**,  {% include w3api/param_description.html metodo=_dato parametro="String x" %}
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
