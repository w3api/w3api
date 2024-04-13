---
title: CookieHandler.setDefault()
permalink: /Java/CookieHandler/setDefault/
date: 2021-01-11
key: Java.C.CookieHandler
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CookieHandler.metodos valor="setDefault" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setDefault(CookieHandler cHandler)
~~~

## Parámetros
* **CookieHandler cHandler**,  {% include w3api/param_description.html metodo=_dato parametro="CookieHandler cHandler" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[CookieHandler](/Java/CookieHandler/)

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
