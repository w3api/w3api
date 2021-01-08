---
title: Recording.dump()
permalink: Java/Recording/dump
date: 2021-01-04
key: JavaJava.R.Recording
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Recording.metodos valor="dump" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void dump(Path destination) throws IOException
~~~

## Parámetros
* **Path destination**,  {% include w3api/param_description.html metodo=_data parametro="Path destination" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[Recording](/Java/Recording/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.Recording.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
