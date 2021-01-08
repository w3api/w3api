---
title: PreparedStatement.setBoolean()
permalink: Java/PreparedStatement/setBoolean
date: 2021-01-04
key: JavaJava.P.PreparedStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="setBoolean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setBoolean(int parameterIndex, boolean x) throws SQLException
~~~

## Parámetros
* **boolean x**,  {% include w3api/param_description.html metodo=_data parametro="boolean x" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_data parametro="int parameterIndex" %}

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
