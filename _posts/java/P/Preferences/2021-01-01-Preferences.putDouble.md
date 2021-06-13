---
title: Preferences.putDouble()
permalink: /Java/Preferences/putDouble/
date: 2021-01-11
key: Java.P.Preferences
category: Java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Preferences.metodos valor="putDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void putDouble(String key, double value)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}
* **double value**,  {% include w3api/param_description.html metodo=_dato parametro="double value" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

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
