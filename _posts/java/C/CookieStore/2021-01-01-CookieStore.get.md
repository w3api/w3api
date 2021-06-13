---
title: CookieStore.get()
permalink: /Java/CookieStore/get/
date: 2021-01-11
key: Java.C.CookieStore
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CookieStore.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<HttpCookie> get(URI uri)
~~~

## Parámetros
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
