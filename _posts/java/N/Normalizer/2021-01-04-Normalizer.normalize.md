---
title: Normalizer.normalize()
permalink: Java/Normalizer/normalize
date: 2021-01-04
key: JavaJava.N.Normalizer
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.Normalizer.metodos valor="normalize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String normalize(CharSequence src, Normalizer.Form form)
~~~

## Parámetros
* **CharSequence src**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence src" %}
* **Normalizer.Form form**,  {% include w3api/param_description.html metodo=_data parametro="Normalizer.Form form" %}

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
{%- for _ldc in site.data.Java.N.Normalizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
