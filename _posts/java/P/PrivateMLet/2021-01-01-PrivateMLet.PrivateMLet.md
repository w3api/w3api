---
title: PrivateMLet.PrivateMLet()
permalink: /Java/PrivateMLet/PrivateMLet/
date: 2021-01-11
key: Java.P.PrivateMLet
category: Java
tags: ['java se', 'javax.management.loading', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrivateMLet.constructores valor="PrivateMLet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrivateMLet(URL[] urls, boolean delegateToCLR)
public PrivateMLet(URL[] urls, ClassLoader parent, boolean delegateToCLR)
public PrivateMLet(URL[] urls, ClassLoader parent, URLStreamHandlerFactory factory, boolean delegateToCLR)
~~~

## Parámetros
* **URL[] urls**,  {% include w3api/param_description.html metodo=_dato parametro="URL[] urls" %}
* **ClassLoader parent**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader parent" %}
* **URLStreamHandlerFactory factory**,  {% include w3api/param_description.html metodo=_dato parametro="URLStreamHandlerFactory factory" %}
* **boolean delegateToCLR**,  {% include w3api/param_description.html metodo=_dato parametro="boolean delegateToCLR" %}

## Clase Padre
[PrivateMLet](/Java/PrivateMLet/)

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
