---
title: ReflectPermission.ReflectPermission()
permalink: Java/ReflectPermission/ReflectPermission
date: 2021-01-04
key: JavaJava.R.ReflectPermission
category: java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReflectPermission.constructores valor="ReflectPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ReflectPermission(String name)
public ReflectPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ReflectPermission](/Java/ReflectPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReflectPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
