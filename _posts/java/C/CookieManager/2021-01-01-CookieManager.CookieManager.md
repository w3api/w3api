---
title: CookieManager.CookieManager()
permalink: /Java/CookieManager/CookieManager/
date: 2021-01-11
key: Java.C.CookieManager
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CookieManager.constructores valor="CookieManager" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CookieManager()
public CookieManager(CookieStore store, CookiePolicy cookiePolicy)
~~~

## Parámetros
* **CookiePolicy cookiePolicy**,  {% include w3api/param_description.html metodo=_dato parametro="CookiePolicy cookiePolicy" %}
* **CookieStore store**,  {% include w3api/param_description.html metodo=_dato parametro="CookieStore store" %}

## Clase Padre
[CookieManager](/Java/CookieManager/)

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
