---
title: Character.toLowerCase()
permalink: Java/Character/toLowerCase
date: 2021-01-04
key: JavaJava.C.Character
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Character.metodos valor="toLowerCase" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static char toLowerCase(char ch)
public static int toLowerCase(int codePoint)
~~~

## Parámetros
* **char ch**,  {% include w3api/param_description.html metodo=_data parametro="char ch" %}
* **int codePoint**,  {% include w3api/param_description.html metodo=_data parametro="int codePoint" %}

## Clase Padre
[Character](/Java/Character/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Character.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
