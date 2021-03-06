---
title: Preferences.getByteArray()
permalink: /Java/Preferences/getByteArray/
date: 2021-01-11
key: Java.P.Preferences
category: Java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Preferences.metodos valor="getByteArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract byte[] getByteArray(String key, byte[] def)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}
* **byte[] def**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] def" %}

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
