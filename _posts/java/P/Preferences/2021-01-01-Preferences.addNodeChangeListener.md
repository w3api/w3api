---
title: Preferences.addNodeChangeListener()
permalink: /Java/Preferences/addNodeChangeListener/
date: 2021-01-11
key: Java.P.Preferences
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Preferences.metodos valor="addNodeChangeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void addNodeChangeListener(NodeChangeListener ncl)
~~~

## Parámetros
* **NodeChangeListener ncl**,  {% include w3api/param_description.html metodo=_dato parametro="NodeChangeListener ncl" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

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
