---
title: ImageInputStream.readBytes()
permalink: /Java/ImageInputStream/readBytes/
date: 2021-01-11
key: Java.I.ImageInputStream
category: Java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageInputStream.metodos valor="readBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void readBytes(IIOByteBuffer buf, int len) throws IOException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **IIOByteBuffer buf**,  {% include w3api/param_description.html metodo=_dato parametro="IIOByteBuffer buf" %}

## Excepciones
[IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ImageInputStream](/Java/ImageInputStream/)

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
