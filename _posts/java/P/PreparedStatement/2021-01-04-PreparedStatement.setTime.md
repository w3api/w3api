---
title: PreparedStatement.setTime()
permalink: Java/PreparedStatement/setTime
date: 2021-01-04
key: JavaJava.P.PreparedStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setTime(int parameterIndex, Time x) throws SQLException
void setTime(int parameterIndex, Time x, Calendar cal) throws SQLException
~~~

## Parámetros
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}
* **Calendar cal**,  {% include w3api/param_description.html metodo=_data parametro="Calendar cal" %}
* **Time x**,  {% include w3api/param_description.html metodo=_data parametro="Time x" %}

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
{%- for _ldc in site.data.Java.P.PreparedStatement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
