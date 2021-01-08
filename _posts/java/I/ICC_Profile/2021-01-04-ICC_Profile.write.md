---
title: ICC_Profile.write()
permalink: Java/ICC_Profile/write
date: 2021-01-04
key: JavaJava.I.ICC_Profile
category: java
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
* **String fileName**,  {% include w3api/param_description.html metodo=_data parametro="String fileName" %}
* **OutputStream s**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream s" %}

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
{%- for _ldc in site.data.Java.I.ICC_Profile.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
