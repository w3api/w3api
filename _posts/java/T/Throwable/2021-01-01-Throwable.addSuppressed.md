---
title: Throwable.addSuppressed()
permalink: /Java/Throwable/addSuppressed/
date: 2021-01-11
key: Java.T.Throwable
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Throwable.metodos valor="addSuppressed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void addSuppressed(Throwable exception)
~~~

## Parámetros
* **Throwable exception**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable exception" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Throwable](/Java/Throwable/)

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
