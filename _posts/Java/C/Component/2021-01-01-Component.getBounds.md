---
title: Component.getBounds()
permalink: /Java/Component/getBounds/
date: 2021-01-11
key: Java.C.Component
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="getBounds" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Rectangle getBounds()
public Rectangle getBounds(Rectangle rv)
~~~

## Parámetros
* **Rectangle rv**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle rv" %}

## Clase Padre
[Component](/Java/Component/)

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
