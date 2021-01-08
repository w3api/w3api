---
title: BasicPermission.BasicPermission()
permalink: Java/BasicPermission/BasicPermission
date: 2021-01-04
key: JavaJava.B.BasicPermission
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicPermission.constructores valor="BasicPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BasicPermission(String name)
public BasicPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BasicPermission](/Java/BasicPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
