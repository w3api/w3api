---
title: Character.UnicodeScript.of()
permalink: /Java/Character/UnicodeScript/of/
date: 2021-01-11
key: Java.C.Character.UnicodeScript
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Character.UnicodeScript.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Character.UnicodeScript of(int codePoint)
~~~

## Parámetros
* **int codePoint**,  {% include w3api/param_description.html metodo=_dato parametro="int codePoint" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Character.UnicodeScript](/Java/Character/UnicodeScript/)

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
