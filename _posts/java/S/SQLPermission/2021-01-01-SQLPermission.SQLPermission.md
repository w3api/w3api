---
title: SQLPermission.SQLPermission()
permalink: Java/SQLPermission/SQLPermission
date: 2021-01-11
key: JavaJava.S.SQLPermission
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLPermission.constructores valor="SQLPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLPermission(String name)
public SQLPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SQLPermission](/Java/SQLPermission/)

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
