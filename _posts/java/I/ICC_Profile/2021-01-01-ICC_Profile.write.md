---
title: ICC_Profile.write()
permalink: /Java/ICC_Profile/write/
date: 2021-01-11
key: Java.I.ICC_Profile
category: Java
tags: ['java se', 'java.awt.color', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ICC_Profile.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(OutputStream s) throws IOException
public void write(String fileName) throws IOException
~~~

## Parámetros
* **OutputStream s**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream s" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_dato parametro="String fileName" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[ICC_Profile](/Java/ICC_Profile/)

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
