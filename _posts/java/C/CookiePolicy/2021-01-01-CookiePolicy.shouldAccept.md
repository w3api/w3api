---
title: CookiePolicy.shouldAccept()
permalink: /Java/CookiePolicy/shouldAccept/
date: 2021-01-11
key: Java.C.CookiePolicy
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CookiePolicy.metodos valor="shouldAccept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean shouldAccept(URI uri, HttpCookie cookie)
~~~

## Parámetros
* **HttpCookie cookie**,  {% include w3api/param_description.html metodo=_dato parametro="HttpCookie cookie" %}
* **URI uri**,  {% include w3api/param_description.html metodo=_dato parametro="URI uri" %}

## Clase Padre
[CookiePolicy](/Java/CookiePolicy/)

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
