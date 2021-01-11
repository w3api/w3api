---
title: DeflaterInputStream.DeflaterInputStream()
permalink: Java/DeflaterInputStream/DeflaterInputStream
date: 2021-01-11
key: JavaJava.D.DeflaterInputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DeflaterInputStream.constructores valor="DeflaterInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DeflaterInputStream(InputStream in)
public DeflaterInputStream(InputStream in, Deflater defl)
public DeflaterInputStream(InputStream in, Deflater defl, int bufLen)
~~~

## Parámetros
* **InputStream in**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream in" %}
* **int bufLen**,  {% include w3api/param_description.html metodo=_dato parametro="int bufLen" %}
* **Deflater defl**,  {% include w3api/param_description.html metodo=_dato parametro="Deflater defl" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DeflaterInputStream](/Java/DeflaterInputStream/)

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
