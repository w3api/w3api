---
title: FileCacheImageInputStream.FileCacheImageInputStream()
permalink: Java/FileCacheImageInputStream/FileCacheImageInputStream
date: 2021-01-11
key: JavaJava.F.FileCacheImageInputStream
category: java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileCacheImageInputStream.constructores valor="FileCacheImageInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileCacheImageInputStream(InputStream stream, File cacheDir) throws IOException
~~~

## Parámetros
* **File cacheDir**,  {% include w3api/param_description.html metodo=_dato parametro="File cacheDir" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[FileCacheImageInputStream](/Java/FileCacheImageInputStream/)

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
