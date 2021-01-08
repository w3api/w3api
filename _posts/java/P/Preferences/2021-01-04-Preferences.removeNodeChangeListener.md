---
title: Preferences.removeNodeChangeListener()
permalink: Java/Preferences/removeNodeChangeListener
date: 2021-01-04
key: JavaJava.P.Preferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Preferences.metodos valor="removeNodeChangeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void removeNodeChangeListener(NodeChangeListener ncl)
~~~

## Parámetros
* **NodeChangeListener ncl**,  {% include w3api/param_description.html metodo=_data parametro="NodeChangeListener ncl" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Preferences](/Java/Preferences/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Preferences.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
