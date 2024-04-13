---
title: MatchResult.start()
permalink: /Java/MatchResult/start/
date: 2021-01-11
key: Java.M.MatchResult
category: Java
tags: ['java se', 'java.util.regex', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MatchResult.metodos valor="start" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int start()
int start(int group)
~~~

## Parámetros
* **int group**,  {% include w3api/param_description.html metodo=_dato parametro="int group" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[MatchResult](/Java/MatchResult/)

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
