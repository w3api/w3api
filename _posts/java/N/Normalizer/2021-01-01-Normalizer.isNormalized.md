---
title: Normalizer.isNormalized()
permalink: Java/Normalizer/isNormalized
date: 2021-01-11
key: JavaJava.N.Normalizer
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.Normalizer.metodos valor="isNormalized" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean isNormalized(CharSequence src, Normalizer.Form form)
~~~

## Parámetros
* **Normalizer.Form form**,  {% include w3api/param_description.html metodo=_dato parametro="Normalizer.Form form" %}
* **CharSequence src**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence src" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Normalizer](/Java/Normalizer/)

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
