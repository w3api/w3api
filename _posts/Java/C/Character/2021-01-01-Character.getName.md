---
title: Character.getName()
permalink: /Java/Character/getName/
date: 2021-01-11
key: Java.C.Character
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Character.metodos valor="getName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String getName(int codePoint)
~~~

## Parámetros
* **int codePoint**,  {% include w3api/param_description.html metodo=_dato parametro="int codePoint" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
