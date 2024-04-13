---
title: AudioInputStream.read()
permalink: /Java/AudioInputStream/read/
date: 2021-01-11
key: Java.A.AudioInputStream
category: Java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioInputStream.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int read() throws IOException
public int read(byte[] b) throws IOException
public int read(byte[] b, int off, int len) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] b" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[AudioInputStream](/Java/AudioInputStream/)

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
