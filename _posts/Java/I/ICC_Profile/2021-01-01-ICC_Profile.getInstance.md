---
title: ICC_Profile.getInstance()
permalink: /Java/ICC_Profile/getInstance/
date: 2021-01-11
key: Java.I.ICC_Profile
category: Java
tags: ['java se', 'java.awt.color', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ICC_Profile.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ICC_Profile getInstance(byte[] data)
public static ICC_Profile getInstance(int cspace)
public static ICC_Profile getInstance(InputStream s) throws IOException
public static ICC_Profile getInstance(String fileName) throws IOException
~~~

## Parámetros
* **String fileName**,  {% include w3api/param_description.html metodo=_dato parametro="String fileName" %}
* **int cspace**,  {% include w3api/param_description.html metodo=_dato parametro="int cspace" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}
* **InputStream s**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream s" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ICC_Profile](/Java/ICC_Profile/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
