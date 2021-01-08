---
title: PreparedStatement.setTimestamp()
permalink: Java/PreparedStatement/setTimestamp
date: 2021-01-04
key: JavaJava.P.PreparedStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setTimestamp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setTimestamp(int parameterIndex, Timestamp x) throws SQLException
void setTimestamp(int parameterIndex, Timestamp x, Calendar cal) throws SQLException
~~~

## Parámetros
* **Timestamp x**,  {% include w3api/param_description.html metodo=_data parametro="Timestamp x" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}
* **Calendar cal**,  {% include w3api/param_description.html metodo=_data parametro="Calendar cal" %}

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
