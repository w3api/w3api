---
title: Character.UnicodeBlock.of()
permalink: Java/Character/UnicodeBlock/of
date: 2021-01-11
key: JavaJava.C.Character.UnicodeBlock
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Character.UnicodeBlock.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Character.UnicodeBlock of(char c)
public static Character.UnicodeBlock of(int codePoint)
~~~

## Parámetros
* **int codePoint**,  {% include w3api/param_description.html metodo=_dato parametro="int codePoint" %}
* **char c**,  {% include w3api/param_description.html metodo=_dato parametro="char c" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Character.UnicodeBlock](/Java/Character/UnicodeBlock/)

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
