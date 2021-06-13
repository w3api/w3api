---
title: ManagementPermission.ManagementPermission()
permalink: /Java/ManagementPermission/ManagementPermission/
date: 2021-01-11
key: Java.M.ManagementPermission
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ManagementPermission.constructores valor="ManagementPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ManagementPermission(String name)
public ManagementPermission(String name, String actions) throws IllegalArgumentException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ManagementPermission](/Java/ManagementPermission/)

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
