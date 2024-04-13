---
title: CookieStore.add()
permalink: /Java/CookieStore/add/
date: 2021-01-11
key: Java.C.CookieStore
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CookieStore.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void add(URI uri, HttpCookie cookie)
~~~

## Parámetros
* **HttpCookie cookie**,  {% include w3api/param_description.html metodo=_dato parametro="HttpCookie cookie" %}
* **URI uri**,  {% include w3api/param_description.html metodo=_dato parametro="URI uri" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CookieStore](/Java/CookieStore/)

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
