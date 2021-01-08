---
title: ImageOutputStream.writeFloats()
permalink: Java/ImageOutputStream/writeFloats
date: 2021-01-04
key: JavaJava.I.ImageOutputStream
category: java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageOutputStream.metodos valor="writeFloats" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeFloats(float[] f, int off, int len) throws IOException
~~~

## Parámetros
* **float[] f**,  {% include w3api/param_description.html metodo=_data parametro="float[] f" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageOutputStream](/Java/ImageOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
