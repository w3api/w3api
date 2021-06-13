---
title: CollatorProvider.getInstance()
permalink: /Java/CollatorProvider/getInstance/
date: 2021-01-11
key: Java.C.CollatorProvider
category: Java
tags: ['java se', 'java.text.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CollatorProvider.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Collator getInstance(Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CollatorProvider](/Java/CollatorProvider/)

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
