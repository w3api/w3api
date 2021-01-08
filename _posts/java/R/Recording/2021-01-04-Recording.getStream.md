---
title: Recording.getStream()
permalink: Java/Recording/getStream
date: 2021-01-04
key: JavaJava.R.Recording
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Recording.metodos valor="getStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputStream getStream(Instant start, Instant end) throws IOException
~~~

## Parámetros
* **Instant end**,  {% include w3api/param_description.html metodo=_data parametro="Instant end" %}
* **Instant start**,  {% include w3api/param_description.html metodo=_data parametro="Instant start" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
