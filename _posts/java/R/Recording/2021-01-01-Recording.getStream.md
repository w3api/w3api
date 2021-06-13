---
title: Recording.getStream()
permalink: Java/Recording/getStream
date: 2021-01-11
key: Java.R.Recording
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
* **Instant start**,  {% include w3api/param_description.html metodo=_dato parametro="Instant start" %}
* **Instant end**,  {% include w3api/param_description.html metodo=_dato parametro="Instant end" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[Recording](/Java/Recording/)

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
