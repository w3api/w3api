---
title: Character.isSurrogatePair()
permalink: /Java/Character/isSurrogatePair/
date: 2021-01-11
key: Java.C.Character
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Character.metodos valor="isSurrogatePair" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean isSurrogatePair(char high, char low)
~~~

## Parámetros
* **char high**,  {% include w3api/param_description.html metodo=_dato parametro="char high" %}
* **char low**,  {% include w3api/param_description.html metodo=_dato parametro="char low" %}

## Clase Padre
[Character](/Java/Character/)

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
