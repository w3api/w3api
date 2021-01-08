---
title: ManagementPermission.ManagementPermission()
permalink: Java/ManagementPermission/ManagementPermission
date: 2021-01-04
key: JavaJava.M.ManagementPermission
category: java
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
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ManagementPermission](/Java/ManagementPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ManagementPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
