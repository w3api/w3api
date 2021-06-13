---
title: Preferences.userNodeForPackage()
permalink: /Java/Preferences/userNodeForPackage/
date: 2021-01-11
key: Java.P.Preferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Preferences.metodos valor="userNodeForPackage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Preferences userNodeForPackage(Class<?> c)
~~~

## Parámetros
* **Class&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> c" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Preferences](/Java/Preferences/)

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
