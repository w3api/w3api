---
title: ICC_Profile.getInstance()
permalink: Java/ICC_Profile/getInstance
date: 2021-01-04
key: JavaJava.I.ICC_Profile
category: java
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
* **byte[] data**,  {% include w3api/param_description.html metodo=_data parametro="byte[] data" %}
* **InputStream s**,  {% include w3api/param_description.html metodo=_data parametro="InputStream s" %}
* **int cspace**,  {% include w3api/param_description.html metodo=_data parametro="int cspace" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_data parametro="String fileName" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ICC_Profile](/Java/ICC_Profile/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ICC_Profile.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
